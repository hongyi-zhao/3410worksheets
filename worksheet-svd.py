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

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">4.6</span> <span class="title">Worksheet: Singular Value Decomposition</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-725">For this worksheet, the reader is directed to Section 8.6 of <em class="emphasis">Linear Algebra with Applications</em>, by Keith Nicholson, and, of course, to <a href="section-matrix-factor.ipynb" class="internal" title="Section 4.5: Matrix Factorizations and Eigenvalues">Section 4.5</a>. (See also <a class="external" href="https://www.juanklopper.com/wp-content/uploads/2015/03/III%5F05%5FSingular%5Fvalue%5Fdecomposition.html" target="_blank">notebook by Dr. Juan H Klopper</a>.)</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-726">In <a href="section-matrix-factor.ipynb" class="internal" title="Section 4.5: Matrix Factorizations and Eigenvalues">Section 4.5</a> we saw that the <code class="code-inline tex2jax_ignore">svd</code> algorithm in the mpmath library does things a little bit differently than Nicholson. If we start with a square matrix $A\text{,}$ the results are the same, but if $A$ is not square, the decomposition $A = P\Sigma_A Q^T$ looks a little different. In particular, if $A$ is $m\times n\text{,}$ the matrix $\Sigma_A$ defined in Nicholson will also be $m\times n\text{,}$ but it will contain some rows or columns of zeros that are added to get the desired size. The matrix $Q$ is an orthogonal $n\times n$ matrix whose columns are an orthonormal basis of eigenvectors for $A^TA\text{.}$ The matrix $P$ is an orthogonal $m\times m$ matrix whose columns are an orthonormal basis of $\R^m\text{.}$ (The first $r$ columns of $P$ are given by $A\vecq_i\text{,}$ where $\vecq_i$ is the eigenvector of $A^TA$ corresponding to the positive singular value $\sigma_i\text{.}$)</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-727">The <code class="code-inline tex2jax_ignore">svd</code> algorithm provided by mpmath replaces $\Sigma_A$ by the $m\times m$ diagonal matrix of singular values. The matrix $Q$ is replaced by the $m\times n$ matrix whose columns are the first $m$ eigenvectors of $A^TA\text{.}$ (Note that the rank of $A^TA$ is equal to the rank of $A\text{,}$ which is equal to the number of nonzero eigenvectors of $A^TA$ (counted with multiplicity).) So we will have $m\geq r\text{,}$ where $r$ is the number of nonzero singular values.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-728">The product $\Sigma_A Q^T$ will be the same in both cases, and the matrix $P$ is the same as well.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-729">This time, rather than using the mpmath algorithm, we will work through the process as outlined in Nicholson step-by-step. First, we will work through (again) Example 8.6.1 in Nicholson. Let $A = \bbm 1\amp 0\amp 1\\-1\amp 1\amp 0\ebm\text{.}$ First, we get the singular values:</p></div>

# In[ ]:


from sympy import *
init_printing()
A = Matrix([[1,0,1],[-1,1,0]])
L0=A.singular_values()
L0


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-730">Next, we get the eigenvalues and eigenvectors of $A^TA\text{:}$</p></div>

# In[ ]:


B = (A.T)*A
L1=B.eigenvects()
L1


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-731">Now we need to normalize the eigenvectors, in the correct order. Note that the eigenvectors were listed in <em class="emphasis">increasing</em> order of eigenvalue, so we need to reverse the order. Note that <code class="code-inline tex2jax_ignore">L1</code> is a list of lists. The eigenvector is the third entry (index 2) in the list (eigenvalue, multiplicity, eigenvector). We also need to turn list elements into matrices. So, for example the second eigenvector is <code class="code-inline tex2jax_ignore">Matrix(L1[1][2])</code>.</p></div>

# In[ ]:


R1=Matrix(L1[2][2])
R2=Matrix(L1[1][2])
R3=Matrix(L1[0][2])
Q1 = (1/R1.norm())*R1
Q2 = (1/R2.norm())*R2
Q3 = (1/R3.norm())*R3
Q1,Q2,Q3


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-732">Next, we can assemble these vectors into a matrix, and confirm that it's orthogonal.</p></div>

# In[ ]:


Q = Matrix(BlockMatrix([Q1,Q2,Q3]))
Q,Q*Q.T


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-733">We've made the matrix $Q\text{!}$ Next, we construct $\Sigma_A\text{.}$ This we will do by hand.</p></div>

# In[ ]:


SigA = Matrix([[L0[0],0,0],[0,L[1],0])
SigA


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-734">Alternatively, you could do <code class="code-inline tex2jax_ignore">SigA = diag(L0[0],L0[1]).row_join(Matrix([0,0]))</code>. Finally, we need to make the matrix $P\text{.}$ First, we find the vectors $A\vecq_1, A\vecq_2$ and normalize. (Note that $A\vecq_3=\zer\text{,}$ so this vector is unneeded, as expected.)</p></div>

# In[ ]:


S1 = A*Q1
S2 = A*Q2
P1 = (1/S1.norm())*S1
P2 = (1/S2.norm())*S2
P = Matrix(BlockMatrix([P1,P2]))
P


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-735">Note that the matrix $P$ is already the correct size, because $\rank(A)=2\dim(\R^2)\text{.}$ In general, for an $m\times n$ matrix $A\text{,}$ if $\rank(A)=r\lt m\text{,}$ we would have to extend the set $\{\vecp_1,\ldots, \vecp_r\}$ to a basis for $\R^m\text{.}$ Finally, we check that our matrices work as advertised.</p></div>

# In[ ]:


P*SigA*(Q.T)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-736">For convenience, here is all of the above code, with all print commands (except the last one) removed. This can be run as a single code cell.</p></div>

# <div class="mathbook-content"><figure class="listing figure-like" id="listing-svd"><div class="code-box" style="width: 100%; margin-left: 0%; margin-right: 0%;"><pre class="program"><code class="language-none">from sympy import *
# init_printing()
# A = Matrix([[1,0,1],[-1,1,0]])
# B=(A.T)*A
# L0=A.singular_values()
# L1=B.eigenvects()
# R1=Matrix(L1[2][2])
# R2=Matrix(L1[1][2])
# R3=Matrix(L1[0][2])
# Q1 = (1/R1.norm())*R1
# Q2 = (1/R2.norm())*R2
# Q3 = (1/R3.norm())*R3
# Q = Matrix(BlockMatrix([Q1,Q2,Q3]))
# SigA = diag(L0[0],L0[1]).row_join(Matrix([0,0]))
# S1 = A*Q1
# S2 = A*Q2
# P1 = (1/S1.norm())*S1
# P2 = (1/S2.norm())*S2
# P = Matrix(BlockMatrix([P1,P2]))
# P,SigA,Q,P*SigA*Q.T
# </code></pre></div><figcaption xmlns:svg="http://www.w3.org/2000/svg"><span class="type">Listing</span><span class="space"> </span><span class="codenumber">4.6.1<span class="period">.</span></span><span class="space"> </span>SymPy code for a singular value decomposition example</figcaption></figure></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-51"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><p id="p-737">Do Exercise 8.6.9 in Nicholson: compute the SVD for the matrices</p><div class="displaymath">
# \begin{equation*}
# \bbm 1\amp -1\\1\amp 0\\0\amp 1\ebm \quad \quad \bbm 1\amp 1\amp 1\\-1\amp 0\amp 2 \\1\amp 2\amp 0\ebm\text{.}
# \end{equation*}
# </div><p class="continuation">Note that for these matrices, you will need to do some additional work to extend the $\vecp_i$ vectors to an orthonormal basis. You can adapt the code above, but you will have to think about how to implement additional code to construct any extra vectors you need.</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-52"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><p id="p-738">Either by reading Nicholson or by searching online (or both), come up with a couple of answers to the question: “Why are people interested in the singular value decomposition?”</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-53"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">3<span class="period">.</span></span></h6><p id="p-739">(Optional) If you are interested, learn how to compute the <abbr class="initialism">SVD</abbr> using tools from the NumPy and SciPy libraries instead.</p></article></div>
