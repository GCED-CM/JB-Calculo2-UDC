#!/usr/bin/env python
# coding: utf-8

# # Boletín 1: Vectores y geometría del espacio
# 
# Este boletín contiene una selección modificada de los problemas que aparecen en el capítulo 11 (pág. 829-830) del libro de R. Larson y B.H. Edwards, *Cálculo de 2 variables*, 10a, McGraw-Hill, 2016.

# **<FONT SIZE=4>[1]</font>** Determina si $\mathbf{u}$ y $\mathbf{v}$ son ortogonales, paralelos o ninguna de las dos cosas en los siguientes casos:
# 
# 1. $\mathbf{u} = (7,-2, 3)^{t}$, $\mathbf{v}=(-1,4,5)^{t}$.
#    
# 2. $\mathbf{u} = (-4,3, -6)^{t}$, $\mathbf{v}=(16,-12,24)^{t}$.

# **<FONT SIZE=4>[2]</font>** Sean $\mathbf{u} = (-3,2,0)$ y $\mathbf{v} = (2,1,0)$. Comprueba, utilizando `numpy`, si te hace falta, que la suma de los cuadrados de las longitudes de las diagonales del paralelogramo determinado por los vectores $\mathbf{u}$ y $\mathbf{v}$ es igual a la suma de los cuadrados de las longitudes de los cuatro lados. Demuestra que esta propiedad es cierta en general (para cualquier par de vectores $\mathbf{u}$ y $\mathbf{v}$).

# **<FONT SIZE=4>[3]</font>** Sean $\mathbf{u} = \vec{PQ}$ y $\mathbf{v} = \vec{PR}$. Calcula las componentes de $\mathbf{u}$ y $\mathbf{v}$, $\mathbf{u}\cdot\mathbf{v}$, $\mathbf{v}\cdot\mathbf{v}$, el ángulo que forman $\mathbf{u}$ y $\mathbf{v}$, los vectores unitarios en estas direcciones, un vector unitario ortogonal a esos dos vectores y las proyecciones de $\mathbf{u}$ sobre $\mathbf{v}$ y de $\mathbf{v}$ sobre $\mathbf{u}$ en los siguientes casos:
# 
# 1. $P=(5,0,0)$, $Q=(4,4,0)$, $R=(2,0,6)$ (coordenadas cartesianas).
# 2. $P=(2,-1,3)$, $Q=(0,5,1)$, $R=(5,5,0)$ (coordenadas cartesianas).

# **<FONT SIZE=4>[4]</font>** Calcula el volumen del paralelepípedo que tiene por vértices los puntos $P=(2,0,3)$, $Q=(4,1,3)$, $R=(4,0,4)$ y $S=(2,-1,5)$, en coordenadas cartesianas, siendo $\vec{PQ}$, $\vec{PR}$ y $\vec{PS}$ tres de sus aristas. 
# 
# Construye una *function* en `numpy` que reciba cuatro puntos en coordenadas cartesianas arbitrarias, $P$, $Q$, $R$ y $S$, y calcule el volumen de tal paralelepípedo. Pruébala con el ejemplo anterior. 

# **<FONT SIZE=4>[5]</font>** Convierte los siguientes puntos y expresiones al sistema de coordenadas que se indique:
# 
# 1. El punto de coordenadas cartesianas $(-2\sqrt{2}, 2\sqrt{2}, 2)$ en coordenadas cilíndricas y esféricas.
# 2. El punto de coordenadas cilíndricas $(100, -\pi/6, 50)$ en coordenadas esféricas y cartesianas.
# 3. La expresión $x^2 - y^2 = 2z$ en coordenadas cilíndricas y esféricas.
# 4. La expresión $x^2 + y^2 + z^2 = 16$ en coordenadas cilíndricas y esféricas.
# 5. La expresión $x^2 -x + y^2 - y = 0$ en coordenadas cilíndricas y esféricas.
# 6. La expresión $r = 5\cos\theta$ en coordenadas cartesianas.
# 7. La expresión $\theta = \pi/4$ en coordenadas cartesianas.
# 8. La expresión $\rho = 3\cos\phi$ en coordenadas cartesianas.
# 9. La expresión $r = \frac{2}{1-\cos\theta}$ en coordenadas cartesianas.

# **<FONT SIZE=4>[6]</font>** Calcula la ecuación cartesiana de las siguientes esferas. Pasa estas ecuaciones a coordenadas esféricas, ayudándote de `sympy`.
# 
# 1. Centro $(3,-2,6)$ y diámetro $15$.
# 2. La esfera que incluye un diámetro con extremos en $(0,0,4)$ y $(4,6,0)$.

# **<FONT SIZE=4>[7]</font>** Pasa las siguientes ecuaciones de esferas a su forma estándar (completando el cuadrado) para obtener su radio y su centro:
# 
# 1. $x^2 + y^2 + z^2 - 4x - 6y + 4 = 0$.
# 2. $x^2 + y^2 + z^2 - 10x + 6y - 4z + 34 = 0$.

# **<FONT SIZE=4>[8]</font>** Encuentra dos curvas generadoras diferentes de las siguientes superficies de revolución:
# 
# 1. $y^2 + z^2 - 4x = 0$.
# 2. $x^2 + 2y^2 + z^2 = 3y$.
# 3. $x^2 + y^2 = 4z^2$.

# **<FONT SIZE=4>[9]</font>** Determina la ecuación de la superficie de revolución generada al rotar
# 
# 1. La curva $z^2 = 2y$ en el plano $YZ$ alrededor del eje $Y$.
# 2. La curva $2x + 3z = 1$ en el plano $XZ$ alrededor del eje $X$.
# 3. La curva $y^2 + (z-1)^2 = 1$ en el plano $YZ$ alrededor del eje $Z$.
