#!/usr/bin/env python
# coding: utf-8

# # Regla de la cadena 
# 
# ## Regla de la cadena para una variable independiente
# 
# ````{prf:theorem}  Regla de la cadena: una variable independiente
# :label: th_regla_cad_var_ind
# :nonumber: 
# 
# Sea $w = f(x,y)$, donde $f$ es una función derivable de $x$ e $y$. Si $x = g(t)$ e $y = h(t)$, donde $g$ y $h$ son funciones derivables de $t$, entonces $w$ es una función diferenciable de $t$, y 
# 
# $$
# \frac{dw}{dt} = \frac{\partial w}{\partial x} \frac{dx}{dt} + \frac{\partial w}{\partial y} \frac{dy}{dt}.
# $$
# ````
# <img src="../../images/3.5.Regla_cadena_1_var_ind.png" width="200"/>
# 
# ¡A practicar!
# 
# ````{prf:example}  
# :label: 3.x._ex
# :nonumber: 
# 
# Sea $w = x^2y - y^2$ donde $x = \sin(t)$ e $y = e^t$. Calcular $dw/dt$ cuando $t = 0$.
# 
# **Solución:**
# 
# Por la regla de la cadena para una variable independiente, tenemos que
# 
# \begin{equation*} 
# \begin{split}
# \frac{dw}{dt} & = \frac{\partial w}{\partial x} \frac{dx}{dt} + \frac{\partial w}{\partial y} \frac{dy}{dt} \\
#  & = 2xy(\cos(t)) + (x^2 - 2y)e^t \\
#  & = 2\sin(t)e^t\cos(t) + (\sin^2(t) - 2e^t)e^t \\
#  & = 2e^t\sin(t)\cos(t) + e^t\sin^2(t) - 2e^(2t).
# \end{split}
# \end{equation*}
# 
# Cuando $t = 0$, se tiene que
# 
# $$
# \frac{dw}{dt} = -2.
# $$
# ````
# 
# ````{prf:remark} 
# :label: rc_01_regla_cadena
# :nonumber:
# 
# La regla de la cadena para una variable independiente se puede extender a cualquier número de variables. Si
# 
# $$
# w = f(x_1,x_2,\ldots,x_n),
# $$
# 
# donde cada una de las $x_j$ es una función diferenciable de una sola variable $t$. Entonces
# 
# $$
# \frac{dw}{dt} = \frac{\partial w}{\partial x_1}\frac{dx_1}{dt} + \frac{\partial w}{\partial x_2}\frac{dx_2}{dt} + \ldots + \frac{\partial w}{\partial x_n}\frac{dx_n}{dt}.
# $$
# ````
# 
# ## Regla de la cadena para dos variables independientes
# 
# ````{prf:theorem}  Regla de la cadena: dos variables independientes
# :label: th_regla_cad_2_var_ind
# :nonumber: 
# 
# Sea $w = f(x,y)$, donde $f$ es una función diferenciable de $x$ e $y$. Si $x = g(s,t)$ e $y = h(s,t)$ son tales que las derivadas parciales de primer order $\partial x / \partial s$, $\partial x / \partial t$, $\partial y / \partial s$ y $\partial y / \partial t$ existen, entonces $\partial w / \partial s$ y $\partial w / \partial t$ existen y vienen dadas por
# 
# $$
# \frac{\partial w}{\partial s} = \frac{\partial w}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial s} \quad \textrm{ y } \quad \frac{\partial w}{\partial t} = \frac{\partial w}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial t}.
# $$
# ````
# 
# <img src="../../images/3.5.Regla_cadena_2_var_ind.png" width="300"/>
# 
# ¡Sigamos practicando!
# 
# ````{prf:example}  
# :label: 3.x._ex
# :nonumber: 
# 
# Utiliza la regla de la cadena para calcular $\frac{dw}{ds}$ y $\frac{dw}{dt}$ para $w = 2xy$ donde $x = s^2 + t^2$ e $y = s/t$. 
# 
# **Solución:**
# 
# Por la regla de la cadena para dos variables independientes, si $t$ se asume constante y diferenciamos con respecto a $s$, obtenemos que
# 
# \begin{equation*} 
# \begin{split}
# \frac{\partial w}{\partial s} & = \frac{\partial w}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial s} \\
#  & = 2y(2s) + 2x\frac{1}{t} \\
#  & = 2 \color{blue}{\frac{s}{t}}\normalcolor(2s) + 2(\color{blue}{s^2 + t^2}\normalcolor)\frac{1}{t} \\
#  & = \frac{4s^2}{t} + \frac{2s^2 + 2t^2}{t} \\
#  & = \frac{6s^2 + 2t^2}{t}.
# \end{split}
# \end{equation*}
# 
# Del mismo modo, asumiendo $s$ constante, obtenemos que
# 
# \begin{equation*} 
# \begin{split}
# \frac{\partial w}{\partial t} & = \frac{\partial w}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial t} \\
#  & = 2y(2t) + 2x\frac{-s}{t^2} \\
#  & = 2\color{blue}{\frac{s}{t}}\normalcolor(2t) + 2(\color{blue}{s^2 + t^2}\normalcolor)\frac{-s}{t^2} \\
#  & = 4s - \frac{2s^3 + 2st^2}{t^2} \\
#  & = \frac{4st^2 - 2s^3 - 2st^2}{t^2} \\
#  & = \frac{2st^2 - 2s^3}{t^2}.
# \end{split}
# \end{equation*}
# ````
# 
# Vamos ahora a practicar con `Python`.

# In[1]:


import sympy as sp


# In[2]:


x, y, s, t = sp.symbols('x y s t', real=True) # define las variables simbólicas x, y, s, t 
w = 2*x*y # define w(x,y)
xx = s**2 + t**2 # define x(s,t)
yy = s/t # define y(s,t)
# Cálculo de la derivada de w con respecto a s:
w_x, w_y = sp.diff(w,x).subs({x:s**2+t**2,y:s/t}), sp.diff(w,y).subs({x:s**2+t**2,y:s/t})
x_s, y_s = sp.diff(xx,s), sp.diff(yy,s)
w_s = w_x * x_s + w_y * y_s
print('Derivada de w con respecto a s: ')
display(sp.simplify(w_s))
# Cálculo de la derivada de w con respecto a t:
x_t, y_t = sp.diff(xx,t), sp.diff(yy,t)
w_t = w_x * x_t + w_y * y_t
print('Derivada de w con respecto a t: ')
display(sp.simplify(w_t))


# ````{prf:remark} 
# :label: rc_02_regla_cadena
# :nonumber:
# 
# La regla de la cadena para dos variables independientes también se puede extender a cualquier número de variables. Si $w$ es una función diferenciable de las $n$ variables $x_1, x_2, \ldots, x_n$, donde cada $x_j$ es una función diferenciable de las $m$ variables $t_1, t_2, \ldots, t_m$. Para $w = f(x_1, x_2, \ldots, x_n)$, se obtiene:  
# 
# \begin{eqnarray*}
# && \frac{\partial w}{\partial t_1} = \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t_1} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t_1} + \ldots + \frac{\partial w}{\partial x_n}\frac{\partial x_n}{\partial t_1}, \\ 
# && \frac{\partial w}{\partial t_2} = \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t_2} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t_2} + \ldots + \frac{\partial w}{\partial x_n}\frac{\partial x_n}{\partial t_2}, \\
# && \quad \vdots \\
# && \frac{\partial w}{\partial t_m} = \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t_m} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t_m} + \ldots + \frac{\partial w}{\partial x_n}\frac{\partial x_n}{\partial t_m}
# \end{eqnarray*}
# ````

# ## Derivación implícita
# 
# Si queremos calcular las derivadas de una función que depende de una o varias variables no tenemos porque conocer su expresión de forma explícita, puede venir dada implícitamente. Por ejemplo, la función $y = f(x)$ puede venir determinada por la expresión $y^3 + y^2 - 5y - x^2 = -4$. En este caso, no se conoce de forma explícita cuál es la expresión de $f$ en términos de $x$. A pesar de ello, es posible calcular la derivada parcial $\partial f/\partial x$. 
# 
# ````{prf:definition} Regla de la cadena: derivación implícita
# :label: def_rc_2vi
# :nonumber: 
# 
# Si la ecuación $F(x,y) = 0$ define a $y$ implícitamente como función derivable de $x$, entonces
# 
# $$
# \frac{dy}{dx} = -\frac{F_x(x,y)}{F_y(x,y)}, \quad F_y(x,y) \neq 0.
# $$
# 
# Si la ecuación $F(x,y,z) = 0$ define a $z$ implícitamente como función diferenciable de $x$ e $y$, entonces
# 
# $$
# \frac{\partial z}{\partial x} = -\frac{F_x(x,y,z)}{F_z(x,y,z)} \quad \textrm{ y } \quad \frac{\partial z}{\partial y} = -\frac{F_y(x,y,z)}{F_z(x,y,z)}, \quad F_z(x,y,z) \neq 0.
# $$
# ````
# 
# ¡A seguir practicando!
# 
# ````{prf:example}  
# :label: 3.x._ex
# :nonumber: 
# 
# Calcular $dy/dx$ para $y^3 + y^2 - 5y - x^2 = -4$. 
# 
# **Solución:**
# 
# Tomando $F$ tal que $F(x,y) = 0$, tenemos que
# 
# $$
# F(x,y) = y^3 + y^2 - 5y - x^2 + 4.
# $$
# 
# Entonces
# 
# $$
# F_x(x,y) = -2x \quad \textrm{ y } \quad F_y(x,y) = 3y^2 + 2y - 5.
# $$
# 
# Usando el resultado teórico de derivación implícita, obtenemos que
# 
# $$
# \frac{dy}{dx} = -\frac{F_x(x,y)}{F_y(x,y)} = - \frac{(-2x)}{3y^2 + 2y - 5} = \frac{2x}{3y^2 + 2y - 5}.
# $$
# ````
# 
# Vamos a comprobar que el cálculo es correcto con la ayuda de `Python`.

# In[3]:


x, y = sp.symbols('x y', real=True) # define la variable simbólica x e y 
F = y**3 + y**2 - 5*y - x**2 + 4 # define F tal que F(x,y) = 0
display(sp.Eq(F,0))
# Cálculo de la derivada implícita con respecto a x
F_x, F_y = sp.diff(F, x), sp.diff(F, y) 
y_x = - F_x/F_y
print('Derivada implícita con respecto a x: ')
display(y_x)

