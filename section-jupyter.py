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

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Section</span> <span class="codenumber">A.1</span> <span class="title">Jupyter</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-744">The first thing you need to know about doing linear algebra in Python is how to access a Python environment. Fortunately, you do not need to install any software for this. The University of Lethbridge has access to the <dfn class="terminology">Syzygy Jupyter Hub</dfn> service, provided by <abbr class="initialism">PIMS</abbr> (the Pacific Institute for Mathematical Sciences), Cybera, and Compute Canada. To access Syzygy, go to <a class="external" href="https://uleth.syzygy.ca" target="_blank">uleth.syzygy.ca</a> and log in with your ULeth credentials. Below is a video explaining some of the features of our Jupyter hub.</p></div>

# <div class="mathbook-content"><div xmlns:svg="http://www.w3.org/2000/svg" class="video-box" style="width: 95%;padding-top: 53.4375%; margin-left: 2.5%; margin-right: 2.5%;"><iframe id="video-1" class="video" allowfullscreen="" src="https://www.youtube-nocookie.com/embed/VUfp7AQdxhk?&modestbranding=1&rel=0" /></div></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-745">Note: if you click the login button and nothing happens, click the back button and try again. Sometimes there's a problem with our single sign-on service.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-746">The primary type of document you'll encounter on Syzygy is the <dfn class="terminology">Jupyter notebook</dfn>. Content in a Juypter notebook is organized into <dfn class="terminology">cells</dfn>. Some cells contain text, which can be in either <abbr class="initialism">HTML</abbr> or <dfn class="terminology">Markdown</dfn>. Markdown is a simple markup language. It's not as versatile as HTML, but it's easier to use. On Jupyter, markdown supports the LaTeX language for mathematical expressions. Use single dollar signs for inline math: <code class="code-inline tex2jax_ignore">$\frac{d}{dx}\sin(x)=\cos(x)$</code> produces $\frac{d}{dx}\sin(x)=\cos(x)\text{,}$ for example.</p></div>

# <div class="mathbook-content"><p id="p-747">If you want “display math”, use double dollar signs. Unfortunately, entering matrices is a bit tedious. For example, <code class="code-inline tex2jax_ignore">$$A = \begin{bmatrix}1 & 2 & 3\\4 & 5 & 6 &\end{bmatrix}$$</code> produces</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# A = \begin{bmatrix}1\amp 2\amp 3\\4\amp 5\amp 6\end{bmatrix}\text{.}
# \end{equation*}
# </div><p data-braille="continuation">Later we'll see how to enter things like matrices in Python.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-748">It's also possible to use markdown to add <em class="emphasis">emphasis</em>, images, URLs, etc.. For details, see the following <a class="external" href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown cheatsheet</a>, or this <a class="external" href="https://callysto.ca/wp-content/uploads/2018/12/Callysto-Cheatsheet%5F12.19.18%5Fweb.pdf" target="_blank">quick reference</a> from <a class="external" href="https://callysto.ca/" target="_blank">callysto.ca</a>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-749">What's cool about a Jupyter notebook is that in addition to markdown cells, which can present content and provide explanation, we can also include <em class="emphasis">code cells</em>. Jupyter supports many different programming languages, but we will stick mainly to Python.</p></div>
