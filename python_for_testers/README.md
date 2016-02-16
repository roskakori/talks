Python for testers
==================

This is a collection of slides to introduce the Python programming language
to testers. The target audience are testers with no prior experience in
Python but a basic understanding of general programming language concepts
such as variables, loops and functions.


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

1. Download [Anaconda](https://www.continuum.io/downloads), a Python
   distrubution with additional packages and tools.
2. Extract Anaconda to e.g. `/home/me/anaconda3`.
3. Install the RISE plugin to add a presentation mode:
```
$ cd /tmp
$ git clone https://github.com/damianavila/RISE.git
$ cd RISE
$ /home/me/anaconda3/bin/python3 setup.py install
```
3. Install additional packages in order to be able to export notebooks to
   PDF:
```
$ sudo apt-get install pandoc texlive-latex-extra
```
4. Write a little launcher scripts and store it in e.g. `/home/me/bin/notebook.sh`:
```
#!/bin/sh
# Start Jupyter Notebook.
export PATH=/home/me/anaconda3/bin:$PATH
jupyter-notebook
```
5. Run the above script to start editing and viewing notebooks in your browser.

