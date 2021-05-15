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
# \newcommand{\vecq}{\mathbf{q}}
# \newcommand{\vecp}{\mathbf{p}}
# \newcommand{\vece}{\mathbf{e}}
# \newcommand{\basis}[2]{\{\mathbf{#1}_1,\mathbf{#1}_2,\ldots,\mathbf{#1}_{#2}\}}
# \newcommand{\gt}{>}
# \newcommand{\amp}{&}
# $

# <div class="mathbook-content"><h6 class="heading hide-type"><span xmlns:svg="http://www.w3.org/2000/svg" class="type">Worksheet</span> <span class="codenumber">2.6</span> <span class="title">Worksheet: dual basis.</span></h6></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-395">This worksheet is more theoretically inclined that most of the other workheets so far. But it introduces a useful concept, so it's worth your while to work through it!</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-396">Let $V$ be a vector space over $\R\text{.}$ (That is, scalars are real numbers, rather than, say, complex.) A linear transformation $\phi:V\to \R$ is called a <dfn class="terminology">linear functional</dfn>.</p></div>

# <div class="mathbook-content"><p id="p-397">Here are some examples of linear functionals:</p><ul class="disc"><li id="li-82"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-398">The map $\phi:\R^3\to \R$ given by $\phi(x,y,z) = 3x-2y+5z\text{.}$</p></li><li id="li-83"><p id="p-399">The evaluation map $ev_a:P_n(\R)\to \R$ given by $ev_a(p) = p(a)\text{.}$ (For example, $ev_2(3-4x+5x^2) = 2-4(2)+5(2^2) = 14\text{.}$)</p></li><li id="li-84"><p id="p-400">The map $\phi:\mathcal{C}[a,b]\to \R$ given by $\phi(f) = \int_a^b f(x)\,dx\text{,}$ where $\mathcal{C}[a,b]$ denotes the space of all continuous functions on $[a,b]\text{.}$</p></li></ul></div>

# <div class="mathbook-content"><p id="p-401">Note that for any vector spaces $V,W\text{,}$ the set $\mathcal{L}(V,W)$ of linear transformations from $V$ to $W$ is itself a vector space, if we define</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# (S+T)(v) = S(v)+T(v),\quad \text{ and } \quad (kT)(v)=k(T(v))\text{.}
# \end{equation*}
# </div><p class="continuation">In particular, given a vector space $V\text{,}$ we denote the set of all linear functionals on $V$ by $V^*=\mathcal{L}(V,\R)\text{,}$ and call this the <em class="emphasis">dual space</em> of $V\text{.}$</p></div>

# <div class="mathbook-content"><p id="p-402">We make the following observations:</p><ul class="disc"><li id="li-85"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-403">If $\dim V=n$ and $\dim W=m\text{,}$ then $\mathcal{L}(V,W)$ is isomorphic to the space $M_{mn}$ of $m\times n$ matrices, so it has dimension $mn\text{.}$</p></li><li id="li-86"><p id="p-404">Since $\dim \R=1\text{,}$ if $V$ is finite-dimensional, then $V^*=\mathcal{L}(V,\R)$ has dimension $1n=n\text{.}$</p></li><li id="li-87"><p id="p-405">Since $\dim V^*=\dim V\text{,}$ $V$ and $V^*$ are isomorphic.</p></li></ul></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-406">Here is a basic example that is intended as a guide to your intuition regarding dual spaces. Take $V = \R^3\text{.}$ Given any $v\in V\text{,}$ define a map $\phi_{v}:V\to \R$ by $\phi_{v}(w) = v\dotp w$ (the usual dot product).</p></div>

# <div class="mathbook-content"><p id="p-407">One way to think about this: if we write $v\in V$ as a column vector $\bbm v_1\\v_2\\v_3\ebm\text{,}$ then we can identify $\phi_{v}$ with $v^T\text{,}$ where the action is via multiplication:</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \phi_{v}(w) = \bbm v_1\amp v_2\amp v_3\ebm\bbm w_1\\w_2\\w_3\ebm = v_1w_1+v_2w_2+v_3w_3\text{.}
# \end{equation*}
# </div><p class="continuation">It turns out that this example can be generalized, but the definition of $\phi_v$ involves the dot product, which is particular to $\R^n\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-408">There is a generalization of the dot product, known as an inner product. (See Chapter 10 of Nicholson, for example.) On any inner product space, we can associate each vector $v\in V$ to a linear functional $\phi_v$ using the procedure above.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-409">Another way to work concretely with dual vectors (without the need for inner products) is to define things in terms of a basis.</p></div>

# <div class="mathbook-content"><p id="p-410">Given a basis $\{v_1,v_2,\ldots, v_n\}$ of $V\text{,}$ we define the corresponding <dfn xmlns:svg="http://www.w3.org/2000/svg" class="terminology">dual basis</dfn> $\{\phi_1,\phi_2,\ldots, \phi_n\}$ of $V^*$ by</p><div class="displaymath">
# \begin{equation*}
# \phi_i(v_j) = \begin{cases} 1, \amp \text{ if } i=j\\ 0, \amp \text{ if } i\neq j\end{cases}\text{.}
# \end{equation*}
# </div><p class="continuation">Note that each $\phi_j$ is well-defined, since any linear transformation can be defined by giving its values on a basis.</p></div>

# <div class="mathbook-content"><p id="p-411">For the standard basis on $\R^n\text{,}$ note that the corresponding dual basis functionals are given by</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \phi_j(x_1,x_2,\ldots, x_n) = x_j\text{.}
# \end{equation*}
# </div><p class="continuation">That is, these are the <em class="emphasis">coordinate functions</em> on $\R^n\text{.}$</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-36"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">1<span class="period">.</span></span></h6><p id="p-412">Show that the dual basis is indeed a basis for $V^*\text{.}$</p></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-416">Next, let $V$ and $W$ be vector spaces, and let $T:V\to W$ be a linear transformation. For any such $T\text{,}$ we can define the <em class="emphasis">dual map</em> $T^*:W^*\to V^*$ by $T^*(\phi) = \phi\circ T$ for each $\phi\in W^*\text{.}$</p></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-37"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">2<span class="period">.</span></span></h6><p id="p-417">Confirm that (a) $T^*(\phi)$ does indeed define an element of $V^*\text{;}$ that is, a linear map from $V$ to $\R\text{,}$ and (b) that $T^*$ is linear.</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-38"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">3<span class="period">.</span></span></h6><p id="p-421">Let $V=P(\R)$ be the space of all polynomials, and let $D:V\to V$ be the derivative transformation $D(p(x))=p'(x)\text{.}$ Let $\phi:V\to \R$ be the linear functional defined by $\phi(p(x)) = \int_0^1 p(x)\,dx\text{.}$</p><p id="p-422">What is the linear functional $D^*(\phi)\text{?}$</p></article></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-39"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">4<span class="period">.</span></span></h6><p id="p-424">Show that dual maps satisfy the following properties: for any $S,T\in \mathcal{L}(V,W)$ and $k\in \R\text{,}$</p><ol class="lower-alpha"><li id="li-88">$\displaystyle (S+T)^* = S^*+T^*$</li><li id="li-89">$\displaystyle (kS)^* = kS^*$</li><li id="list-property-last">$\displaystyle (ST)^* = T^*S^*$</li></ol><p id="p-425">In item <a href="worksheet-dual-basis.ipynb#list-property-last" class="internal" title="Item 2.6.4.c">Item 2.6.4.c</a>, assume $S\in \mathcal{L}(V,W)$ and $T\in \mathcal{L}(U,V)\text{.}$ (Reminder: the notation $ST$ is sometimes referred to as the “product” of $S$ and $T\text{,}$ in analogy with matrices, but actually represents the composition $S\circ T\text{.}$)</p></article></div>

# <div class="mathbook-content"><p id="p-427">We have one topic remaining in relation to dual spaces: determining the kernel and image of a dual map $T^*$ (in terms of the kernel and image of $T$). Let $V$ be a vector space, and let $U$ be a subspace of $V\text{.}$ Any such subspace determines an important subspace of $V^*\text{:}$ the <dfn xmlns:svg="http://www.w3.org/2000/svg" class="terminology">annihilator</dfn> of $U\text{,}$ denoted by $U^0$ and defined by</p><div class="displaymath">
# \begin{equation*}
# U^0 = \{\phi\in V^* \,|\, \phi(u)=0 \text{ for all } u\in U\}\text{.}
# \end{equation*}
# </div></div>

# <div class="mathbook-content"><article class="exercise exercise-like" id="exercise-40"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="codenumber">5<span class="period">.</span></span></h6><p id="p-428">Determine a basis (in terms of the standard dual basis for $(\R^4)^*$) for the annihilator $U^0$ of the subspace $U\subseteq \R^4$ given by</p><div class="displaymath">
# \begin{equation*}
# U = \{(2a+b,3b,a,a-2b)\,|\, a,b\in\R\}\text{.}
# \end{equation*}
# </div><div class="solutions"><span class="type">Hint:</span>
# <div class="hint solution-like"><p id="p-429">Write $\phi = c_1\phi_1+c_2\phi_2+c_3\phi_3+c_4\phi_4\text{,}$ and note that each $\phi_j$ simply gives the $j$th component of a vector in $\R^4\text{.}$</p></div></div></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-432">Here is a fun theorem about annihilators that I won't ask you to prove.</p></div>

# <div class="mathbook-content"><article class="theorem theorem-like" id="thm-anihilator-dimension"><h6 xmlns:svg="http://www.w3.org/2000/svg" class="heading"><span class="type">Theorem</span><span class="space"> </span><span class="codenumber">2.6.1</span><span class="period">.</span></h6><p id="p-433">Let $V$ be a finite dimensional vector space. For any subspace $U$ of $V\text{,}$</p><div class="displaymath">
# \begin{equation*}
# \dim U + \dim U^0 = \dim V\text{.}
# \end{equation*}
# </div></article></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-434">Here's an outline of the proof. For any subspace $U\subseteq V\text{,}$ we can define the <em class="emphasis">inclusion</em> map $i:U\to V\text{,}$ given by $i(u)=u\text{.}$ (This is not the identity on $V$ since it's only defined on $U\text{.}$ In particular, it is not onto unless $U=V\text{,}$ although it is clearly one-to-one.)</p></div>

# <div class="mathbook-content"><p id="p-435">Then $i^*$ is a map from $V^*$ to $U^*\text{.}$ Moreover, note that for any $\phi\in V^*\text{,}$ $i^*(\phi)\in U^*$ satisfies, for any $u\in U\text{,}$</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# i^*(\phi)(u) = \phi(i(u))=\phi(u)\text{.}
# \end{equation*}
# </div><p class="continuation">Thus, $\phi\in \ker i^*$ if and only if $i^*(\phi)=0\text{,}$ which is if and only if $\phi(u)=0$ for all $u\in U\text{,}$ which is if and only if $\phi\in U^0\text{.}$ Therefore, $\ker i^* = U^0\text{.}$</p></div>

# <div class="mathbook-content"><p id="p-436">By the dimension theorem, we have:</p><div xmlns:svg="http://www.w3.org/2000/svg" class="displaymath">
# \begin{equation*}
# \dim V^* = \dim \ker i^* + \dim \operatorname{im} i^*\text{.}
# \end{equation*}
# </div><p class="continuation">With a bit of work, one can show that $\operatorname{im} i^* = U^*\text{,}$ and we get the result from the fact that $\dim V^*=\dim V$ and $\dim U^* = \dim U\text{.}$</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-437">There are a number of interesting results of this flavour. For example, one can show that a map $T$ is injective if and only if $T^*$ is surjective, and vice-versa.</p></div>

# <div class="mathbook-content"><p xmlns:svg="http://www.w3.org/2000/svg" id="p-438">One final, optional task: return to the example of $\R^n\text{,}$ viewed as column vectors, and consider a matrix transformation $T_A:\R^n\to \R^m$ given by $T_A(\vec{x}) = A\vec{x}$ as usual. Viewing $(\R^n)^*$ as row vectors, convince yourself that $(T_A)^* = T_{A^T}\text{;}$ that is, that what we've really been talking about all along is just the transpose of a matrix!</p></div>
