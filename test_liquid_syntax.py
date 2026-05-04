#!/usr/bin/env python3
"""
Jekyll Liquid Syntax Validator
Comprehensive check for common Liquid syntax errors in Jekyll templates.
"""

import re
import os
import sys
from pathlib import Path

def check_liquid_syntax(filepath, repo_dir):
    """Check a single file for Liquid syntax issues."""
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove comments
        content = re.sub(r'\{%\s*comment\s*%.*?\{%\s*endcomment\s*%}', '', content, flags=re.DOTALL)
        
        # Check if tag structure is balanced
        if_tags = len(re.findall(r'\{%\s*if\s+', content))
        endif_tags = len(re.findall(r'\{%\s*endif\s*%}', content))
        for_tags = len(re.findall(r'\{%\s*for\s+', content))
        endfor_tags = len(re.findall(r'\{%\s*endfor\s*%}', content))
        unless_tags = len(re.findall(r'\{%\s*unless\s+', content))
        endunless_tags = len(re.findall(r'\{%\s*endunless\s*%}', content))
        
        if if_tags != endif_tags:
            errors.append(f"if/endif mismatch: {if_tags} if vs {endif_tags} endif")
        
        if for_tags != endfor_tags:
            errors.append(f"for/endfor mismatch: {for_tags} for vs {endfor_tags} endfor")
        
        if unless_tags != endunless_tags:
            errors.append(f"unless/endunless mismatch: {unless_tags} unless vs {endunless_tags} endunless")
        
        # Check for common Jekyll errors
        # 1. Check for 'sort: 0' on hashes (site.categories, site.tags)
        if re.search(r'site\.(categories|tags)\s*\|\s*sort\s*:\s*0', content):
            errors.append("Found 'sort: 0' on site.categories or site.tags (not supported)")
        
        # 2. Check for missing includes
        includes = re.findall(r'\{%\s*include\s+([^%]+)\s*%}', content)
        if includes:
            includes_dir = filepath.parent / '_includes'
            if not includes_dir.exists():
                errors.append(f"_includes directory not found")
            else:
                for include in includes:
                    include_path = includes_dir / include.strip()
                    if not include_path.exists():
                        errors.append(f"Missing include: {include.strip()}")
        
        # 3. Check for broken image paths
        images = re.findall(r'(?:src|href)=["\']?([^"\']*\.(?:png|jpg|jpeg|gif|svg|webp))["\']?', content)
        for img in images:
            if not img.startswith('http'):
                # Check relative to repo root, strip leading / if present
                clean_path = img.lstrip('/')
                full_path = repo_dir / clean_path
                if not full_path.exists():
                    errors.append(f"Potentially broken image path: {img}")
        
    except Exception as e:
        errors.append(f"Error reading file: {e}")
    
    return errors

def main():
    """Main test function."""
    repo_dir = Path('/home/fido/work/mattions.github.com')
    
    if not repo_dir.exists():
        print(f"ERROR: Repository directory not found: {repo_dir}")
        sys.exit(1)
    
    print(f"🔍 Validating Liquid syntax in {repo_dir}")
    print("=" * 60)
    
    # Find all Liquid template files
    template_extensions = ['.html', '.liquid', '.md']
    files_to_check = []
    
    for ext in template_extensions:
        files_to_check.extend(repo_dir.rglob(f'*{ext}'))
        files_to_check.extend(repo_dir.rglob(f'_{ext}/**/*{ext}'))
    
    # Remove duplicates
    files_to_check = list(set(files_to_check))
    
    total_errors = 0
    files_checked = 0
    
    for filepath in sorted(files_to_check):
        # Skip node_modules, vendor, and .git directories
        if any(part in ['node_modules', 'vendor', '.git', '.hermes'] for part in filepath.parts):
            continue
        
        errors = check_liquid_syntax(filepath, repo_dir)
        files_checked += 1
        
        if errors:
            print(f"❌ {filepath.relative_to(repo_dir)}")
            for error in errors:
                print(f"   • {error}")
            total_errors += len(errors)
        else:
            print(f"✅ {filepath.relative_to(repo_dir)}")
    
    print("=" * 60)
    print(f"📊 Results: {files_checked} files checked, {total_errors} errors found")
    
    if total_errors == 0:
        print("🎉 All Liquid syntax checks passed!")
        return 0
    else:
        print(f"⚠️  Found {total_errors} Liquid syntax errors that need to be fixed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
