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
# \newcommand{\vecq}{\mathbf{q}}
# \newcommand{\vecp}{\mathbf{p}}
# \newcommand{\vece}{\mathbf{e}}
# \newcommand{\basis}[2]{\{\mathbf{#1}_1,\mathbf{#1}_2,\ldots,\mathbf{#1}_{#2}\}}
# \newcommand{\gt}{>}
# \newcommand{\amp}{&}
# $

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">1.4</span> <span class="title">Worksheet: understanding span</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-97">In this worksheet, we will attempt to understand the concept of span. Recall from <a href="sec-span.ipynb" class="internal" title="Section 1.3: Span">Section 1.3</a> that the span of a set of vectors $\vv_1, \vv_2,\ldots, \vv_k$ in a vector space $V$ is the set of all linear combinations that can be generated from those vectors.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-98">Therefore, the question “Does the vector $\ww$ belong to the span of $\vv_1, \vv_2,\ldots, \vv_k\text{?}$” is equivalent to asking, “Can I write $\ww$ as a linear combination of the $\vv_i\text{?}$”, which, in turn, is equivalent to asking:</p></div>

# <div class="mathbook-content"><p id="p-99">Do there exist scalars $c_1,c_2,\ldots, c_k$ such that</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \ww=c_1\vv_1+c_2\vv_2+\cdots +c_k\vv_k\text{?}
# \end{equation*}
# </div></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-100">In any finite-dimensional vector space, this last question can be turned into a system of equations. If that system has a solution, then yes — your vector is in the span. If the system is inconsistent, then the answer is no.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-6"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><p id="p-101">Determine whether or not the vector $\ww=\langle 3,-1, 4, 2\rangle$ in $\R^4$ belongs to the span of the vectors</p><div class="displaymath">
# \begin{equation*}
# \langle 2, 1, 4, -3\rangle, \langle 0, 2, 1, 4\rangle, \langle -1, 1, 0, 2\rangle\text{.}
# \end{equation*}
# </div></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-102">To assist with solving this problem, a code cell is provided below. Once you have determined the augmented matrix of your system of equations, see <a href="sec-sympy.ipynb" class="internal" title="Section A.3: SymPy for linear algebra">Section A.3</a> for details on how to enter your matrix, and then compute its reduced row-echelon form.</p></div>

# In[ ]:


from sympy import *
init_printing()


# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-7"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><p id="p-103">Determine whether or not the polynomial $q(x) = 4-6x-11x^2$ belongs to the span of the polynomials</p><div class="displaymath">
# \begin{equation*}
# p_1(x) = x-3x^2, p_2(x)=2-x, p_3(x) = -1+4x+x^2\text{.}
# \end{equation*}
# </div></article></div>

# In[ ]:





# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-104">For our next activity, we are going to look at <abbr class="initialism">RGB</abbr> colours. Here, <abbr class="initialism">RGB</abbr> stands for Red, Green, Blue. All colours displayed by your computer monitor can be expressed in terms of these colours.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-105">First, we load some Python libraries we'll need. These are intended for use in a Jupyter notebook and won't run properly if you are using Sagecell in the <abbr class="initialism">HTML</abbr> textbook.</p></div>

# In[ ]:


import ipywidgets as wid
import matplotlib.pyplot as plt


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-106">Next, we will create a widget that lets us select values for red, green, and blue. The <abbr class="initialism">RGB</abbr> colour system assigns 8-bit values to each colour. Possible values for each range from 0 to 255; this indicates how much of each colour will be blended to create the colour you want. Extensive information on the <abbr class="initialism">RGB</abbr> colour system can be found <a class="external" href="https://en.wikipedia.org/wiki/RGB%5Fcolor%5Fmodel" target="_blank">on wikipedia</a>, and there are a number of good online resources about the use of <abbr class="initialism">RGB</abbr> in web design, <a class="external" href="https://www.w3schools.com/colors/colors%5Frgb.asp" target="_blank">such as this one from w3schools</a>.</p></div>

# In[ ]:


r=wid.IntSlider(
    value=155,
    min=0,
    max=255,
    step=1,
    description='Red:'
)
g=wid.IntSlider(
    value=155,
    min=0,
    max=255,
    step=1,
    description='Green:'
)
b=wid.IntSlider(
    value=155,
    min=0,
    max=255,
    step=1,
    description='Blue:'
)
display(r,g,b)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-107">By moving the sliders generated above, you can create different colours. To see what colour you've created by moving the sliders, run the code below.</p></div>

# In[ ]:


plt.imshow([[(r.value/255, g.value/255, b.value/255)]])


# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-8"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">3<span class="period">.</span></span></h6><p id="p-108">In what ways can you explain the <abbr class="initialism">RGB</abbr> colour system in terms of span?</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-9"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">4<span class="period">.</span></span></h6><p id="p-109">Why would it nonetheless be inappropriate to describe the set of all <abbr class="initialism">RGB</abbr> colours as a vector space?</p></article></div>
