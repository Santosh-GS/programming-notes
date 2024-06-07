# Based on pep8 style guide : https://peps.python.org/pep-0008/

# Naming Conventions and Various Cases
"""
SNAKE CASE:
lower caps with semicolons
used for general variables, functions, modules while naming and importing
my_variable = 123
def my_function() :
main.py
import pandas_datareader

SCREAMING SNAKE CASE: (upper snake case, macro case)
all upper caps with semicolons
used for constant variables
PI = 3.14
ACCELERATION_DUE_TO_GRAVITY = 9.81
SCREEN_HEIGHT, SCREEN_WIDTH = 1920, 1080

PASCAL CASE: (Upper Camel Case)
first capital letter for each word without any space
used for classes and exceptions (exception is a class in python)
class BaseClass
class XException

CAMEL CASE:
pascal case with the very first letter in lower case
rarely used in some python modules
used to declare variable in other languages like java, cpp, etc.
int myVariableName
cv2.destroyAllWindows()

KEBAB CASE: (lisp case, caterpillar case)
snake case with dashes
used while installing packages
pip install opencv-python
pip install pandas-datareader (but "import pandas_datareader" while importing)
pip install -U scikit-learn

FLAT CASE:
all lower caps with no spaces
rarely used, only for packages
mypackage

COBOL CASE:
upper snake case with dashes
not used usually
MY-VARIABLE-NAME

References:
https://www.youtube.com/watch?v=D4_s3q038I0
https://www.youtube.com/watch?v=uet8ZQpyJV8
"""

# General Guidelines
"""
* Limit each line to 80 characters
* Indentation using 4 Spaces
* Keep object names as detailed as possible
* Be consistent with single and double quotes for strings and characters
* Preferably use one space around operators
  except while showing precedence of operators and default values inside function parameter declaration
  final_sum = a*b + c*d
  def my_color_function(color="black", imag=0.0)
* Use self for method, cls for classmethod, *args and **kwargs when using
* Seperate any top level classes and function with 2 blank lines

* Import everything at top and import one module per line (after module docstring)
* While importing from a module, import multiple in the same line
  from os import path, stat
* Avoid wilcard import (everything from a module)
  from os import * (don't do this)
* Import alphabetically, first std libraries and then user defined ones

* Use triple double-quotes for docstring
* Module docstring goes before imports
* start writing in the same line of docstring initiation

* Use 2 spaces before # in one-liner (in-line) comments and 1 space after #
* Mostly white space goes after a comma except between a trailing comma and closing paranthesis
  foo = (0,)
  my_list = [1, 2, 3]

* Use "is" instead of "==" while checking for None
  x = None
  if x is None:
      do_this
* if foo is not x:
  if not foo is x: (equivalent to not (foo is x) but not (not foo) is x)
  both are equivalent but prefer the former one as "is not" kinda acts like a single operator

* Except a specific exception instead of empty except error in try-except statements

* if foo.startswith("bar"):  # Preferred
  if foo[:3] == "bar":
  prefer .startswith or .endswith instead of slice for more accuracy and performance

References:
https://youtu.be/D4_s3q038I0
"""

# Complete Comprehensive Style Guide at https://gist.github.com/RichardBronosky/454964087739a449da04
