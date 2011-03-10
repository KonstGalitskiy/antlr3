""" @package antlr3
@brief ANTLR3 runtime package

This module contains all support classes, which are needed to use recognizers
generated by ANTLR3.

@mainpage

\note Please be warned that the line numbers in the API documentation do not
match the real locations in the source code of the package. This is an
unintended artifact of doxygen, which I could only convince to use the
correct module names by concatenating all files from the package into a single
module file...

Here is a little overview over the most commonly used classes provided by
this runtime:

@section recognizers Recognizers

These recognizers are baseclasses for the code which is generated by ANTLR3.

- BaseRecognizer: Base class with common recognizer functionality.
- Lexer: Base class for lexers.
- Parser: Base class for parsers.
- tree.TreeParser: Base class for %tree parser.

@section streams Streams

Each recognizer pulls its input from one of the stream classes below. Streams
handle stuff like buffering, look-ahead and seeking.

A character stream is usually the first element in the pipeline of a typical
ANTLR3 application. It is used as the input for a Lexer.

- ANTLRStringStream: Reads from a string objects. The input should be a unicode
  object, or ANTLR3 will have trouble decoding non-ascii data.
- ANTLRFileStream: Opens a file and read the contents, with optional character
  decoding.
- ANTLRInputStream: Reads the date from a file-like object, with optional
  character decoding.

A Parser needs a TokenStream as input (which in turn is usually fed by a
Lexer):

- CommonTokenStream: A basic and most commonly used TokenStream
  implementation.
- TokenRewriteStream: A modification of CommonTokenStream that allows the
  stream to be altered (by the Parser). See the 'tweak' example for a usecase.

And tree.TreeParser finally fetches its input from a tree.TreeNodeStream:

- tree.CommonTreeNodeStream: A basic and most commonly used tree.TreeNodeStream
  implementation.
  

@section tokenstrees Tokens and Trees

A Lexer emits Token objects which are usually buffered by a TokenStream. A
Parser can build a Tree, if the output=AST option has been set in the grammar.

The runtime provides these Token implementations:

- CommonToken: A basic and most commonly used Token implementation.
- ClassicToken: A Token object as used in ANTLR 2.x, used to %tree
  construction.

Tree objects are wrapper for Token objects.

- tree.CommonTree: A basic and most commonly used Tree implementation.

A tree.TreeAdaptor is used by the parser to create tree.Tree objects for the
input Token objects.

- tree.CommonTreeAdaptor: A basic and most commonly used tree.TreeAdaptor
implementation.


@section Exceptions

RecognitionException are generated, when a recognizer encounters incorrect
or unexpected input.

- RecognitionException
  - MismatchedRangeException
  - MismatchedSetException
    - MismatchedNotSetException
    .
  - MismatchedTokenException
  - MismatchedTreeNodeException
  - NoViableAltException
  - EarlyExitException
  - FailedPredicateException
  .
.

A tree.RewriteCardinalityException is raised, when the parsers hits a
cardinality mismatch during AST construction. Although this is basically a
bug in your grammar, it can only be detected at runtime.

- tree.RewriteCardinalityException
  - tree.RewriteEarlyExitException
  - tree.RewriteEmptyStreamException
  .
.

"""

# tree.RewriteRuleElementStream
# tree.RewriteRuleSubtreeStream
# tree.RewriteRuleTokenStream
# CharStream
# DFA
# TokenSource

# [The "BSD licence"]
# Copyright (c) 2005-2008 Terence Parr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__version__ = 'HEAD'

def version_str_to_tuple(version_str):
    import re
    import sys

    if version_str == 'HEAD':
        return (sys.maxint, sys.maxint, sys.maxint, sys.maxint)

    m = re.match(r'(\d+)\.(\d+)(\.(\d+))?(b(\d+))?', version_str)
    if m is None:
        raise ValueError("Bad version string %r" % version_str)

    major = int(m.group(1))
    minor = int(m.group(2))
    patch = int(m.group(4) or 0)
    beta = int(m.group(6) or sys.maxint)

    return (major, minor, patch, beta)


runtime_version_str = __version__
runtime_version = version_str_to_tuple(runtime_version_str)


from constants import *
from dfa import *
from exceptions import *
from recognizers import *
from streams import *
from tokens import *