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
# \mathrm{J}(G \circ \mathbf{F}) (\mathbf{a}) = \mathrm{J}G(\mathbf{F}(\mathbf{a})) \; \mathrm{J}\mathbf{F}(\mathbf{a}),
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
# \mathrm{J}(G \circ \mathbf{F}) (\mathbf{a}) = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(\mathbf{a})) \; \mathrm{J}\mathbf{F}(\mathbf{a}).
# $$
# 
# **NOTA 2:** La regla de la cadena para el caso multivariable es una generalización de la regla de la cadena para una variable. Si $n = m = 1$, tal que $a \in \mathbb{R}$, $\mathbf{F}: D \subset \mathbb{R} \rightarrow \mathbb{R}$ y $G: \mathbb{R} \rightarrow \mathbb{R}$, entonces 
# 
# $$
# \mathrm{J}(G \circ F) (a) = \mathrm{J}G(F(a)) \; \mathrm{J}F(a) = G'(F(a))\; F'(a).
# $$
# 
# Aunque no lo haremos así, os dejamos un par de *remarks*, por si lo veis en algún libro y os llama la atención:
# 
# ````{prf:remark} Regla de la cadena para una variable independiente
# :label: rc_01_regla_cadena
# :nonumber:
# 
# Sea $w = G(x_1,x_2,...,x_m)$, donde $G$ es una función diferenciable de las $m$ variables $x_1, x_2, ... , x_m$. Si cada una de las $x_j = F_j(t)$ es una función diferenciable de $t$, entonces $w$ es una función diferenciable de $t$, y
# 
# $$
# \frac{dw}{dt} = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(t)) \; \mathrm{J}\mathbf{F}(t) = \frac{\partial w}{\partial x_1}\frac{dx_1}{dt} + \frac{\partial w}{\partial x_2}\frac{dx_2}{dt} + ... + \frac{\partial w}{\partial x_m}\frac{dx_m}{dt}.
# $$
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
# = (\mathbf{\nabla}G)^\mathrm{t} (\mathbf{F}(s,t)) \; \mathrm{J}\mathbf{F}(s,t) = 
# \begin{bmatrix}
# \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial s} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial s} + \ldots + \frac{\partial w}{\partial x_m}\frac{\partial x_m}{\partial s}\\
# \frac{\partial w}{\partial x_1}\frac{\partial x_1}{\partial t} + \frac{\partial w}{\partial x_2}\frac{\partial x_2}{\partial t} + \ldots + \frac{\partial w}{\partial x_m}\frac{\partial x_m}{\partial t}
# \end{bmatrix}
# $$
# ````

# ## Ejemplo una variable
# 
# Consideramos la composición de funciones:
# 
# $$
# \begin{array}{ccccc}
# \mathbb{R} & \stackrel{\mathbf{F}}{\longrightarrow} & \mathbb{R}^{2} & \stackrel{G}{\longrightarrow} & \mathbb{R} \\
# t &\to & \mathbf{F}(t) = \begin{bmatrix} x=\sin(t) \\ y=e^{t} \end{bmatrix} & \to & G(x,y) = x^2y-y^2 
# \end{array}
# $$
# 
# Vamos a calcular el jacobiano de esta composición. Recordemos que
# 
# $$
# \mathrm{J}\left( G\circ\mathbf{F}\right)(t) = \mathrm{J}G(\mathbf{F}(t)) \; \mathrm{J}\mathbf{F}(t).
# $$
# 
# Vamos a calcular cada uno de los factores de este producto:
# 
# $$
# \mathrm{J}\mathbf{F}(t) = \begin{bmatrix} \frac{\partial x}{\partial t} (t) \\ \\ \frac{\partial y}{\partial t} (t) \end{bmatrix}
# = \begin{bmatrix} \cos(t) \\ \\ e^t \end{bmatrix}. 
# $$
# 
# El segundo factor es:
# 
# $$
# \mathrm{J}G(x,y) = \begin{bmatrix} \dfrac{\partial G}{\partial x} (x,y) & \dfrac{\partial G}{\partial y} (x,y) \end{bmatrix} = 
# \begin{bmatrix} 2xy & x^2-2y\end{bmatrix},
# $$
# entonces:
# 
# $$
# \mathrm{J}G (\mathbf{F}(t)) = \mathrm{J}G \left( \sin(t), e^{t} \right) = \begin{bmatrix} 2\sin(t) e^{t} & \sin^2(t)-2e^{t}\end{bmatrix}.
# $$
# Y, por lo tanto,
# 
# $$
# \mathrm{J}\left( G\circ\mathbf{F}\right)(t) = \begin{bmatrix} 2\sin(t) e^{t} & \sin^2(t)-2e^{t}\end{bmatrix} \begin{bmatrix} \cos(t) \\ \\ e^t \end{bmatrix} 
# = 2e^{t}\sin(t)\cos(t) + e^{t}\sin^{2}(t)-2e^{2t}.
# $$
# 
# Ya estaría, pero vamos a hacerlo por otro camino: vamos a construir explícitamente la función composición y a derivarla:
# 
# $$
# t \stackrel{\mathbf{F}}\longrightarrow \left(\sin(t),e^{t}\right) \stackrel{G}{\longrightarrow} e^{t}\sin^{2}(t)-e^{2t},
# $$
# y, derivando directamente,
# 
# $$
# \mathrm{J}\left( G\circ\mathbf{F}\right)(t) = \frac{d}{dt}\left(e^{t}\sin^{2}(t)-e^{2t}\right) = e^{t}\sin^{2}(t) + 2 e^{t}\sin(t)\cos(t) - 2e^{2t}.
# $$
# 
# ¡¡Da lo mismo de las dos maneras!! I can't believe it!!

# ## Ejemplo de dos variables
# 
# Consideramos la composición de funciones:
# 
# $$
# \begin{array}{ccccc}
# \mathbb{R}^{2} & \stackrel{\mathbf{F}}{\longrightarrow} & \mathbb{R}^{2} & \stackrel{G}{\longrightarrow} & \mathbb{R} \\
# \begin{bmatrix} r \\ \theta \end{bmatrix} &\to & \mathbf{F}(r,\theta) = \begin{bmatrix} x=r\cos(\theta) \\ y=r\sin(\theta) \end{bmatrix} & \to & G(x,y) = x^2 + y^2 
# \end{array}
# $$
# 
# Vamos a calcular el jacobiano de esta composición. Recordemos que
# 
# $$
# \mathrm{J}\left( G\circ\mathbf{F}\right)(r,\theta) = \mathrm{J}G(\mathbf{F}(r,\theta)) \; \mathrm{J}\mathbf{F}(r,\theta).
# $$
# 
# Vamos a calcular cada uno de los factores de este producto:
# 
# $$
# \mathrm{J}\mathbf{F}(r,\theta) = 
# \begin{bmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\ \\ \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{bmatrix}
# = \begin{bmatrix} \cos(\theta) & -r\sin(\theta) \\ \\ \sin(\theta) & r\cos(\theta) \end{bmatrix}.
# $$
# 
# El segundo factor es:
# 
# $$
# \mathrm{J}G(x,y) = \begin{bmatrix} \dfrac{\partial G}{\partial x} &  \dfrac{\partial G}{\partial y} \end{bmatrix} = \begin{bmatrix} 2x & 2y \end{bmatrix}.
# $$
# 
# Entonces:
# 
# $$
# \mathrm{J}G (\mathbf{F}(t)) = \mathrm{J}G \left( r\cos(t), r\sin(\theta) \right) = \begin{bmatrix} 2r\cos(\theta) & 2r\sin(\theta) \end{bmatrix}.
# $$
# Y, por lo tanto,
# 
# \begin{eqnarray*}
# \mathrm{J}\left( G\circ\mathbf{F}\right)(t) &=& \begin{bmatrix} 2r\cos(\theta) & 2r\sin(\theta) \end{bmatrix} 
# \begin{bmatrix} \cos(\theta) & -r\sin(\theta) \\ \\ \sin(\theta) & r\cos(\theta) \end{bmatrix} \\
# \\
# &=& \begin{bmatrix} 2r\cos^{2}(\theta) + 2r\sin^2(\theta) & -2r^2\sin(\theta)\cos(\theta) + 2r^2\sin(\theta)\cos(\theta) \end{bmatrix}
# = \begin{bmatrix} 2r & 0 \end{bmatrix}.
# \end{eqnarray*}
# 
# Como en el ejemplo anterior, vamos a construir explícitamente la función composición y a calcular su jacobiano:
# 
# $$
# (r,\theta) \stackrel{\mathbf{F}}\longrightarrow \left(r\cos(\theta), r\sin(t)\right) \stackrel{G}{\longrightarrow} r^{2}\cos^{2}(\theta) + r^{2}\sin^{2}(\theta),
# $$
# y, derivando directamente,
# 
# $$
# \mathrm{J}\left( G\circ\mathbf{F}\right)(r,\theta) = \begin{bmatrix} \dfrac{(G\circ\mathbf{F})}{\partial r} (r,\theta) & \dfrac{(G\circ\mathbf{F})}{\partial \theta} (r,\theta) \end{bmatrix}
# = \begin{bmatrix} 2r & 0\end{bmatrix}.
# $$
# 
# Again... ¡¡Da lo mismo!! ¡¡GUAU, GUAU, GUAUUUU!!

# ## Jacobiano de la composición de funciones con `sympy`
# 
# Retomamos este último ejemplo para resolverlo ayudados por `sympy`. A ver si vuelve a dar lo mismo... aunque ya sería mucha suerte, ¿no? 

# In[5]:


import sympy as sp

x, y, r, t = sp.symbols('x y r t', real=True) 

# Definimos las funciones F y G como matrices
F = sp.Matrix([r*sp.cos(t), r*sp.sin(t)])
G = sp.Matrix([ x**2 + y**2 ])

# Calculamos (y mostramos) las matrices jacobianas asociadas a F y G
jac_F = F.jacobian([r,t])
display(jac_F)

jac_G = G.jacobian([x,y])
display(jac_G)

# Calculamos la jacobiana de la composición como producto de matrices
jac_GoF = jac_G.subs({x:r*sp.cos(t),y:r*sp.sin(t)})*jac_F
display(sp.simplify(jac_GoF))


# ## Derivación implícita
# 
# Como ya aprendimos al comienzo de la Sección {ref}`sec:3.4.PlanoTangente`, es posible que una función venga dada implícitamente. 
# Por ejemplo, la función de una variable $y = f(x)$ puede venir determinada por la expresión $y^3 + y^2 - 5y - x^2 = -4$. 
# Aunque no conozcamos su expresión explícita podemos fácilmente calcular las derivadas de las variables dependientes en función de las independientes. Os mostramos a continuación cómo hacerlo.
# 
# * **Funciones con una única variable independiente**. Supongamos que existe una única variable independiente, $x$, y una variable dependiente, $y\equiv y(x)$. En este caso, 
# 
#     $$
#     F(x,y) = 0 \stackrel{\frac{\partial}{\partial x}}{\Longrightarrow} 
#     \frac{\partial F}{\partial x}(x,y)\frac{\partial x}{\partial x} + \frac{\partial F}{\partial y}(x,y)\frac{\partial y}{\partial x}.
#     $$
# 
#     Despejamos en la anterior expresión, teniendo en cuenta que $\frac{\partial x}{\partial x}=1$, y obtenemos:
# 
#     $$
#     \frac{\partial y}{\partial x} = - \frac{ \frac{\partial F}{\partial x}(x,y)  } { \frac{\partial F}{\partial y}(x,y) }.
#     $$
# 
# * **Funciones con dos variables independientes**. Si ahora tenemos una relación implícita entre dos variables independientes, $x$ e $y$, y una variable que depende de las anteriores, $z \equiv z(x,y)$, ,
# 
#     \begin{eqnarray*}
#     F(x,y,z) = 0 &\stackrel{\frac{\partial}{\partial x}}{\Longrightarrow}&
#     \frac{\partial F}{\partial x}(x,y,z)\frac{\partial x}{\partial x} + \cancel{ \frac{\partial F}{\partial y}(x,y,z)
#     {\color{red} \frac{\partial y}{\partial x}} } 
#     + \frac{\partial F}{\partial z}(x,y,z)\frac{\partial z}{\partial x} = 0 \\
#     & \Rightarrow & \frac{\partial z}{\partial x} = - \frac{ \frac{\partial F}{\partial x}(x,y,z)  } { \frac{\partial F}{\partial z}(x,y,z) } \\
#     F(x,y,z) = 0 &\stackrel{\frac{\partial}{\partial y}}{\Longrightarrow}&
#     \cancel{ \frac{\partial F}{\partial y}(x,y,z){\color{red} \frac{\partial x}{\partial y}} } 
#     + \frac{\partial F}{\partial y}(x,y,z) \frac{\partial y}{\partial y} 
#     + \frac{\partial F}{\partial z}(x,y,z)\frac{\partial z}{\partial y} = 0\\
#     & \Rightarrow & \frac{\partial z}{\partial y} = - \frac{ \frac{\partial F}{\partial y}(x,y,z)  } { \frac{\partial F}{\partial z}(x,y,z) }
#     \end{eqnarray*}
# 
# Veamos algún ejemplo.
# 
# ````{prf:example}  
# :label: 3.x._ex
# :nonumber: 
# 
# Calcula $\dfrac{\partial y}{\partial x}$ a partir de la expresión $y^3 + y^2 - 5y - x^2 = -4$. 
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
# \frac{\partial F}{\partial x}(x,y) = -2x \quad \textrm{ y } \quad \frac{\partial F}{\partial y}(x,y) = 3y^2 + 2y - 5.
# $$
# 
# Entonces
# 
# $$
# \frac{\partial y}{\partial x} = -\frac{F_x(x,y)}{F_y(x,y)} = - \frac{(-2x)}{3y^2 + 2y - 5} = \frac{2x}{3y^2 + 2y - 5}.
# $$
# ````
# 
# Vamos a preguntarle a nuestro oráculo, por si nos hemos equivocado.

# In[14]:


import sympy as sp
x, y = sp.symbols('x y', real=True) 

F = y**3 + y**2 - 5*y - x**2 + 4 
display(sp.Eq(F,0)) # Aqui está la ec. implícita F(x,y) = 0 

# Cálculo de las derivadas de F respecto x e y
F_x, F_y = sp.diff(F, x), sp.diff(F, y) 

# Utilizamos la fórmula
y_x = - F_x/F_y

print('Derivada implícita con respecto a x: ')
display(y_x)


# Ya por último vamos a resolver directamente con `sympy` un ejemplo con dos variables independientes (te queda como ejercicio comprobar que `sympy` no se equivoca).
# 
# ````{prf:example}  
# :label: 3.5.Ej2
# :nonumber: 
# 
# Calcular $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$ a partir de la expresión  $\cos(x^2 z)+\sin(y^2 z) + z^2 = 0$.
# ````

# In[37]:


import sympy as sp
x, y, z = sp.symbols('x y z', real=True) 

F = sp.cos(x**2 * z) + sp.sin(y**2 * z) + z**2 
display(sp.Eq(F,0)) # Aqui está la ec. implícita F(x,y) = 0 

# Cálculo de las derivadas de F respecto x, y, z
F_x, F_y, F_z = sp.diff(F, x), sp.diff(F, y), sp.diff(F,z) 

# Utilizamos las fórmulas
z_x = - F_x/F_z
z_y = - F_y/F_z

print('Derivada implícita con respecto a x: ')
display(z_x)
print('Derivada implícita con respecto a y: ')
display(z_y)

