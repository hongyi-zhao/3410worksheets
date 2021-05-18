#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
# \newcommand{\gt}{>}
# \newcommand{\amp}{&}
# $

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">2.4</span> <span class="title">Worksheet: matrix transformations</span></h6></div>

# <div class="mathbook-content"></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-340">This worksheet deals with matrix transformations, and in particular, kernel and image. The goal is to understand these important subspaces in a familiar context.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-341">Let $A$ be an $m\times n$ matrix. We can use $A$ to define a transformation $T_A:\R^n\to \R^m$ given by $T_A(\vec{x})=A\vec x\text{,}$ where we view $\vec x$ as an $n\times 1$ column vector.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-342">The <dfn class="terminology">kernel</dfn> of $T_A$ is the set of vectors $\vec x$ such that $T_A(\vec x)=\vec 0\text{.}$ That is, $\ker T_A$ is the set of solutions to the homogeneous system $A\vec x = \vec 0\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-343">The <dfn class="terminology">image</dfn> of $T_A$ (also known as the range of $T_A$) is the set of vectors $\vec y\in \R^m$ such that $\vec y = A\vec x$ for some $\vec{x}\in\R^n\text{.}$ In other words, $\im(T_A)$ is the set of vectors $\vec y$ for which the non-homogeneous system $A\vec x=\vec y$ is consistent.</p></div>

# <div class="mathbook-content"><p id="p-344">Because $T_A$ is a linear transformation, we can compute it as long as we're given its values on a basis. If $\{\vec{v}_1, \vec{v}_2,\ldots, \vec{v}_n\}$ is a basis for $\R^n\text{,}$ then for any $\vec{x}\in\R^n$ there exist unique scalars $c_1,c_2,\ldots, c_n$ such that</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \vec{x} = c_1\vec{v}_1+c_2\vec{v}_2+\cdots + c_n\vec{v}_n\text{,}
# \end{equation*}
# </div><p class="continuation">and since $T_A$ is linear, we have</p><div class="displaymath">
# \begin{equation*}
# T_A(\vec{x})=c_1T_A(\vec{v}_1)+c_2T_A(\vec{v}_2)+\cdots +c_nT_A(\vec{v}_n)\text{.}
# \end{equation*}
# </div></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-345">The main challenge, computationally speaking, is that if our basis is not the standard basis, some effort will be required to write $\vec x$ in terms of the given basis.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-30"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><div class="introduction" id="introduction-5"><p id="p-346">A linear transformation $T:\R^4\to \R^4$ is defined as follows:</p><div class="displaymath">
# \begin{equation*}
# T\left(\begin{bmatrix}1\\0\\2\\3\end{bmatrix}\right)=\begin{bmatrix}3\\0\\2\\-1\end{bmatrix},
# T\left(\begin{bmatrix}4\\2\\0\\-3\end{bmatrix}\right)=\begin{bmatrix}1\\2\\0\\5\end{bmatrix},
# T\left(\begin{bmatrix}0\\4\\-3\\2\end{bmatrix}\right)=\begin{bmatrix}4\\2\\2\\4\end{bmatrix},
# T\left(\begin{bmatrix}3\\5\\-2\\1\end{bmatrix}\right)=\begin{bmatrix}2\\4\\0\\10\end{bmatrix}\text{.}
# \end{equation*}
# </div><p id="p-347">Let $\{\vec{e}_1,\vec{e}_2,\vec{e}_3, \vec{e}_4\}$ denote the standard basis for $\R^4\text{.}$</p></div><article class="task exercise-like" id="task-3"><h6 class="heading"><span class="codenumber">(a)</span></h6><p id="p-348">Confirm that</p><div class="displaymath">
# \begin{equation*}
# B=\left\{\begin{bmatrix}1\\0\\2\\3\end{bmatrix},\begin{bmatrix}4\\2\\0\\-3\end{bmatrix},
# \begin{bmatrix}0\\4\\-3\\2\end{bmatrix}, \begin{bmatrix}3\\5\\-2\\1\end{bmatrix}\right\}
# \end{equation*}
# </div><p class="continuation">is a basis for $\R^4\text{.}$</p></article><article class="task exercise-like" id="task-4"><h6 class="heading"><span class="codenumber">(b)</span></h6><p id="p-349">Write each of the standard basis vectors in terms of this basis.</p><p id="p-350"><em class="emphasis">Suggestion:</em> in each case, this can be done by solving a matrix equation, using the inverse of an appropriate matrix.</p></article><article class="task exercise-like" id="task-5"><h6 class="heading"><span class="codenumber">(c)</span></h6><p id="p-351">Determine $T(\vec{e}_i)$ for $i=1,2,3,4\text{,}$ and in so doing, determine the matrix $A$ such that $T=T_A\text{.}$</p></article><article class="task exercise-like" id="task-6"><h6 class="heading"><span class="codenumber">(d)</span></h6><p id="p-352">Let $M$ be the matrix whose columns are given by the values of $T$ on the basis $B\text{.}$ (This would be the matrix of $T$ if $B$ was actually the standard basis.) Let $N$ be the matrix whose inverse you used to solve part (b). Can you find a way to combine these matrices to obtain the matrix $A\text{?}$ If so, explain why your result makes sense.</p></article></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-353">To assist with solving this problem, a code cell is provided below. Recall that you can enter the matrix $\begin{bmatrix}a\amp b\amp c\\d\amp e\amp f\\g\amp h\amp i\end{bmatrix}$ as <code class="code-inline tex2jax_ignore">Matrix([[a,b,c],[d,e,f],[g,h,i]])</code> or as <code class="code-inline tex2jax_ignore">Matrix(3,3,[a,b,c,d,e,f,g,h,i])</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-354">The reduced row-echeleon form of <code class="code-inline tex2jax_ignore">A</code> is given by <code class="code-inline tex2jax_ignore">A.rref()</code>. The product of matrices <code class="code-inline tex2jax_ignore">A</code> and <code class="code-inline tex2jax_ignore">B</code> is simply <code class="code-inline tex2jax_ignore">A*B</code>. The inverse of a matrix <code class="code-inline tex2jax_ignore">A</code> can be found using <code class="code-inline tex2jax_ignore">A.inv()</code> or simply <code class="code-inline tex2jax_ignore">A**(-1)</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-355">One note of caution: if you don't import <code class="code-inline tex2jax_ignore">sympy</code> as your first line of code, you'll instead use Sage syntax. Sage uses <code class="code-inline tex2jax_ignore">A.inverse()</code> instead of <code class="code-inline tex2jax_ignore">A.inv()</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-356">In a Jupyter notebook, remember you can generate additional code cells by clicking on the <code class="code-inline tex2jax_ignore">+</code> button.</p></div>

# ## Solution to Part (a): 
# 
# we know that a matrix is invertible if any only if its columns are independent. So to show the vectors are independent (which will imply that they span, since we have 4 vectors in $\mathbb{R}^4$), it suffices to show that the matrix $N=\begin{bmatrix}1&4&0&3\\0&2&4&5\\2&0&-3&-2\\3&-3&2&1\end{bmatrix}$ whose columns are the given vectors is invertible.
# 
# For later use, I will first define the column vectors in the basis $B$, and then concatenate them to get the matrix $N$.

# In[2]:


from sympy import *
init_printing(wrap_line=False)
V1=Matrix([1,0,2,3])
V2=Matrix([4,2,0,-3])
V3=Matrix([0,4,-3,2])
V4=Matrix([3,5,-2,1])
V1,V2,V3,V4


# In[3]:


N=Matrix(BlockMatrix([V1,V2,V3,V4]))
N


#In [103]: A4 == N
#Out[103]: True


# Wrapping `BlockMatrix` in `Matrix` gets rid of extra brackets around each column. (I found this on [StackOverflow](https://stackoverflow.com/questions/50606675/build-matrices-from-block-matrices-in-sympy).) You can also use the `row_join` command (from the [SymPy documentation](https://docs.sympy.org/latest/tutorial/matrices.html)) as follows:

# In[ ]:


A2=V1.row_join(V2)
A3=A2.row_join(V3)
A4=A3.row_join(V4)
A4


# Finally, we confirm that the matrix is invertible, which implies that its columns (the vectors in $B$) are linearly independent.

# In[4]:


N.det()


# Since $\det N \neq 0$, the matrix $N$ is invertible, and our vectors form a basis.

# ### Solution to part (b):
# 
# Suppose $x_1\vec{v}_1+x_2\vec{v}_2+x_3\vec{v}_3+x_4\vec{v}_4=\vec{e}_i$, where the $\vec{v}_j$ are the given basis vectors. This is equivalent to the matrix equation $N\vec{x}=\vec{e}_i$, where $N$ is the matrix from part (a), and $\vec{x} = \begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}$.
# 
# A solution to this equation is given by $\vec{x}=N^{-1}\vec{e}_i$, and since $\vec{e}_i$ is a standard basis vector, we know that $N^{-1}\vec{e}_i$ is the $i$th column of $N^{-1}$. In fact, the columns of $N^{-1}$ are precisely the coefficients we need.

# In[6]:


B=N**(-1)
B


# From the above, we have:
# 
# $$\begin{aligned}
# \vec{e}_1 &= 19\vec{v}_1+33\vec{v}_2+46\vec{v}_3-50\vec{v}_4\\
# \vec{e}_2 &= -23\vec{v}_1-40\vec{v}_2-56\vec{v}_3+61\vec{v}_4\\
# \vec{e}_3 &= -24\vec{v}_1-42\vec{v}_2-59\vec{v}_3+64\vec{v}_4\\
# \vec{e}_4 &= 10\vec{v}_1+17\vec{v}_2+24\vec{v}_3-26\vec{v}_4\end{aligned}$$
# 
# Let us confirm this fact:

# In[7]:


19*V1+33*V2+46*V3-50*V4,-23*V1-40*V2-56*V3+61*V4,-24*V1-42*V2-59*V3+64*V4,10*V1+17*V2+24*V3-26*V4


# ### Solution to part (c)
# 
# Since $T$ is a linear transformation, we know that
# $$T(\vec{e}_1)=19T(\vec{v}_1)+33T(\vec{v}_2)+46T(\vec{v}_3)-50T(\vec{v}_4)=19\vec{w}_1+33\vec{w}_2+46\vec{w}_3-50\vec{w}_4,$$
# with similar results for the other three vectors, where we define $\vec{w}_i = T(\vec{v}_i)$ for $i=1,2,3,4$.
# 
# Let us now input the vectors $\vec{w}_i$, which are given above.

# In[8]:


W1 = Matrix([3,0,2,-1])
W2 = Matrix([1,2,0,5])
W3 = Matrix([4,2,2,4])
W4 = Matrix([2,4,0,10])
W1,W2,W3,W4


# Next, let us define $\vec{y}_i = T(\vec{e}_i)$ for $i=1,2,3,4$, and compute the results.

# In[9]:


Y1=19*W1+33*W2+46*W3-50*W4
Y2=-23*W1-40*W2-56*W3+61*W4
Y3=-24*W1-42*W2-59*W3+64*W4
Y4=10*W1+17*W2+24*W3-26*W4
Y1,Y2,Y3,Y4


# Now, we recall that the columns of the matrix $A$ such that $T(\vec{x})=T_A(\vec{x})=A\vec{x}$ are given by $T(\vec{e}_i)$, $i=1,2,3,4$. It follows that we have:

# In[10]:


A = Matrix(BlockMatrix([Y1,Y2,Y3,Y4]))
A


# If we want to check our work, we can make sure that the transformation $T_A$ defined using the matrix $A$ has the correct values on the original basis $B$:

# In[11]:


A*V1,A*V2,A*V3,A*V4


# In[12]:


A*V1==W1, A*V2==W2, A*V3==W3, A*V4==W4


# ### Solution to part (d)
# 
# Let us think about our original transformation. Given a vector $\vec{x}$, we can write
# $$\vec{x} = c_1\vec{v}_1+c_2\vec{v}_2+c_3\vec{v}_3+c_4\vec{v}_4,$$
# and then
# $$T(\vec{x}) = c_1\vec{w}_1+c_2\vec{w}_2+c_3\vec{w}_3+c_4\vec{w}_4.$$
# 
# Let $M$ be the matrix whose columns are the vectors $\vec{w}_i$:
# 

# In[13]:


M=Matrix(BlockMatrix([W1,W2,W3,W4]))
M


# Notice that 
# $$T(\vec{x}) = c_1\vec{w}_1+c_2\vec{w}_2+c_3\vec{w}_3+c_4\vec{w}_4 = M\begin{bmatrix}c_1\\c_2\\c_3\\c_4\end{bmatrix}=M\vec{c}.$$
# 
# We would like to compute $T(\vec{x})$ using the matrix $A$ instead. The matrix $A$ was constructed so that $T(\vec{x})=A\vec{x}$. Notice that we have $M\vec{c}=T(\vec{x})=A\vec{x}$. But we also have $\vec{x}=N\vec{c}$ from above. So
# $$M\vec{c}=A(N\vec{c})=(AN)\vec{c}.$$
# 
# Since $\vec{x}$ (and hence, $\vec{c}$) was arbitrary, we must have $M=AN$, and therefore, $A=MN^{-1}$. Let us check:

# In[15]:


M*(N**-1),A


# In[16]:


A == M*(N**-1)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-357">Next we will compute the kernel and image of the transformation from the previous exercise. Recall that when solving a homogeneous system $A\vec x = \vec 0\text{,}$ we find the <abbr class="initialism">RREF</abbr> of $A\text{,}$ and any variables whose columns do not contain a leading 1 are assigned as parameters. We then express the general solution $x$ in terms of those parameters.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-358">The image of a matrix transformation $T_A$ is also known as the <dfn class="terminology">column space</dfn> of $A\text{,}$ because the range of $T_A$ is precisely the span of the columns of $A\text{.}$ The <abbr class="initialism">RREF</abbr> of $A$ tells us which columns to keep: the columns of $A$ that correspond to the columns in the <abbr class="initialism">RREF</abbr> of $A$ with a leading 1.</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-31"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><div class="introduction" id="introduction-6">Let $T$ be the linear transformation given in the previous exercise.</div><article class="task exercise-like" id="task-7"><h6 class="heading"><span class="codenumber">(a)</span></h6><p id="p-359">Determine the kernel of $T\text{.}$</p></article><article class="task exercise-like" id="task-8"><h6 class="heading"><span class="codenumber">(b)</span></h6><p id="p-360">Determine the image of $T\text{.}$</p></article><article class="task exercise-like" id="task-9"><h6 class="heading"><span class="codenumber">(c)</span></h6><p id="p-361">The <dfn class="terminology">Dimension Theorem</dfn> states that for a linear transformation $T:V\to W\text{,}$ where $V$ is finite-dimensional,</p><div class="displaymath">
# \begin{equation*}
# \dim V = \dim\ker(T)+ \dim\im(T)\text{.}
# \end{equation*}
# </div><p class="continuation">Explain why this result makes sense using your results for this problem.</p></article></article></div>

# ### Solution to parts (a) and (b)
# 
# To determine the kernel and image of $T$, it suffices to find the reduced row-echelon form of $A$, and interpret appropriately.

# In[17]:


A.rref()


# If $\vec{x} = \begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}$ belongs to $\ker(T)$, then $A\vec{x}=\vec{0}$. The first row of the RREF above tells us that $x_1=\frac{25}{31}x_3-\frac{15}{31}x_4$, and $x_2 = -\frac{12}{31}x_3+\frac{1}{31}x_4$. Thus,
# 
# $$\vec{x} = \begin{bmatrix}\frac{25}{31}x_3-\frac{15}{31}x_4\\-\frac{12}{31}x_3+\frac{1}{31}x_4\\x_3\\x_4\end{bmatrix} = \frac{x_3}{31}\begin{bmatrix}25\\-15\\31\\0\end{bmatrix}+\frac{x_4}{31}\begin{bmatrix}-12\\1\\0\\31\end{bmatrix}.$$
# 
# It follows that 
# $$\ker(T) = \operatorname{span}\left\{\begin{bmatrix}25\\-15\\31\\0\end{bmatrix},\begin{bmatrix}-12\\1\\0\\31\end{bmatrix}\right\}.$$
# 
# 
# We also know that the image of $T$ is spanned by the columns of $A$ that correspond to the columns with leading ones in the RREF of $A$. Therefore,
# 
# $$\operatorname{im}(T) = \operatorname{span}\left\{\begin{bmatrix}174\\-42\\130\\-170\end{bmatrix}, \begin{bmatrix}-211\\52\\-158\\209\end{bmatrix}\right\}.$$

# One point worth noting: to determine the kernel of $T$, we really do need the matrix $A$. Otherwise, we would first have to write the vector $\vec{x}$ in terms of the original basis $B$. Solving $N\vec{x}=\vec{0}$ would give us the coefficients needed to write an element of the kernel in terms of $B$, rather than the standard basis.
# 
# This might be useful in some cases, but we should be sure to distinguish between the two.
# 
# On the other hand, the values of $T$ on the basis $B$ were already expressed in terms of the standard basis. So we could equally well use the RREF of the matrix $M$ to determine the image of $T$. Since $M$ is a simpler matrix (or at least, its entries are numerically smaller), we might prefer the results we get from that.

# In[18]:


M.rref(),M


# Notice that the rank of $M$ (number of leading ones) is the same as that of $A$. So we could equally well have written the image of $T$ as
# 
# $$\operatorname{im}(T) = \operatorname{span}\left\{\begin{bmatrix}3\\0\\2\\-1\end{bmatrix}, \begin{bmatrix}1\\2\\0\\5\end{bmatrix}\right\}.$$
# 
# You can confirm that the vectors we found above can be written in terms of these vectors, and vice-versa.
# 
# For example, let us confirm that the system $x\begin{bmatrix}174\\-42\\130\\-170\end{bmatrix}+y\begin{bmatrix}-211\\52\\-158\\209\end{bmatrix}=\begin{bmatrix}3\\0\\2\\-1\end{bmatrix}$ has a solution.

# In[ ]:


X1=Matrix(BlockMatrix([A.col(0),A.col(1),M.col(0)]))
X1,X1.rref()


# And if we wanted to do the second column of $M$ instead:

# In[ ]:


X2=Matrix(BlockMatrix([A.col(0),A.col(1),M.col(1)]))
X2,X2.rref()


# In[23]:


G=-V1-V2+V3
A*G


# ### Solution to part (c)
# 
# In this example, we have $T:\R^4\to \R^4$, and $\dim \R^4=4$. We just found that $\dim \ker(T)=2$ and $\dim\im(T)=2$. So indeed, $\dim \R^4 = \dim \ker(T)+\dim\im(T)$.
# 
# This makes sense, since the matrix of $T$ is a $4\times 4$ matrix, with the 4 columns of $A$ corresponding to the dimension of the domain $\R^4$. (We need 4 columns to multiply on the right by a $4\times 1$ column vector.)
# 
# The dimension of $\ker(T)$ is equal to the number of parameters in the general solution to the homogeneous system $A\vec{x}=\vec{0}$, and this is equal to the number of columns in the RREF of $A$ that do not have leading ones.
# 
# On the other hand, the dimension of $\im(T)$ is equal to the number of leading ones in the RREF of $A$. So the dimension theorem, in this case, boils down to the simple fact that the numnber of columns with leading ones, plus the number of columns without leading ones, is equal to the total number of columns!
