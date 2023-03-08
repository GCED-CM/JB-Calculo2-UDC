#!/usr/bin/env python
# coding: utf-8

# # Regla de la cadena 
# 
# ## Matriz jacobiana y regla de la cadena
# 
# La noción de matriz jacobiana, junto con la de regla general de la cadena, nos va a permitir calcular las derivadas parciales de una composición de funciones diferenciables. 
# 
# ````{prf:theorem}  Diferenciabilidad de una función compuesta
# :label: th_dif_func_comp
# :nonumber: 
# 
# Sean $\mathbf{F}: D \subset \mathbb{R}^n \rightarrow \mathbb{R}^m$ y $G: \mathbb{R}^m \rightarrow \mathbb{R}$ dos funciones tales que $\mathbf{F}(D) \subset \mathbb{R}^m$. Sea $\mathbf{a} \in D$ tal que $\mathbf{F}$ es diferenciable en $\mathbf{a}$ y $G$ es diferenciable en $\mathbf{F}(\mathbf{a})$. Entonces la función compuesta $G \circ \mathbf{F}$ es diferenciable en $\mathbf{a}$ y a partir de la **regla general de la cadena** se tiene:
# 
# $$
# \mathrm{J}(G \circ \mathbf{F}) (\mathbf{a}) = \mathrm{J}G(\mathbf{F}(\mathbf{a}))\mathrm{J}\mathbf{F}(\mathbf{a}),
# $$
# 
# donde $\mathrm{J}G = \left[\frac{\partial G}{\partial \overline{x}_{1}}, \frac{\partial G}{\partial \overline{x}_{2}}, ... , \frac{\partial G}{\partial \overline{x}_{m}}\right]$ es la matriz jacobiana de $G$, y 
# 
# $$
# \mathrm{J}\mathbf{F} =
# \begin{bmatrix}
# \frac{\partial F_{1}}{\partial x_{1}} & \frac{\partial F_{1}}{\partial x_{2}} & ... & \frac{\partial F_{1}}{\partial x_{n}} \\
# \frac{\partial F_{2}}{\partial x_{1}} & \frac{\partial F_{2}}{\partial x_{2}} & ... & \frac{\partial F_{2}}{\partial x_{n}} \\
# ... & ... & ... & ... \\
# \frac{\partial F_{m}}{\partial x_{1}} & \frac{\partial F_{m}}{\partial x_{2}} & ... & \frac{\partial F_{m}}{\partial x_{n}} \\
# \end{bmatrix}
# $$
# 
# es la matriz jacobiana de $\mathbf{F}$.
# ````
# 
# **NOTA 1:** Recuerda que para una función $G: \mathbb{R}^m \rightarrow \mathbb{R}$, la matriz jacobiana es igual a la transpuesta del gradiente. Por tanto, a partir de la igualdad anterior, tenemos que 
# 
# $$
# \mathrm{J}(G \circ \mathbf{F}) (\mathbf{a}) = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(\mathbf{a}))\mathrm{J}\mathbf{F}(\mathbf{a}).
# $$
# 
# **NOTA 2:** La regla de la cadena para el caso multivariable es una generalización de la regla de la cadena para una variable. Si $n = m = 1$, tal que $a \in \mathbb{R}$, $\mathbf{F}: D \subset \mathbb{R} \rightarrow \mathbb{R}$ y $G: \mathbb{R} \rightarrow \mathbb{R}$, entonces 
# 
# $$
# \mathrm{J}(G \circ F) (a) = \mathrm{J}G(F(a))\mathrm{J}F(a) = G'(F(a))F'(a).
# $$
# 
# ````{prf:remark} Regla de la cadena para una variable independiente
# :label: rc_01_regla_cadena
# :nonumber:
# 
# Sea $w = G(x_1,x_2,...,x_m)$, donde $G$ es una función diferenciable de las $m$ variables $x_1, x_2, ... , x_m$. Si cada una de las $x_j = F_j(t)$ es una función diferenciable de $t$, entonces $w$ es una función diferenciable de $t$, y
# 
# $$
# \frac{dw}{dt} = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(t))\mathrm{J}\mathbf{F}(t) = \frac{\partial w}{\partial x_1}\frac{dx_1}{dt} + \frac{\partial w}{\partial x_2}\frac{dx_2}{dt} + ... + \frac{\partial w}{\partial x_m}\frac{dx_m}{dt}.
# $$
# ````
# 
# ¡A practicar!
# 
# ````{prf:example}  
# :label: 3.x._ex
# :nonumber: 
# 
# Sea $w = x^2y - y^2$ donde $x = \sin(t)$ e $y = e^t$. Calcular $\frac{\partial w}{\partial t}$.
# 
# **Solución:**
# 
# Por la regla de la cadena para una variable independiente, tenemos que
# 
# \begin{equation*} 
# \begin{split}
# \frac{dw}{dt} & = \frac{\partial w}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial t} \\
#  & = 2xy(\cos(t)) + (x^2 - 2y)e^t \\
#  & = 2\color{blue}{\sin(t)}\color{blue}{e^t}\cos(t) + (\color{blue}{\sin}^2\color{blue}{(t)} - 2\color{blue}{e^t})e^t \\
#  & = 2e^t\sin(t)\cos(t) + e^t\sin^2(t) - 2e^(2t).
# \end{split}
# \end{equation*}
# ````
# 
# ````{prf:remark} Regla de la cadena para dos variables independientes
# :label: rc_02_regla_cadena
# :nonumber:
# 
# Sea $w = G(x_1,x_2,...,x_m)$, donde $G$ es una función diferenciable de las $m$ variables $x_1, x_2, ... , x_m$. Si cada una de las $x_j = F_j(s,t)$ es una función diferenciable de $s$ y $t$, entonces $w$ es una función diferenciable de $s$ y $t$, y 
# 
# $$
# \begin{bmatrix}
# \frac{\partial w}{\partial s}\\
# \frac{\partial w}{\partial t}\\
# \end{bmatrix}
# = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(s,t))\mathrm{J}\mathbf{F}(s,t) = 
# \begin{bmatrix}
# \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial s} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial s} + \ldots + \frac{\partial w}{\partial x_m}\frac{\partial x_m}{\partial s}\\
# \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t} + \ldots + \frac{\partial w}{\partial x_m}\frac{\partial x_m}{\partial t}
# \end{bmatrix}
# $$
# ````
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
# Por la regla de la cadena para dos variables independientes, obtenemos que
# 
# $$
# \begin{bmatrix}
# \frac{\partial w}{\partial s}\\
# \frac{\partial w}{\partial t}\\
# \end{bmatrix} = 
# \begin{bmatrix}
# \frac{\partial w}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial s}\\
# \frac{\partial w}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial t}\\
# \end{bmatrix} =
# \begin{bmatrix}
# 2y(2s) + 2x\frac{1}{t}\\
# 2y(2t) + 2x\frac{-s}{t^2}\\
# \end{bmatrix} = 
# \begin{bmatrix}
# 2 \color{blue}{\frac{s}{t}}(2s) + 2(\color{blue}{s^2 + t^2})\frac{1}{t}\\
# 2\color{blue}{\frac{s}{t}}(2t) + 2(\color{blue}{s^2 + t^2})\frac{-s}{t^2}\\
# \end{bmatrix} = 
# \begin{bmatrix}
# \frac{4s^2}{t} + \frac{2s^2 + 2t^2}{t}\\
# 4s - \frac{2s^3 + 2st^2}{t^2}\\
# \end{bmatrix} = 
# \begin{bmatrix}
# \frac{6s^2 + 2t^2}{t}\\
# \frac{2st^2 - 2s^3}{t^2}\\
# \end{bmatrix} 
# $$
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

# Cálculo de las derivadas parciales de w con respecto a s y t:
F, G = sp.Matrix([xx, yy]), sp.Matrix([w])
jac_F, jac_G = F.jacobian([s,t]), G.jacobian([x,y]) # cálculo del jacobiano de F y G
dw_s, dw_t = sp.simplify(jac_G.subs({x:s**2+t**2,y:s/t})*jac_F)

# Cálculo de la derivada de w con respecto a s:
print('Derivada parcial de w con respecto a s: ')
display(dw_s)

# Cálculo de la derivada de w con respecto a t:
print('Derivada parcial de w con respecto a t: ')
display(dw_t)


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
# \frac{\partial y}{\partial x} = -\frac{F_x(x,y)}{F_y(x,y)}, \quad F_y(x,y) \neq 0.
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
# Calcular $\frac{\partial y}{partial x}$ para $y^3 + y^2 - 5y - x^2 = -4$. 
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
# \frac{\partial y}{\partial x} = -\frac{F_x(x,y)}{F_y(x,y)} = - \frac{(-2x)}{3y^2 + 2y - 5} = \frac{2x}{3y^2 + 2y - 5}.
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

