#!/usr/bin/env python
# coding: utf-8

# # Extremos absolutos
# 
# Vamos a enfrentarnos ahora al equivalente multidimensional a los ejercicios que hacíais en vuestra tierna juventud (o sea: el año pasado) de calcular el máximo y el mínimo absoluto de una función definida en un intervalo cerrado y acotado.
# 
# Lo que en el caso de una variable era simplemente incluir los extremos del intervalo, ahora (se complica y) se enriquece mucho.
# Aparecen las llamadas **restricciones** o **ligaduras** entre variables que nos permiten limitar el conjunto en el que buscamos los extremos a un subconjunto cerrado y acotado del dominio en el que ya podremos buscar los extremos absolutos de la función. 
# 
# <img src="../../images/07_ejemplo.png" width="400"/>
# 
# Al igual que pasaba en funciones de una variable, en estos casos el máximo (o mínimo) absoluto, puede estar en el interior del dominio o en su frontera. Pero esta frontera, que para funciones de una variable sólo tiene dos puntos (los extremos del intervalo, puntos $a$ y $b$), ahora se convierte en un conjunto infinito y, por tanto, tendremos que localizar los candidatos a extremos absolutos. 
# 
# En esta sección estudiaremos una ingeniosa técnica que nos permite resolver problemas de optimización sobre las fronteras de regiones cerradas y acotadas, consistente en el llamado método de los **multiplicadores de Lagrange**. Por tanto, en esta sección se aborda el problema de encontrar los extremos absolutos (globales) de una función escalar de varias variables sobre una región cerrada y acotada.   

# ## Existencia de solución 
# 
# Vamos, antes de nada, a definir correctamente nuestro campo de juego.
# 
# ````{prf:definition} Conjunto cerrado y acotado
# :label: def_3.7_compacto 
# :nonumber:
# 
# Un conjunto $C$ en $\mathbb{R}^{2}$ se dice cerrado y acotado si:
# 
# 1. Contiene a toda su frontera.
# 2. Está contenido en alguna bola de centro $(0,0)$.
# 
# <img src="../../images/3.7.compacto.png" width="300"/>
# 
# ````
# 
# **Nota:** Una definición similar nos valdría para $\mathbb{R}^{3}$.
# 
# Ahora, nos preguntamos si el problema planteado tiene solución. La respuesta, que es afirmativa, se obtiene aplicando nuestro viejo conocido: el teorema de Weierstrass (en este caso, para funciones de dos variables).
# 
# ````{prf:theorem} Teorema de Weierstrass 
# :label: th_07_valor_extr
# :nonumber: 
# Sea $f$ una función escalar arbitraria definida en una región cerrada y acotada $C$. Entonces, $f$ alcanza en $C$ su valor máximo y su valor mínimo, es decir,
# 
# * Existe por lo menos un punto $\mathbf{x}_{1}\in C$ en el que $f$ toma su valor mínimo: 
# 
# $$f(\mathbf{x}_{1})=\min_{\mathbf{x}\in C}f(\mathbf{x}).$$
# 
# * Existe por lo menos un punto $\mathbf{x}_{2}\in C$ en el que $f$ toma su valor máximo: 
# 
# $$f(\mathbf{x}_{2})=\max_{\mathbf{x}\in C}f(\mathbf{x}).$$
# 
# ````

# ## Método de los multiplicadores de Lagrange con una restricción
# 
# ````{prf:example}
# :label: ex_07_lagrange 
# :nonumber:
# 
# Para ver cómo funciona esta técnica, consideramos el problema de encontrar el rectángulo de área máxima que puede estar inscrito en la elipse de ecuación 
# 
# $$
# \frac{x^2}{3^2}+\frac{y^2}{4^2}=1.
# $$
# 
# Consideramos un rectángulo arbitrario inscrito en la elipse con $(x,y)$ el vértice que se encuentra en el primer cuadrante, como se muestra en la figura.
# 
# <img src="../../images/07_ejemplo2.png" width="400"/>
# 
# Debido a que el rectángulo tiene lados de longitudes $2x$ y $2y$, su área está dada por 
# 
# $$
# \textbf{Función objetivo: }f(x,y)=4xy. 
# $$
# 
# Por otro lado, la elección de $(x, y)$ se limita a los puntos del primer cuadrante que se encuentran en la elipse
# 
# $$
# \textbf{Restricción: }\frac{x^2}{3^2}+\frac{y^2}{4^2}=1.
# $$
# 
# Ahora, consideramos esta ecuación como la curva de nivel uno de la función 
# 
# $$
# \textbf{Función asociada a la restricción: }g(x,y)=\frac{x^2}{3^2}+\frac{y^2}{4^2}. 
# $$
# 
# Al mismo tiempo, las curvas de nivel de $f$ representan una familia de hipérbolas:
# 
# $$
# f(x,y)=4xy=c.
# $$
# 
# En esta familia, las curvas de nivel factibles se corresponden con las hipérbolas que intersecan a la elipse. Maximizar $f$ sobre la elipse, consiste en encontrar la hipérbola de nivel máximo que interseca a la elipse. La curva de nivel que hace esto es la que es tangente a la elipse, como se muestra en la figura, alcanzándose el óptimo global en el punto de tangencia. 
# 
# <img src="../../images/07_ejemplo3.png" width="400"/>
# 
# Para encontrar este valor, hay que tener en cuenta que el vector gradiente es ortogonal a las curvas de nivel, y en consecuencia dos curvas son tangentes en un punto si y solo si sus gradientes son paralelos. Esto se traduce en que $\nabla f$ debe ser múltiplo escalar de $\nabla g$ en el óptimo global de nuestro problema (punto de tangencia): 
# 
# $$
# \nabla f(x,y)=\lambda \nabla g(x,y),
# $$
# 
# para algún $\lambda \in \mathbb{R}$. En el contexto de problemas de optimización, este escalar, que se suele denotar por $\lambda$, se llama **multiplicador de Lagrange**. Esta ecuación junto con la restricción forman un sistema de condiciones necesarias de extremo global, como se establece en los siguientes teoremas.  
# ````
# 
# 
# ````{prf:theorem} Teorema de Lagrange 
# :label: th_07_lagrange
# :nonumber: 
# Sean $f$ y $g$ dos funciones escalares arbitrarias con derivadas parciales primeras continuas, y $\mathbf{x}_0$ un extremo de $f$ sujeto a $g(\mathbf{x})=c$. Si $\nabla g(\mathbf{x}_0)\neq \mathbf{0}$, entonces existe un número real $\lambda$ tal que 
# 
# $$
# \nabla f(\mathbf{x}_0)=\lambda \nabla g(\mathbf{x}_0).
# $$
# ````
# A continuación, aplicamos este teorema a problemas de optimización en dos variables e indicamos los pasos a seguir para su resolución, resultando inmediata su exensión a más variables.   
# 
# ````{prf:remark} Método de los multiplicadores de Lagrange en 2D
# :label: rem_07_lagrange
# :nonumber:
# Sean $f$ y $g$ dos funciones escalares de dos variables con derivadas parciales primeras continuas. Para hallar el óptimo (máximo o mínimo) de $f$ sujeto a la restricción $g(x,y)=c$, en caso de existir, seguimos los pasos descritos a continuación.
# 
# * Resolvemos simultáneamente las ecuaciones $\nabla f(x,y)=\lambda \nabla g(x,y)$ y $g(x,y)=c$, calculando las soluciones del siguiente sistema de ecuaciones:
# 
# $$
# \left\{
# \begin{array}{rcl}
# \displaystyle\frac{\partial f}{\partial x}(x,y)&=&\displaystyle\lambda \frac{\partial g}{\partial x}(x,y),\\
# \displaystyle\frac{\partial f}{\partial y}(x,y)&=& \displaystyle\lambda \frac{\partial g}{\partial y}(x,y),\\
# g(x,y)&=&c.
# \end{array}\right.
# $$
# * Evaluamos $f$ en cada punto solución obtenido en el primer paso. El valor mayor da el máximo de $f$ sujeto a la restricción $g(x,y)=c$, y el valor menor da el mínimo de $f$ sujeto a la restricción $g(x,y)=c$. 
# 
# ````
# 
# ````{prf:example}
# :label: ex_07_lagrange_cont  
# :nonumber:
# 
# Retomamos el ejemplo anterior para aplicar el método de los multiplicadores de Lagrange. Recordemos que queremos encontrar el valor máximo de f(x,y)=4xy con $x,y\geq 0$, sujeto a la restricción $x^2/3^2+y^2/4^2=1$. En primer lugar, observamos que dicho problema tiene solución puesto que la función a optimizar es continua y la región de soluciones factibles es cerrada y acotada. Además, se observa que el gradiente de $g$ no se anula sobre ningún punto factible. A continuación, planteamos y resolvemos el sistema de ecuaciones que tienen que satisfacer los extremos globales.   
# 
# $$
# \left\{
# \begin{array}{ccccc}
# \displaystyle\frac{\partial f}{\partial x}(x,y)=\lambda \frac{\partial g}{\partial x}(x,y)
# &\Leftrightarrow& \displaystyle 4y=\frac{2}{9}\lambda x &\Leftrightarrow& \displaystyle \lambda=\frac{18y}{x},\\
# \displaystyle\frac{\partial f}{\partial y}(x,y)=\lambda \frac{\partial g}{\partial y}(x,y) &\Leftrightarrow& 
# \displaystyle 4x=\frac{1}{8}\lambda y &\Leftrightarrow& \displaystyle\lambda=\frac{32x}{y},\\
# g(x,y)=c &\Leftrightarrow& \displaystyle \frac{x^2}{9}+\frac{y^2}{16}=1. & & 
# \end{array}\right.
# $$
# 
# Igualando las dos expresiones para $\lambda$ obtenidas en las dos primeras ecuaciones se deduce  
# 
# $$
# \frac{18y}{x}=\frac{32x}{y} \Leftrightarrow y^2=\frac{16}{9}x^2.
# $$
# 
# Sustituyendo esta expresión para $y^2$ en la tercera ecuación, se obtiene el valor de $x$:
# 
# $$
# \frac{x^2}{9}+\frac{\frac{16}{9}x^2}{16}=1 \Leftrightarrow \frac{2}{9}x^2=1\Leftrightarrow x= \pm \frac{3}{\sqrt{2}}.
# $$
# 
# Volvemos a utilizar la expresión para $y^2$ de arriba, esta vez para despejar el valor de $y$ a partir del de $x$:
# 
# $$
# y^2=\frac{16}{9}\frac{9}{2}=8 \Leftrightarrow y=\pm 2\sqrt{2}.
# $$
# 
# Como $x,y\geq0$, elegimos los valores positivos y concluimos que el rectángulo de área máxima inscrito en la elipse tiene área 
# 
# $$f\left(\frac{3}{\sqrt{2}},2\sqrt{2}\right)=4\frac{3}{\sqrt{2}}2\sqrt{2}=24.$$
# 
# A continuación, vamos a resolver este ejercicio pero con la ayuda del módulo `Sympy`.
# 
# ````
# 

# In[1]:


import sympy as sp

x, y, l = sp.symbols('x y l', real=True) # definimos las variables simbólicas x, y, l
f = sp.Lambda((x,y), 4*x*y) # función a optimizar
g = sp.Lambda((x,y), x**2/9 + y**2/16) # restricción

# Cálculo de puntos críticos (posibles extremos globales)
grad_f =  sp.transpose(sp.Matrix([f(x,y)]).jacobian([x,y]))
grad_g = sp.transpose(sp.Matrix([g(x,y)]).jacobian([x,y]))
sol = sp.solve((sp.Eq(grad_f[0],l*grad_g[0]),sp.Eq(grad_f[1],l*grad_g[1]),sp.Eq(g(x,y),1)), 
               (x,y,l))
for p in sol:
    print('Punto crítico (x,y,lambda)=',p,'; f(x,y)=', sp.N(f(*p[0:2])))


# Podemos comprobamos visualmente el tipo de puntos críticos como sigue.

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Nube de puntos para el cálculo de las curvas de nivel
N = 100  
xvec = np.linspace(-5, 5, N)
yvec = np.linspace(-5, 5, N)
X, Y = np.meshgrid(xvec, yvec)
F = sp.lambdify((x,y),f(x,y),"numpy")

# Representación gráfica de f
plt.contourf(X, Y, F(X,Y))
plt.colorbar()  
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')

# Representación gráfica de la restricción
xvec = np.linspace(-3, 3, N)
sol_curve = sp.solve(sp.Eq(g(x,y),1),y) # despejar y en función de x en g(x,y)=1
for c in sol_curve:
    curve = sp.lambdify(x,c,"numpy")
    plt.plot(xvec, curve(xvec),'r')

# Representación gráfica de los extremos relativos
for p in sol:
    plt.plot(p[0],p[1],'ko')

plt.show()


# ## Método de los multiplicadores de Lagrange con dos restricciones
# 
# El método anterior se puede extender para problemas de optimización que impliquen dos restricciones,  con funciones asociadas $g$ y $h$. En este caso, debe incluirse un segundo multiplicador de Lagrange, $\mu$, que interviene en la ecuación que hay que añadir a las restricciones, y que es la siguiente
# 
# $$
# \nabla f=\lambda \nabla g+\mu \nabla h.
# $$
