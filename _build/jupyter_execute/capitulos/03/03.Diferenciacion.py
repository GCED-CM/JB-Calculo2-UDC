#!/usr/bin/env python
# coding: utf-8

# # Diferenciabilidad
# 
# Comenzaremos esta sección motivando la aparición de un concepto más fuerte que el asociado a la existencia de las derivadas parciales, que resulta ser el concepto de diferenciabilidad. Para ello es necesario explicar que para funciones de dos o más variables la existencia de las derivadas parciales (es decir, la derivabilidad en la dirección de los ejes) no garantiza la continuidad, a diferencia de lo que ocurre para funciones de una variable. Además, la existencia de las derivadas parciales tampoco garantiza la existencia de todas las derivadas direccionales. Como ejemplo que ilustra ambas cuestiones, se puede considerar el siguiente. 
# 
# ````{prf:example}
# :label: ex_03_der_cont Existencia de derivadas parciales no implica continuidad ni derivabilidad 
# :nonumber:
# 
# La función 
# 
# $$
# f(x,y)=\left\{
# \begin{array}{ll}
# \dfrac{-3xy}{x^2+y^2} & \textrm{si }(x,y)\neq
# (0,0),
# \\ 
#  0 & \textrm{si }(x,y)=(0,0),
# \end{array}
# \right.
# $$
# 
# no es continua en $(0,0)$ ni existen todas sus derivadas direccionales, pero existen sus derivadas parciales (de primer orden) en dicho punto. Se puede comprobar que $f$ no es continua en $(0,0)$ analizando su límite a través de dos caminos como se muestra en la figura. En concreto, el límite restringido a la recta $y=x$ es
# 
# $$
# \lim_{\substack{ (x,y)\to (0,0)\\ y=x}} f(x,y)=\lim_{x\to 0} f(x,x)=\lim_{x\to 0}\dfrac{-3x^2}{2x^2}=-\dfrac{3}{2},
# $$
# 
# mientras que considerando la recta $y=-x$ se tiene 
# 
# $$
# \lim_{\substack{ (x,y)\to (0,0)\\ y=-x}} f(x,y)=\lim_{x\to 0} f(x,-x)=\lim_{x\to 0}\dfrac{3x^2}{2x^2}=\dfrac{3}{2}.
# $$
# 
# Por tanto, el límite de $f$ en $(0,0)$ no existe, y podemos concluir que $f$ no es continua en $(0,0)$. A continuación, comprobamos la existencia de las derivadas parciales en el $(0,0)$ utilizando la definición,    
# 
# \begin{eqnarray*}
# \dfrac{\partial f}{\partial x}(0,0)&=\lim_{h\to 0} \dfrac{f(h,0)-f(0,0)}{h}=\lim_{h\to 0}\dfrac{0-0}{h}=0,\\
# \dfrac{\partial f}{\partial y}(0,0)&=\lim_{h\to 0} \dfrac{f(0,h)-f(0,0)}{h}=\lim_{h\to 0}\dfrac{0-0}{h}=0.
# \end{eqnarray*}
# 
# Sin embargo, en este caso podemos comprobar, de forma análoga a como sigue, que no existe en el $(0,0)$ ninguna otra derivada direccional distinta a las parciales. Por simplicidad, lo comprobamos únicamente en la dirección del vector $\mathbf{u}=\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)$: 
# 
# \begin{eqnarray*}
#  D_{\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)}f(0,0) &:=& 
#     \lim_{h\to 0}\frac{f\left( (0,0) + h\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right) \right)-f(0,0)}{h} \\
#     &=& \lim_{h\to 0}\frac{f\left(\frac{h}{\sqrt{2}},\frac{h}{\sqrt{2}}\right)}{h}=\lim_{h\to 0}\frac{\frac{-\frac{3h^2}{2}}{\frac{h^2}{2}+\frac{h^2}{2}}}{h}=
#     \left\{\begin{array}{l}\displaystyle\lim_{h\to 0^-}\frac{-3}{2h}=\infty\\ \displaystyle\lim_{h\to 0^+}\frac{-3}{2h}=-\infty\end{array} \right.
# \end{eqnarray*}
# 
# 
# <img src="../../images/03_ejemplo1.png" width="250"/>
# 
# A continuación, vamos a calcular estos límites pero con la ayuda de la librería `Sympy`.
# 
# ````
# 

# In[9]:


import sympy as sp

x, y, h = sp.symbols('x y h', real=True) # definimos las variables simbólicas
f1 = sp.Lambda((x,y),-3*x*y/(x**2+y**2)) # definimos la expresión de f para puntos distintos del origen

print('Límite restringido a y=x: ',sp.limit(f1(x,x),x,0))
print('Límite restringido a y=-x: ',sp.limit(f1(x,-x),x,0))
print('Derivada parcial respecto a x en el (0,0): ',sp.limit((f1(h,0)-0)/h,h,0))
print('Derivada parcial respecto a y en el (0,0): ',sp.limit((f1(0,h)-0)/h,h,0))
print('Derivada direccional en el (0,0) en la dirección de la recta y=x: ',sp.limit((f1(h/sp.sqrt(2),h/sp.sqrt(2))-0)/h,h,0,dir='-')
                                                                        , sp.limit((f1(h/sp.sqrt(2),h/sp.sqrt(2))-0)/h,h,0,dir='+'))


# El concepto de diferenciabilidad está relacionado con la existencia de una aproximación lineal de la función en las proximidades del punto. En concreto, introducimos a continuación su definición formal para el caso de funciones escalares de dos variables resultando natural su extensión a más variables,
# 
# ````{prf:definition} Diferenciabilidad
# :label: def_03_difer 
# :nonumber: 
# 
# Sea $f:R\subset \mathbb{R}^2\longrightarrow
# \mathbb{R}$ con $R$ abierto. Decimos que $f$ es diferenciable en $(x_0,y_0)\in D$, si existen las derivadas parciales primeras de $f$ en el punto $(x_0,y_0)$, y además
# 
# $$
# \lim_{(x,y)\to (x_0,y_0)}\dfrac{f(x,y)-[f(x_0,y_0)+\nabla f(x_0,y_0)\cdot (x-x_0,y-y_0)]}{||(x-x_0,y-y_0)||}=0.
# $$
# 
# Decimos que $f$ es diferenciable en $R$, si lo es en cada punto de $R$.
# 
# ````
# 
# A continuación, vamos a analizar este límite, con la ayuda de la librería `Sympy`, para comprobar que la función del ejemplo anterior no es diferenciable en el $(0,0)$.    

# In[3]:


import sympy as sp

x, y = sp.symbols('x y', real=True) # definimos las variables simbólicas
f1 = sp.Lambda((x,y),-3*x*y/(x**2+y**2)) # definimos la expresión de f para puntos distintos del origen
fun = sp.Lambda((x,y),f1(x,y)/sp.sqrt(x**2+y**2)) # definimos la función del límite asociado a la diferenciabilidad 

# calculamos el límite a través de rectas
m = sp.Symbol('m', real=True)
print('Límites direccionales: ',sp.limit(fun(x,m*x),x,0)) # son infinitos

# calculamos los límites iterados (coinciden aunque en este caso no existe el límite)
fy = sp.limit(fun(x,y),x,0)
print('Límite iterado empezando en x: ',sp.limit(fy,y,0))
fx = sp.limit(fun(x,y),y,0)
print('Límite iterado empezando en y: ',sp.limit(fx,x,0))

# calculamos el límite en coordenadas polares
r = sp.Symbol('r', nonnegative=True)
theta = sp.Symbol('theta', real=True)
fpol=fun(r*sp.cos(theta), r*sp.sin(theta))
display('Función en polares: ',sp.simplify(fpol))
print('Límite en polares: ',sp.limit(fpol,r,0,dir='+')) 
# restringidos a semirectas son infinitos 


# Por tanto, no existe el límite que tiene que ser cero para la diferenciabilidad en el $(0,0)$, y en consecuencia la función no es diferenciable en dicho punto. Finalizamos la sección estableciendo dos condiciones para la diferenciabilidad, la necesaria de continuidad y la suficiente de continuidad de las derivadas parciales.
# 
# ````{prf:theorem} Diferenciabilidad implica continuidad 
# :label: th_03_cont
# :nonumber: 
# Si $f$ es diferenciable en $\mathbf{x}_0$, entonces $f$ es continua en $\mathbf{x}_0$.
# 
# ````
# 
# ````{prf:theorem} Condición suficiente para la diferenciabilidad 
# :label: th_03_cont_der
# :nonumber: 
# Si las derivadas parciales (de primer orden) de $f$ son continuas en una región abierta $R$, entonces $f$ es diferenciable en $R$.
# 
# ````
# 

# In[ ]:




