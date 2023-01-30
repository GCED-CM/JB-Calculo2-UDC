#!/usr/bin/env python
# coding: utf-8

# # Coordenadas cilíndricas y esféricas
# 
# Hasta ahora hemos utilizado las coordenadas cartesianas para representar punto, rectas y superficies en $\mathbb{R}^{3}$. 
# Es decir, caracterizamos cada punto por sus coordenadas respecto a los tres ejes cartesianos: $(x,y,z)$. 
# En esta sección vamos a estudiar otras dos maneras de describir un punto con las coordenadas cilíndircas y esféricas, lo que, 
# en ocasiones, nos permitirá simplificar la escritura.
# 
# ## Coordenadas cilíndricas
# 
# El sistema de coordenadas cilíndricas es una extensión de las coordenadas polares en el plano al espacio 3D. Mantendremos las
# coordenadas polares en el plano $XY$ añadiendo la altura $Z$. Es decir:
# 
# ````{prf:definition} Coordenadas cilíndricas
# :label: def_1.8.cilindricas
# :nonumber: 
# 
# En un **sistema de coordenadas cilíndricas** un punto $P$ del espacio se representa por medio de una terna ordenada
# $\left(r,\theta,z\right)$, donde:
# 
# 1. $(r,\theta)$ es una representación en coordenadas polares de la proyección de $P$ sobre el plano $XY$.
# 2. $z$ es la distancia dirigida de $(r,\theta)$ a $P$.
# 
# <img src="../../images/1.8.coordenadas_cilindricas.jpg" width="350"/>
# 
# ````
# 
# Para realizar los cambios de coordenadas, de cartesianas a cilíndricas y viceversa, aplicaremos las siguientes fórmulas:
# 
# * **Cartesianas a cilíndricas**: 
# 
#     $r = \sqrt{x^2+y^2}$, $\theta = \arctan\left(\frac{y}{x}\right)$, $z=z$.
# * **Cilíndricas a cartesianas**:
# 
#     $x = r\cos\theta$, $y=r\sin\theta$, $z=z$.
# 
# Las coordenadas cilíndricas son especialmente convenientes para representar superficies cilíndircas y superficies de revolución con el eje $Z$ como eje de simetría, 
# como mostramos en la figura a continuación:
# 
# <img src="../../images/1.8.cilindros_en_cilindricas.jpg" width="1000"/>
# 
# También los planos verticales y horizontales tienen ecuaciones simples en coordenadas cilíndricas:
# 
# <img src="../../images/1.8.planos_en_cilindricas.jpg" width="750"/>
# 
# 
