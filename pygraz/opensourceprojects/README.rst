Open source projects with Python
================================

These are the notes on a talk about starting your own open source project
using Python as implementation language.

Check name availability
-----------------------

http://ivantomic.com/projects/ospnc/

Create a repository
-------------------

1. Login to http://github.com and click "+ New repository".
2. Fill in form:
   * Repository name: dividemo
   * Description: simple tool to divide two integer numbers
   * Public: yes
   * Initialize this repository with a README: no (will be provided later)
   * Add .gitignore: None (will be provided later)
   * Add a license: None (will be provided later)
3. Click "Create repository"
4. View the repository: https://github.com/roskakori/dividemo

More information on creating a Github repository:
https://help.github.com/articles/create-a-repo/

More information on open source licenses: http://opensource.org/licenses

Create a local working copy
---------------------------

Clone the repository to your local computer in order to edit and add files::

  $ git clone https://github.com/roskakori/dividemo.git
  Cloning into 'dividemo'...
  remote: Counting objects: 5, done.
  remote: Compressing objects: 100% (5/5), done.
  remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
  Unpacking objects: 100% (5/5), done.
  Checking connectivity... done.

Create a project scaffold
-------------------------

Can be done manually, but easier with pyscaffold::

  $ sudo pip install --upgrade pyscaffold
  $ putup --force --description "simple tool to divide two integer numbers" --url https://github.com/roskakori/dividemo --license "simple-bsd" --with-travis --with-tox dividemo

Note: we need ``--force`` to overwrite files in the folder created by ``git clone``.

Overview of the project::

  $ ls -1 dividemo/
  AUTHORS.rst        - authors and contributors
  dividemo           - source code for the dividemo package
  docs               - documentation
  LICENSE.txt        - license
  README.rst         - README created by pyscaffold
  requirements.txt   - Python packages to install before this package
  setup.cfg          - setup.py configuration
  setup.py           - build specification and tool
  tests              - source code for test cases
  tox.ini            - tox configuration

Change into the project folder::

    $ cd dividemo

Remove the skeleton for a command line application because we don't need it::
    
    $ rm dividemo/skeleton.py

Update the README.rst::

    ========
    dividemo
    ========

    dividemo is a tool to divide two integer numbers.

    It showcases a simple Python project and explains how to integrate various
    tools and services with it.


Write and run the application
-----------------------------

If necessary, add required external modules to ``requirements.txt`` and
install them running::

    sudo pip install -r requirements.txt

Write the application::

    """
    dividemo - tool to divide two integer numbers.
    """
    import argparse
    import logging
    import sys


    def divided(divident, divisor):
        return divident // divisor  # //=integer division


    def main(arguments):
        # Parse command line arguments.
        parser = argparse.ArgumentParser(description='divide two integer numbers.')
        parser.add_argument('divident', metavar='DIVIDENT', type=int,
                            help='number to divide')
        parser.add_argument('divisor', metavar='DIVISOR', type=int,
                            help='number to divide by')
        args = parser.parse_args(arguments)

        # Process arguments and print result.
        result = divided(args.divident, args.divisor)
        print(result)


    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        main(sys.argv[1:])

Run it with some test options::

    $ python dividemo/dividemo.py 10 5
    2
    $ python dividemo/dividemo.py 11 5
    2
    $ python dividemo/dividemo.py 10
    usage: dividemo.py [-h] DIVIDENT DIVISOR
    dividemo.py: error: too few arguments
    $ python dividemo/dividemo.py -9.5 3
    usage: dividemo.py [-h] DIVIDENT DIVISOR
    dividemo.py: error: argument DIVIDENT: invalid int value: '-9.5'


Write and run the test cases
----------------------------

Write a test case::

    """
    Tests for dividemo.
    """
    import unittest

    from dividemo import dividemo

    class DividemoTest(unittest.TestCase):
        def test_can_divide(self):
            self.assertEqual(2, dividemo.divided(10, 5))

        def test_can_print_divided(self):
            dividemo.main(['10', '5'])

        def test_fails_on_non_integer_divisor(self):
            self.assertRaises(SystemExit, dividemo.main, ['10', 'hello'])

Run the test cases::

    $ python setup.py test
    ...
    tests/test_dividemo.py::DividemoTest::test_can_divide PASSED
    tests/test_dividemo.py::DividemoTest::test_can_print_divided PASSED
    tests/test_dividemo.py::DividemoTest::test_fails_on_non_integer_divisor PASSED
    ...
    --------------- coverage: platform linux2, python 2.7.6-final-0 ----------------
    Name                Stmts   Miss Branch BrMiss  Cover   Missing
    ---------------------------------------------------------------
    dividemo/__init__       3      0      0      0   100%   
    dividemo/dividemo      12      0      0      0   100%   
    ---------------------------------------------------------------
    TOTAL                  15      0      0      0   100%   
    Coverage HTML written to dir htmlcov

Browse test coverage report: ``htmlcov/index.html``.

If necessary, modify coverage settings in ``.coveragerc``; usually works out
of the box.

Commit what we did so far::

    $ git add dividemo/ tests/ requirements.txt setup.cfg setup.py AUTHORS.rst LICENSE.txt README.rst .coveragerc .gitattributes .gitignore

    $ git commit -m "Added initial implementation." dividemo/ tests/ requirements.txt setup.cfg setup.py AUTHORS.rst LICENSE.txt README.rst .coveragerc .gitattributes .gitignore
    [master 6f9748d] Added initial implementation.^Cividemo/
     11 files changed, 821 insertions(+), 54 deletions(-)
     create mode 100644 .gitattributes
     rewrite .gitignore (88%)
     create mode 100644 AUTHORS.rst
     create mode 100644 LICENSE.txt
     create mode 100644 README.rst
     ...

    $ git push
    Username for 'https://github.com': roskakori
    Password for 'https://roskakori@github.com': ********
    Counting objects: 21, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (17/17), done.
    Writing objects: 100% (19/19), 11.26 KiB | 0 bytes/s, done.
    Total 19 (delta 2), reused 0 (delta 0)
    To https://github.com/roskakori/dividemo.git
       d1514c6..4848043  master -> master


Continuous integration with Travis
----------------------------------

Travis is a continuous integrations services that runs your test suite
automatically after each push. It can notify you about test failures and
keeps a build history.

Sign in on https://github.com then go to http://travis-ci.org/ and sign in
using Github credentials.

Visit your profile at https://travis-ci.org/profile/roskakori, sync the list
of repositories and enable travis for ``dividemo``.

Modify ``.travis.yml``::

    env:
      matrix:
        - DISTRIB="ubuntu" PYTHON_VERSION="2.7" COVERAGE="true" *** REMOVE
        - DISTRIB="conda" PYTHON_VERSION="2.7" COVERAGE="false" *** REMOVE
        - DISTRIB="conda" PYTHON_VERSION="3.3" COVERAGE="false" *** REMOVE
        - DISTRIB="conda" PYTHON_VERSION="3.4" COVERAGE="false"
    before_script:
      - git config --global user.email "roskakori@users.sourceforge.net"
      - git config --global user.name "Thomas Aglassinger"

If necessary, modify ``tests/travis_install.sh``; usually works out of the box.

Commit and push ``.travis.yml``::

    $ git commit -m "Added Travis build." .travis.yml 
    [master 0d32115] Added Travis build.
     1 file changed, 22 insertions(+)
     create mode 100644 .travis.yml

    $ git push
    Counting objects: 4, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 744 bytes | 0 bytes/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    To https://github.com/roskakori/dividemo.git
       4848043..0d32115  master -> master

Watch the build online: https://travis-ci.org/roskakori/dividemo

More information on Travis:

* http://docs.travis-ci.com/user/build-configuration/
* http://docs.travis-ci.com/user/languages/python/


Continuous integration with Jenkins
-----------------------------------

Available from https://jenkins-ci.org.

* Works with any version control system
* Works in house
* Open source and free of charge
* Better reporting than Travis
* Many plugins for all kinds of useful things
* More difficult to install and configure

Notes on Jenkins and Python: TODO


Coverage with coveralls
-----------------------

1. Visit https://coveralls.io/ and sign in with Github account.
2. Go to https://coveralls.io/repos
3. Click "Refresh private repositories"
4. Set "dividemo" to "on".

Enable coveralls in ``.travis.yml``::

    env:
      matrix:
        - DISTRIB="conda" PYTHON_VERSION="3.4" COVERAGE="true"
                                                         ^^^^

Commit and push to github::

    $ git commit -m "Activated coveralls to track code coverage online." .travis.yml
    [master 7be7e9d] Activated coveralls to track code coverage online.
     1 file changed, 1 insertion(+), 1 deletion(-)
    
    $ git push
    Counting objects: 10, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (8/8), 1.08 KiB | 0 bytes/s, done.
    Total 8 (delta 4), reused 0 (delta 0)
    To https://github.com/roskakori/dividemo.git
       0d32115..7be7e9d  master -> master


Code quality metrics
--------------------

Flake8 checks various minor issues (e.g. formatting) and is already
preconfigured by pyscaffold::

    $ tox -e flake
    GLOB sdist-make: /home/roskakori/workspace/dividemo/setup.py
    flake8 inst-nodeps: /home/roskakori/workspace/dividemo/.tox/dist/dividemo-unknown.zip
    flake8 runtests: PYTHONHASHSEED='1506682030'
    flake8 runtests: commands[0] | flake8 setup.py dividemo tests
    tests/test_dividemo.py:8:1: E302 expected 2 blank lines, found 1
    ERROR: InvocationError: '/home/roskakori/workspace/dividemo/.tox/flake8/bin/flake8 setup.py dividemo tests'
    ___________________________________ summary ____________________________________
    ERROR:   flake8: commands failed

Relevant message::

    tests/test_dividemo.py:8:1: E302 expected 2 blank lines, found 1

Violates `PEP8 Style guide for Python code <http://legacy.python.org/dev/peps/pep-0008/>`_,
can be fixed manually or using tools like
`autopep8 <https://pypi.python.org/pypi/autopep8>`_.

For more comprehensive checks use `PyLint <http://www.pylint.org/>`_, but the
default configuration is overy verbose.

Simple alternative with online reports: https://landscape.io

1. Visit https://landscape.io/
2. Sign in with Github
3. Visit https://landscape.io/dashboard
4. Click "Add repository", select "dividemo" and click the "Add repository"
   button.
5. Wait a bit and browse report at https://landscape.io/github/roskakori/dividemo

Landscape is just an interface to existing open source tools. The core tool
is `Prospector <https://pypi.python.org/pypi/prospector>`_.


Pull requests for contributions from others
-------------------------------------------

The initial version of dividemo does not handle attempts to divide by 0
in a constructive way and dumps a stack trace at the user:

    $ python dividemo/dividemo.py 4 0
    Traceback (most recent call last):
      File "dividemo/dividemo.py", line 29, in <module>
        main(sys.argv[1:])
      File "dividemo/dividemo.py", line 23, in main
        result = divided(args.divident, args.divisor)
      File "dividemo/dividemo.py", line 10, in divided
        return divident // divisor  # //=integer division
    ZeroDivisionError: integer division or modulo by zero

Other people can clone your repository to their own Github account, fix the
issue and submit a pull request to integrate their fix in your repository.

An improved version of ``dividemo.py``could include the following lines::

        args = parser.parse_args(arguments)
        if args.divisor == 0:                      # NEW
            parser.error('DIVISOR must not be 0')  # NEW

The result::

    $ python dividemo/dividemo.py 4 0
    usage: dividemo.py [-h] DIVIDENT DIVISOR
    dividemo.py: error: DIVISOR must not be 0

Notes on pull requests:

* Travis automatically tests the contributed version and adds a comment on
  Github with the results.
* Coveralls automatically computes the coverage of  the contributed version
  and adds a comment on Github with the results.
* You can review the contributed code and comment on specific lines.
* Additional pushes of the contributor automatically update the pull request.
* This allows a very effective workflow to iteratively improve a
  contribution.


Documenation
------------

The standard documentation format for Python is ReSTructured Text, typically
stored in ``.rst`` files. They are text files with a little markup for
formatting, headings, links, tables etc.

Online editor: http://rst.ninjs.org/

`Sphinx <http://sphinx-doc.org/>`_ is a documentation builder with extensive
linking capabilities, syntax coloring of code examples, index generation,
API generator and more.

Edit the documentation in ``docs`` and build it with::

    $ python setup.py docs

The results are located in in ``docs/_build/html``.


`Read the docs <https://readthedocs.org/>`_ can monitor your repository and
build the Sphinx documentation after each push.

1. Login and visit https://readthedocs.org/dashboard/
2. Click "Import Project"
3. Click "Import from Github"
4. If dividemo is not visible yet, click "Sync your GitHub projects".
5. Find dividemo and click "Create"
6. Click "Next"
7. Wait for the build to finish
8. Read the documentation at https://readthedocs.org/projects/dividemo/


Build a distribution package
----------------------------

PyPI (Python package index) is a public repository for Python packages. Using
pip it is easy to install and update packages and resolve dependencies.

With ``setup.py`` all functions to build and publish a module are integrated.

Metainformation in ``setup.py`` describes the package. By default, pyscaffold
generates::

    setup(name=package,
          version=version,
          url=metadata['url'],
          description=metadata['description'],
          author=metadata['author'],
          author_email=metadata['author_email'],
          license=metadata['license'],
          long_description=read('README.rst'),
          classifiers=metadata['classifiers'],
          test_suite='tests',
          packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
          namespace_packages=namespace,
          install_requires=install_reqs,
          setup_requires=['six'],
          cmdclass=cmdclass,
          tests_require=['pytest-cov', 'pytest'],
          include_package_data=True,
          package_data={package: metadata['package_data']},
          data_files=[('.', metadata['data_files'])],
          command_options=command_options,
          entry_points={'console_scripts': console_scripts})

Values starting with ``metadata[...]`` can be changed to hardcoded values,
e.g.::

          # url=metadata['url'],
          url='https://github.com/roskakori/dividemo',

However pyscaffold intends to modify them in ``setup.cfg`` in section
``[metadata]``:

    [metadata]
    description = simple tool to divide two integer numbers
    author = Thomas Aglassinger
    author_email = roskakori@users.sourceforge.net
    license = simple-bsd
    url = https://github.com/roskakori/dividemo

Of particular interest are 
`Trove classifiers <https://pypi.python.org/pypi?%3Aaction=list_classifiers>`_
which help to describe your package / tool and make it easier for users to
find what they are looking for::

    # Add here all kinds of additional classifiers as defined under
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = Development Status :: 4 - Beta,
                  Programming Language :: Python

For dividemo, we can set this to::

    classifiers = Development Status :: 4 - Beta,
                  Environment :: Console,
                  License :: OSI Approved :: BSD License,
                  Operating System :: OS Independent,
                  Programming Language :: Python,
                  Topic :: Utilities

Build a distribution package::

    $ python setup.py sdist --formats=zip
  
Instead of a source distribution you can also use binary wheels provided the
`wheel <https://pypi.python.org/pypi/wheel>` package is installed::

    $ pip install --upgrade setuptools wheel

Then you can::

    $ python setup.py bdist_wheel

Eggs (``bdist_egg``) are an older format and should not be used for new
packages.

However, we seem to lack a proper version number::

    $ ls -1 dist
    dividemo-unknown.zip
    dividemo-unknown-py2-none-any.whl 


Version numbers
---------------

The ``setup.py`` generated by pyscaffold uses
`versioneer <>`, which uses the current tag as version number. So in order to
get a decent version number, we need to tag the current code::

  $ git tag -a -m "Tagged version 0.1.0." v0.1.0
  $ git push --tags

Now we can build again::

    $ python setup.py sdist --formats=zip
    $ ls dist
    dividemo-0.1.0.zip


This version number is also available to the program::

    >>> from  dividemo import _version
    >>> _version.get_versions()['version']
    '0.1.0'


Publish the package
-------------------

Again, ``setup.py`` offers all functions necessary.

For the first release, you have to register your package::

    $ python setup.py register

Once the package is registered, it has its own page on PyPI.

Optinally you can store the PyPI login in ``~/.pypirc``::

    [distutils]
    index-servers=pypi

    [pypi]
    repository=https://pypi.python.org/pypi
    username=someone
    password=secret

To publish a new release, use::

    $ python setup.py sdist --formats=zip upload

Conclusion
----------

Python
