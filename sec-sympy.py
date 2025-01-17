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

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Section</span> <span class="codenumber">A.3</span> <span class="title">SymPy for linear algebra</span></h6></div>

# <div class="mathbook-content"></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-758"><dfn class="terminology">SymPy</dfn> is a Python library for symbolic algebra. On its own, it's not as powerful as programs like Maple, but it handles a lot of basic manipulations in a fairly simple fashion, and when we need more power, it can interface with other Python libraries.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-759">Another advantage of SymPy is sophisticated “pretty-printing”. In fact, we can enable MathJax within SymPy, so that output is rendered in the same way as when LaTeX is entered in a markdown cell.</p></div>

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Subsection</span> <span class="codenumber">A.3.1</span> <span class="title">SymPy basics</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-760">Running the following Sage cell will load the SymPy library and turn on MathJax.</p></div>

# In[ ]:


#https://discuss.python.org/t/the-span-lines-problem-when-p-eigenvects-displays-some-too-long-expressions/8769/2?u=hongyi-zhao
#Jean Abou Samra
#jeanas
#2h

#I think you want to replace

#sympy.init_printing()

#with

#sympy.init_printing(wrap_line=False)

#The output of help(sympy.init_printing) explains all possible parameters.

#For more info, see:
#In [97]: init_printing?
#In [98]: help(init_printing)

from sympy import *
#init_printing()
init_printing(wrap_line=False)



# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-761"><em class="alert">Note:</em> if you are going to be working with multiple libraries, and more than one of them defines a certain command, instead of <code class="code-inline tex2jax_ignore">from sympy import all</code> you can do <code class="code-inline tex2jax_ignore">import sympy as sy</code>. If you do this, each SymPy command will need to be appended with <code class="code-inline tex2jax_ignore">sy</code>; for example, you might write <code class="code-inline tex2jax_ignore">sy.Matrix</code> instead of simply <code class="code-inline tex2jax_ignore">Matrix</code>. Let's use SymPy to create a $2\times 3$ matrix.</p></div>

# In[ ]:


A = Matrix(2,3,[1,2,3,4,5,6])
A


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-762">The <code class="code-inline tex2jax_ignore">A</code> on the second line asks Python to print the matrix using SymPy's printing support. If we use Python's <code class="code-inline tex2jax_ignore">print</code> command, we get something different:</p></div>

# In[ ]:


print(A)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-763">We'll have more on matrices in <a href="sec-sympy.ipynb#subsec-sympy-matrix" class="internal" title="Subsection A.3.2: Matrices in SymPy">Subsection A.3.2</a>. For now, let's look at some more basic constructions. One basic thing to be mindful of is the type of numbers we're working with. For example, if we enter <code class="code-inline tex2jax_ignore">2/7</code> in a code cell, Python will interpret this as a floating point number (essentially, a division).</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-764">(If you are using Sage cells in HTML rather than Jupyter, this will automatically be interpreted as a fraction.)</p></div>

# In[ ]:


2/7


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-765">But we often do linear algebra over the rational numbers, and so SymPy will let you specify this:</p></div>

# In[ ]:


Rational(2,7)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-766">You might not think to add the comma above, because you're used to writing fractions like $2/7\text{.}$ Fortunately, the SymPy authors thought of that:</p></div>

# In[ ]:


Rational(2/7)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-767">Hmm... You might have got the output you expected in the cell above, but maybe not. If you got a much worse looking fraction, read on.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-768">Another cool command is the <code class="code-inline tex2jax_ignore">sympify</code> command, which can be called with the shortcut <code class="code-inline tex2jax_ignore">S</code>. The input <code class="code-inline tex2jax_ignore">2</code> is interpreted as an <code class="code-inline tex2jax_ignore">int</code> by Python, but <code class="code-inline tex2jax_ignore">S(2)</code> is a “SymPy <code class="code-inline tex2jax_ignore">Integer</code>”:</p></div>

# In[ ]:



#https://stackoverflow.com/questions/41860294/what-does-s-signify-in-sympy
#For more info, check it with:
#In [28]: S??

S(2)/7


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-769">Of course, sometimes you <em class="emphasis">do</em> want to use floating point, and you can specify this, too:</p></div>

# In[ ]:


2.5


# In[ ]:


Float(2.5)


# In[ ]:


Float(2.5e10)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-770">One note of caution: <code class="code-inline tex2jax_ignore">Float</code> is part of SymPy, and not the same as the core Python <code class="code-inline tex2jax_ignore">float</code> command. You can also put decimals into the Rational command and get the corresponding fraction:</p></div>

# In[ ]:


Rational(0.75)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-771">The only thing to beware of is that computers convert from decimal to binary and then back again, and sometimes weird things can happen:</p></div>

# In[ ]:


Rational(0.2)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-772">Of course, there are workarounds. One way is to enter $0.2$ as a string:</p></div>

# In[ ]:


Rational('0.2')


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-773">Another is to limit the size of the denominator:</p></div>

# In[ ]:


Rational(0.2).limit_denominator(10**12)


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-774">Try some other examples above. Some inputs to try are <code class="code-inline tex2jax_ignore">1.23</code> and <code class="code-inline tex2jax_ignore">23e-10</code></p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-775">We can also deal with repeating decimals. These are entered as strings, with square brackets around the repeating part. Then we can “sympify”:</p></div>

# In[ ]:


S('0.[1]')


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-776">Finally, SymPy knows about mathematical constants like $e, \pi, i\text{,}$ which you'll need from time to time in linear algebra. If you ever need $\infty\text{,}$ this is entered as <code class="code-inline tex2jax_ignore">oo</code>.</p></div>

# In[ ]:


I*I


# In[ ]:


I-sqrt(-1)


# In[ ]:


pi.is_irrational


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-777">Finally, from time to time you may need to include parameters (variables) in an expression. Typical code for this is of the form <code class="code-inline tex2jax_ignore">a, b, c = symbols('a b c', real = True, constant = True)</code>. Here, we introduce the symbols <code class="code-inline tex2jax_ignore">a,b,c</code> with the specification that they represent real-valued constants.</p></div>

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Subsection</span> <span class="codenumber">A.3.2</span> <span class="title">Matrices in SymPy</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-778">Here we collect some of the SymPy commands used throughout this text, for ease of reference. For further details, please consult the <a class="external" href="https://docs.sympy.org/latest/modules/matrices/matrices.html" target="_blank">online documentation</a>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-779">To create a $2\times 3$ matrix, we can write either <code class="code-inline tex2jax_ignore">A=Matrix(2,3,[1,2,3,4,5,6])</code> or <code class="code-inline tex2jax_ignore">A=Matrix([[1,2,3],[4,5,6]])</code>, where of course the size and entries can be changed to whatever you want. The former method is a bit faster, but once your matrices get a bit bigger, the latter method is less prone to typos.</p></div>

# In[ ]:


A=Matrix(2,3,[1,2,3,4,5,6])
B=Matrix([[1,2,3],[4,5,6]])
A,B


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-780">Also of note: a column vector $\bbm 1\\2\\3\ebm$ can be entered using <code class="code-inline tex2jax_ignore">Matrix([1,2,3])</code>. There are also certain built in special matrices. To get an $n\times n$ identity matrix, use <code class="code-inline tex2jax_ignore">eye(n)</code>. To get an $m\times n$ zero matrix, use <code class="code-inline tex2jax_ignore">zeros(m,n)</code>, or <code class="code-inline tex2jax_ignore">zeros(n)</code> for a square matrix. There is also syntax for diagonal matrices, such as <code class="code-inline tex2jax_ignore">diag(1,2,3)</code>. What's cool is that you can even use this for block diagonal matrices:</p></div>

# In[ ]:


A=Matrix(2,2,[1,2,3,4])
B=Matrix(2,2,[5,6,7,8])
D=diag(A,B)
D


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-781">To get the reduced row-echelon form of the matrix $A\text{,}$ simply use <code class="code-inline tex2jax_ignore">A.rref()</code>. Addition, subtraction, and multiplication use the obvious syntax: <code class="code-inline tex2jax_ignore">A+B</code>, <code class="code-inline tex2jax_ignore">A\*B</code>, etc.. The determinant of a square matrix is given by <code class="code-inline tex2jax_ignore">A.det()</code>. Inverses can be computed using <code class="code-inline tex2jax_ignore">A.inv()</code> or <code class="code-inline tex2jax_ignore">A\*\*-1</code>. The latter is rather natural, since powers in general are entered as <code class="code-inline tex2jax_ignore">A\*\*n</code> for $A^n\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-782">In most cases where you want to reduce a matrix, you're going to want to simply use the <code class="code-inline tex2jax_ignore">rref</code> function. But there are times where this can be overzealous; for example, if you have a matrix with one or more symbols. One option is to replace <code class="code-inline tex2jax_ignore">A.rref()</code> with <code class="code-inline tex2jax_ignore">A.echelon\_form()</code>. The <code class="code-inline tex2jax_ignore">echelon\_form</code> function creates zeros in the pivot columns, but does not create leading on ones.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-783">For example, let's take the matrix $A = \bbm a \amp 2\amp b\\2\amp 1\amp a\\2a\amp b\amp 3\ebm\text{.}$ Note the difference in output between <code class="code-inline tex2jax_ignore">rref</code> and <code class="code-inline tex2jax_ignore">echelon\_form</code>.</p></div>

# In[ ]:

#https://docs.sympy.org/latest/tutorial/matrices.html#rref
#To put a matrix into reduced row echelon form, use rref. rref returns a tuple of two elements. The first is the reduced row echelon form, and the second is a tuple of indices of the pivot columns.

#https://en.wikipedia.org/wiki/Row_echelon_form#Reduced_row_echelon_form
a = Symbol('a')
b = Symbol('b')
A = Matrix(3,3,[a,2,b,2,1,a,2*a,b,3])
A, A.rref(), A.echelon_form()


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-784">It is possible to manually perform row operations when you need additional control. This is achieved using the function <code class="code-inline tex2jax_ignore">A.elementary\_row\_op(&lt;arguments>)</code>, with arguments <code class="code-inline tex2jax_ignore">op,row,k,row1,row2</code>.</p></div>

# <div class="mathbook-content"><p id="p-785">We have the following general syntax:</p><ul class="disc"><li id="li-140"><p id="p-786">To swap two rows:</p><ul class="circle"><li id="li-141"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-787"><code class="code-inline tex2jax_ignore">op='n&lt;->m'</code></p></li><li id="li-142"><p id="p-788"><code class="code-inline tex2jax_ignore">row1=i</code>, where <code class="code-inline tex2jax_ignore">i</code> is the index of the first row being swapped (remembering that rows are indexed starting with $0$ for the first row).</p></li><li id="li-143"><p id="p-789"><code class="code-inline tex2jax_ignore">row2=j</code>, where <code class="code-inline tex2jax_ignore">j</code> is the index of the second row being swapped.</p></li></ul></li><li id="li-144"><p id="p-790">To rescale a row:</p><ul class="circle"><li id="li-145"><p id="p-791"><code class="code-inline tex2jax_ignore">op='n->kn'</code></p></li><li id="li-146"><p id="p-792"><code class="code-inline tex2jax_ignore">row=i</code>, where <code class="code-inline tex2jax_ignore">i</code> is the index of the row being rescaled.</p></li><li id="li-147"><p id="p-793"><code class="code-inline tex2jax_ignore">k=c</code>, where <code class="code-inline tex2jax_ignore">c</code> is the value of the scalar you want to multiply by.</p></li></ul></li><li id="li-148"><p id="p-794">To add a multiple of one row to another:</p><ul class="circle"><li id="li-149"><p id="p-795"><code class="code-inline tex2jax_ignore">op='n->n+km'</code></p></li><li id="li-150"><p id="p-796"><code class="code-inline tex2jax_ignore">row=i</code>, where <code class="code-inline tex2jax_ignore">i</code> is the index of the row you want to change.</p></li><li id="li-151"><p id="p-797"><code class="code-inline tex2jax_ignore">k=c</code>, where <code class="code-inline tex2jax_ignore">c</code> is the multiple of the other row.</p></li><li id="li-152"><p id="p-798"><code class="code-inline tex2jax_ignore">row2=j</code>, where <code class="code-inline tex2jax_ignore">j</code> is the index of the other row.</p></li></ul></li></ul></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-799">When studying matrix transformations, we are often interested in the <em class="emphasis">null space</em> and <em class="emphasis">column space</em>, since these correspond to the kernel and image of a linear transformation. This is achieved, simply enough, using <code class="code-inline tex2jax_ignore">A.nullspace()</code> and <code class="code-inline tex2jax_ignore">A.colspace()</code>. The output will be a basis of column vectors for these spaces, and these are exactly the ones you'd find doing Gaussian elimination by hand.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-800">Once you get to orthogonality, you'll want to be able to compute things like dot products, and transpose. These are simple enough. The dot product of vectors <code class="code-inline tex2jax_ignore">X,Y</code> is simply <code class="code-inline tex2jax_ignore">X.dot(Y)</code>. The transpose of a matrix <code class="code-inline tex2jax_ignore">A</code> is <code class="code-inline tex2jax_ignore">A.T</code>. As we should expect, <code class="code-inline tex2jax_ignore">X\dotp Y = X^TY</code>.</p></div>

# In[ ]:


X=Matrix([1,2,3])
Y=Matrix([4,5,6])
X.dot(Y),(X.T)*Y


# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-801">Of course, nobody wants to do things like the Gram Schmidt algorithm by hand. Fortunately, there's a function for that. If we have vectors <code class="code-inline tex2jax_ignore">X,Y,Z</code>, we can make a list <code class="code-inline tex2jax_ignore">L=[X,Y,Z]</code>, and perform Gram Schmidt with <code class="code-inline tex2jax_ignore">GramSchmidt(L)</code>. If you want your output to be an orthonormal basis (and not merely orthogonal), then you can use <code class="code-inline tex2jax_ignore">GramSchmidt(L,true)</code>.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-802">It's useful to note that the output from functions like <code class="code-inline tex2jax_ignore">nullspace()</code> are automatically treated as lists. So one can use simple code like the following:</p></div>

# In[ ]:

#https://www.geeksforgeeks.org/null-space-and-nullity-of-a-matrix/
A=Matrix(2,3,[1,0,3,2,-1,4])
L=A.nullspace()
GramSchmidt(L)

GramSchmidt(L,True)

#https://stackoverflow.com/questions/43777147/creating-sympy-matrices-from-columns
#In [85]: a=.5*eye(2)

#In [86]: a
#Out[86]: 
#⎡0.5   0 ⎤
#⎢        ⎥
#⎣ 0   0.5⎦

#In [87]: GramSchmidt([a.col(i) for i in range(a.cols)],orthonormal=True)
#Out[87]: 
#⎡⎡1.0⎤  ⎡ 0 ⎤⎤
#⎢⎢   ⎥, ⎢   ⎥⎥
#⎣⎣ 0 ⎦  ⎣1.0⎦⎦

#In [88]: GramSchmidt([a.col(i) for i in range(a.cols)],True)
#Out[88]: 
#⎡⎡1.0⎤  ⎡ 0 ⎤⎤
#⎢⎢   ⎥, ⎢   ⎥⎥
#⎣⎣ 0 ⎦  ⎣1.0⎦⎦

#In [89]: GramSchmidt([a.col(i) for i in range(a.cols)])
#Out[89]: 
#⎡⎡0.5⎤  ⎡ 0 ⎤⎤
#⎢⎢   ⎥, ⎢   ⎥⎥
#⎣⎣ 0 ⎦  ⎣0.5⎦⎦

#In [90]: GramSchmidt(([a.col(i) for i in range(a.cols)]),True)
#Out[90]: 
#⎡⎡1.0⎤  ⎡ 0 ⎤⎤
#⎢⎢   ⎥, ⎢   ⎥⎥
#⎣⎣ 0 ⎦  ⎣1.0⎦⎦






# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-803">If for some reason you need to reference particular vectors in a list, this can be done by specifying the index. If <code class="code-inline tex2jax_ignore">L=[X,Y,Z]</code>, then <code class="code-inline tex2jax_ignore">L[0]==X</code>, <code class="code-inline tex2jax_ignore">L[1]==Y</code>, and <code class="code-inline tex2jax_ignore">L[2]==Z</code>.</p></div>

# <div class="mathbook-content"><p id="p-804">Next up is eigenvalues and eigenvectors. Given an $n\times n$ matrix $A\text{,}$ we have the following:</p><ul class="disc"><li id="li-153"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-805">For the characteristic polynomial, use <code class="code-inline tex2jax_ignore">A.charpoly()</code>. However, the result will give you something SymPy calls a “PurePoly”, and the <code class="code-inline tex2jax_ignore">factor</code> command will have no effect. Instead, use <code class="code-inline tex2jax_ignore">A.charpoly().as\_expr()</code>.</p></li><li id="li-154"><p id="p-806">If we know that $3$ is an eigenvalue of a $4\times 4$ matrix $A\text{,}$ one way to get a basis for the eigenspace $E_3(A)$ is to do:</p><pre class="code-display tex2jax_ignore">B=A-3*eye(4)
# B.nullspace()
# </pre><p data-braille="continuation">If you just want all the eigenvalues and eigenvectors without going through the steps, then you can simply execute <code class="code-inline tex2jax_ignore">A.eigenvects()</code>. The result is a list of lists — each list in the list is of the form: eigenvalue, multiplicity, basis for the eigenspace.</p><p id="p-807">For diagonalization, one can do <code class="code-inline tex2jax_ignore">A.diagonalize()</code>. But this will not necessarily produce orthogonal diagonalization for a symmetric matrix.</p></li></ul></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-808">For complex vectors and matrices, the main additional operation we need is the <dfn class="terminology">hermitian conjugate</dfn>. The hermitian conjugate of a matrix <code class="code-inline tex2jax_ignore">A</code> is called using <code class="code-inline tex2jax_ignore">A.H</code>, which is simple enough. Unfortunately, there is no built-in complex inner product, perhaps because mathematicians and physicists cannot agree on which of the two vectors in the inner product should have the complex conjugate applied to it. Since we define the complex inner product by $\langle \zz,\ww\rangle = \zz\dotp\bar{\ww}\text{,}$ we can execute the inner product in SymPy using <code class="code-inline tex2jax_ignore">Z.dot(W.H)</code>, or <code class="code-inline tex2jax_ignore">(W.H)\*Z</code>, although the latter gives the output as a $1\times 1$ matrix rather than a number.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-809">Don't forget that when entering complex matrices, the complex unit is entered as <code class="code-inline tex2jax_ignore">I</code>. Also, complex expressions are not simplified by default, so you will often need to wrap your output line in <code class="code-inline tex2jax_ignore">simplify()</code>. The Sage Cell below contains complete code for the unitary diagonalization of a $2\times 2$ hermitian matrix with distinct eigenvalues. When doing a problem like this in a Sage cell, it's a good idea to execute each line of code (and display output) before moving on to the next. In this case, printing the output for the list <code class="code-inline tex2jax_ignore">L</code> given by <code class="code-inline tex2jax_ignore">A.eigenvects()</code> helps explain the complicated-looking definitions of the vectors <code class="code-inline tex2jax_ignore">v,w</code>. Of course, if we had a matrix with repeated eigenvalues, we'd need to add steps involving Gram Schmidt.</p></div>

# In[ ]:


#In [94]: L[0][2][0] == ((L[0])[2])[0]
#Out[94]: True


from sympy import *
init_printing()
A = Matrix(2,2,[4,3-I,3+I,1])
L = A.eigenvects()
v = ((L[0])[2])[0]
w = ((L[1])[2])[0]
u1 = (1/v.norm())*v
u2 = (1/w.norm())*w
U = u1.row_join(u2)
u1, u2, U, simplify(U.H*A*U)


# <div class="mathbook-content"><p id="p-810">There are a few other commands that might come in handy as you work through this material:</p><ul class="disc"><li id="li-155"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-811">Two matrices can be glued together. If matrices <code class="code-inline tex2jax_ignore">A,B</code> have the same number of rows, the command <code class="code-inline tex2jax_ignore">A.row\_join(B)</code> will glue the matrices together, left-to-right. If they have the same number of columns, <code class="code-inline tex2jax_ignore">A.col\_join(B)</code> will glue them together top-to-bottom.</p></li><li id="li-156"><p id="p-812">To insert a column <code class="code-inline tex2jax_ignore">C</code> into a matrix <code class="code-inline tex2jax_ignore">M</code> (of appropriate size) as the $j$th column, you can do <code class="code-inline tex2jax_ignore">M.col\_insert(j,C)</code>. Just remember that columns are indexed starting at zero, so you might want <code class="code-inline tex2jax_ignore">j-1</code> instead of <code class="code-inline tex2jax_ignore">j</code>. This can be useful for things like solving a system $A\xx=B\text{,}$ where you want to append the column $B$ to the matrix $A\text{.}$</p></li><li id="li-157"><p id="p-813">A $QR$-factorization can be performed using <code class="code-inline tex2jax_ignore">Q,R=A.QRdecomposition()</code></p></li><li id="li-158"><p id="p-814">The Jordan canonical form $M$ of a matrix $A$ can be obtained (along with the matrix $P$ whose columns are a Jordan basis) using <code class="code-inline tex2jax_ignore">P,M=A.jordan\_form()</code>.</p></li></ul></div>
