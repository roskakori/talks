# Introduction to Pygments

This is a presentation given at the pyGRAZ user group meeting in Graz,
Austria, on 4 April 2017.

Pygments is a Python package for syntax highlighting over 300
programming languages and text format. Many popular web sites, services
and tools use Pygments to make source code or code snipplets easier to
read.

The intended audience are developers who have to maintain source code in
various languages and sometimes want to process it in an automatic
manner. Furthermore developers who want to extend Pygments with lexers
for very new or obscure languages can take away suggestions on how to do
that.

Topics covered during the talk are:

1. How to use pygmentize to convert source code to syntax highlighted
   HTML or other formats. This is useful to include easy to read source
   code examples into other documents such as articles or a master
   thesis.
2. How to use the Pygment's API to find an appropriate lexer for a source
   code and split it into tokens. This can be used to analyze or convert
   existing source code. Example applications are tools to analyze source
   code for conformance to coding guidelines, convert legacy source code
   into an easier to maintain variant or implement site specific build
   tools.
3. How to write a new lexer. This is done as life coding starting from a
   skeleton RegexLexer and gradually adding regular expression to
   increasingly recognize more tokens. The example language is a
   simplified variant of SQL, showcasing comments, keywords and strings
   (with escape mechanics for quotes inside a string) and more. These
   are elements available in many
