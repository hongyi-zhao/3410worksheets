#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('html', '', '<link href="https://pretextbook.org/beta/mathbook-content.css" rel="stylesheet" type="text/css" />\n<link href="https://aimath.org/mathbook/mathbook-add-on.css" rel="stylesheet" type="text/css" />\n<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400italic,600,600italic" rel="stylesheet" type="text/css" />\n<link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700&subset=latin,latin-ext" rel="stylesheet" type="text/css" /><!-- Hide this cell. -->\n<script>\nvar cell = $(".container .cell").eq(0), ia = cell.find(".input_area")\nif (cell.find(".toggle-button").length == 0) {\nia.after(\n    $(\'<button class="toggle-button">Toggle hidden code</button>\').click(\n        function (){ ia.toggle() }\n        )\n    )\nia.hide()\n}\n</script>')


# **Important:** to view this notebook properly you will need to execute the cell above, which assumes you have an Internet connection.  It should already be selected, or place your cursor anywhere above to select.  Then press the "Run" button in the menu bar above (the right-pointing arrowhead), or press Shift-Enter on your keyboard.

# $\newcommand{\spn}{\operatorname{span}}
# \newcommand{\bbm}{\begin{bmatrix}}
# \newcommand{\ebm}{\end{bmatrix}}
# \newcommand{\R}{\mathbb{R}}
# \renewcommand{\C}{\mathbb{C}}
# \newcommand{\im}{\operatorname{im}}
# \newcommand{\nll}{\operatorname{null}}
# \newcommand{\csp}{\operatorname{col}}
# \newcommand{\rank}{\operatorname{rank}}
# \newcommand{\diag}{\operatorname{diag}}
# \newcommand{\tr}{\operatorname{tr}}
# \newcommand{\dotp}{\!\boldsymbol{\cdot}\!}
# \newcommand{\len}[1]{\lVert #1\rVert}
# \newcommand{\abs}[1]{\lvert #1\rvert}
# \newcommand{\proj}[2]{\operatorname{proj}_{#1}{#2}}
# \newcommand{\bz}{\overline{z}}
# \newcommand{\zz}{\mathbf{z}}
# \newcommand{\uu}{\mathbf{u}}
# \newcommand{\vv}{\mathbf{v}}
# \newcommand{\ww}{\mathbf{w}}
# \newcommand{\xx}{\mathbf{x}}
# \newcommand{\yy}{\mathbf{y}}
# \newcommand{\zer}{\mathbf{0}}
# \newcommand{\basis}[2]{\{\mathbf{#1}_1,\mathbf{#1}_2,\ldots,\mathbf{#1}_{#2}\}}
# \newcommand{\lt}{<}
# \newcommand{\gt}{>}
# \newcommand{\amp}{&}
# $

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Section</span> <span class="codenumber">A.2</span> <span class="title">Python basics</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-750">OK, so you've logged into Syzygy and you're ready to write some code. What does basic code look like in Python? The good news is that you don't need to be a programmer to do linear algebra in Python. Python includes many different <em class="emphasis">libraries</em> that keep most of the code under the hood, so all you have to remember is what command you need to use to accomplish a task. That said, it won't hurt to learn a little bit of basic coding.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-751">Basic arithmetic operations are understood, and you can simply type them in. Hit <code class="code-inline tex2jax_ignore">shift+enter</code> in a code cell to execute the code and see the result.</p></div>

# In[ ]:


3+4


# In[ ]:


3*4


# In[ ]:


3**4


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-752">OK, great. But sometimes we want to do calculations with more than one step. For that, we can assign variables.</p></div>

# In[ ]:


a = 14
b = -9
c = a+b
print(a, b, c)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-753">Sometimes you might need input that's a string, rather than a number. We can do that, too.</p></div>

# In[ ]:


string_var = "Hey, look at my string!"
print(string_var)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-754">Another basic construction is a list. Getting the hang of lists is useful, because in a sense, matrices are just really fancy lists.</p></div>

# In[ ]:


empty_list = list()
this_too = []
list_of_zeros = [0]*7
print(list_of_zeros)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-755">Once you have an empty list, you might want to add something to it. This can be done with the <code class="code-inline tex2jax_ignore">append</code> command.</p></div>

# In[ ]:


empty_list.append(3)
print(empty_list)
print(len(empty_list))


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-756">Go back and re-run the above code cell two or three more times. What happens? Probably you can guess what the <code class="code-inline tex2jax_ignore">len</code> command is for. Now let's get really carried away and do some “for real” coding, like loops!</p></div>

# In[ ]:


for i in range(10):
    empty_list.append(i)
print(empty_list)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-757">Notice the indentation in the second line. This is how Python handles things like for loops, with indentation rather than bracketing. We could say more about lists but perhaps it's time to talk about matrices. For further reading, you can <a class="external" href="https://developers.google.com/edu/python/lists" target="_blank">start here</a>.</p></div>
