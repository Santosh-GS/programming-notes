# General Guidelines
A quick guide on few general and specific guidelines in Python   
Based on PEP 8 style guide : https://peps.python.org/pep-0008/ or https://pep8.org/

* Limit each line to 80 characters
* Indent using 4 Spaces
* Keep object names as descriptive as possible
* Be consistent with single and double quotes for strings and characters
* Preferably use one space around operators  
  Except while showing precedence of operators and for default values in function parameter declaration  
  `final_sum = a*b + c*d`  
  `def my_color_function(color="black", imag=0.0):`
* Conventionally use `self` for method, `cls` for classmethod, `*args` and `**kwargs` when using
* Seperate any top level classes and function with 2 blank lines and nested ones with 1 blank line  
  <br>
* Import everything at top and import one module per line (after module docstring)
* While importing from a single module, import multiple in the same line  
  `from os import path, stat`
* Avoid wilcard import (importing everything from a module)  
  `from os import *` **(Don't do this)**
* Import alphabetically, first std libraries and then the user defined ones  
  <br>
* Use triple double-quotes for docstring
* Module docstring goes before imports
* start writing in the same line of docstring initiation  
  <br>
* Use 2 spaces before `#` in one-liner (in-line) comments and 1 space after `#`
* Mostly white space goes after a comma except between a trailing comma and closing paranthesis  
  `foo = (0,)`  
 `my_list = [1, 2, 3]`  
  <br>
* Use `is` instead of `==` while checking for `None`  
  `x = None`  
  `if x is None: do_this()`
* `if foo is not x:`  
  `if not foo is x:` (equivalent to `not (foo is x)` but not `(not foo) is x`  
  both are equivalent but prefer the former one as `is not` kinda acts like a single operator  
  <br>
* Except a specific exception instead of empty except error in try-except statements  
  <br>
* `if foo.startswith("bar"):`  (Preferred)  
  `if foo[:3] == "bar":`  
  prefer `.startswith` or `.endswith` instead of slice (allegedly for better accuracy and performance)  

### References:
https://youtu.be/D4_s3q038I0

### Full Guide
A comprehensive style guide is available at https://gist.github.com/RichardBronosky/454964087739a449da04
