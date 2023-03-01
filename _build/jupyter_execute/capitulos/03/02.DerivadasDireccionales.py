#!/usr/bin/env python
# coding: utf-8

# # Derivadas direccionales y gradiente
# 
# ## Derivadas direccionales
# 
# En la sección anterior hemos aprendido cómo, dado el gráfico de una función de dos variables,  calcular la inclinación haciendo cortes por planos paralelos a los ejes $X$ e $Y$. 
# Ahora vamos a ampliar esta idea y veremos cómo calcular la inclinación en cualquier dirección. 
# 
# Es decir, veremos la inclinación que tenemos que afrontar si queremos bajar (o subir) por la ladera de una montaña, en cualquier dirección...
# 
# <img src="../../images/3.2.Montaña.png" width="300"/>
# 
# ````{prf:definition} Derivada direccional
# :label: def_DerivDirec
# :nonumber: 
# 
# Sea $f:\mathbb{R}^{2} \to \mathbb{R}$ y $\left(x_{0}, y_{0}\right)$ un punto en el dominio de $f$. 
# Sea $\mathbf{u}=\left(u_{1},u_{2}\right)$, un vector unitario ($\|\mathbf{u}\|=1$). 
# Definimos la **derivada direccional de $f$ en $\left(x_{0}, y_{0}\right)$ en la dirección de $\mathbf{u}$**, 
# $D_{\mathbf{u}}f\left(x_{0}, y_{0}\right)$, como el límite, si existe,
# 
# \begin{eqnarray*}
#  D_{\mathbf{u}}f\left(x_{0}, y_{0}\right) &:=& 
#     \lim_{h\to 0}\frac{f\left( (x_{0}, y_{0}) + h(v_{1},v_{2}) \right)-f\left(x_{0}, y_{0}\right)}{h} \\
#     &=& \lim_{h\to 0}\frac{f\left(x_{0}+hv_{1}, y_{0}+hv_{2} \right)-f\left(x_{0}, y_{0}\right)}{h}.
# \end{eqnarray*}
#     
# <img src="../../images/3.2.Derivada_direccional.jpg" width="400"/>
#     
# ````
# 
# La imagen anterior la hemos obtenido de la aplicación de Geogebra, creada por Laura del Río, https://www.geogebra.org/m/ZTttemYc.
# 
# Destaquemos que, si $f$ es una función que depende de tres variables, podemos definir de forma análoga la derivada direccional de $f$ en un punto de su dominio según la dirección marcada por cualquier vector unitario en $\mathbb{R}^3$.
# 
# 

# ## Vector gradiente
# 
# ````{prf:definition} Vector gradiente
# :label: def_gradiente
# :nonumber: 
# 
# Sea $f:\mathbb{R}^{2} \to \mathbb{R}$ y $\left(x_{0}, y_{0}\right)$ un punto en el dominio de $f$. 
#  Definimos el **vector gradiente de $f$ en $\left(x_{0}, y_{0}\right)$** como el límite, si existe,
# 
# $$
#  \mathbf{\nabla}f \left(x_{0}, y_{0}\right) = 
#  \left( \frac{\partial f}{\partial x} \left(x_{0}, y_{0}\right), \frac{\partial f}{\partial y} \left(x_{0}, y_{0}\right) \right).
# $$
#         
# ````
