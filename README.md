# NGFF ELMI 2021 Workshop

This repository contains notebooks for the practicals during ELMI 2021.

## Running on MyBinder.org

You can launch workshop.ipynb by clicking on
[![binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/joshmoore/NGFF-ELMI-2021-Workshop/HEAD?filepath=0_Intro.ipynb)

## Running in Docker

Alternatively, if you have Docker installed, you can use the [repo2docker](https://repo2docker.readthedocs.io/en/latest/)
tool to run this repository as a local Docker instance:

    $ git clone git://github.com/joshmoore/NGFF-ELMI-2021-Workshop
    $ cd NGFF-ELMI-2021-Workshop
    $ repo2docker .

Then follow the instructions that are printed after the Docker image is built.

## Running locally

Or finally, if you would like to install the necessary requirements locally,
we suggest using conda:

Install Anaconda https://www.anaconda.com/products/individual#Downloads

Then, to create the environment:

    $ git clone git://github.com/joshmoore/NGFF-ELMI-2021-Workshop
    $ cd NGFF-ELMI-2021-Workshop
    $ conda env create -n ngff -f binder/environment.yml

and run a Notebook:

    $ conda activate ngff
    $ pip install jupyter
    $ jupyter notebook 0_Intro.ipynb

An additional benefit of installing the requirements locally is that you
can then use the tools like `bioformats2raw` without needing to launch
Jupyter itself:

    $ conda activate ngff
    $ bioformats2raw my.tiff . --file_type=zarr --dimension-order=XYZCT
