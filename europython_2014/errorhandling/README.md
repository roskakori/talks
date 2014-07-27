Solution oriented error handling
================================

Solution oriented error handling is a set of guidelines and best practices
using Python's built in error handling mechanisms to keep the productive code
clean, derive helpful error messages directly from the code and release
ressources properly. It simplifies focusing on the productive parts of the
code and supporting your applications in case things go wrong.

These are the slides and code examples for a talk given at the EuroPython 2014
conference. A video is a available at
<https://www.youtube.com/watch?v=kT34QMil-FQ>.

* application.py - a template for a command line application that logs errors
  the user can fix without a stack trace and the errors only the developer
  can fix with a stack trace.
* chaining.py - example usage of exception chaining
* contextmanager.py - an example on how to implement context managers that
  properly clean up even if initialization was only partially possibly.
* dataerror.py - an example on how to define your own exception that can
  indicate that there is an issue in the data the user provided and should
  fix. There is both a simple variant that just allows to specify an error
  message and a more sophisticated on where you can specify the file, line
  number and column where the error originated from.
* fragments.py - various code fragments used in the slides
* performance.py - a performance test showcasing there is hardly any
  difference in dealing with non existent dictionary keys by means of
  existence checks, default values and exception handling. This was not
  mentioned in the talk due time constraints.

The code examples work with Python 3.4+ though most features also apply for
Python 2.

An earlier German version of this talk was presented at the Grazer Linuxtag
2013, you can find the slides at
<https://github.com/roskakori/talks/tree/master/linuxtage/>.
