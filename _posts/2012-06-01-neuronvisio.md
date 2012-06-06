---
layout: post
title: "Neuronvisio, a Neuron companion"
description: ""
category: academic
tags: [3D visualization, computational neuroscience, neurons, neuroml]
---
{% include JB/setup %}

<img src="{{BASE_PATH}}/assets/gfx/pyramidal_3D_change_voltage.png" />

Neuronvisio is a Graphical User Interface for NEURON simulator environment with 
3D capabilities. Neuronvisio makes easy to select and investigate sections’ 
properties and it offers easy integration with matplotlib for plotting the 
results.

The geometry can be saved using NeuroML and the computational results in a 
customised and extensible HDF5 format; the results can then be reload in the 
software and analysed in a later stage, without re-running the simulation.

## Features

- 3D visualization of the model with the possibility to change it runtime
- Creation of vectors to record any variables present in the section
- Pylab integration to plot directly the result of the simulation
- Exploration of the timecourse of any variable among time using a color coded scale
- Saving the results simulation for later analysis
- Automatic download and running of models in ModelDB

More info at [http://neuronvisio.org](http://neuronvisio.org)
Neuronvisio paper has been published in [Frontiers in Neuroinformatics](http://www.frontiersin.org/neuroinformatics/10.3389/fninf.2012.00020/abstract).
