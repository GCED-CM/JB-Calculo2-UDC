#!/usr/bin/env python
# coding: utf-8

# # Límites
# 
# Esta sección está destinada fundamentalmente al cálculo de límites en dos variables. Cabe señalar que este concepto está relacionado con el concepto de continuidad, y por tanto será utilizado en la siguiente sección. Nótese que ambos conceptos deben ser conocidos para el caso unidimensional (es decir, para funciones reales de variable real), y en esta sección se hace una extensión al caso bidimensional del concepto de límite. La generalización a más variables resultaría natural.   

# ## Entornos  en el plano
# 
# Antes de abordar el concepto de límite de una función de dos variables, es necesario introducir el concepto de entorno para el caso bidimensional. Nótese que este concepto debe ser conocido para el caso unidimensional ($\mathbb{R}$), en cuyo caso se corresponde con los intervalos centrados. En $\mathbb{R}^2$, el **entorno (abierto)** alrededor de $(x_0,y_0)\in \mathbb{R}^2$ y de radio $\delta>0$ se define como el conjunto de puntos del plano cuya distancia a $(x_0,y_0)$ es menor que $\delta$. Por tanto, se corresponde con el llamado **disco (abierto)** centrado en $(x_0,y_0)$ y con radio $\delta$:
# 
# ````{prf:definition} Disco abierto
# :label: def_disco
# :nonumber: 
# 
# El disco abierto de centro $(x_0,y_0)\in \mathbb{R}^2$ y radio $\delta>0$ es el conjunto:
# 
# $$
# D_\delta(x_0,y_0)=\left\{(x,y)\in \mathbb{R}^2:\sqrt{(x-x_0)^2+(y-y_0)^2}<\delta\right\}.
# $$
# 
# <img src="../../images/02_disco.png" width="250"/>
# ````
# De forma análoga al caso unidimensional (para los intervalos/entornos), decimos que el disco/entorno es cerrado cuando la desigualdad que lo define no es estricta, es decir, cuando es $\leq$ y por tanto incluye a los puntos que están en la circunferencia correspondiente.  
# 
# Utilizando el concepto de entorno, podemos clasificar puntos y conjuntos en el plano. En concreto, consideramos $R\subset \mathbb{R}^2$ una región arbitraria del plano y $(x_0,y_0)\in \mathbb{R}^2$ un punto arbitrario del plano, 
# 
# * Decimos que $(x_0,y_0)$ es un **punto interior** de $R$ si existe un entorno centrado en $(x_0,y_0)$ totalmente contenido en $R$ (como se muestra en la figura):  
# 
#     $$ 
#     (x_0,y_0) \textrm{ es un punto interior de }R\Leftrightarrow \left[ \exists\delta > 0 \, \Big{/}\,  
#     D_\delta(x_0,y_0)\subset R.\right]
#     $$    
#     
#     
#     **Nota**: De la definición se deduce que todo punto interior de $R$ está en $R$.
#     
# * Decimos que $R$ es una **región abierta** si todos sus puntos son interiores.   
# 
# * Decimos que $(x_0,y_0)$ es un **punto frontera** de $R$ si todo entorno centrado en $(x_0,y_0)$ tiene puntos que están dentro y fuera de $R$:  
# 
#     $$ 
#     (x_0,y_0) \textrm{ es un punto frontera de }R \Leftrightarrow \left[ R\cap D_\delta(x_0,y_0)\neq \emptyset 
#     \textrm{ y }(\mathbb{R}^2\backslash R)\cap D_\delta(x_0,y_0)\neq \emptyset\right],$$    
#     para todo $\delta>0$.
#     
#     **Nota**: los puntos frontera de $R$ pueden estar o no en $R$ (dependiendo de la región).
#    
# * Decimos que $R$ es una **región cerrada** si contiene a todos sus puntos frontera.   
# 
# <img src="../../images/02_punto_frontera_interior.png" width="400"/>

# ## Límite de una función de dos variables
# 
# ````{prf:definition} Límite de una función de dos variables
# :label: def_limite
# :nonumber: 
# 
# Sea $f$ una función de dos variables bien definida en un disco abierto centrado en $(x_0,y_0)$ excepto posiblemente en $(x_0,y_0)$ y sea $L$ un número real. Decimos que el límite de $f$ en $(x_0,y_0)$ es $L$ y escribimos
# 
# $$\lim\limits_{(x,y)
# \rightarrow (x_0,y_0)}\,f(x,y)=L,$$
# 
# si para cada número real $\varepsilon>0$ existe un número real $\delta>0$ tal que
# $$
# |f(x,y)-L|<\varepsilon \textrm{ siempre que } 0<\sqrt{(x-x_0)^2+(y-y_0)^2}<\delta. 
# $$
# 
# ````
# Gráficamente, esta condición implica que el valor de $f(x,y)$ se encuentra entre $L-\varepsilon$ y $L+\varepsilon$ para todo punto $(x,y)\neq (x_0,y_0)$ del disco centrado en $(x_0,y_0)$ y de radio $\delta$. Dicho de otra forma equivalente, se tiene que la gráfica de $f$ restringida a dicho entorno y excluyendo el centro se encuentra dentro del trozo de cilindro circular recto correspondiente que está contenido entre los planos $z=L-\varepsilon$ y $z=L+\varepsilon$, como se muestra en la siguiente figura. 
# 
# <img src="../../images/02_limite_def.png" width="250"/>
# 
# **Nota:** Decimos que el límite de $f$ en $(x_0,y_0)$ es $+\infty$ si la función crece ''indefinidamente'' (sin cota superior) al acercarse las variables a $(x_0,y_0)$. Análogamente, decimos que el límite de $f$ en $(x_0,y_0)$ es $-\infty$ si la función decrece ''indefinidamente'' (sin cota inferior) al acercarse las variables a $(x_0,y_0)$.
# 
# El concepto de límite de una función de dos variables es el mismo que el de una función de una variable (se analiza la tendencia de la función al aproximarnos a un punto sea cual sea la dirección), y también lo son sus propiedades con respecto a sumas, diferencias, productos y cocientes. Sin embargo, en el cálculo práctico de límites, hay una característica crítica asociada a la dimensión que marca la diferencia. En el caso unidimensional (en la recta real), solo nos podemos aproximar a un punto por dos direcciones, derecha o izquierda, por eso en este caso es suficiente con analizar los dos límites laterales (la tendencia de la función por la derecha y por la izquierda), y concluir que el límite existe y toma ese valor si y solo si ambos límites laterales coinciden. En el caso bidimensional ($\mathbb{R}^2$), hay infinitas maneras de aproximarse a un punto $(x_0,y_0)$ del plano, por lo que en este caso no se puede aplicar el procedimiento empleado en el caso unidimensional para el cálculo de límites. Por el contrario, la no existencia de límite se puede argumentar de forma similar tanto en una como en varias variables, encontrando dos caminos diferentes hacia el punto cuyos límites restringidos (a dichos caminos) sean distintos. A continuación, enumeramos algunas consecuencias inmediatas de la definición previa de límite que se pueden utilizar para demostrar la no existencia de límite.  
# 
# ````{prf:property} 
# :label: prop_02_limites
# :nonumber: 
# 
# * Si existe el límite de $f$ en $(x_0,y_0)$ y vale $L$, entonces el límite restringido a cualquier camino hacia el punto existe y coincide con $L$:
# 
# $$
# \lim\limits_{(x,y)
# \rightarrow (x_0,y_0)}\,f(x,y)=\lim\limits_{x
# \rightarrow x_0}\,f(x,\alpha(x))=L,
# $$
# para cualquiera que sea el camino $\alpha$ que lleve al punto $(x_0,y_0)$.
# 
# * Particularizando la propiedad anterior a rectas, se deduce que una condición **necesaria** para que el límite exista es que los límites restringidos a rectas que pasan por el punto existan y sean iguales (independientes de la pendiente de la recta):
# 
# $$
# \textrm{Si} \lim\limits_{(x,y)
# \rightarrow (x_0,y_0)}\,f(x,y)=L \Rightarrow \lim_{x\to x_0}\,f(x,y_0+m(x-x_0))=L,$$
# para cualquier valor de $m\in \mathbb{R}$. 
# 
# **Nota:** Los límites restringidos a rectas se llaman límites direccionales.
# 
# * Si no existe algún límite restringido a un camino hacia el punto, entonces no existe el límite de la función en dicho punto: 
# 
# $$
# \textrm{si} \nexists \lim\limits_{x
# \rightarrow x_0}\,f(x,\alpha(x))\Rightarrow \nexists\lim\limits_{(x,y)
# \rightarrow (x_0,y_0)}\,f(x,y),
# $$
# siendo $\alpha$ un camino que lleva al punto $(x_0,y_0)$.  
# 
# * Si los límites restringidos a dos caminos diferentes hacia el punto no coinciden, entonces no existe el límite de la función en dicho punto:
# $$
# \textrm{Si} \lim\limits_{x
# \rightarrow x_0}\,f(x,\alpha(x))\neq \lim\limits_{x
# \rightarrow x_0}\,f(x,\beta(x)) \Rightarrow \nexists\lim\limits_{(x,y)
# \rightarrow (x_0,y_0)}\,f(x,y),
# $$
# siendo $\alpha$ y $\beta$ dos caminos diferentes que llevan al punto $(x_0,y_0)$.  
# 
# ````
# A continuación, se introduce otro criterio que se puede considerar para demostrar la no existencia de límite, y es el asociado a los límites iterados, cuya definición se enuncia en primer lugar.  
# 
# ````{prf:definition} 
# :label: def_02_limit_iter Límites iterados
# :nonumber: 
# 
# Se definen los límites iterados de $f:D\subset \mathbb{R}^2\longrightarrow
# \mathbb{R}$ en $(x_0,y_0)$ como 
# 
# $$
# \lim\limits_{x
# \rightarrow x_0}\big(\lim\limits_{y
# \rightarrow y_0}f(x,y)\big),\quad \lim\limits_{y
# \rightarrow y_0}\big(\lim\limits_{x
# \rightarrow x_0}f(x,y)\big).
# $$
# ````
# **Nota:** en ambos casos los límites iterados se corresponden con dos límites en una variable calculados de forma sucesiva.  
# 
# ````{prf:theorem}  
# :label: th_02_limit_iter
# :nonumber: 
# 
# Si los límites iterados de $f:D\subset \mathbb{R}^2\longrightarrow
# \mathbb{R}$ en $(x_0,y_0)$ **existen y son diferentes** entonces **no existe** el límite de la función en dicho punto. 
# 
# ````
# El único procedimiento que nos permite asegurar la existencia del límite de una función  de dos variables consiste en utilizar las coordenadas polares en el límite y aplicar el **criterio de la función mayorante**. A continuación, se introduce este criterio para el caso particular en el que el punto de aproximación en el límite sea el origen de coordenadas $(x_0,y_0)=(0,0)$. 
# 
# ````{prf:theorem}  
# :label: th_02_func_mayorante
# :nonumber: 
# 
# Una condición **necesaria y suficiente** para que $$
# \lim\limits_{(x,y)
# \rightarrow (0,0)}\,f(x,y)=L,
# $$
# es que exista una función $H(r)$ (independiente de $\theta$) tal que   
# 
# $$
# |f(r\cos\theta,r\,\textrm{sen}\,\theta)-L|\leq H(r) \textrm{ y } \lim\limits_{r
# \rightarrow 0^+}\,H(r)=0.
# $$
# 
# ````
# **Nota:** Este prodecimiento se puede generalizar de forma natural para un punto de aproximación en el límite arbitrario $(x_0,y_0)\in \mathbb{R}^2$ aplicando el cambio de coordenadas polares con origen en dicho punto:
# $$
# x=x_0+r\cos\theta,\quad y=y_0+r\,\textrm{sen}\,\theta.
# $$
# 
# Teniendo en cuenta la definición de límite y el teorema previo, estudiamos a continuación algunos casos de aparición en el cálculo de límites en coordenadas polares. 
# 
# ````{prf:property} 
# :label: prop_02_limit_polar Cambio a coordenadas polares en el límite
# :nonumber: 
# Sea $f:D\subset \mathbb{R}^2\longrightarrow
# \mathbb{R}$ y $(x_0,y_0)=(0,0)$. 
# 
# * **Caso I:** Si $f(r\cos\theta,r\,\textrm{sen}\,\theta)\equiv F(r)$ (independiente de $\theta$), entonces
# $$
# \lim\limits_{(x,y)
# \to (0,0)}\,f(x,y)=\lim\limits_{r\to 0^+}F(r).
# $$  
# 
# * **Caso II:** Si $f(r\cos\theta,r\,\textrm{sen}\,\theta)\equiv h(r)\cdot g(\theta)$ con $\lim\limits_{r
# \to 0^+}\,h(r)=0$ y $g$ acotada en $[0,2\pi)$, entonces
# $$
#  \lim\limits_{(x,y)
# \to (0,0)}\,f(x,y)=0.$$
# 
# * **Caso III:** Si $\lim\limits_{\substack{r
# \to 0^+\\ \theta\in [0,2\pi)}}\,f(r\cos\theta,r\,\textrm{sen}\,\theta)$ depende de $\theta$, entonces el límite $\lim\limits_{(x,y)
# \to (0,0)}\,f(x,y)$ no existe puesto que los límites restringidos a semirectas no coinciden.
# 
# ````

# ## Algunos ejemplos de límites con `Python`
# 
# Analizamos a continuación dos límites en dos variables aplicando las técnicas expuestas y haciendo uso de la librería `Sympy` de `Python` que nos permite calcular límites de funciones que dependen de una única variable a través de la función `sp.limit`. En primer lugar, consideramos el siguiente límite
# $$
#  \lim\limits_{(x,y)
# \to (0,0)}\,\dfrac{xy^2}{x^2+y^4}.
# $$
# Este límite no existe como se puede visualizar en la aplicación de Geogebra, creada por Menchu Blanco del Prado, https://www.geogebra.org/m/urfz8pad, de la que extraemos la siguiente imagen
# 
# <img src="../../images/02_limite_ejemplo_geo.png" width="500"/>
# 
# A continuación, comprobamos analíticamente la no existencia de límite como sigue:

# In[1]:


import sympy as sp
x, y = sp.symbols('x y', real=True) # definimos las variables simbólicas
f = sp.Lambda((x,y),x*y**2/(x**2+y**4)) # definimos la función
# calculamos el límite a través de rectas
m = sp.Symbol('m', real=True)
display('Límites direccionales:',sp.limit(f(x,m*x),x,0)) # todos valen 0
# calculamos el límite en coordenadas polares
r = sp.Symbol('r', nonnegative=True)
theta = sp.Symbol('theta', real=True)
fpol=f(r*sp.cos(theta), r*sp.sin(theta))
display('Función en polares:',sp.simplify(fpol))
display('Límite en polares:',sp.simplify(sp.limit(fpol,r,0,dir='+'))) # restringidos a semirectas valen 0 
# calculamos los límites iterados (coinciden aunque en este caso no existe el límite)
fy = sp.limit(f(x,y),x,0)
display('Límite iterado empezando en x',sp.limit(fy,y,0))
fx = sp.limit(f(x,y),y,0)
display('Límite iterado empezando en y',sp.limit(fy,x,0))
# calculamos el límite restringido a la curva y=sqrt(x)
display('Límite restringido a y=sqrt(x):',sp.simplify(sp.limit(f(x,sp.sqrt(x)),x,0))) # el límite no existe, depende del camino


# Por tanto, el límite no existe porque depende del camino. 
# 
# Por último, consideramos el límite
# $$
#  \lim\limits_{(x,y)
# \to (0,0)}\,\dfrac{xy}{\sqrt{x^2+y^2}},
# $$
# que resolvemos de la siguiente manera:

# In[2]:


import sympy as sp
x, y = sp.symbols('x y', real=True) # definimos las variables simbólicas
f = sp.Lambda((x,y),x*y/sp.sqrt(x**2+y**2)) # definimos la función
# calculamos el límite a través de rectas
m = sp.Symbol('m', real=True)
display('Límites direccionales:',sp.limit(f(x,m*x),x,0)) # todos valen 0
# calculamos el límite en coordenadas polares
r = sp.Symbol('r', nonnegative=True)
theta = sp.Symbol('theta', real=True)
fpol=f(r*sp.cos(theta), r*sp.sin(theta))
display('Función en polares:',sp.simplify(fpol)) # el límite es 0, Caso II del cálculo en polares 
display('Límite en polares:',sp.simplify(sp.limit(fpol,r,0,dir='+'))) # restringidos a semirectas valen 0 
# calculamos los límites iterados
fy = sp.limit(f(x,y),x,0)
display('Límite iterado empezando en x',sp.limit(fy,y,0))
fx = sp.limit(f(x,y),y,0)
display('Límite iterado empezando en y',sp.limit(fy,x,0))


# En este caso, existe el límite y vale $0$ porque el término del límite, en coordenadas polares, está compuesto por un producto de dos factores, uno de ellos que depende únicamente de $r$ y que tiende a $0$ ($r$) y el otro que depende enteramente de $\theta$ y está acotado ($\textrm{sen}(2\theta)/2$). A continuación, lo comprobamos gráficamente:

# In[3]:


import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
# Inicialización de la representación 3D
fig = plt.figure()
ax = plt.axes(projection="3d")
fn= sp.lambdify((x,y),f(x,y),"numpy") # función numpy de f
# Creación de la nube de puntos (50 puntos en cada eje, x e y) 
xx = np.linspace(-1, 1, 50)
yy = np.linspace(-1, 1, 50)
xx, yy = np.meshgrid(xx, yy)
zz = fn(xx,yy)
# Representación de la superficie
surf = ax.plot_surface(xx, yy, zz)
# Etiquetas de los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# Orientamos los ejes
ax.azim = 25
ax.elev = 15

plt.show()

