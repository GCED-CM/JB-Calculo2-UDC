#!/usr/bin/env python
# coding: utf-8

# # Boletín 1: Vectores y geometría del espacio
# 
# Este boletín contiene una selección modificada de los problemas que aparecen recogidos en las secciones 13.1 y 13.2 (capítulo 13) del libro de R. Larson y B.H. Edwards, *Cálculo de 2 variables*, 10a, McGraw-Hill, 2016.

# **<FONT SIZE=4>[1]</font>** Describe el dominio y el rango de las siguientes funciones:
# 
# 1. $g(x,y) = x\sqrt{y}$,
# 2. $h(x,y) = \arccos(x+y)$,
# 3. $s(x,y) = \ln(xy-6)$,
# 4. $u(x,y) = \dfrac{-4x}{x^2+y^2+1}$.
# 
# 

# **<FONT SIZE=4>[2]</font>** Dibuja las curvas de nivel para los valores indicados de la constante $c$ en los siguientes casos. Hazlo sobre papel y, también, utilizando la función `contour` de `matplotlib.pyplot`, como se muestra en la Sección 2.1.3 del presente Jupyter Book.
# 
# 1. $z = x^2+4y^2$, $c=0$, $2$, $4$, $6$,
# 2. $f(x,y) = xy$, $c=\pm 1$, $\pm 2$, $\pm 3$, $\pm 4$,
# 3. $g(x,y) = \dfrac{x}{x^2+y^2}$, $c=\pm \frac{1}{2}$, $\pm 1$, $\pm 2$,
# 4. $h(x,y) = \ln(x-y)$, $c=0$, $c=\pm \frac{1}{2}$, $\pm 1$, 
# 5. $p(x,y) = \dfrac{y}{x^2}$, $c=0$, $c=\pm 1$, $\pm 2$,
# 6. $s(x,y) = 1-|x| - |y|$, $c=0$, $c=\pm \frac{1}{2}$, $\pm 1$, $\pm 2$.

# **<FONT SIZE=4>[3]</font>** Razona si son correctas las siguientes afirmaciones:
# 
# 1. Si $f\left(x_{0}, y_{0}\right) = f\left(x_{1}, y_{1}\right)$ entonces $x_{0}=x_{1}$ e $y_{0}=y_{1}$.
# 2. Si $f$ es una función entonces $f(ax,ay) = a^2 f(x,y)$.
# 3. Una recta vertical puede cortar a la gráfica de $z=f(x,y)$ como mucho en un solo punto.
# 4. Dos curvas de nivel diferentes de la gráfica $z=f(x,y)$ pueden intersecarse.

# **<FONT SIZE=4>[4]</font>** Calcula el límite en el punto indicado y analiza la continuidad en el mismo punto de las siguientes funciones:
# 
# 1. $$\displaystyle\lim_{(x,y)\to(0,2)} \dfrac{x}{y},$$
# 2. $$\displaystyle\lim_{(x,y)\to(1,1)} \dfrac{x}{\sqrt{x+y}},$$
# 3. $$\displaystyle\lim_{(x,y)\to(0,1)} \dfrac{\arcsin(xy)}{1-xy},$$
# 4. $$\displaystyle\lim_{(x,y)\to(2\pi,4)} \sin\left(\dfrac{x}{y}\right).$$

# **<FONT SIZE=4>[5]</font>** Calcula el límite, si existe, y, si no es así, explica el motivo:
# 
# 1. $$\displaystyle\lim_{(x,y)\to(1,1)} \dfrac{xy-1}{1+xy},$$
# 2. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x^4-4y^4}{x^2+2y^2},$$
# 3. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x-y}{\sqrt{x}-\sqrt{y}},$$
# 4. $$\displaystyle\lim_{(x,y,z)\to(0,0,0)} \dfrac{xy+yz^2+xz^2}{x^2+y^2+z^2},$$
# 5. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x}{\sqrt{x^2+y^2}},$$
# 6. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x^2y^2}{\left(x^2+y^2\right)^2},$$
# 7. $$\displaystyle\lim_{(x,y)\to(0,0)} xy\cos\left(\dfrac{1}{xy}\right),$$
# 8. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x^2y^2}{x^2y^2+\left(x-y\right)^2},$$

# **<FONT SIZE=4>[6]</font>** Calcula los siguientes límites. Es muy posible que tengas que usar coordenadas polares o esféricas y la regla de l'Hôpital. Y, ya de paso, comprueba tus cálculos usando `sympy`, tal como se hace en la Sección 2.2.4.
# 
# 1. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{xy^2}{x^2+y^2},$$
# 2. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x^2-y^2}{\sqrt{x^2+y^2}},$$
# 3. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{\sin(x^2+y^2)}{x^2+y^2},$$
# 4. $$\displaystyle\lim_{(x,y)\to(0,0)} \left(x^2+y^2\right)\ln\left(x^2+y^2\right),$$
# 5. $$\displaystyle\lim_{(x,y,z)\to(0,0,0)} \dfrac{xyz}{x^2+y^2},$$
# 6. $$\displaystyle\lim_{(x,y,z)\to(0,0,0)} \arctan\left(\dfrac{1}{x^2+y^2+z^2}\right),$$
# 7. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{\cos\left(x^2+y^2\right)-e^{x^2+y^2}}{\sin\left(x^2+y^2\right)},$$
# 8. $$\displaystyle\lim_{(x,y)\to(0,0)} \dfrac{x^2+y^2}{\sqrt{x^2+y^2+1}-1}.$$

# **<FONT SIZE=4>[7]</font>** Analiza la continuidad de las siguientes funciones respecto al valor del parámetro constante $a$:
# 
# 1. $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{x^4-y^4}{x^2+y^2} & \quad \mbox{si}\; (x,y)\neq(0,0), \\
# a & \quad \mbox{si}\; (x,y)=(0,0),\end{array}\right.$$
# 2. $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{4x^2y^2}{x^2+y^2} & \quad \mbox{si}\; (x,y)\neq(0,0), \\
# a & \quad \mbox{si}\; (x,y)=(0,0),\end{array}\right.$$
# 3. $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{x^2+2xy^2+y^2}{x^2+y^2} & \quad \mbox{si}\; (x,y)\neq(0,0), \\
# a & \quad \mbox{si}\; (x,y)=(0,0),\end{array}\right.$$
# 4. $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{\sin(xy)}{xy} & \quad \mbox{si}\; xy\neq 0, \\
# a & \quad \mbox{si}\; xy=0,\end{array}\right.$$
# 5. $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{\sin\left(x^2-y^2\right)}{x^2-y^2} & \quad \mbox{si}\; x^2\neq y^2, \\
# a & \quad \mbox{si}\; x^2=y^2,\end{array}\right.$$
# 6. $$f(x,y,z) = \frac{z}{x^2+y^2+a}.$$

# **<FONT SIZE=4>[8]</font>** Dada la función 
# 
# $$f(x,y)=xy\frac{x^2-y^2}{x^2+y^2},$$
# definir $f(0,0)$ de manera que $f$ sea continua en el origen de coordenadas.

# **<FONT SIZE=4>[9]</font>** Consideramos la siguiente función
# 
# $$f(x,y)=\left\{ \begin{array}{ll}
# \dfrac{x^2+y^2}{\alpha\ln\left(x^2+y^2+1\right)}+\beta x & \quad \mbox{si}\; x\neq 0\; \mbox{e}\; y\neq 0, \\
# \gamma & \quad \mbox{si}\; x=0\; \mbox{o}\; y=0,\end{array}\right.$$
# siendo $\alpha$, $\beta$, $\gamma\in\mathbb{R}$. Obtén los valores de estas constantes para que se verifiquen las siguientes propiedades (todas a la vez, por supuesto):
# 
# 1. El punto $(1,0)$ pertenece a la curva de nivel $1$ de $f$,
# 2. la función $f$ es continua en el punto $(0,0)$ y
# 3. la función $f$ es continua en el punto $(1,0)$.
