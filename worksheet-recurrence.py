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

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">2.5</span> <span class="title">Worksheet: linear recurrences</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-370">For this worksheet, the reader is directed to Section 7.5 of <em class="emphasis">Linear Algebra with Applications</em>, by Keith Nicholson. You will probably want to read this section before proceeding.</p></div>

# <div class="mathbook-content"><p id="p-371">A <em xmlns:svg="http://www.w3.org/2000/svg" class="emphasis">linear recurrence</em> of length $k$ is a sequence $[x_n)$ that is recursively defined, with successive terms in the sequence defined in terms of the previous $k$ terms, via a linear recursion formula of the form</p><div class="displaymath">
# \begin{equation*}
# x_{n+k} = a_0x_k + a_1x_{k+1}+\cdots + a_{k-1}x_{n+k-1}\text{.}
# \end{equation*}
# </div><p class="continuation">(Here we assume $a_0\neq 0$ to have the appropriate length.) The most famous example of a linear recurrence is, of course, the Fibonacci sequence, which is defined by $x_0=1, x_1=1\text{,}$ and $x_{n+2}=x_n+x_{n+1}$ for all $n\geq 0\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-372">As demonstrated in the Nicholson's book, the set of all sequences satisfying a linear recursion of length $k$ form a subspace $V$ of the vector space $\mathbb{R}^\infty$ of all real-valued sequences. Since each sequence is determined by the $k$ initial conditions $x_0, x_1, \ldots, x_{k-1}\text{,}$ we see that $V$ is isomorphic to $\mathbb{R}^k\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-373">The goal of this worksheeet is to understand how to obtain <em class="emphasis">closed form</em> expressions for a recursively defined sequence using linear algebra. That is, rather than having to generate terms of the sequence one-by-one using the recursion formula, we want a function of $n$ that will produce each term $x_n$ in the sequence.</p></div>

# <div class="mathbook-content"><p id="p-374">Since we know the dimension of the space $V$ of solutions, it suffices to understand two things:</p><ul class="disc"><li id="li-80"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-375">How to produce a basis for $V\text{.}$</p></li><li id="li-81"><p id="p-376">How to write a given solution in terms of that basis.</p></li></ul></div>

# <div class="mathbook-content"><p id="p-377">The key observation is that for each recursion relation, there is an associated polynomial. For the recursion</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# x_{n+k} = a_0x_k + a_1x_{k+1}+\cdots + a_{k-1}x_{n+k-1}\text{,}
# \end{equation*}
# </div><p class="continuation">the associated polynomial is</p><div class="displaymath">
# \begin{equation*}
# p(x) = x^k - a_{k-1}x^{k-1}-\cdots -a_1x-a_0\text{.}
# \end{equation*}
# </div></div>

# <div class="mathbook-content"><p id="p-378">The key result is Theorem 7.5.4 in Nicholson. If we can factor $p(x)$ completely over the reals as</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# p(x) = (x-\lambda_1)^{m_1}(x-\lambda_2)^{m_2}\cdots (x-\lambda_p)^{m_p}\text{,}
# \end{equation*}
# </div><p class="continuation">then a basis for the space of solutions is given by</p><div class="displaymath">
# \begin{align*}
# \left[\lambda_1^n\right), \amp \left[n\lambda_1^n\right),\ldots, \left[n^{m_1-1}\lambda_1^n\right)\\
# \left[\lambda_2^n\right), \amp \left[n\lambda_2^n\right),\ldots, \left[n^{m_2-1}\lambda_2^n\right)\\
# \amp \vdots \\
# \left[\lambda_p^n\right), \amp \left[n\lambda_p^n\right),\ldots, \left[n^{m_p-1}\lambda_p^n\right)\text{.}
# \end{align*}
# </div></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-379">Once we have a basis, we can apply the given coefficients to determine how to write a particular sequence as a linear combination of the basis vectors.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-32"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><p id="p-380">Find a basis for the space $V$ of sequences $[x_n)$ satisfying the recurrence</p><div class="displaymath">
# \begin{equation*}
# x_{n+3}=-2x_n+x_{n+1}+2x_{n+2}\text{.}
# \end{equation*}
# </div><p class="continuation">Then find a formula for the sequence satisfying the initial conditions $x_0=1, x_1=2, x_2=1\text{.}$</p></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-381">To solve this problem, you may use Python code, as outlined below. To get started, load the SymPy library.</p></div>

# In[ ]:


from sympy import *
x = symbols('x')
init_printing()


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-382">The associated polynomial for the recurrence is:</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-383">(Input your polynomial here. You can type <code class="code-inline tex2jax_ignore">$</code> to enter and exit math mode in a Markdown cell, and you can use <code class="code-inline tex2jax_ignore">^</code> to enter exponents.)</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-384">Next, factor the polynomial. You can do this using the <code class="code-inline tex2jax_ignore">factor()</code> command. In Python, you will need to enter <code class="code-inline tex2jax_ignore">**</code> for the exponents.</p></div>

# In[ ]:





# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-385">If you are doing this worksheet in Jupyter, change the cell below to Markdown. In it, list the roots of the polynomial, and the resulting basis $B$ for the space $V$ of solutions. Recall that if $\lambda$ is a root of the polynomial, then $[\lambda^n)$ will be a basis vector for the vector space $V$ of solutions. You may wish to confirm that each of your basis sequences indeed satisfies our recursion.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-386">Next, let $s=[x_n)$ be the recursion that satisfies the given initial conditions. We want to write $[x_n)$ in terms of the basis we just found. Recall, from Nicholson, that since our basis has three elements, there is an isomorphism $T:\R^3\to V\text{,}$ where $T(a,b,c)$ is equal to the sequence $[x_n)$ in $V$ that satisfies the initial conditions $x_0=a, x_1=b, x_2=c\text{.}$ Thus, our desired sequence is given by $s=T(1,2,1)\text{.}$</p></div>

# <div class="mathbook-content"><p id="p-387">Let $\vv_1, \vv_2, \vv_3\in\R^3$ be the vectors such that $B=\{T(\vv_1), T(\vv_2), T(\vv_3)\}\text{.}$ (That is, write out the first three terms in each sequence in your basis to get three vectors.) We then need to find scalars $c_1,c_2,c_3$ such that</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# c_1\vv_1+c_2\vv_2+c_3\vv_3=(1,2,1)\text{.}
# \end{equation*}
# </div><p class="continuation">We will then have</p><div class="displaymath">
# \begin{align*}
# s \amp = T(1,2,1)\\
# \amp = c_1T(\vv_1)+c_2T(\vv_2)+c_3T(\vv_3)\text{,}
# \end{align*}
# </div><p class="continuation">and we recall that the sequences $T(\vv_i)$ are the sequences in our basis $B\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-388">Set up this system, and then use the computer to solve. Let <code class="code-inline tex2jax_ignore">A</code> be the coefficient matrix for the system, and let <code class="code-inline tex2jax_ignore">B</code> be the column vector containing the initial conditions.</p></div>

# In[ ]:


A = Matrix()
B = Matrix([1,2,1])
X = A**(-1)*B
X


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-389">Using the solution above, state the answer to this exercise.</p></div>

# In[ ]:





# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-390">Now, we leave you with two more exercises. Recall that if the associated polynomial for your recursion has a repeated root $(x-\lambda)^k\text{,}$ then your basis will include the sequences $[\lambda^n), [n\lambda^n), \ldots, [n^{k-1}\lambda^n)\text{.}$</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-33"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><p id="p-391">Find a basis for the space \$V\$ of sequences $[x_n)$ satisfying the recurrence</p><div class="displaymath">
# \begin{equation*}
# x_{n+3} = -4x_n+3x_{n+2}\text{.}
# \end{equation*}
# </div><p class="continuation">Then find a formula for the sequence satisfying the initial conditions $x_0=1, x_1=-1, x_2=1\text{.}$</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-34"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">3<span class="period">.</span></span></h6><p id="p-392">Find a basis for the space \$V\$ of sequences $[x_n)$ satisfying the recurrence</p><div class="displaymath">
# \begin{equation*}
# x_{n+3} = 8x_n-12x_{n+1}+6x_{n+2}\text{.}
# \end{equation*}
# </div><p class="continuation">Then find a formula for the sequence satisfying the initial conditions $x_0=1, x_1=-1, x_2=1\text{.}$</p></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-393">Our last exercise is more theoretical, and less computational. Recall that the <em class="emphasis">shift operator</em> $S$ on the vector space $\R^\infty$ of sequences is the operator that deletes the first entry of a sequence. (So the remaining entries get “shifted” once to the left.)</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-35"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">4<span class="period">.</span></span></h6><p id="p-394">Show that the shift operator is onto, but not one-to-one. Then, determine the kernel of the shift operator.</p></article></div>
