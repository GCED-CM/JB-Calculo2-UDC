#!/usr/bin/env python
# coding: utf-8

# # Límites y continuidad con **Sympy**
# 
# El módulo **Sympy** puede utilizarse se para obtener las singularidades de una función, su dominio y su rango, entre otras cosas. 
# Como veremos en esta práctica, también podremos calcular límites en una variable y comprobar si una función es continua en un punto dado. 
# 
# **Objetivos:**
# 
# - Diferenciar una expresión de una función en Sympy,
# - definir funciones a trozos,
# - explorar el dominio, singularidades y rango de una función,
# - cálculo de límites en una variable,
# - análisis de la continuidad de una función.

# Recordemos que lo primero que debemos hacer es importar el módulo **Sympy** para el resto de la práctica:

# In[2]:


import sympy as sp


# ## Expresiones y funciones en **Sympy**
# Hasta ahora hemos usado expresiones matemáticas que se guardaban en objetos del módulo **Sympy**. Sin embargo, todavía no hemos utilizado funciones. Para ver las diferencias entre una expresión y su función asociada vamos a mostrar como evaluar funciones y expresiones en **Sympy** sobre un ejemplo sencillo: la función $f(x) \to x\cos(4x)$:

# In[3]:


x = sp.symbols('x', real=True) # define la variable simbólica x
f_expr = x*sp.cos(4*x) # Esto es una expresión
display(f_expr)
print('Valor de f_expr(2)=',f_expr.subs({x:2})) # Evaluamos la expresión f con "subs"

y = sp.symbols('y', real=True)
f2_expr=sp.exp(x**3+1)
sp.solve(f2_expr-y,x)

sp.solve(sp.Abs(2*x-4)-sp.Abs(x-3))


# En el caso de las funciones, la evauación es mucho más sencilla: se hace como en cualquier otra función pre-definida (seno, coseno, exponencial, *etc.*).
# 
# Para definir funciones en **Sympy** tenemos que utilizar la función `sp.Lambda`:

# In[4]:


f = sp.Lambda((x),f_expr) # Creamos la función "f" a partir de la expresión "f_expr"
display(f)
print('Valor de f(2)=',f(2)) # Evaluación de la función
print(f(x)==f_expr)


# ## Funciones definidas a trozos
# 
# Las funciones también pueden definirse a partir de expresiones **a trozos**, teniendo en cuenta distintas expresiones que serán evluadas si se cumplen ciertas condiciones. El módulo **Sympy** irá evaluando cada una de las tuplas que aparecen como argumentos (de izquierda a derecha) hasta encontrar una en la que la condición sea cierta. Por ejemplo: 
# 
# $$
# g\_expr(x)=
# \begin{cases}
# \dfrac{1}{x} & \text{si } x>0,\\
# 1 & \text{si } x \le 0.
# \end{cases}
# $$

# In[5]:


g_expr = sp.Piecewise((1/(x), x>0), (1, True))
g = sp.Lambda((x), g_expr)
display(g(x))


# La forma de escritura anterior, pese a ser muy cómoda, tiene muchas limitaciones (por ejemplo, para el cálculo de límites laterales, que veremos un poco más abajo). En general, es más útil definir las funciones a trozos apoyándonos en la función **escalón**, matemáticamente conocida como función de **Heaviside**, $\theta$, que viene dada por
# 
# $$
# \theta(x)=
# \begin{cases}
# 0 & \text{si } x \le 0,\\
# 1 & \text{si } x \gt 0.\\
# \end{cases}
# $$
# 
# Entonces, una función definida por
# 
# $$
# f(x)=
# \begin{cases}
# f_1(x) & \text{si } x>0,\\
# f_{2}(x) & \text{si } x < 0,
# \end{cases}
# $$
# 
# se escribiría como
# 
# $$
# f(x) = f_2(x)+(f_1(x)-f_2(x))\theta(x).
# $$

# In[57]:


# Definición de la función
g1 = 1/x; g2 = 1
g_expr = g2 + (g1 - g2) * sp.Heaviside(x, 0)  
g = sp.Lambda(x, g_expr)
# Comprobar la definición de la función g
display(sp.simplify(g(x).rewrite(sp.Piecewise)))


# ## Dominio e imagen de una función
# 
# Para calcular el **dominio** de una función se puede, en primer lugar, calcular las singularidades de una función dada. Entonces, el dominio máximo de la función será todo $\mathbb{R}$ menos las singularidades. 

# In[23]:


f=sp.Lambda(x, x/(sp.cos(x)))
display(sp.calculus.singularities(f(x), x))


# Para calcular la **imagen** de una función (o, lo que es lo mismo, su **rango**), utilizaremos la función `sp.calculus.util.function_range`:

# In[44]:


f=sp.Lambda(x, x/(x**2+1))
R = sp.calculus.util.function_range(f(x), x, sp.Reals)
display(R)


# **Ejercicio 5.1** 
# Calcula las singularidades y la imagen de la función $f(x)=\displaystyle\frac{x+5}{x^3-2}+\frac{x^2}{x-2}$.
# Para ello, debes definir en primer lugar la expresión asociada y, a continuación, la función `Lambda` correspondiente. Después, debes calcular su dominio y su imagen. Por último, dibuja la función $f$.

# In[58]:


# ESCRIBE AQUÍ TU CÓDIGO


# ## Límites
# Los límites de expresiones de una variable se pueden calcular con la función `sp.limit`. 
# Esta función también permite calcular límites laterales, como se muestra en el siguiente ejemplo:

# In[65]:


g_expr = sp.cos(x)/(x+1)
g = sp.Lambda(x, g_expr)
display(g(x))

display(sp.limit(g(x),x,-1,dir='-')) # límite por la izquierda
display(sp.limit(g(x),x,-1,dir='+')) # límite por la derecha


# En este caso, el límite $\displaystyle\lim_{x\to -1}g(x)$ no existe ya que, como acabamos de ver, los límite laterales no coinciden. Pero una incorrecta utilización del paquete informático nos podría llevar a una conclusión errónea:

# In[63]:


display(sp.limit(g(x),x,-1)) # ¡Da un resultado (incorrecto) ya que, por defecto, utiliza el valor del límite por la derecha!


# A continuación mostramos como se pueden calcular los límites laterales de una función definida a trozos. 
# En este caso, la definición mediante `sp.Piecewise` dará un error de ejecución (¡prueba!), por lo que tendremos que definir la función utilizando nuestro ya odiado escalón (Heaviside):

# In[66]:


# Definición de la función a trozos (utilizando la función Heaviside)
f1 = 1/x; f2 = 1
f_expr = f2 + (f1 - f2) * sp.Heaviside(x, 0)  
f = sp.Lambda(x, f_expr)
display(sp.simplify(f(x).rewrite(sp.Piecewise)))

display(sp.limit(f(x),x,0,dir='-')) # límite por la izquierda
display(sp.limit(f(x),x,0,dir='+')) # límite por la derecha


# No hay ningún problema si queremos calcular límites en el infinito, $x\to+\infty$ o $x\to-\infty$. El valor de $\infty$ se representa en **Sympy** por `sp.oo`. Por ejemplo:

# In[67]:


display(sp.limit(sp.exp(x),x,-sp.oo))
display(sp.limit(sp.exp(x),x,sp.oo))


# **Ejercicio 5.2** 
# 
# Representa gráficamente la siguiente función y calcula los límites que se indican: 
# 
# $$
# f(x)=
# \begin{cases}
# \cos(x) & \text{si } x<0,\\
# \frac{x^2}{x+1} & \text{si } x \geq 0,
# \end{cases}
# $$
# 
# - $\lim_{x\to -1} f(x)$,
# - $\lim_{x\to 1} f(x)$,
# - $\lim_{x\to 0^{-}} f(x)$,
# - $\lim_{x\to 0^{+}} f(x)$.

# In[78]:


# ESCRIBE AQUÍ TU CÓDIGO


# ## Continuidad
# 
# En el módulo de **Sympy** existe una función que calcula el dominio de continuidad (es decir, el conjunto de puntos en los que la función es continua): `sp.calculus.util.continuous_domain`

# In[72]:


f=sp.Lambda(x, x/sp.cos(x))
I = sp.calculus.util.continuous_domain(f, x, sp.Reals)
display(I)


# Además, para analizar la continuidad de $f$ en un punto $a$, basta con comprobar que
# $$
# f(a)=\lim_{x\to a}f(x).
# $$
# Por ejemplo:

# In[77]:


# Dominio de continuidad de la función valor absoluto
f = sp.Lambda((x), sp.Abs(x))
I = sp.calculus.util.continuous_domain(f(x), x, sp.Reals)
display(I)

# Comprobación de la continuidad para la misma función, pero ahora definida a trozos
f1 = x; f2 = -x
f_expr = f2 + (f1-f2) * sp.Heaviside(x, 0)
f = sp.Lambda(x, f_expr)
# Comprobamos la definición de la función f
display(sp.simplify(f.rewrite(sp.Piecewise)))

print('La función f es continua en x=0:', sp.limit(f(x),x,0)==f(0))
I = sp.calculus.util.continuous_domain(f(x), x, sp.Reals)
display(I)


# **Ejercicio 5.3** 
# Analiza la continuidad de la función del Ejercicio 5.2. 

# In[79]:


# ESCRIBE AQUÍ TU CÓDIGO

