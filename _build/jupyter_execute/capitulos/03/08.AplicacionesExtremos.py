#!/usr/bin/env python
# coding: utf-8

# # Aplicaciones del cálculo de extremos
# 
# En esta sección, vamos a calcular extremos relativos y absolutos. En primer lugar, obtendremos los extremos relativos de una función, aplicando el criterio de la matriz hessiana. Después, trataremos de obtener un modelo lineal que ajuste una colección de datos, mediante el método de mínimos cuadrados. Y, por último, resolveremos un problema de optimización, calculando extremos absolutos en un dominio compacto. 
# 
# ## Extremos relativos y hessiana 
# 
# ````{prf:example} 
# :label: 3.x._ex
# :nonumber: 
# 
# Encuentra el extremo relativo de
# 
# $$
# f(x,y) = -x^3 + 4xy - 2y^2 + 1.
# $$
# 
# **Solución:**
# 
# Comenzamos por encontrar los puntos críticos de $f$. Puesto que
# 
# $$
# \dfrac{\partial f}{\partial x}(x,y) = -3x^2 + 4y \quad \text{ y } \quad \dfrac{\partial f}{\partial y}(x,y) = 4x - 4y,
# $$
# 
# los únicos puntos críticos son aquellos para los que ambas derivadas parciales son $0$.
# 
# Para localizar estos puntos, igualamos $\dfrac{\partial f}{\partial x}(x,y)$ y $\dfrac{\partial f}{\partial y}(x,y)$ a $0$:
# 
# $$
# -3x^2 + 4y = 0 \quad \text{ y } \quad 4x - 4y = 0.
# $$
# 
# De la segunda ecuación, se obtiene que $x = y$, y, a partir de la primera, se obtiene que 
# 
# $$
# y = x = 0 \quad \text{ y } \quad y = x = \frac{4}{3}.
# $$
# 
# Ahora, podemos aplicar el criterio de la matriz hessiana en el punto crítico $(0,0)$. Como
# 
# $$
# \mathrm{Hess}f(x,y) = \begin{bmatrix}
# -6x & 4 \\
# 4 & -4 
# \end{bmatrix},
# $$
# 
# entonces
# 
# $$
# \det\mathrm{Hess}f(0,0) = \left|
# 
# \begin{ array}{cc}
# 
# 0 & 4\\
# 
# 4 & -4
# 
# \end{array}
# 
# \right| = 0 - 16 < 0,
# $$
# 
# por lo que podemos concluir que $f$ tiene en $(0,0)$ un punto silla.
# 
# Además, aplicando de nuevo el criterio de la matriz hessiana para el punto crítico $(\frac{4}{3},\frac{4}{3})$. Como
# 
# $$
# $\det\mathrm{Hess}f(\frac{4}{3},\frac{4}{3}) = \left|
# 
# \begin{ array}{cc}
# 
# -8 & 4\\
# 
# 4 & -4
# 
# \end{array}
# 
# \right| = -8(-4) - 16 = 16 > 0,
# $$
# 
# y $\dfrac{\partial^2 f}{\partial x^2}(\frac{4}{3},\frac{4}{3}) = -8 < 0$, podemos concluir que $f$ tiene un máximo relativo en $(\frac{4}{3},\frac{4}{3})$.
# ````

# ## Método de mínimos cuadrados
# 
# Al construir un **modelo matemático** para representar un fenómeno particular, los objetivos son simplicidad y precisión. Existen varias maneras para desarrollar tales modelos, una es la conocida como el **método de mínimos cuadrados**. 
# 
# Como medida de lo bien que el modelo $y = f(x)$ se ajusta a la colección de puntos
# 
# $$
# \{(x_1,y_1),(x_2,y_2),...,(x_n,y_n)\}
# $$
# 
# se puede calcular el cuadrado de la distancia entre los datos de los que se parte y los valores predichos por el modelo para obtener la **suma de los errores al cuadrado** o el **error cuadrático**: 
# 
# $$
# S = \sum_{i = 1}^n [f(x_i) - y_i]^2.
# $$
# 
# En estadística, se llama **recta de regresión** al modelo lineal que minimiza $S$ mediante el **método de mínimos cuadrados**. La prueba de que esta línea, $y = f(x) = ax + b$, en realidad minimiza $S$ implica minimizar una función de dos variables:
# 
# $$
# S(a,b) = \sum_{i = 1}^n [ax_i + b - y_i]^2,
# $$
# 
# donde $a, b \in \mathbb{R}$.
# 
# Para obtener los valores de $a$ y $b$ que minimizan $S$, calculamos su gradiente:
# 
# $$
# \mathbf{\nabla} S(a,b) = \left[2\sum_{i = 1}^n x_i (ax_i + b - y_i), 2\sum_{i = 1}^n (ax_i + b - y_i)\right].
# $$
# 
# E igualando a $0$:
# 
# $$
# 2\sum_{i = 1}^n x_i (ax_i + b - y_i) = 0 \quad \text{ y } \quad 2\sum_{i = 1}^n (ax_i + b - y_i) = 0,
# $$
# 
# se obtiene un sistema de dos ecuaciones y dos incógnitas del que se despeja $a$ y $b$.
# 
# ````{prf:theorem}  Recta de regresión de mínimos cuadrados
# :label: th_recta_regr_mc
# :nonumber: 
# 
# La **recta de regresión de mínimos cuadrados** para $\{(x_1,y_1),(x_2,y_2),...,(x_n,y_n)\}$ está dada por $f(x) = ax + b$, donde
# 
# $$
# a = \frac{\displaystyle n \sum_{i=1}^{n}x_iy_i - \sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i}{\displaystyle n \sum_{i=1}^{n}x_i^2 - \left(\sum_{i=1}^{n}x_i\right)^2} \quad \text{ y } \quad b = \frac{1}{n}\left(\sum_{i=1}^{n}y_i - a\sum_{i=1}^{n}x_i\right).
# $$
# ````
# Veamos un caso práctico.
# 
# ````{prf:example} 
# :label: 3.x._ex
# :nonumber: 
# 
# Hallar la recta de regresión de mínimos cuadrados para los puntos $(-3,0), (-1,1), (0,2)$ y $(2,3)$.
# 
# **Solución:**
# 
# A partir del resultado teórico anterior, tenemos que
# 
# $$
# a = \frac{\displaystyle n \sum_{i=1}^{n}x_iy_i - \sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i}{\displaystyle n \sum_{i=1}^{n}x_i^2 - \left(\sum_{i=1}^{n}x_i\right)^2} = \dfrac{4(5) - (-2)(6)}{4(14) - (-2)^2}
# $$
# 
# y 
# 
# $$
# b = \frac{1}{n}\left(\sum_{i=1}^{n}y_i - a\sum_{i=1}^{n}x_i\right) = \frac{1}{4}\left[6 - \frac{8}{3}(-2)\right] = \frac{47}{26}.
# $$
# 
# Por tanto, la recta de regresión de mínimos cuadrados es 
# 
# $$
# f(x) = \frac{8}{13}x + \frac{47}{26}.
# $$
# ````
# 
# Vamos a preguntarle a nuestro oráculo por si nos hemos equivocado.

# In[1]:


import sympy as sp
import numpy as np


# In[2]:


x, y = sp.symbols('x y', real=True) # define las variables simbólicas x e y

# Datos
xi = np.array([-3, -1, 0, 2])
yi = np.array([0, 1, 2, 3])

# Cálculo de la recta de regresión
n = len(xi) # número de datos
a = (n*np.dot(xi,yi) - np.sum(xi)*np.sum(yi))/(n*np.sum(xi**2) - np.sum(xi)**2) 
b = (np.sum(yi) - a*np.sum(xi))/n

print('Recta de regresión: \n\n', y, ' = ', a*x + b)


# ## Extremos absolutos en un dominio compacto 
# 
# ````{prf:example} Cálculo de volumen máximo 
# :label: 3.x._ex
# :nonumber: 
# 
# Una caja rectangular descansa sobre el plano $xy$ con un vértice en el origen. El vértice opuesto se encuentra en el plano
# 
# $$
# 6x + 4y + 3z = 24.
# $$
# 
# <img src="../../images/3.8.Volumen_maximo.png" width="250"/>
# 
# Encuentra el volumen máximo de la caja. 
# 
# **Solución:**
# 
# Supongamos que $x, y, z$ representan la longitud, anchura y altura de la caja. Debido a que un vértice de la caja se encuentra en el plano $6x + 4y + 3z = 24$, como $z = \frac{1}{3}(24 - 6x - 4y)$, podemos escribir el volumen de la caja, $V = xyz$, en función de dos variables:
# 
# $$
# V(x,y) = x y \left[\frac{1}{3}(24 - 6x - 4y)\right] = \frac{1}{3}(24xy - 6x^2y - 4xy^2).
# $$
# 
# A continuación, calculamos el gradiente de $V$:
# 
# $$
# \mathbf{\nabla} V (x,y) = \left[\frac{1}{3}(24y - 12xy - 4y^2), \frac{1}{3}(24x - 6x^2 - 8xy)\right] = \left[\frac{y}{3}(24 - 12x - 4y), \frac{x}{3}(24 - 6x - 8y)\right].
# $$
# 
# E igualando a $0$:
# 
# $$
# \frac{y}{3}(24 - 12x - 4y) = 0 \quad \text{ y } \quad \frac{x}{3}(24 - 6x - 8y) = 0, 
# $$
# 
# se obtienen los puntos críticos $(0,0), (4,0), (0,6)$ y $\left(\frac{4}{3},2\right)$. 
# 
# En $(0,0), (4,0)$ y $(0,6)$, el volumen es $0$, por lo que esos puntos no producen un volumen máximo. 
# 
# En el punto $\left(\frac{4}{3},2\right)$, se puede aplicar el criterio de la matriz hessiana. Como 
# 
# $$
# \mathrm{Hess}V(x,y) = \begin{bmatrix}
# -4y & \frac{1}{3}(24 - 12x -8y) \\
# \frac{1}{3}(24 - 12x -8y) & -\frac{8x}{3}
# \end{bmatrix},
# $$
# 
# entonces
# 
# $$
# \det\mathrm{Hess}V\left(\frac{4}{3},2\right) = \left|
# 
# \begin{array}{cc}
# 
# -8 & -\frac{8}{3}\\
# 
# -\frac{8}{3} & -\frac{32}{9}
# 
# \end{array}
# 
# \right| = \frac{64}{3} > 0
# $$
# 
# y $\dfrac{\partial^2 V}{\partial {x^2}}(\frac{4}{3},2) = -8 < 0$, por lo que podemos concluir que $V$ tiene un máximo relativo en $\left(\frac{4}{3},2\right)$ y su valor es: 
# 
# $$
# V\left(\frac{4}{3},2\right) = \frac{1}{3}\left[24\left(\frac{4}{3}\right)(2) - 6\left(\frac{4}{3}\right)^2(2) - 4\left(\frac{4}{3}\right)(2^2)\right] = \frac{64}{9}.
# $$
# 
# ¿Hemos terminado? No, porque faltaría comprobar el volumen en los puntos de la frontera del dominio triangular de $V$. Comprueba que el volumen en estos puntos es igual a $0$. 
# 
# Ahora sí, podemos concluir que el volumen máximo es $V\left(\frac{4}{3},2\right) = \frac{64}{9}$ unidades cúbicas.
# ````
# 
# Ya por último, vamos a resolver con `Python` el ejercicio propuesto. 

# In[3]:


x, y = sp.symbols('x y', real=True) # define las variables simbólicas x e y
V = sp.Lambda((x,y), (24*x*y - 6*x**2*y -4 *x*y**2)/3)

# Calculamos el gradiente de f
grad_V =  sp.transpose(sp.Matrix([V(x,y)]).jacobian([x,y]))
display('Gradiente en (x,y): ', grad_V)

# Buscamos los puntos críticos
sol = sp.solve((sp.Eq(grad_V[0],0),sp.Eq(grad_V[1],0)),(x,y))
display('Puntos críticos:', sol)

# V en (0,0), (4,0), (0,6) es igual a 0
print('V(0,0) =', V(*sol[0]), ', V(4,0) =', V(*sol[3]), ', V(0,6) =', V(*sol[1]))

# Definimos la hessiana con sp.hessian
H = sp.Lambda((x,y), sp.hessian(V(x,y), (x,y)))
display('Matriz hessiana en (x,y): ', H(x,y))

# Clasificación del punto crítico (4/3,2)
H0 = H(*sol[2])
display('Hessiana del punto crítico (4/3,2): ', H0)
print("Determinante: ",sp.det(H0), ". Posición (1,1):", H0[0,0])

# V en (4/3,2) es igual a 64/9
print('\nEl volumen máximo de la caja es: \n\n V(4/3,2) =', V(*sol[2]))

