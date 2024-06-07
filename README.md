
[![DOI](https://zenodo.org/badge/148214993.svg)](https://zenodo.org/badge/latestdoi/148214993)
# Changes in Oct 2020
Changes have been made in Cython by Xiyuan Bao to improve the stability and quality of the PIV result with and without GPU.
# OpenPIV Python version with GPU support
GPU accelerated version of OpenPIV in Python. The algorithm and functions are mostly the same 
as the CPU version. The main difference is that it runs much faster. The source code has been 
augmented with CUDA, so it will only run on NVIDIA GPUs.


## Warning
The OpenPIV GPU version is still in pre-beta state. This means that
it still might have some bugs and the API may change. However testing and contributing
is very welcome, especially if you can contribute with new algorithms and features.

Validation of the code for instantaneous and time averaged flow has been done, and a 
paper on that topic has been submitted and will be published in the near future

Development is currently done on a Linux/Mac OSX environment, but as soon as possible 
Windows will be tested. If you have access to one of these platforms
please test the code. 


## Test without installation
You can test the code without needing to install anything locally. Included in this 
repository is the IPython Notebook [Openpiv_Python_Cython_GPU_demo.ipynb](Openpiv_Python_Cython_GPU_demo.ipynb). 
When viewing the file on Github there will be a link to view the notebook with Colaboratory. 
Clicking this will load the notebook into Googles free cloud computing service and you can test
the GPU capabilities. 


## Install From Source

Make sure you have installed all the dependancies (`numpy, matplotlib, scipy, cython, skcuda, pycuda`).
The GPU version will only install if it detects both `skcuda` and `pycuda`. Otherwise, only the CPU version will be installed. 

Clone the repository from Github onto your computer:

    git clone https://github.com/OpenPIV/openpiv-python-gpu.git

Compile the cython and CUDA code (this can take a while):

    python setup.py build_ext --inplace
  
After this the GPU functions should be good to go. You will likely need to add the openpiv directory to the PYTHONPATH to be able to import the functions. 

## How to cite this work

Dallas CA, Wu M, Chou VP, Liberzon A, Sullivan PE. GPU Accelerated Open Source Particle Image Velocimetry Software for High Performance Computing Systems. ASME. J. Fluids Eng. 2019;():. [doi:10.1115/1.4043422](http://fluidsengineering.asmedigitalcollection.asme.org/article.aspx?articleid=2730543).
  

## Contributors
1. OpenPIV team, https://groups.google.com/forum/#!forum/openpiv-users
2. Cameron Dallas https://github.com/CameronDallas5000
3. Alex Liberzon https://github.com/alexlib
