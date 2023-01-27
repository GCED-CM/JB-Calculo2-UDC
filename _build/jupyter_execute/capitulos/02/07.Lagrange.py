#!/usr/bin/env python
# coding: utf-8

# # Polinomio de interpolación de Lagrange
# 
# ## Soporte teórico
# 
# En general, cuando queremos resolver un problema, tendremos una serie de datos puntuales (por ejemplo, el número de infectados por COVID día a día). Para trabajar matemáticamente con esos datos necesitamos definir una función a partir de ellos y, después, trabajar con esa función (por ejemplo, derivarla, para conocer la tendencia de la curva, o integrarla, para conocer el número de personas afectadas, *etc.*). Por lo tanto, conseguir crear una función que aproxime un conjunto de datos es una parte fundamental del trabajo práctico de un matemático. Hay varias formas de hacer esto. Ahora vamos a ver la más sencilla de todas: **el polinomio de interpolación de Lagrage**.
# 
# En este caso, si tenemos $n+1$ puntos construiremos un polinomio de orden $n$ que pase por esos puntos. Pensemos que es algo que ya hemos hecho en el instituto... pero restringido a un caso concreto: si nos dan 2 puntos sabemos (ejem...) construir una recta (es decir, un polinomio de orden 1) que pase por esos 2 puntos. Ahora vamos a aprender a hacer esto para más puntos.
# 
# Primero necesitamos un teorema que nos garantice la existencia de ese polinomio:
# 
# **Teorema (de interpolación de Lagrange):**
# Dados
# * $n+1$ puntos distintos, $x_0,x_1,\ldots,x_n$;
# * $n+1$ valores cualesquiera, $y_0,y_1,\ldots,y_n$;
# existe un único  polinomio $p_n$ de grado {$\leq n$} tal que 
# 
# $$
# p_n(x_i)=y_i \, , \quad\forall i=0,1,2,\ldots,n \, .
# $$
# 
# Este polinomio $p_n$ se denomina **polinomio de interpolación de Lagrange en los puntos $x_0,x_1,\ldots,x_n$ 
# relativo a los valores $y_0,y_1,\ldots,y_n$**. 
# 
# En particular, si $y_i=f(x_i)$, decimos que **$p_n$ es el polinomio de interpolación de Lagrange de la 
# función $f$ en los puntos $x_i$**.

# In[72]:


import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(20,10))

# Figura izquierda
ax1 = axs[0]
x_coef = [-1, 0, 1, 3]
y_coef = [-2, 1, -4, 10]
x= np.linspace(-1.5, 3.1, 200)
P_expr = 2*x**3 - 4*x**2 - 3*x + 1

ax1.set_title('Polinomio de interpolación de Lagrange para puntos', fontsize=20)
ax1.scatter(x_coef, y_coef, s=200, c='r')
ax1.plot(x, P_expr, c='b', ls='-', lw='3', label = 'P')
ax1.grid()
ax1.legend(fontsize=20, loc='upper left')

# Figura derecha
ax2 = axs[1]
x_coef = [-np.pi/2, 0, np.pi/3, np.pi/2]
y_coef = [0, 1, 0.5, 0]
x= np.linspace(-np.pi, np.pi, 200)
f = np.cos(x)
P_expr = 2/np.pi*(x+np.pi/2)-21/(5*np.pi**2)*(x+np.pi/2)*x+6/(5*np.pi**3)*(x+np.pi/2)*x*(x-np.pi/3)

ax2.set_title('Polinomio de interpolación de Lagrange para una función', fontsize=20)
ax2.scatter(x_coef, y_coef, s=200, c='r')
ax2.plot(x, f, c='g', ls='--', lw='3', label = '$cos(x)$')
ax2.plot(x, P_expr, c='b', ls='-', lw='3', label = 'P')
ax2.grid()
ax2.legend(fontsize=20, loc='upper right')


# Una vez que ya sabemos que ese polinomio existe viene la segunda parte: ¿cómo lo calculamos?
# 
# Hay 2 maneras de hacer esto:

# ## Construcción por polinomios fundamentales
# 
# **Definición:**
# Para cada $i=0,1,\ldots,n\,$,
# existe un único polinomio $l_i$ de grado $\leq n$ tal que 
# * $l_i(x_i)= 1$, y 
# * $l_i(x_j)=0$, $\forall j\neq i$. 
# 
# Para la construcción de $l_i$, es inmediato comprobar que:
# 
# $$
# l_i(x)\, = \frac{(x-x_0)(x-x_1)\ldots(x-x_{i-1})(x-x_{i+1})\ldots(x-x_n)}
# {(x_i-x_0)(x_i-x_1)\ldots(x_i-x_{i-1})(x_i-x_{i+1})\ldots(x_i-x_n)}.
# $$
# 
# Ahora pensemos un momento: $l_i$ es un polinomio de grado $n$ que vale 1 en $x_{i}$ y 0 en el resto de nodos, eso quiere decir que si lo multiplicamos por un número real, por ejemplo, por $y_i$, tendremos que 
# * $y_i l_i (x_i) = y_i 1 = y_i$,
# * $y_i l_i (x_j) = y_i 0 = 0$,
# 
# como, además, la suma de polinomios de grado $n$ es un polinomio de grado $n$, es inmediato el siguiente resultado:
# 
# **Teorema:** 
# El polinomio de interpolaci\'on de Lagrange en los nodos $x_0,\, x_1,\ldots,\, x_n$ relativo a los valores
# $y_0,\,y_1,\ldots,\,y_n$ es
# 
# $$
# p_n(x) \, = \, %\sum_{i=0}^ny_i\,\ell_i(x)=
# y_0\,\ell_0(x)+y_1\,\ell_1(x)+\ldots+y_n\,\ell_n(x).
# $$

# In[73]:


import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2, figsize=(20,10))

x_coef = [-1, 0, 1, 3]
y_ceros = [0, 0, 0, 0]
y_unos = [1, 1, 1, 1]
y_coef = [-2, 1, -4, 10]

x= np.linspace(-1.5, 3.1, 200)

P0_expr = ( (x-x_coef[1])*(x-x_coef[2])*(x-x_coef[3]) ) / ( (x_coef[0]-x_coef[1])*(x_coef[0]-x_coef[2])*(x_coef[0]-x_coef[3]) )
P1_expr = ( (x-x_coef[0])*(x-x_coef[2])*(x-x_coef[3]) ) / ( (x_coef[1]-x_coef[0])*(x_coef[1]-x_coef[2])*(x_coef[1]-x_coef[3]) )
P2_expr = ( (x-x_coef[0])*(x-x_coef[1])*(x-x_coef[3]) ) / ( (x_coef[2]-x_coef[0])*(x_coef[2]-x_coef[1])*(x_coef[2]-x_coef[3]) )
P3_expr = ( (x-x_coef[0])*(x-x_coef[1])*(x-x_coef[2]) ) / ( (x_coef[3]-x_coef[0])*(x_coef[3]-x_coef[1])*(x_coef[3]-x_coef[2]) )

P_expr = y_coef[0]*P0_expr + y_coef[1]*P1_expr + y_coef[2]*P2_expr + y_coef[3]*P3_expr

# Figura izquierda
ax1 = axs[0]
ax1.set_title('Polinomios fundamentales de Lagrange', fontsize=20)
ax1.scatter(x_coef, y_ceros, s=150, c='b')
ax1.scatter(x_coef, y_unos, s=200, c='g')
ax1.plot(x, P0_expr, c='black', ls='--', lw='3', label = 'P0')
ax1.plot(x, P1_expr, c='y', ls='--', lw='3', label = 'P1')
ax1.plot(x, P2_expr, c='c', ls='--', lw='3', label = 'P2')
ax1.plot(x, P3_expr, c='m', ls='--', lw='3', label = 'P3')
ax1.grid()
ax1.legend(fontsize=20, loc='upper right')

# Figura derecha
ax2 = axs[1]
ax2.set_title("Polinomio de Lagrange", fontsize=20)
ax2.scatter(x_coef, y_coef, s=200, c='r')
ax2.plot(x, P_expr, c='b', ls='--', lw='3', label = 'P')
ax2.grid()
ax2.legend(fontsize=20, loc='upper left')


# 
# ## Construcción mediante diferencias divididas
# 
# La construcción del Polinomio de Lagrange mediante los polinomios fundamentales, que acabamos de explicar, es sencilla de entender pero difícil de implementar en la práctica. Además, si aparece un nuevo dato debemos recomenzar la construcción desde 0. 
# 
# En general, a efectos prácticos y, sobre todo, de programación, es preferible construir el polinomio de Lagrange utilizando la tabla de diferencias divididas, como explicaremos a continuación.
# 
# Antes de nada, debemos recordar que el polinomio de Lagrange es único y, por tanto, el resultado debe ser el mismo utilizando un método u otro.
# 
# * Diferencias divididas de orden 0:
# 
#     $$ 
#     [y_i] \, =\, y_i \, ,\quad \forall i=0,1,\ldots,n\, .
#     $$
# 
# * Diferencias divididas de orden $k$:
# 
#     $$
#     [y_i,y_{i+1},\ldots,y_{i+k}] = 
#     \displaystyle\frac{[y_i,y_{i+1},...,y_{i+k-1}]-[y_{i+1},...,y_{i+k}]}{x_i-x_{i+k}} , \, \forall 
#     i=0,1,...,n-k \, . 
#     $$
# 
# 
# En la práctica, el cálculo de las diferencias divididas se dispone en tabla: 
# 
# $
# \begin{array}{c|ccccc}
# x_0 & {\color{red} y_0}  & {\color{red} [y_0 , y_1]} & {\color{red} [y_0 , y_1 , y_2]}  &  \ldots & {\color{red} [y_0,y_1,\ldots,y_n]}  \\[1ex]
# x_1 & y_1  & [y_1 , y_2]  & [y_1 , y_2 , y_3] & \ldots &  \\[1ex]
# x_2 & y_2  & [y_2 , y_3]  & [y_2 , y_3 , y_4] & \ldots &  \\[1ex]
# \ldots & \ldots & \ldots & \ldots & \ldots &  \\[1ex]
# x_{n-1} & y_{n-1}  & [y_{n-1} , y_n]  &  &  &  \\[1ex]
# x_n & y_n 
# \end{array}
# $
# 
# Aquí nos interesa la primera fila de la matriz resultante (en rojo).  
# 
# **Fórmula de Newton:**
# El polinomio de interpolación de Lagrange en los puntos $x_0,\, x_1,\ldots,\, x_n \,$ relativo a los valores $y_0,\,y_1,\ldots,\,y_n\,$ puede escribirse como
# 
# $$
# \begin{array}{lcl}
# p_n(x)\, &=& [y_0] \, +\, [y_0,y_1]\, (x-x_0) \, +\, [y_0,y_1,y_2]\, (x-x_0)(x-x_1) \, +  \\
#          & & \ldots +\, [y_0,y_1,\ldots,y_n]\, (x-x_0)(x-x_1)\ldots(x-x_{n-1}).
# \end{array}
# $$
# 
# **Nota:**
# Después de construir la tabla, se puede añadir un dato adicional aprovechando los cálculos ya realizados.

# Vamos a hacer nuestra versión en **Numpy** del cálculo del polinomio de interpolación de Lagrange mediante la tabla de diferencias divididas. 
# 
# Ésta será la primera vez que usemos una `function`. En este caso es (casi) inevitable, ya que, en principio desconocemos el número de puntos que tomaremos como dato. Entonces, si queremos que nuestro programa valga siempre, necesitamos un bucle acumulativo para el sumatorio de la fórmula de Newton. 

# In[74]:


import numpy as np
import matplotlib.pyplot as plt

def newton_poly(coef, x_data, x):
    # evaluamos el polinomio de Lagrange, construido con la 
    # tabla de diferencias divididas, en el punto x
    # in: 
    #    coef ---> primera fila de la tabla de diferencias divididas
    #    x_data -> valores de x_i
    #    x ------> punto en el que queremos evaluar el polinomio 
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

x_coef = [-1, 0, 1, 3]
y_coef = [-2, 1, -4, 10]

x= np.linspace(-1.5, 3.1, 200)

n = len(x_coef)
coef = np.zeros([n, n])
# La primera columna serán los datos en y
coef[:,0] = y_coef

# Necesitamos un doble bucle para crear la matriz (perdón, tabla) de diferencias divididas
for j in range(1,n):
    for i in range(n-j):
        coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x_coef[i+j]-x_coef[i])

# evaluamos el polinomio según la function definida al principio
P_expr = newton_poly(coef[0,:],x_coef,x)

# dibujamos el resultado
fig = plt.figure(figsize = (10,8))
plt.scatter(x_coef, y_coef, s=200, c='r')
plt.plot(x, P_expr, 'b', lw='3')
plt.title('Polinomio de Lagrange (fórmula de Newton)', fontsize=20)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# **Nota:**
# 
# Hay una librería en Python, **SciPy**, en la que ya están pre-programados bastantes métodos numéricos (bueno, más bien muchos), entre ellos, por supuesto, el polinomio de Lagrange. 
# Aunque en este curso no usaremos SciPy (**lo que quiere decir que NO lo admitiremos como correcto en vuestras prácticas**), os dejamos a continuación su uso con esta librería, por si os pudiera ser útil en el futuro:

# In[75]:


from scipy.interpolate import lagrange

x_coef = [-1, 0, 1, 3]
y_coef = [-2, 1, -4, 10]
x= np.linspace(-1.5, 3.1, 200)

pol_lag = lagrange(x_coef, y_coef)

fig = plt.figure(figsize = (10,8))
plt.scatter(x_coef, y_coef, s=200, c='r')
plt.plot(x, pol_lag(x), 'b', lw='3')
plt.title('Polinomio de Lagrange (scipy)', fontsize=20)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# ## Links para ampliar
# 
# Aquí os dejamos algunos links, por si queréis echarles un vistazo:
# * https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html
# * https://es.wikipedia.org/wiki/Interpolaci%C3%B3n_polin%C3%B3mica_de_Lagrange#:~:text=En%20an%C3%A1lisis%20num%C3%A9rico%2C%20el%20polinomio,por%20Leonhard%20Euler%20en%201783.
# * https://es.wikipedia.org/wiki/Interpolaci%C3%B3n_polin%C3%B3mica_de_Newton

# ## Ejercicios para que hagáis
# 
# **Ejercicio 1:** 
# 
# Prepara un programa para evaluar y dibujar el polinomio de Lagrange, construido mediante los monomios fundamentales, utilizando una function.  

# In[76]:


# ESCRIBE AQUÍ TU CÓDIGO


# **Ejercicio 2:** 
# 
# Construye un polinomio de Lagrange, mediante la tabla de diferencias divididas, para interpolar la función $\sin(x)$ en los puntos $\frac{\pi}{2}, \; 0, \; \frac{\pi}{3}, \; \frac{\pi}{2}$.

# In[77]:


# ESCRIBE AQUÍ TU CÓDIGO


# ## Ejercicios para practicar un poco más
# 
# Para practicar un poco sobre lo que acabamos de explicar, te sugerimos que hagas (con la ayuda de Pyhton, si quieres) los siguientes ejercicios:
# 
# * https://existelimite.blogspot.com/2014/02/calculo-del-polinomio-de-interpolacion.html
# * https://existelimite.blogspot.com/2016/11/aproximamos-la-funcion-seno-con-un.html
#   
