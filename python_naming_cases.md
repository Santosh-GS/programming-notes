# Python Naming Cases

A quick guide on various naming cases and the places where the case is used in Python  
Conventions are based on PEP 8 Style Guide available at https://peps.python.org/pep-0008/ or https://pep8.org/

### Snake Case:
lower caps with underscores  
used for general variables, functions, modules while naming and imports  
`my_variable = 123`  
`def my_function():`  
`main.py`  
`import pandas_datareader`  

### Screaming Snake Case: (Upper Snake Case, Macro Case)
all upper caps with semicolons  
used for constant variables  
`PI = 3.14`  
`ACCELERATION_DUE_TO_GRAVITY = 9.81`  
`SCREEN_HEIGHT, SCREEN_WIDTH = 1920, 1080`  

### Pascal Case: (Upper Camel Case)
first capital letter for each word without any spaces  
used for classes and exceptions (exception is a class in python)  
`class BaseClass`  
`class XException`  

### Camel Case:
pascal case where the very first letter is in lower case  
rarely used in some python modules  
used to declare variable in other languages like java, cpp, etc.  
`int myVariableName`  
`cv2.destroyAllWindows()`  

### Kebab Case: (lisp case, caterpillar case)
snake case with dashes  
used while installing packages  
`pip install opencv-python`  
`pip install pandas-datareader` (but use `import pandas_datareader` while importing)  
`pip install -U scikit-learn`  

### Flat Case:
all lower caps with no spaces  
rarely used, only for packages  
`mypackage`  

### Cobol Case:
upper snake case with dashes  
not used usually  
`MY-VARIABLE-NAME`

### Video References:  
[Write Python Code Properly!](https://www.youtube.com/watch?v=D4_s3q038I0)  
[Python Case Types and Naming Conventions](https://www.youtube.com/watch?v=uet8ZQpyJV8)   
