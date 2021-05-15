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

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">2.4</span> <span class="title">Worksheet: matrix transformations</span></h6></div>

# <div class="mathbook-content"></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-347">This worksheet deals with matrix transformations, and in particular, kernel and image. The goal is to understand these important subspaces in a familiar context.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-348">Let $A$ be an $m\times n$ matrix. We can use $A$ to define a transformation $T_A:\R^n\to \R^m$ given by $T_A(\xx)=A\xx\text{,}$ where we view $\xx$ as an $n\times 1$ column vector.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-349">The <dfn class="terminology">kernel</dfn> of $T_A$ is the set of vectors $\xx$ such that $T_A(\xx)=\zer\text{.}$ That is, $\ker T_A$ is the set of solutions to the homogeneous system $A\xx = \zer\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-350">The <dfn class="terminology">image</dfn> of $T_A$ (also known as the range of $T_A$) is the set of vectors $\yy\in \R^m$ such that $\yy = A\xx$ for some $\xx\in\R^n\text{.}$ In other words, $\im(T_A)$ is the set of vectors $\yy$ for which the non-homogeneous system $A\xx=\yy$ is consistent.</p></div>

# <div class="mathbook-content"><p id="p-351">Because $T_A$ is a linear transformation, we can compute it as long as we're given its values on a basis. If $\{\vv_1, \vv_2,\ldots, \vv_n\}$ is a basis for $\R^n\text{,}$ then for any $\xx\in\R^n$ there exist unique scalars $c_1,c_2,\ldots, c_n$ such that</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \xx = c_1\vv_1+c_2\vv_2+\cdots + c_n\vv_n\text{,}
# \end{equation*}
# </div><p class="continuation">and since $T_A$ is linear, we have</p><div class="displaymath">
# \begin{equation*}
# T_A(\xx)=c_1T_A(\vv_1)+c_2T_A(\vv_2)+\cdots +c_nT_A(\vv_n)\text{.}
# \end{equation*}
# </div></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-352">The main challenge, computationally speaking, is that if our basis is not the standard basis, some effort will be required to write $\xx$ in terms of the given basis.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-30"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><div class="introduction" id="introduction-5"><p id="p-353">A linear transformation $T:\R^4\to \R^4$ is defined as follows:</p><div class="displaymath">
# \begin{equation*}
# T\left(\begin{bmatrix}1\\0\\2\\3\end{bmatrix}\right)=\begin{bmatrix}3\\0\\2\\-1\end{bmatrix},
# T\left(\begin{bmatrix}4\\2\\0\\-3\end{bmatrix}\right)=\begin{bmatrix}1\\2\\0\\5\end{bmatrix},
# T\left(\begin{bmatrix}0\\4\\-3\\2\end{bmatrix}\right)=\begin{bmatrix}4\\2\\2\\4\end{bmatrix},
# T\left(\begin{bmatrix}3\\5\\-2\\1\end{bmatrix}\right)=\begin{bmatrix}2\\4\\0\\10\end{bmatrix}\text{.}
# \end{equation*}
# </div><p id="p-354">Let $\{\vece_1,\vece_2,\vece_3, \vece_4\}$ denote the standard basis for $\R^4\text{.}$</p></div><article class="task exercise-like" id="task-3"><h6 class="heading"><span class="codenumber">(a)</span></h6><p id="p-355">Confirm that</p><div class="displaymath">
# \begin{equation*}
# B=\left\{\begin{bmatrix}1\\0\\2\\3\end{bmatrix},\begin{bmatrix}4\\2\\0\\-3\end{bmatrix},
# \begin{bmatrix}0\\4\\-3\\2\end{bmatrix}, \begin{bmatrix}3\\5\\-2\\1\end{bmatrix}\right\}
# \end{equation*}
# </div><p class="continuation">is a basis for $\R^4\text{.}$</p></article><article class="task exercise-like" id="task-4"><h6 class="heading"><span class="codenumber">(b)</span></h6><p id="p-356">Write each of the standard basis vectors in terms of this basis.</p><p id="p-357"><em class="emphasis">Suggestion:</em> in each case, this can be done by solving a matrix equation, using the inverse of an appropriate matrix.</p></article><article class="task exercise-like" id="task-5"><h6 class="heading"><span class="codenumber">(c)</span></h6><p id="p-358">Determine $T(\vece_i)$ for $i=1,2,3,4\text{,}$ and in so doing, determine the matrix $A$ such that $T=T_A\text{.}$</p></article><article class="task exercise-like" id="task-6"><h6 class="heading"><span class="codenumber">(d)</span></h6><p id="p-359">Let $M$ be the matrix whose columns are given by the values of $T$ on the basis $B\text{.}$ (This would be the matrix of $T$ if $B$ was actually the standard basis.) Let $N$ be the matrix whose inverse you used to solve part (b). Can you find a way to combine these matrices to obtain the matrix $A\text{?}$ If so, explain why your result makes sense.</p></article></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-360">To assist with solving this problem, a code cell is provided below. Recall that you can enter the matrix $\begin{bmatrix}a\amp b\amp c\\d\amp e\amp f\\g\amp h\amp i\end{bmatrix}$ as <code class="code-inline tex2jax_ignore">Matrix([[a,b,c],[d,e,f],[g,h,i]])</code> or as <code class="code-inline tex2jax_ignore">Matrix(3,3,[a,b,c,d,e,f,g,h,i])</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-361">The reduced row-echeleon form of <code class="code-inline tex2jax_ignore">A</code> is given by <code class="code-inline tex2jax_ignore">A.rref()</code>. The product of matrices <code class="code-inline tex2jax_ignore">A</code> and <code class="code-inline tex2jax_ignore">B</code> is simply <code class="code-inline tex2jax_ignore">A*B</code>. The inverse of a matrix <code class="code-inline tex2jax_ignore">A</code> can be found using <code class="code-inline tex2jax_ignore">A.inv()</code> or simply <code class="code-inline tex2jax_ignore">A**(-1)</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-362">One note of caution: if you don't import <code class="code-inline tex2jax_ignore">sympy</code> as your first line of code, you'll instead use Sage syntax. Sage uses <code class="code-inline tex2jax_ignore">A.inverse()</code> instead of <code class="code-inline tex2jax_ignore">A.inv()</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-363">In a Jupyter notebook, remember you can generate additional code cells by clicking on the <code class="code-inline tex2jax_ignore">+</code> button.</p></div>

# In[ ]:


from sympy import *
init_printing()


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-364">Next we will compute the kernel and image of the transformation from the previous exercise. Recall that when solving a homogeneous system $A\xx = \zer\text{,}$ we find the <abbr class="initialism">RREF</abbr> of $A\text{,}$ and any variables whose columns do not contain a leading 1 are assigned as parameters. We then express the general solution $x$ in terms of those parameters.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-365">The image of a matrix transformation $T_A$ is also known as the <dfn class="terminology">column space</dfn> of $A\text{,}$ because the range of $T_A$ is precisely the span of the columns of $A\text{.}$ The <abbr class="initialism">RREF</abbr> of $A$ tells us which columns to keep: the columns of $A$ that correspond to the columns in the <abbr class="initialism">RREF</abbr> of $A$ with a leading 1.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-31"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><div class="introduction" id="introduction-6"><p id="p-366">Let $T$ be the linear transformation given in the previous exercise.</p></div><article class="task exercise-like" id="task-7"><h6 class="heading"><span class="codenumber">(a)</span></h6><p id="p-367">Determine the kernel of $T\text{.}$</p></article><article class="task exercise-like" id="task-8"><h6 class="heading"><span class="codenumber">(b)</span></h6><p id="p-368">Determine the image of $T\text{.}$</p></article><article class="task exercise-like" id="task-9"><h6 class="heading"><span class="codenumber">(c)</span></h6><p id="p-369">The <dfn class="terminology">Dimension Theorem</dfn> states that for a linear transformation $T:V\to W\text{,}$ where $V$ is finite-dimensional,</p><div class="displaymath">
# \begin{equation*}
# \dim V = \dim\ker(T)+ \dim\im(T)\text{.}
# \end{equation*}
# </div><p class="continuation">Explain why this result makes sense using your results for this problem.</p></article></article></div>

# In[ ]:




