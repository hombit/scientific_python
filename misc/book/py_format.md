# Syntax proposal for `.py` files and its relation to Markdown syntax

`.py` files under `scientific_python/` directory are valid Python 2/3 modules.
These files are full of comments that use Markdown-like syntax.

These is a syntax description, the least rules are more weighty, but the first rules are more general:

### Python code

These lines start with any symbol except `#` and should be converted to code blocks.

**Example**

```python
print('Hello world')
```

should transform to

````markdown
```python
print('Hello world')
```
````

### Text
Text is located in comment lines that start with `# ` (with trailing space).

**Example**

```python
# This is a part of the text.
# The text could be long!
```

transforms to

```markdown
This is a part of the text.
The text could be long!
```

### Empty line
Empty lines between comments are empty Markdown lines, and empty lines between code are empty code lines.
Empty lines between code and Markdown lines should be empty Markdown lines.
This is important due Markdown syntax and [PEP8](http://pep8.org).

### Shabang
When file starts with `#!`, the first line should be removed.

### Part of Markdown syntax inside text
Text can contain little parts of Markdown syntax, it just shouldn't be cleaned during transformation.

**Example**

```python
# # Header 1
# ## Header 2
# ### Header 3
# Function `print` prints printable variables
# Latex is supported by some Markdown processors: $E = mc^2$

# **Bold** is not a _crime_
```

transforms to

```markdown
# Header 1
## Header 2
### Header 3
Function `print` prints printable variables
Latex is supported by some Markdown processors: $E = mc^2$

**Bold** is not a _crime_
```

### Code output
The special case of the comment is code output. Such strings are look like ``# `...` ``, where ellipses devote code output. Code output should look different from code blocks and plain text.

The possible transformation is:

```python
print('Hello world')
# `Hello world`
```

to

````markdown
```python
print('Hello world')
```

_Hello world_
````


### Commented code
Sometimes it is useful to comment code that doesn't work or has a bad style. Such strings start with `# >>> ` (with trailing space). In this case ` >>>` (with one of the spaces) should be removed and string should be added to the surrounding code block.

**Example**

```python
# Bad style is commented:
x is not None
# >>> x != None
x == 1
```

transforms to

````markdown
Bad style is commented:

```python
x is not None
# x != None
x == 1
```
````
