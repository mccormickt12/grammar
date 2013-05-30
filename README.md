Grammar.py
=================

Grammar.py is a script that takes away the worst aspect of Python, the necessity for perfect whitespace and indentation.  Grammar.py allows the user to completely ignore indentation and focus on the code.  All the user needs to do is add a line containing the word 'end' at the end of any block that does not have a return statement.  Any ```if```, ```else```, ```elif```, ```while```, ```for```, ```def```, ```class```, ```try```, or ```except``` that does not end in a return must have 'end' to denote the end of the block.  Other variations of the word 'end' are ok as long as it starts with 'end'. So for stylistic purposes you could do:

```python
def foo():
print 'hello world'
endfoo
```

To run this script all you need to do is:
		python grammar.py filename.py

And the result will be a file named filename_grammar.py in the directory of the original python file. That file will have the correctly indented python code that you can run.
	     
