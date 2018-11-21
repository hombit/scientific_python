# Materials for Scientific Python Course for astronomers of Moscow University

[![Build Status](https://travis-ci.org/hombit/scientific_python.svg?branch=master)](https://travis-ci.org/hombit/scientific_python)


# How to use this repository

Read files from [`scientific_python`](./scientific_python/) folder in alphabetical order and try to understand how all prints
and asserts work.


# Repository structure

This repository has a structure of [a Python package](https://packaging.python.org/tutorials/distributing-packages/) with some additional files:
 - [`scientific_python`](./scientific_python/) folder represents top level package of the same name. This package contains
   several sub-packages and modules. You can start with [`a_intro`](./scientific_python/a_intro) sub-package and read its 
   modules one by one in alphabetical order. All modules can be used as separate modules and scripts without package
   installation
 - [`bin`](./bin/) folder contains scripts that can be used after package installation. Now they are used for testing
 - [`doc`](./doc/) folder is used for documentation. Now it contains only MS Word file with course annotation (in Russian)
 - [`misc`](./misc/) contains two sub-folders related to [`Juyter`](http://jupyter.org) notebooks used in class:
   - [`jupyter_notebooks`](./misc/jupyter_notebooks/) contains notebooks and other files used in class sorted by date
   - [`share_jupyter`](./misc/share_jupyter/) contains little [`Docker`](http://docker.com) project that runs my class `Jupyter` server and exposes notebook `HTML` copies to the world on [sai.homb.it](http://sai.homb.it/)
 - [`setup.py`](./setup.py) is used to install this package
 - [`requirements.txt`](./requirements.txt) file contains Python dependencies of the project.
 - [`virtualenv_activation.sh`](./virtualenv_activation.sh) is a sample shell script (for \*nix systems only) that can be used to activate [`virtualenv`](https://virtualenv.pypa.io/) and install the package. Use it by typing `. virtualenv_activation.sh` or `source virtualenv_activation.sh`. For exit virtualenv type `deactivate`
 - [`Dockerfile`](./Dockerfile) and [`docker-compose.yml`](./docker-compose.yml) files can be used to run the project inside [`Docker`](http://docker.com) container
 - [`.gitignore`](./.gitignore) and [`.gitattributes`](.gitattributes) are [`git`](https://git-scm.com)  files
 - [`.dockerignore`](./.dockerignore) is just a link to [`.gitignore`](./.gitignore), it used to prevent load garbage into Docker container
 - [`.travis.yml`](./.travis.yml) is a [`Travis`](https://travis-ci.org) configuration file. `Travis` is a continuous integration (CI) system used to test this project with various Python versions, 2.7 and 3.5+ are supported

# Useful links

## Install Python

Remember to use Python 3, 3.6 and later is good enough in 2018. You can check python version typing in console `python3 --version` or `import sys; print(sys.version)` in Python itself

### All platforms
- [Anaconda Python distribution](https://www.anaconda.com/download/) is a good choice for scientific Python programming on every platform. It includes a lot of pre-compiled numerical and scientific packages and `conda` package manager where you can find even more packages, like `astropy` or `scikit-learn`
- [Official Python distribution](https://www.python.org/downloads/): good on Windows or macOS, when you like to build your environment from scratch.

### macOS
Instead of official Python distribution I recommend to use [Homebrew](http://brew.sh) package manager, type `brew install python`

### Linux
Probably you already have Python 3, check its version before start. If you haven't use your Linus package manager to install

### iOS
iOS doesn't have any application to use for scientific programming. The best choice is [Pythonista](http://omz-software.com/pythonista/) paid application that can run and edit Python 3.5 code and supports `numpy` package, but doesn't support `scipy` and other useful packages.

### Android
[PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) looks good

## Source code editors for Python
- [IDLE](https://docs.python.org/3/library/idle.html): a simple Python source code editor. It is a part of Python standard library, so if you have Python, you probably have IDLE
- [Visual Studio Code](https://code.visualstudio.com) (do not be confused with Visual Studio, they are two different products): a powerful source code editor
- [Spyder](https://www.spyder-ide.org): the scientific Python development environment
- [PyCharm](https://www.jetbrains.com/pycharm/): a powerful Python IDE (integrated development environment). PyCharm is closed source product, but Community edition is free to use and every student and professor can ask for a [free professional version](https://www.jetbrains.com/student/)

## Dive into Python
- [Learn Python in Y minutes](http://learnxinyminutes.com/python3/): short and deep language tutorial. This tutorial has [Russian version](https://learnxinyminutes.com/docs/ru-ru/python3-ru/)
- [Official Python tutorial](https://docs.python.org/3/tutorial/)
- [Python for astronomers](https://python4astronomers.github.io)
- [Python 3 in one picture](https://fossbytes.com/wp-content/uploads/2015/09/python-3-in-one-pic.png): print it and enjoy
- [Use of Python programming language in astronomy and science](https://arxiv.org/abs/1807.04806)
- [WTF Python](https://github.com/satwikkansal/wtfpython)

## General documentation
- [Zen of Python](http://pep20.prg) or just run `import this` in Python
- [Official documentation](http://docs.python.org)
- [Python code style guide](http://pep8.org)

# Classes materials (2018)

Classes have place in classroom 48 of Sternberg Astronomical Institute MSU at 9:00 on Wednesdays from September to December 2018. Development of the course in 2018 is supported by [BASIS foundation](https://basis-foundation.ru/en/).

Date | Description | Materials | Links | Video (in Russian)
---- | ----------- | --------- | ----- | ------------------
2018.09.05 | Introduction, coursework requirements. About Python. Numbers, lists, if-else, while, Boolean variables | [`a_intro.basics`](./scientific_python/a_intro/basics.py), [`a_intro.sequences`](./scientific_python/a_intro/sequences.py) (the first part about lists) | [Python documentation](https://docs.python.org/), see section "Dive into Python" above | [link](https://youtu.be/yN5__ZYKeOE)
2018.09.12 | Built-in collections: tuples, dictionaries, sets. for-in, in. | [`a_intro.sequences`](./scientific_python/a_intro/sequences.py) | [Iteration](https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python), ["Hash table" Wikipedia article](https://en.wikipedia.org/wiki/Hash_table), [CPython implementation of lists and tuples](https://rushter.com/blog/python-lists-and-tuples/) | [link](https://www.youtube.com/watch?v=Hqjt6VEkhUM)
2018.09.19 | Strings: unicode and formating. Functions: functions as objects, lambdas, argument packing and unpacking | [`a_intro.strings`](./scientific_python/a_intro/strings.py), [`b_modules.functions`](./scientific_python/b_modules/functions.py), [dump of iPython session](./misc/jupyter_notebooks/18.09.19/ipython_notes.py) | [String formating](https://pyformat.info) (use "new" syntax), [keyword arguments](http://treyhunner.com/2018/04/keyword-arguments-in-python) | [link](https://www.youtube.com/watch?v=W-tjVzoZphc&t=2943s)
2018.09.26 | Some more details about strings: methods and `re`. Generators, list comprehance syntax. Python source file as module, import system. Introduction to classes. | [`b_modules`](./scientific_python/b_modules/), [`*.py`](./misc/jupyter_notebooks/18.09.26) files used on seminar | [Regular expressions (in Russian)](https://habr.com/post/349860/), [iteration and generators](https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python), [scope and namespaces](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html), [modules](https://realpython.com/python-modules-packages/) | [link](https://www.youtube.com/watch?v=v1ryYXkfDHQ)
2018.10.03 | Jupyter notebook: a good way to use Python and another languages. Introduction in `numpy` | [`c_numpy.arrays`](./scientific_python/c_numpy/arrays.py), [Jupyter notebook](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.03/numpy-arrays.ipynb) | [Jupyter website](http://jupyter.org), [Jupyter guide](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook), [`numpy` user guide](https://docs.scipy.org/doc/numpy/user/) | [link](https://www.youtube.com/watch?v=BWJP40Hp5Tc)
2018.10.10 | Multidimensional arrays in `numpy`: reshaping, broadcasting, stacking. Review of `numpy` subpackages | [`c_numpy`](./scientific_python/c_numpy/), [Jupyter notebook](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.10/multidim-arrays.ipynb) | [`numpy` user guide](https://docs.scipy.org/doc/numpy/user/), ["An introduction to Numpy and Scipy"](https://engineering.ucsb.edu/~shell/che210d/numpy.pdf) | [link](https://youtu.be/jnjE93pfusk)
2018.10.17 | Read of files and cats. `open()` builtin, `with`-`as` statement, textual and binary files. Tabular data: `np.genfromtxt` and `pandas` | [Jupiter notebook and data files](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.17/) | [`open()` documentation](https://docs.python.org/3/library/functions.html#open), standard library modules for path and file manipulations: [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path) and [`shutil`](https://docs.python.org/3/library/shutil.html), ["10 minutes to pandas"](http://pandas.pydata.org/pandas-docs/stable/10min.html) | [link](https://youtu.be/jimNsY2TlLM)
2018.10.24 | `matplotlib`: basics and examples. Introduction to `scipy`, `scipy.integrate`, `scipy.optimize` | [Jupyter notebooks](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.24/) | ["Scientific graphics in Python" (In Russian)](https://github.com/whitehorn/Scientific_graphics_in_python), [Python matplotlib guide](https://realpython.com/python-matplotlib-guide/), ["An introduction to Numpy and Scipy"](https://engineering.ucsb.edu/~shell/che210d/numpy.pdf) | [link](https://youtu.be/wooDiM7IHMI)
2018.10.31 | Python packages and how to prepare them. Testing, `unittest`. Example of class usage | [Sample Python project](https://github.com/hombit/scientific_python/blob/master/misc/sample_project/), [unit test example](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.31/sin_test.py), [Jupyter notebook with `Parabola` class](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.10.31/parabola_class.ipynb) | ["Python modules and packages"](https://realpython.com/python-modules-packages/), [`virtualenv` docs](https://virtualenv.pypa.io/en/stable/), [`pipenv` docs](http://pipenv.readthedocs.io/en/latest/), [official packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/), [How to Publish Your Package on PyPI](https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/), [`unittest` docs](http://docs.python.org/3/library/unittest.html), [`numpy.testing` docs](https://docs.scipy.org/doc/numpy/reference/routines.testing.html), [`pytest`](https://docs.pytest.org/en/latest/) | [link](https://youtu.be/wXflAwWBteA)
2018.11.07 | Introduction to Astropy. Constants, units, quantities. Coordinates: sky coordinates, Earth coordinates, rtansformations beetween frames. Breif introduction to `astropy.io`: FITS ans ASCII. | [Jupyter notebooks](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.11.07/) | [`astropy` docs](http://docs.astropy.org/en/stable/): [tutorials](http://tutorials.astropy.org/), [`constants`](http://docs.astropy.org/en/stable/constants/), [`units`](http://docs.astropy.org/en/stable/units/index.html), [`io` interface](http://docs.astropy.org/en/stable/io/unified.html), [`coordinates`](http://docs.astropy.org/en/stable/coordinates/index.html) | [link](https://www.youtube.com/watch?v=9wuodNtLj2M)
2018.11.14 | Least squares method usage with `scipy.optimize`. Module `astroquery` for web-access to astronomical data bases, e.g. Vizier and SIMBAD. Problem of cosmological parameters fit using SN Ia data. | [Jupyter notebooks](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.11.14/) | [`scipy.optimize` tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html), [`lmfit`](https://lmfit.github.io/lmfit-py/index.html) module with pretty interface for least squares. `astroquery` [docs](https://astroquery.readthedocs.io/): [A Gallery of Queries](https://astroquery.readthedocs.io/en/latest/gallery.html), [GAIA via TAP+](https://astroquery.readthedocs.io/en/latest/gaia/gaia.html), [SIMBAD](https://astroquery.readthedocs.io/en/latest/simbad/simbad.html), [Vizier](https://astroquery.readthedocs.io/en/latest/vizier/vizier.html) | [link](https://www.youtube.com/watch?v=tSVGrkP7lRI)
2018.11.21 | Sky coordinate match: `astropy.coordinates`. Problem of transient object discovery on FITS image: `photutils`, `astroquery`, `astropy.wcs` and `astropy.coordinates` | [Jupyter notebooks](https://github.com/hombit/scientific_python/blob/master/misc/jupyter_notebooks/18.11.21/) | `astropy` tutorial [Separations, Catalog Matching, and Related Functionality](http://docs.astropy.org/en/stable/coordinates/matchsep.html), `photutils` [docs](https://photutils.readthedocs.io/): [source detection](https://photutils.readthedocs.io/en/stable/detection.html), [aperture photometry](https://photutils.readthedocs.io/en/stable/aperture.html) | [link](https://www.youtube.com/watch?v=XsavdJrrve4)


# Classes materials (2017)

Seminars had place in classroom 17 of Sternberg Astronomical Institute MSU at 13:30 on Fridays from September to December 2017. Records of on-line translations of the seminars are hosted [on YouTube](https://www.youtube.com/playlist?list=PLmgwC9JZdQnsPAZTVzzD5tttStuYGgskg).

Date | Description | Materials | Video (in Russian)
---- | ----------- | --------- | ------------------
2017.09.15 | Introduction, coursework requirements. Why Python 3? Numbers, lists, if-else, loops. | [`a_intro.basics`](./scientific_python/a_intro/basics.py), [`a_intro.sequences`](./scientific_python/a_intro/sequences.py) | [link](https://www.youtube.com/watch?v=-mHpM6Dmc9k)
2017.09.22 | Boolean variables, lists, tuples, dictionaries, sets. Strings and their formatting. Functions, arguments packing and unpacking. | [`a_intro.sequences`](./scientific_python/a_intro/sequences.py), [`a_intro.strings`](./scientific_python/a_intro/strings.py), [`b_modules.functions`](./scientific_python/b_modules/functions.py) | [link](https://www.youtube.com/watch?v=30_PbnAz_SI)
2017.09.29 | Functions: default values of keyword arguments, docstrings. Iterators and generators. Modules: file.py as a module. | [`b_modules.*`](./scientific_python/b_modules) | [link](https://www.youtube.com/watch?v=0p0Vmcqk3hU)
2017.10.06 | Jupyter notebooks. Read and write files and cats. Introduction to `numpy`: one-dimensional arrays and indexing. | [Notebooks](./misc/jupyter_notebooks/17.10.06/), [`c_numpy.arrays`](./scientific_python/c_numpy/arrays.py) | [link](https://www.youtube.com/watch?v=QzGCcURJATI)
2017.10.13 | `numpy`: multidimensional arrays, read tabular data files. | [Notebooks](./misc/jupyter_notebooks/17.10.13/), [`c_numpy.multidim_arrays`](./scientific_python/c_numpy/multidim_arrays.py) | [link](https://www.youtube.com/watch?v=rstATYs4l20)
2017.10.20 | Read tabular data files with `numpy` and `pandas`. Figure plotting with `matplotlib`. |  [Notebooks](./misc/jupyter_notebooks/17.10.20/) | [link](https://www.youtube.com/watch?v=GL7Buv3PiXY)
2017.10.27 | `scipy`: integration, interpolation, optimization. Short overview of other features. | [Notebook](./misc/jupyter_notebooks/17.10.27/), [`d_scipy.*`](./scientific_python/d_scipy) | [link](https://www.youtube.com/watch?v=wwZTAcxdw48)
2017.11.03 | Introduction to `astropy`: physical and astronomical constants, quantity calculations, sky coordinates, image manipulation, read and write data. | [Notebook](./misc/jupyter_notebooks/17.11.03/) | [link](https://www.youtube.com/watch?v=_RmMIYeFaqU)
2017.11.10 | Packaging of Python project. Classes: example and magic methods. Unit testing. | [Notebook and script](./misc/jupyter_notebooks/17.11.10/), [`setup.py`](./setup.py) of this project, [`e_testing.*`](./scientific_python/e_testing) | [link](https://www.youtube.com/watch?v=2WilTrbjDIg)
2017.11.17 | Two examples of `astropy`, `astroquery` and `photutils` usage: Hubble diagram fitting and transient object discovery. | [Notebooks](./misc/jupyter_notebooks/17.11.17/) | [link](https://www.youtube.com/watch?v=quwNr4l3NvE)
2017.11.24 | Dr. Ivan Zolotukhin tells about `Django` web framework, scientific web programming and model-template-view paradigm. | [Scripts](./misc/jupyter_notebooks/17.11.24/) | —
2017.12.01 | Student [Nikita Utkin](https://github.com/GalacticCat) tells about `argparse`. Speed up Python script: why Python is slow, why to avoid loops and why we should know how Python works, `numba` as a simple way to speed up calculations. | [Scripts and notebook](./misc/jupyter_notebooks/17.12.01/), [`c_numpy.arrays`](./scientific_python/c_numpy/arrays.py#L223) | [link](https://www.youtube.com/watch?v=q73dwgkxsR8)
2017.12.08 | Parallel execution of Python code. `threading` and its limitations due GIL. `multiprocessing` and its limitations due serialisation via `pickle`. | [Notebooks](./misc/jupyter_notebooks/17.12.08/) | [link](https://www.youtube.com/watch?v=Rz6c07SKnmI)
2017.12.15 | Cython language and C-code usage with Python. | [Python, Cython and C code](./misc/jupyter_notebooks/17.12.15/), [`f_speed.compilers`](./scientific_python/f_speed/compilers.py) and [Cython/C files for this module](./src/), [`setup.py`](./setup.py) | [link](https://www.youtube.com/watch?v=cBSm9ag9eIg)


# License

Copyright (c) 2017, Konstantin L. Malanchev.

All program code in this repository is distributed under the terms of the MIT license. All data files are properties of their authors, see `COPYRIGHT_NOTE` files in folders with foreign data.
