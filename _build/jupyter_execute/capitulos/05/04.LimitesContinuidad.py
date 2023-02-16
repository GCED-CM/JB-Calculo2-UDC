#!/usr/bin/env python
# coding: utf-8

# # Límites y continuidad en Python
# 
# Esta sección pretende ser un compendio (esperemos que más claro y mejor ordenado) de todo el `Python` 
# que hemos ido usando en el Capítulo 2. 
# 
# **Objetivos:**
# 
# - Explorar el dominio, singularidades y rango de una función.
# - Cálculo de límites en una y varias variables.
# - Análisis de la continuidad de una función.

# ## Dominio e rango dunha función de varias variables
# Para calcular el dominio de una función, se puede, en primer lugar, calcular las singularidades de una función dada. 
# 
# En la implementación del módulo `Sympy` únicamente está disponible este cálculo para funciones de tipo racional y con dependencia de una única variable. 
# 
# Si tenemos esto en cuenta, el dominio de la función vendrá dado por el conjunto de puntos del espacio excepto las singularidades. Para el caso de varias variables, este análisis sólo se puede hacer con respecto a una de las variables, tomando como fijas el resto. 

# In[6]:


import sympy as sp



f=sp.Lambda((x,y), x/((x+y)*y))
display(sp.calculus.singularities(f(x,y), x))
display(sp.calculus.singularities(f(x,y), y))


# Do mesmo xeito ao que ocorre coas singularidades, **Sympy** soamente é capaz de calcular o rango de funcións dunha única variable. Aínda que isto supón unha limitación, é posible explorar o rango dunha función de varias variables restrinxindo os valores dos argumentos a certos planos cartesianos e analizando o rango das funcións resultantes (dunha variable):

# In[7]:


x, y, z = sp.symbols('x y z', real=True) # define as variables simbólicas x, y, z
f=sp.Lambda((x,y,z), x*z/((x+y)*y))
Rx = sp.calculus.util.function_range(f(x,1,1), x, sp.Reals)
Ry = sp.calculus.util.function_range(f(1,y,1), y, sp.Reals)
Rz = sp.calculus.util.function_range(f(1,1,z), z, sp.Reals)
display(Rx)
display(Ry)
display(Rz)


# ### **Exercicio 5.1** 
# Calcula as singularidades e o rango da función $f(x,y)=\displaystyle\frac{y+x}{y-x^3}$.

# In[8]:


# O TEU CÓDIGO AQUÍ


# ## Límites
# O módulo **Sympy** soamente dispón de ferramentas para cálcular os límites que depende dunha única variable. A pesar desta limitación, é posible calcular límites en varias variables usando as técnicas que xa revisamos nas clases de pizarra como son o uso de camiños por rectas $y=mx$, os límites (re)iterados, ou o cambio a coordenadas polares.

# ### Límites de expresións nunha variable
# Os límites de expresións nunha variable poden calcularse usando a función `sp.limit`. O mesmo comando tamén permite o cálculo de límites laterais. Comprobemos o seu uso cunha función dunha variable moi sinxela (que non posúe límite):
# $$
# f(x)=
# \begin{cases}
# -1 & \text{se } x\le 0,\\
# +1 & \text{se } x \gt 0.\\
# \end{cases}
# $$

# In[9]:


x = sp.Symbol('x', real=True) # define a variable simbólica x
f = -1 + 2 * sp.Heaviside(x, 0)
F = sp.Lambda(x, f)
# Comprobar a definición da función F
display(sp.simplify(F(x).rewrite(sp.Piecewise)))


# Neste caso, o límite $\displaystyle\lim_{x\to 0}f(x)$ non existe xa que os límite laterais non coinciden. A pesar disto, obtense:

# In[10]:


display(sp.limit(F(x),x,0)) # Por defecto usa o valor do límite pola dereita
display(sp.limit(F(x),x,0,dir='+')) # límite pola dereita
display(sp.limit(f,x,0,dir='-')) # límite pola esquerda


# Do mesmo xeito a como se definen os límite cando $x$ tende a un valor finito $a$, tamén se poden calcular os valores cando $x\to+\infty$ ou $x\to-\infty$. O valor de $\infty$ está representado en **Sympy** por `sp.oo`. No caso da función $f(x)=e^x$, se obtén:

# In[11]:


display(sp.limit(sp.exp(x),x,-sp.oo))
display(sp.limit(sp.exp(x),x,sp.oo))


# ### Límites de expresións en varias variables
# Como xa revisamos nas clases de pizarra, o cálculo de límites en varias variables é máis complexo xa que debemos analizar todos os camiños posibles para poder asegurar que o límite existe e coincide cun valor dado. Por exemplo, no caso da función $f(x,y)=\frac{x^2y}{x^5+y^2}$ podemos ter valores diferentes segundo o camiño escollido para chegar ao punto $(0,0)$:

# In[12]:


x, y = sp.symbols('x y', real=True) # define a variable simbólica x e y
f = sp.Lambda((x,y), x**2*y/(x**5+y**2)) # agora temos definida a función simbólica f(x)
sp.limit(f(x,y),x,0) # límite fixando o valor de y


# In[13]:


sp.limit(f(x,y),y,0) # límite fixando o valor de x


# In[14]:


m = sp.Symbol('m', real=True)
display(f(x,m*x))
sp.limit(f(x,m*x),x,0) # límites polas rectas de pendente m


# Nembargantes, se se emprega o camiño $y=x^3$ obtense un valor do límite diferentes de cero, do que se conclúe que o límite non existe:

# In[15]:


sp.limit(f(x,x**3),x,0)


# ### Límites (re)iterados
# Os límites (re)iterados é outra ferramenta máis para tratar de analizar o que ocorre co límite de funcións de varias variables. Posto que estos límite iterados son unha sucesión de cálculos de límites tendo en conta unha soa variable, este procedemento pode implementarse en **Sympy**. Por exemplo, se consideramos $f(x,y)= \displaystyle \frac{x^2-y^2}{x^2+y^2}$, resulta

# In[16]:


f = sp.Lambda((x,y),(x**2-y**2)/(x**2+y**2))
g = sp.limit(f(x,y),x,0)
sp.limit(g,y,0)


# In[17]:


g = sp.limit(f(x,y),y,0)
sp.limit(g,x,0)


# e polo tanto pódese concluir que non existe o límite, xa que os valores non coinciden.
# 
# ### Casos onde non existe límites
# Como xa vimos nos exemplos analizados en clase de pizarra, existen multitude de exemplos onde os límites non existe, como é o caso de $\displaystyle\lim_{(x,y)\to(0,0)}f(x,y)$ con 
# $$
# f(x,y)=
# \begin{cases}
# \frac{xy}{x^2+y^2} & \text{se } x^2+y^2 \gt 0,\\
# 0 & \text{se } (x,y)=(0,0).
# \end{cases}
# $$

# In[18]:


# Definición das función definida a cachos
f1 = x*y/(x**2+y**2); f2 = 0
f = f2 + (f1-f2) * sp.Heaviside(x**2+y**2, 0)
F = sp.Lambda((x,y), f)
# Comprobar a definición da función F
display(sp.simplify(F.rewrite(sp.Piecewise)))
# Límite iterado primeiro en x e despois en y
G = sp.limit(F(x,y),x,0)
sp.limit(G,y,0)


# Tendo en conta o límite sobre a recta $y=mx$, resulta:

# In[19]:


display(F(x,m*x))
sp.limit(F(x,m*x),x,0)


# Polo que podemos asegurar que o límite non existe xa que o valor do límite dependería de $m$. Un último exemplo, onde os límites iterados dan lugar a funcións descontinuas (nos cálculos intermedios), pero aínda así, os límite iterados existen e ademais son iguais. Consideramos a función:
# $$
# f(x,y)=
# \begin{cases}
# y & \text{se } x \gt 0,\\
# -y & \text{se } x \le 0.
# \end{cases}
# $$

# In[20]:


# f = sp.Piecewise((y, x > 0), (-y, True))
# Definición das función definida a cachos
f1 = y; f2 = -y
f = f2 + (f1-f2) * sp.Heaviside(x, 0)
F = sp.Lambda((x,y), f)
# Comprobar a definición da función F
display(sp.simplify(F.rewrite(sp.Piecewise)))
# Límite iterado primeiro en x e despois en y
Gp = sp.limit(F(x,y),x,0,dir='+')
display(Gp)
Gm = sp.limit(F(x,y),x,0,dir='-')
display(Gm)
sp.limit(Gp,y,0) # que ten o mesmo resultado que sp.limit(Gm,y,0)


# In[21]:


# Límite iterado primeiro en y e despois en x
G = sp.limit(F(x,y),y,0)
display(G)


# ### Límites con coordenadas polares
# Un dos recursos que usaremos con máis frecuencia para calcular límites en varias variables será o uso de coordenadas polares (no plano) ou coordenadas esféricas (no espazo tridimensional), para calcular límites do tipo $\displaystyle\lim_{(x,y)\to(0,0)}f(x,y)$ substitutindo $x=r\cos\theta$ e $y=r\sin\theta$. Por exemplo:

# In[22]:


r = sp.Symbol('r', nonnegative=True)
theta = sp.Symbol('theta', real=True)
f = (x**3+2*x*y**2)/(x**2+y**2)
F = sp.Lambda((x,y), f)
display(F)
display(F(r*sp.cos(theta), r*sp.sin(theta)))
sp.limit(F(r*sp.cos(theta), r*sp.sin(theta)),r,0)


# ### **Exercicio 5.2** 
# 
# Dada a función $f(x,y)=\displaystyle\frac{x-y^3}{x+y^3}$ calcula os seguintes límites cando $(x,y)\to (0,0)$:
# - Límites sobre as rectas $y=mx$
# - Límites iterados
# - Límite usando coordenadas polares

# In[23]:


# O TEU CÓDIGO AQUÍ


# ## Análise da continuidade de varias variables
# 
# No módulo de **Sympy** existe unha función que calcular o dominio de continuidade (o conxunto de puntos onde a funciín é continua) dunha función dunha única variable. No caso de varias variables, o que se pode analizar é a continuidade dunha función con respecto ao resto de variables fixas. A función  empregar é `sp.calculus.util.continuous_domain(f(x,y), x, sp.Reals)`

# In[24]:


f=sp.Lambda((x,y), x/((x+y)*y))
Ix = sp.calculus.util.continuous_domain(f(x,y), x, sp.Reals)
Iy = sp.calculus.util.continuous_domain(f(x,y), y, sp.Reals)
display(Ix)
display(Iy)


# Ademáis, para analizar a continuidade de $F$ nun punto $(a,b)$, basta con comprobar que
# $$
# F(a,b)=\lim_{(x,y)\to(a,b)}F(x,y).
# $$
# Por exemplo, no caso dunha función dunha única variable:

# In[27]:


# Dominio de continuidade da función valor absoluto
F = sp.Lambda((x), sp.Abs(x))
Ix = sp.calculus.util.continuous_domain(F(x), x, sp.Reals)
display(Ix)

# Comprobación da continuidade definida a cachos
# f = sp.Piecewise((x, x > 0), (-x, True))
# Definición das función definida a cachos
f1 = x; f2 = -x
f = f2 + (f1-f2) * sp.Heaviside(x, 0)
F = sp.Lambda((x), f)
# Comprobar a definición da función F
display(sp.simplify(F.rewrite(sp.Piecewise)))

F = sp.Lambda((x), f)
print('A función F é continua en x=0:', sp.limit(F(x),x,0)==F(0))
Ix = sp.calculus.util.continuous_domain(F(x), x, sp.Reals)


# ### **Exercicio 5.3** 
# Analiza a continuidade da función 
# $$
# f(x,y)=
# \begin{cases}
# \displaystyle\frac{1}{xy} & \text{se }x\neq 0, y\neq 0,\\
# 1 & \text{noutro caso},
# \end{cases}
# $$
# en calquera punto $(x,y)$ do plano

# In[26]:


# O TEU CÓDIGO AQUÍ

