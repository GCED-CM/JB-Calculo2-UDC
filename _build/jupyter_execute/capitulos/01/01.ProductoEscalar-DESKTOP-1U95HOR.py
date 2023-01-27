#!/usr/bin/env python
# coding: utf-8

# # El producto escalar
# 
# En las dos secciones precedentes hemos introducido dos operaciones para vectores: la suma y el producto por un escalar. Ahora vamos a estudiar una tercera operación: el producto escalar.
# 
# ## Producto escalar. Definición y propiedades
# 
# ````{prf:definition} Producto escalar
# :label: def_01_producto_escalar
# :nonumber: 
# 
# El producto escalar es una aplicación $\mathbb{R}^{n} \times \mathbb{R}^{n} \to \mathbb{R}$ que se define, en general, como
# 
# $$
# \mathbf{u}\cdot\mathbf{v} := \sum_{i=1}^{n} u_{i} v_{i} \in \mathbb{R}.
# $$
# 
# Así, en los casos que venimos estudiando,
# 
# 1. En $\mathbb{R}^{2}$, $\displaystyle \mathbf{u} \cdot \mathbf{v} = u_{1}v_{1} + u_{2}v_{2} \in \mathbb{R}$.
# 2. En $\mathbb{R}^{3}$, $\displaystyle \mathbf{u} \cdot \mathbf{v} = u_{1}v_{1} + u_{2}v_{2} + u_{3}v_{3} \in \mathbb{R}$.
# 
# ````
# 
# ````{prf:example} 
# :label: ex_01_producto_escalar
# :nonumber: 
# 
# * El producto escalar de los vectores en el plano $\mathbf{u} = (1,2)$ y $\mathbf{v} = (-3,4)$ es:
# 
#     $$ \mathbf{u}\cdot\mathbf{v} = 1 \, (-3) + 2* 4 = -3 + 8 = 5.$$
# * El producto escalar de los vectores en el espacio $\mathbf{u} = (1,2,3)$ y $\mathbf{v} = (-3,4,-5)$ es:
# 
#     $$ \mathbf{u}\cdot\mathbf{v} = 1 \, (-3) + 2* 4 + 3 \, (-5)= -3 + 8 -15 = -10.$$
# ````
# 
# ````{prf:property} 
# :label: prop_01_producto_escalar
# :nonumber: 
# 
# Sean $\mathbf{u}$, $\mathbf{v}$ y $\mathbf{v}$ vectores en $\mathbb{R}^{n}$ y $c\in\mathbb{R}$. Entonces
# 
# 1. $\mathbf{u}\cdot\mathbf{v} = \mathbf{v}\cdot\mathbf{u}$ (propiedad conmutativa).
# 2. $\mathbf{u}\cdot(\mathbf{v}+\mathbf{w}) = \mathbf{u}\cdot\mathbf{v} + \mathbf{u}\cdot\mathbf{w}$ (propiedad distributiva).
# 3. $c\, (\mathbf{u}\cdot\mathbf{v}) = c\, \mathbf{u}\cdot \mathbf{v} = \mathbf{u}\cdot c\, \mathbf{v}$.
# 4. $\mathbf{0}\cdot\mathbf{v} = \mathbf{0}$.
# 5. $\mathbf{u}\cdot\mathbf{u} = \|\mathbf{u}\|^2$.
# 
# ````
# 
# **Nota:** En `Numpy` se calcula con el comando np.dot (que también admite la sintaxis, para los vectores u y v, `u.dot(v)`):
# 
# 

# In[9]:


import numpy as np

# Definimos los vectores u y v
u = np.array([1, 2, 3])
v = np.array([-3, 4, -5])

# Calculamos el producto escalar de u y v con np.dot
dot_product = np.dot (u,v)
print('Producto escalar de u y v: ', dot_product)

# Una opción equivalente de llamar a la misma función np.dot:
dot_product = u.dot(v)
print('Producto escalar de u y v: ', dot_product)



# Para hacer el producto vectorial en `Sympy` tenemos que usar la segunda sintaxis. Recuerda que en este caso los vectores tienen que definirse como `sp.Matrix`.

# In[12]:


import sympy as sp

u = sp.Matrix([sp.frac('1/2'), sp.frac('1/3'), 1])
v = sp.Matrix([sp.frac('1/5'), 1, 2])

# Calculamos el producto escalar de u y v en Sympy
product = u.dot(v)
print(product)


# ## Ángulo entre dos vectores
# 
# El ángulo entre dos vectores, $\mathbf{u}$, $\mathbf{v}\in\mathbb{R}^{2}$, ambos distintos de $\mathbb{0}$, es el ángulo $\theta$, $\theta\in [0,\pi]$, entre estos vectores situados 
# en su posición estándar (es decir, con el punto inicial de ambos en el origen de coordenadas).
# 
# <img src="../../images/01_angulo_vectores.png" width="250"/>
# 
# Puede calcularse utilizando la siguiente propiedad:
# 
# ````{prf:property} 
# :label: prop_01_angulo_vectores
# :nonumber: 
# 
# Si $\theta$ es el ángulo entre los vectores $\mathbf{u}$, $\mathbf{v}\in\mathbb{R}^{2}$, ambos distintos de $\mathbb{0}$, entonces
# 
# $$
# \cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|},
# $$
# 
# o, equivalentemente,
# 
# $$
# \theta = \arccos\left(\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}\right),
# $$
# ````
# 
# Queremos destacar que, como el denominador en esta fracción es siempre un número positivo, $\mathbf{u}\cdot\mathbf{v}$ y $\cos\theta$ tendrán siempre el mismo signo. Por lo tanto podemos deducir fácilmente el signo de $\mathbf{u}\cdot\mathbf{v}$ según el signo de $\cos\theta$, como mostramos en la siguiente figura.
# 
# <img src="../../images/01_signo_producto_escalar.png" width="1200"/>
# 

# 
