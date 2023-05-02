#!/usr/bin/env python
# coding: utf-8

# # Integrales triples

# ## Integración de Riemann 3D
# 
# Todo el análisis que hemos hecho en la Sección {ref}`sec:4.3.IntegralesDobles` se extiende directamente de dos a tres variables. En este caso, en lugar de dividir el dominio en rectángulos y hacer que el tamaño del dichos rectángulos tienda a $0$, lo que hacemos es dividir el dominio de partida (en 3D) en cubos, evaluar la función que queremos integrar en algún punto de cada cubo y, a continuación, hacer que el tamaño del cubo tienda a $0$.
# 
# Queremos definir 
# 
# $$
# \int\int_{Q}\int f(x,y,z) dV ,
# $$
# donde $Q$ es un dominio tridimensional que suponemos divisible en cubos (si no fuera así, aproximaríamos $Q$ por una suma de cubos) y $f:\mathbb{R}^3 \to \mathbb{R}$ una función que suponemos, por simplicidad, continua en $Q$.
# 
# Es decir, $Q$ sería algo parecido a lo que mostramos en la siguiente imagen (tomada de  [esta página web](https://sites.google.com/site/kevinportafoliodigital/cuarto-parcial/integrales-triples) ):
# 
# <img src="../../images/4.5.Dominio1.png" width="300"/>
# 
# El volumen del i-ésimo cubo será 
# 
# $$
# \Delta V_{i} = \Delta x_{i} \Delta y_{i} \Delta z_{i}.
# $$
# 
# <img src="../../images/4.5.Dominio2.png" width="300"/>
# 
# Entonces, eligiendo un punto $\left(x_{i},y_{i},z_{i}\right)$, en cada cubo de la partición, podemos definir la suma de Riemann como
# 
# $$
# \sum_{i=1}^{N} f\left(x_{i},y_{i},z_{i}\right) \Delta V_{i}.
# $$
# 
# Si ahora definimos la norma de la partición, $\|\Delta\|$, como la longitud de la diagonal más larga de los $N$ cubos de la partición, tomando el límite $\|\Delta\| \to 0$, llegamos a la definición de integral de Riemann en $Q$:
# 
# ````{prf:definition} Integral de Riemann para una función de tres variables 
# :label: def_4.5_Riemann
# :nonumber:
# 
# Supongamos una región $Q$ contenida en $\mathbb{R}^{3}$ y descompuesta en $N$ cubos, $V_{i}$, $i=1,2,...,N$. Sea $f$ una función real continua definida sobre $Q$. Definimos la **integral triple de $f$ sobre $Q$** como el siguiente límite, si existe:
# 
# $$
# \int\int_{Q}\int f(x,y,z) dV := \lim_{\|\Delta\|\to 0} \sum_{i=1}^{N} f\left(x_{i},y_{i},z_{i}\right) \Delta V_{i}.
# $$
# ````
# 
# Las propiedades de las integrales triples son las mismas que para las dobles. Las recordamos a continuación:
# 
# ````{prf:property} Propiedades de las integrales dobles
# :label: prop_4.5_int_triples
# :nonumber: 
# 
# Sean $f$ y $g$ continuas en una región cerrada y acotada $R$ del plano, y sea $c$ una constante.
# 
# * $\displaystyle\int\int_Q\int cf(x,y,z)\,dV=c\int\int_Q\int f(x,y,z)\,dV$.
# 
# * $\displaystyle\int\int_Q\int \left(f(x,y,z)\pm g(x,y,z)\right)\,dV=\int\int_Q\int f(x,y,z) \,dA\pm \int\int_Q\int g(x,y,z) \,dV$.
# 
# * Si $Q$ es la unión de dos subregiones, $Q_1$ y $Q_2$, que no se sobreponen, entonces 
#     $\displaystyle\int\int_Q\int f(x,y,z)\,dV=\int\int_{Q_1}\int f(x,y,z)\,dV+\int\int_{Q_2}\int f(x,y,z)\,dV$.
# ````

# ## Integrales triples iteradas
# 
# ````{prf:theorem} Evaluación mediante integrales iteradas
# :label: Th_4.5_iteradas
# :nonumber: 
# 
# Sea $f$ una función continua definida sobre la siguiente región sólida $Q$:
# 
# $$
# a\leq x \leq b, \quad h_{1}(x)\leq y \leq h_{2}(x), \quad g_{1}(x,y) \leq z \leq g_{2}(x,y),
# $$
# donde $h_{1}$, $h_{2}$, $g_{1}$ y $g_{2}$ son funciones continuas. Entonces,
# 
# $$
# \int\int_{Q}\int f(x,y,z) dV = \int_{a}^{b} \int_{h_{1}(x)}^{h_{2}(x)} \int_{g_{1}(x,y)}^{g_{2}(x,y)} f(x,y,z) \, dz\, dy\, dx.
# $$
# ````
# 
# ````{prf:example} Evaluación de una integral triple iterada
# :label: Ej_4.5_ejemplo1
# :nonumber: 
# 
# Evaluar la integral triple iterada
# 
# $$
# \int_{0}^{2} \int_{0}^{x} \int_{0}^{x+y} e^{x}(y+2z) \, dz\, dy\, dx.
# $$
# 
# **Solución:**
# 
# En primer lugar, realizamos la integral más interna (respecto a $z$):
# 
# \begin{eqnarray*}
# \int_{0}^{2} \int_{0}^{x} \int_{0}^{x+y} e^{x}(y+2z) \, dz\, dy\, dx &=& \int_{0}^{2} \int_{0}^{x} e^{x} \left( yz+z^2\right) \Big]_{0}^{x+y} dy\,dx \\
# &=& \int_{0}^{2} \int_{0}^{x} e^{x}\left( x^2 + 3xy + 2y^2 \right) dy\, dx.
# \end{eqnarray*}
# Vamos a continuación con la segunda integral:
# 
# \begin{eqnarray*}
# \int_{0}^{2} \int_{0}^{x} e^{x}\left( x^2 + 3xy + 2y^2 \right) dy\, dx &=& \int_{0}^{2} \left[e^{x}\left( x^2y + \frac{3xy^{2}}{2} \frac{2y^{3}}{3}\right)\right]_{0}^{x} dx \\
# &=& \frac{19}{6} \int_{0}^{2} x^3 e^{x} dx.
# \end{eqnarray*}
# 
# Por último, la tercera integral, ahora respecto a $x$:
# 
# \begin{eqnarray*}
# \frac{19}{6} \int_{0}^{2} x^3 e^{x} dx &=& \frac{19}{6} \left[ e^{x}\left( x^3 + 3x^2 + 6x -6 \right) \right]_{0}^{2} \\
# &=& 19\left(\frac{e^2}{3} + 1 \right).
# \end{eqnarray*}
# 
# ````
# 
# Vamos a hacer este mismo ejemplo aprovechando la potencia de `Sympy`:

# In[1]:


import sympy as sp
x, y, z = sp.symbols('x y z', real=True)
f = sp.Lambda((x,y,z),sp.exp(x)*(y+2*z))
integral = sp.integrate(f(x,y,z), (z,0,x+y), (y, 0, x), (x, 0, 2))
display(integral)


# ## Centro de masas y momentos de inercia
# 
# Vamos a ver una aplicación del cálculo de integrales para funciones que dependen de tres variables. Hablaremos del centro de masa y de los momentos de inercia (de primer y de segundo orden). 
# 
# El centro de masas para un cuerpo que ocupa la región $Q$, y cuya densidad de masa viene dada por la función $\rho(x,y,z)$, es un punto geométrico que se comporta como si en él estuviera aplicada la resultante de todas las fuerzas aplicadas sobre el sistema. Para un cuerpo, salvo en situaciones excepcionales (campos gravitacionales no uniformes), coincide con el centro de gravedad. También puede aplicarse a sistemas discretos (por ejemplo, órbitas planetarias o movimientos de moléculas). Aquí puedes encontrar más información:
# 
# * [Definición en la Wikipedia](https://es.wikipedia.org/wiki/Centro_de_masas).
# * [Artículo de la Khan Academy](https://es.khanacademy.org/science/physics/linear-momentum/center-of-mass/a/what-is-center-of-mass#:~:text=El%20centro%20de%20gravedad%20es,que%20el%20centro%20de%20masa.).
# 
# ¡Pues vamos a aprender a calcularlo utilizando la integración sobre el cuerpo $Q$!
# 
# ````{prf:definition} Centro de masas y momentos de primer orden 
# :label: def_4.5_CM
# :nonumber:
# 
# Consideramos un cuerpo sólido que ocupa la región $Q$ y cuya densidad de masas viene dada por la función $\rho(x,y,z)$. Definimos
# 
# * **Masa del sólido**: $\displaystyle m = \int\int_{Q}\int\rho(x,y,z)\, dV$.
# * **Momentos de primer orden**:
#     * Primer momento con respecto al plano $YZ$: $\displaystyle\quad M_{yz} = \int\int_{Q}\int x\rho(x,y,z)\, dV$.
#     * Primer momento con respecto al plano $XZ$: $\displaystyle\quad M_{xz} = \int\int_{Q}\int y\rho(x,y,z)\, dV$.
#     * Primer momento con respecto al plano $XY$: $\displaystyle\quad M_{xy} = \int\int_{Q}\int z\rho(x,y,z)\, dV$.
# * **Centro de masas**. Es el punto de $Q$ con coordenadas $\left(\bar{x}, \bar{y}, \bar{z}\right)$, donde
#     * $\displaystyle \bar{x} = \frac{M_{yz}}{m}$,
#     * $\displaystyle \bar{y} = \frac{M_{xz}}{m}$,
#     * $\displaystyle \bar{z} = \frac{M_{xy}}{m}$.
# ````
# 
# Ahora vamos a definir los momentos de segundo orden, también llamados momentos de inercia:
# 
# ````{prf:definition} Momentos de segundo orden (momentos de inercia) 
# :label: def_4.5_MomentosInercia
# :nonumber:
# 
# * **Momento de inercia con respecto al eje $X$**: $\displaystyle \quad I_{x} = \int\int_{Q}\int \left(y^2 + z^2 \right) \rho(x,y,z)\, dV$.
# * **Momento de inercia con respecto al eje $Y$**: $\displaystyle \quad I_{y} = \int\int_{Q}\int \left(x^2 + z^2 \right) \rho(x,y,z)\, dV$.
# * **Momento de inercia con respecto al eje $Z$**: $\displaystyle \quad I_{z} = \int\int_{Q}\int \left(x^2 + y^2 \right) \rho(x,y,z)\, dV$.
# 
# ````
# 
# Vamos a comentar un *truco* muy usado. Si tenemos que calcular los tres momentos de inercia, podemos ahorrar tiempo de ejecución (ya sea en papel o en CPU) si calculamos:
# 
# * $\displaystyle \quad I_{xy} = \int\int_{Q}\int z^2 \, \rho(x,y,z)\, dV$,
# * $\displaystyle \quad I_{xz} = \int\int_{Q}\int y^2 \, \rho(x,y,z)\, dV$,
# * $\displaystyle \quad I_{yz} = \int\int_{Q}\int x^2 \, \rho(x,y,z)\, dV$,
# 
# y luego, aplicando la aditividad de la integral, hacemos las sumas correspondientes:
# 
# * $I_{x} = I_{xz} + I_{xy}$,
# * $I_{y} = I_{yz} + I_{xy}$,
# * $I_{z} = I_{xz} + I_{yz}$.
# 
# 
# ````{prf:example} Masa y momentos para un cubo de Rubik
# :label: ex_4.5_Rubik
# :nonumber:
# 
# Vamos a calcular, mediante integración, el centro de masa y los momentos de orden 2 de un cubo *tipo Rubik* 2x2 (imagen extraída de la [página web de la tienda de puzzles y juegos de mesa, Doctor Panush](https://doctorpanush.com/)) en el que suponemos que cada uno de los ocho cubitos está hecho de un plástico diferente y tienen, por tanto, diferente densidad: de 1 a 8 g/cm$^3$ (la densidad exacta en cada cubito puede inferirse de la integral en la que se calcula $m$). 
# 
# El cubo ocupa el dominio $[0,4]^{3}$, con unidades en cm (es decir, cada arista pequeña mide 2 cm).
# 
# <img src="../../images/4.5.Cubo_Panush.webp" width="300"/>
# 
# \begin{eqnarray*}
# m &=& \int_0^2\int_0^2\int_0^2 1 \, dx \, dy \, dz + \int_2^4\int_0^2\int_0^2 2 \, dx \, dy \, dz + \int_0^2\int_2^4\int_0^2 3 \, dx \, dy \, dz + \\
# && \int_2^4\int_2^4\int_0^2 4 \, dx \, dy \, dz + \int_0^2\int_0^2\int_2^4 5 \, dx \, dy \, dz + \int_2^4\int_0^2\int_2^4 6 \, dx \, dy \, dz + \\
# && \int_0^2\int_2^4\int_2^4 7 \, dx \, dy \, dz +  \int_2^4\int_2^4\int_2^4 8 \, dx \, dy \, dz \\
# &=& 1*8 + 2*8 + 3*8 + 4*8 + 5*8 + 6*8 + 7*8 + 8*8 = 288 \, \text{gr.}
# \end{eqnarray*}
# 
# Escribimos la fórmula para el cálculo de $M_{yz}$, pero dejaremos éste y el resto de los cálculos para `Sympy`, ¡que para eso está!
# 
# \begin{eqnarray*}
# M_{yz} &=& \int_{0}^{4}\int_{0}^{4}\int_{0}^{4} x\rho(x,y,z)\, dz\, dy\, dx \\
# &=& \int_0^2\int_0^2\int_0^2 x \, dz \, dy \, dx + \int_0^2\int_0^2\int_2^4 2x \, dz \, dy \, dx + \int_2^4\int_0^2\int_0^2 3x \, dz \, dy \, dx + \\
# && \int_2^4\int_0^2\int_2^4 4x \, dz \, dy \, dx + \int_0^2\int_2^4\int_0^2 5x \, dz \, dy \, dx + \int_0^2\int_2^4\int_2^4 6x \, dz \, dy \, dx + \\
# && \int_2^4\int_2^4\int_0^2 7x \, dz \, dy \, dx +  \int_2^4\int_2^4\int_2^4 8x \, dz \, dy \, dx
# \end{eqnarray*}
# ````
# 

# In[25]:


import sympy as sp
import numpy as np
x, y, z = sp.symbols('x y z', real=True)

m = ( sp.integrate(1, (z,0,2), (y, 0, 2), (x, 0, 2)) + sp.integrate(2, (z,2,4), (y, 0, 2), (x, 0, 2)) 
    + sp.integrate(3, (z,0,2), (y, 0, 2), (x, 2, 4)) + sp.integrate(4, (z,2,4), (y, 0, 2), (x, 2, 4))
    + sp.integrate(5, (z,0,2), (y, 2, 4), (x, 0, 2)) + sp.integrate(6, (z,2,4), (y, 2, 4), (x, 0, 2))
    + sp.integrate(7, (z,0,2), (y, 2, 4), (x, 2, 4)) + sp.integrate(8, (z,2,4), (y, 2, 4), (x, 2, 4)) )
print('m: ',m)

Myz = ( sp.integrate(x, (z,0,2), (y, 0, 2), (x, 0, 2)) + sp.integrate(2*x, (z,2,4), (y, 0, 2), (x, 0, 2))
    + sp.integrate(3*x, (z,0,2), (y, 0, 2), (x, 2, 4)) + sp.integrate(4*x, (z,2,4), (y, 0, 2), (x, 2, 4))
    + sp.integrate(5*x, (z,0,2), (y, 2, 4), (x, 0, 2)) + sp.integrate(6*x, (z,2,4), (y, 2, 4), (x, 0, 2))
    + sp.integrate(7*x, (z,0,2), (y, 2, 4), (x, 2, 4)) + sp.integrate(8*x, (z,2,4), (y, 2, 4), (x, 2, 4)) )
print('Myz: ', Myz)

Mxz = ( sp.integrate(y, (z,0,2), (x, 0, 2), (y, 0, 2)) + sp.integrate(2*y, (z,2,4), (x, 0, 2), (y, 0, 2))
    + sp.integrate(3*y, (z,0,2), (x, 2, 4), (y, 0, 2)) + sp.integrate(4*y, (z,2,4), (x, 2, 4), (y, 0, 2))
    + sp.integrate(5*y, (z,0,2), (x, 0, 2), (y, 2, 4)) + sp.integrate(6*y, (z,2,4), (x, 0, 2), (y, 2, 4))
    + sp.integrate(7*y, (z,0,2), (x, 2, 4), (y, 2, 4)) + sp.integrate(8*y, (z,2,4), (x, 2, 4), (y, 2, 4)) )
print('Mxz: ', Mxz)

Mxy = ( sp.integrate(z, (y, 0, 2), (x, 0, 2), (z,0,2)) + sp.integrate(2*z, (x, 0, 2), (y, 0, 2), (z,2,4))
    + sp.integrate(3*z, (x, 2, 4), (y, 0, 2), (z,0,2)) + sp.integrate(4*z, (x, 2, 4), (y, 0, 2), (z,2,4))
    + sp.integrate(5*z, (x, 0, 2), (y, 2, 4), (z,0,2)) + sp.integrate(6*z, (x, 0, 2), (y, 2, 4), (z,2,4))
    + sp.integrate(7*z, (x, 2, 4), (y, 2, 4), (z,0,2)) + sp.integrate(8*z, (x, 2, 4), (y, 2, 4), (z,2,4)) )
print('Mxy: ', Mxy)

CM = np.array([np.float64(Myz/m),np.float64(Mxz/m),np.float64(Mxy/m)])
print('Centro de masas: ', CM)

Iyz = ( sp.integrate(x**2, (z,0,2), (y, 0, 2), (x, 0, 2)) + sp.integrate(2*x**2, (z,2,4), (y, 0, 2), (x, 0, 2))
    + sp.integrate(3*x**2, (z,0,2), (y, 0, 2), (x, 2, 4)) + sp.integrate(4*x**2, (z,2,4), (y, 0, 2), (x, 2, 4))
    + sp.integrate(5*x**2, (z,0,2), (y, 2, 4), (x, 0, 2)) + sp.integrate(6*x**2, (z,2,4), (y, 2, 4), (x, 0, 2))
    + sp.integrate(7*x**2, (z,0,2), (y, 2, 4), (x, 2, 4)) + sp.integrate(8*x**2, (z,2,4), (y, 2, 4), (x, 2, 4)) )

Ixz = ( sp.integrate(y**2, (z,0,2), (x, 0, 2), (y, 0, 2)) + sp.integrate(2*y**2, (z,2,4), (x, 0, 2), (y, 0, 2))
    + sp.integrate(3*y**2, (z,0,2), (x, 2, 4), (y, 0, 2)) + sp.integrate(4*y**2, (z,2,4), (x, 2, 4), (y, 0, 2))
    + sp.integrate(5*y**2, (z,0,2), (x, 0, 2), (y, 2, 4)) + sp.integrate(6*y**2, (z,2,4), (x, 0, 2), (y, 2, 4))
    + sp.integrate(7*y**2, (z,0,2), (x, 2, 4), (y, 2, 4)) + sp.integrate(8*y**2, (z,2,4), (x, 2, 4), (y, 2, 4)) )

Ixy = ( sp.integrate(z**2, (y, 0, 2), (x, 0, 2), (z,0,2)) + sp.integrate(2*z**2, (x, 0, 2), (y, 0, 2), (z,2,4))
    + sp.integrate(3*z**2, (x, 2, 4), (y, 0, 2), (z,0,2)) + sp.integrate(4*z**2, (x, 2, 4), (y, 0, 2), (z,2,4))
    + sp.integrate(5*z**2, (x, 0, 2), (y, 2, 4), (z,0,2)) + sp.integrate(6*z**2, (x, 0, 2), (y, 2, 4), (z,2,4))
    + sp.integrate(7*z**2, (x, 2, 4), (y, 2, 4), (z,0,2)) + sp.integrate(8*z**2, (x, 2, 4), (y, 2, 4), (z,2,4)) )

print('Ix: ', Ixz+Ixy)
print('Iy: ', Ixy+Iyz)
print('Iz: ', Ixz+Iyz)


# **Ejercicio propuesto:**
# 
# Calcula el centro de masas y los momentos de inercia para un cuerpo que ocupa el cubo unidad, $[0,1]^3$, y cuya densidad de masa en el punto $(x,y,z)$ es proporcional al cuadrado de su distancia desde el origen. Es decir:
# 
# $$
# \rho(x,y,z) = k\left(x^2 + y^2 + z^2\right),
# $$
# para alguna constante $k\in\mathbb{R}$.
