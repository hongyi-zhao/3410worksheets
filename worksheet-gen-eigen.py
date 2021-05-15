#!/usr/bin/env python
# coding: utf-8

# # Generalized Eigenvectors
# 
# Let $V$ be a finite-dimensional vector space, and let $T:V\to V$ be a linear operator. Assume that $T$ has all real eigenvalues (alternatively, assume we're working over the complex numbers). Let $A$ be the matrix of $T$ with respect to some standard basis $B_0$ of $V$.
# 
# Our goal will be to replace the basis $B_0$ with a basis $B$ such that the matrix of $T$ with respect to $B$ is as simple as possible. (Where we agree that the "simplest" possible matrix would be diagonal.)
# 
# Recall the following results that we've observed so far. 
# 
# - The characteristic polynomial $c_T(x)$ of $T$ does not depend on the choice of basis.
# - The eigenvalues of $T$ are the roots of this polynomial.
# - The eigenspaces $E_\lambda(T)$ are $T$-invariant subspaces of $V$.
# - The matrix $A$ can be diagonalized if and only if there is a basis of $V$ consisting of eigenvectors of $T$.
# - Suppose
# $$c_T(x) = (x-\lambda_1)^{m_1}(x-\lambda_2)^{m_2}\cdots (x-\lambda_k)^{m_k}.$$
# Then $A$ can be diagonalized if and only if $\dim E_{\lambda_i}(T) = m_i$ for each $i=1,\ldots, k$.

# In the case where $A$ can be diagonalized, we have the direct sum decomposition
# $$V = E_{\lambda_1}(T)\oplus E_{\lambda_2}(T) \oplus \cdots \oplus E_{\lambda_k}(T).$$
# 
# **The question is**: what do we do if there aren't enough eigenvectors to form a basis of $V$? When that happens, the direct sum of all the eigenspaces will not give us all of $V$.
# 
# The idea: replace $E_{\lambda_j}(T)$ with a **generalized eigenspace** $G_{\lambda_j}(T)$ whose dimension is $m_i$.
# 
# Our candidate: instead of $E_{\lambda}(T) = \ker(T-\lambda I)$, we use $G_\lambda(T) = \ker((T-\lambda I)^m)$, where $m$ is the multiplicity of $\lambda$.

# ## Problem 1
# 
# Recall that in class we proved that $\ker(T)$ and $\operatorname{im}(T)$ are $T$-invariant subspaces. Let $p(x)$ be any polynomial, and prove that $\ker (p(T))$ and $\operatorname{im}(p(T))$ are also $T$-invariant.
# 
# Hint: first show that $p(T)T=Tp(T)$ for any polynomial $T$.

# Applying the result of Problem 1 to the polynomial $p(x) = (x-\lambda)^m$ shows that $G_\lambda(T)$ is $T$-invariant. It is possible to show that $\dim G_\lambda(T)=m$ but I won't ask you to do that. (A proof is in Nicholson if you really want to see it.)
# 
# Instead, we will try to understand what's going on by exploring an example.
# 

# ## Problem 2
# 
# Consider the following matrix.

# In[11]:


from sympy import *
init_printing()
A=Matrix([[2,0,0,1,0],[-1,0,1,2,3],[0,1,2,0,-1],[-2,-3,2,5,3],[0,-1,0,1,4]])
A


# (a) find (and factor) the characteristic polynomial of $A$. For the commands you might need, [refer to the textbook](https://opentext.uleth.ca/Math3410/sec-sympy.html#p-1000)

# In[ ]:





# (b) find the eigenvectors. What are the dimensions of the eigenspaces? Based on this observation, can $A$ be diagonalized?

# In[ ]:





# (You may comment on the eigenspaces by editing this cell. Double-click to edit.)

# ## Problem 3
# 
# Prove that for any $n\times n$ matrix $A$, we have:
# 
# $$\{0\}\subseteq \operatorname{null}(A)\subseteq \operatorname{null}(A^2) \subseteq \cdots \subseteq \operatorname{null}(A^n)$$

# It turns out that at some point, the null spaces stabilize. If $\operatorname{null}(A^k)=\operatorname{null}A^{k+1}$ for some $k$, then $\operatorname{null}(A^k)=\operatorname{null}(A^{k+l})$ for all $l\geq 0$.

# ## Problem 4
# 
# For each eigenvalue found in Problem 2, compute the nullspace of $A-\lambda I$, $(A-\lambda I)^2$, $(A-\lambda I)^3$, etc. until you find two consecutive nullspaces that are the same.
# 
# By Problem 3, any vector in $\operatorname{null}(A-\lambda I)^m$ will also be a vector in $\operatorname{null}(A-\lambda I)^{m+1}$. In particular, at each step, we can find a basis for $\operatorname{null}(A-\lambda I)^m$ that includes the basis for $\operatorname{null}(A-\lambda I)^{m-1}$.
# 
# For each eigenvalue found in Problem 2, determine such a basis for the corresponding generalized eigenspace. You will want to list your vectors so that the vectors from the basis of the nullspace for $A-\lambda I$ come first, then the vectors for the basis of the nullspace for $(A-\lambda I)^2$, and so on.

# In[ ]:





# ## Problem 5
# 
# Finally, let's see how all of this works. Let $P$ be the matrix whose columns consist of the vectors found in Problem 4. What do you get when you compute the matrix $P^{-1}AP$?

# In[ ]:




