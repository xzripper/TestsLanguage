# TestsLanguage - Simple language for tests!
[/-|-\\]

# About
Simple language for tests, line unittest, but, um, easier!
This language writen on clear Python, with only 1 user library (Colorama)!
Version - 1.0;

# Syntax.
It's look like...
```
#use <module>;

$ Is plus function works normally;
@plus(5, 5) => 10;
```

# Run.
```
tl *.tl N
```

First argument - file.
Second argument - print exit code.

# Learn it in 10 minutes!
```
$ It's a commentary! All lines must have semicolon at end, commentaries too!;
$ Lets import a module!;
#use <ModuleName>;

$ Lets create a tests!;
@Function(5, 5) => 10;
@Function(10, 10) => 20;
```

ModuleName.py
```python
def Function(a, b):
    return a + b
```

# Exceptions.
Lets make an error.
```
$ "Function" - not exists;
@Function(5, 5) => 10;
```

If we run this, we see this.
```

An exception raised;
    TLObjectUndefined: name 'Function' is not defined;
;Exc

```

How you see, exceptions in lang is readable and easy to understand.

# API.
You can use language API! You can parse file myself step by step!
Here is example:

Tests1.tl
```
#use <module>;

@func(1, 1) => 2;
@func(2, 2) => 4;
```

Main.py
```python
from tl import TestsLanguage

my_file = TestsLanguage('Tests1.tl')
print(my_file.getteststree())
```

It's will return this:
```python
{'func(1, 1)': 2, 'func(2, 2)': 4}
```

# Python & TestsLanguage!
You can use python in source of file!
Example:
```
#use <module>;

print('Checking 1 out of 2!');
@foo(5, 5) => 10;

print('Checking 2 out of 2!');
@foo(10, 5) => 15;
```
Yeah, that's cool!

# Cache cleaning.
At end of programm, app automatically cleans a cache.

# Simplicity.
This language is very easy! You can run it just in one line! Language is small, and this is big plus! You can learn it just in 30 minutes.

# Install.
Install code, unpack it to your directory, delete README and LICENSE. Next do next command in cmd. ```pip install colorama```. Done!

# License.
Mit License.

# End.
Thank you for reading! I hope you liked this is language! Have a good day, bye!
