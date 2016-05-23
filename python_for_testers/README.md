Introduction to Python
======================

This is a collection of slides to introduce the Python programming language
to testers or devops. The target audience are testers with no prior experience
in Python but a basic understanding of general programming language concepts
such as variables, loops and functions.


Curriculum for testers
----------------------

* Numbers
* Strings, 
* Collections and loops
* Conversion and formatting
* Date and time
* Files
* Unicode
* CSV
* HTTP-queries, JSON and REST
* Functions
* object orientation
* Error handling
* XML
* Testing
* Style guide
* command line parsing
* Packages
* Bits and low level protocols
* Logging

Curriculum for devpos
---------------------

* Numbers
* Strings
* Time
* Conversion
* Collections
* Patterns
* Functions
* Errors
* Files


License
-------

![CC-BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)

This work is licensed under a 
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).


Notes on IPython Notebooks
--------------------------

The slides use IPython Notebook as format. Such notebooks allow for
interactive presentations where you can modify and excute examples on the
fly.

At the time of this writting, I used the following steps to install and setup
an environment to view and publish the slides using Ubuntu 14.04:

First, download [Anaconda](https://www.continuum.io/downloads), a Python
distribution with additional packages and tools. Then extract the archive to
e.g. `/home/me/anaconda3`.

Next, install the RISE plugin to add a presentation mode to IPython / Jupyter
Notebook:
```sh
$ cd /tmp
$ git clone https://github.com/damianavila/RISE.git
$ cd RISE
$ /home/me/anaconda3/bin/python3 setup.py install
```

To order to export notebooks to PDF you need to install a few additional
Ubuntu packages:
```
$ sudo apt-get install pandoc texlive-latex-extra
```

Finally, write a little launcher scripts and store it in e.g.
`/home/me/bin/notebook.sh`:
```sh
#!/bin/sh
# Start Jupyter Notebook.
export PATH=/home/me/anaconda3/bin:$PATH
jupyter-notebook
```

Now you can run the above script to start editing and viewing notebooks in
your browser.
