#!/usr/bin/env python
# coding: utf-8

# (sec_IntegracionNumerica)=
# # Integración numérica

# ## Casos en los que se utiliza
# 
# Hay algunos casos en los que, en vez de buscar la primitiva de una función y aplicar la regla de Barrow, usaremos una fórmula de integración numérica. Sobre todo cuando
# 
# * Sólo conocemos los valores de la función en un número finito de puntos. 
# * Su primitiva no se expresa en términos de funciones elementales. Por ejemplo:
# 
# $$ 
# \int \frac{\sin x}{x} \,dx;\qquad \int e^{-x^2}\,dx.
# $$
# * Su primitiva es muy costosa de calcular o evaluar. Por ejemplo:
# 
# $$
# \int \frac{1}{(x-8)\sqrt{x^2-4x-7}} \, dx.
# $$
# 
# ````{prf:definition} Fórmula de integración numérica o de cuadratura
# :label: def_intnum 
# :nonumber: 
# Una fórmula de **integración numérica** o fórmula de **cuadratura** es una suma de la forma:
# 
# $$
# \sum_{i=0}^n\omega_i\,f(x_i)\approx \int_a^bf(x)\,dx,
# $$
# 
# donde los puntos $x_0$, $x_1$, ..., $x_n$ son los llamados nodos de cuadratura y los valores $\omega_0$, $\omega_1$, ..., $\omega_n$ son los pesos asociados a cada nodo.
# ````

# ## Fórmulas simples
# 
# * **Fórmula del punto medio**:
#     <center>
# 
#     $$
#     \int_a^bf(x)\,dx\,\simeq\,(b-a)\,f\left(\frac{a+b}{2}\right) \,. 
#     $$
#     <img src="../../images/cap4_punto_medio.png" width="300"/>
#     </center>
# 
# * **Fórmula del trapecio**:
#     <center>
# 
#     $$
#     \int_a^bf(x)\,dx\,\simeq\,\frac{b-a}{2}\,\big(f(a) + f(b)\big) 
#     $$
#     <img src="../../images/cap4_trapecio.png" width="300"/>
#     </center>
# 
# * **Fórmula de Simpson**: Está basada en una interpolación cuadrática (tres nodos):
#     <center>
# 
#     $$
#     \int_a^bf(x)\,dx
#     \,\simeq\,
#     \frac{b-a}{6}\,\Big(\,f(a)\,+\,4\,\, f(\frac{a+b}{2})\,+\,f(b)\Big)
#     $$
#     <img src="../../images/cap4_simpson.png" width="300"/>
#     </center>
# 
# ````{prf:example} 
# :label: ex_intnumersimple 
# :nonumber: 
# Determinar una aproximación de $\displaystyle \int_1^3 \sin(\sqrt{x}) \, dx$ mediante las fórmulas del trapecio y de Simpson, y comparar con la solución exacta:
# 
# Tomando el cambio de variable $u = x^{1/2}$ e integrando por partes llegamos a:
# 
# $$
# \displaystyle \int \sin(\sqrt{x}) \, dx = 2 \sin(\sqrt{x}) - 2 \sqrt{x} \cos(\sqrt{x}) + C; \quad \displaystyle \int_1^3 \sin(\sqrt{x}) \, dx = 1.9279...
# $$
# Mientras que por integración numérica:
# 
# \begin{eqnarray*}
# &\bullet& \quad \text{Trapecio: }\displaystyle \int_1^3 \sin(\sqrt{x}) \simeq \frac{3 - 1}{2}\big(\sin(1) + \sin(\sqrt{3}) \big) = 1.8285...\\
# &\bullet& \quad \text{Simpson: } \displaystyle \int_1^3 \sin(\sqrt{x}) \simeq \frac{3 - 1}{6}\big(\sin(1) + 4 \sin(\sqrt{2}) + \sin(\sqrt{3}) \big) = 1.9265...
# \end{eqnarray*}
# 
# La fórmula de Simpson tiene en cuenta un nodo más que la del trapecio y en este ejemplo podemos ver que arroja una mejor aproximación.
# ````

# ## Fórmulas compuestas
# 
# La idea es sencilla: se divide el intervalo de integración, $[a,b]$, en subintervalos y en cada uno de estos se usa una fórmula de integración numérica simple.
# 
# El caso más habitual surge cuando tomamos $n$ subintervalos, $[x_i, x_{i + 1}]$, de igual longitud $h$. Es decir, cuando elegimos
# $x_i = a + ih$, $i = 0, 1, ..., n$, para un valor $h = \frac{b - a}{n}$.
# 
# Entonces aproximamos la integral mediante una fórmula simple en cada subintervalo. Pero, ¡cuidado!: 
# * para punto medio o Simpson los intervalos los tenemos que tomar los intervalos de tamaño $2h$, es decir, de 3 en 3 puntos, porque necesitamos el punto medio de cada subintervalo,  $[x_{2i-2}, x_{2i}]$,
# * para trapecio, como no necesitamos el punto medio, podemos tomar todos los subintervalos que, en este caso, tendrán tamaño $h$: $[x_{i}, x_{i-1}]$.
# 
# Entonces tendremos:
# 
# * Punto medio o Simpson compuestos, con $n$ par: $\displaystyle \int_a^b f(x)\,dx = \sum_{i=1}^{n/2} \int_{x_{2i-2}}^{x_{2i}} f(x)\,dx$.
# * Trapecio compuesto: $\displaystyle \int_a^b f(x)\,dx = \sum_{i=0}^{n} \int_{x_{i-1}}^{x_{i}} f(x)\,dx$.
# 
# Ahora, dependiendo de la fórmula simple que elijamos tendremos:
# 
# * **Fórmula del punto medio compuesta**:
#     <center>
# 
#     \begin{eqnarray*}
#     \int_a^b f(x)\,dx = \sum_{i=1}^{n/2} \int_{x_{2i-2}}^{x_{2i}} f(x)\, dx &\approx& \sum_{i=1}^{n/2} \left(x_{2i}-x_{2i-2}\right) f\left(x_{2i-1}\right) \\
#     &=& 2h\sum_{i=1}^{n/2} f\left(x_{2i-1}\right)
#     \end{eqnarray*}
#     <img src="../../images/cap4_punto_medio_compuesto.png" width="300"/>
#     </center>
# 
# * **Fórmula del trapecio compuesta**:
#     <center>
# 
#     \begin{eqnarray*}
#     \int_a^b f(x)\,dx = \sum_{i=1}^{n} \int_{x_{i-1}}^{x_{i}} f(x)\, dx &\approx& 
#     \sum_{i=1}^{n} \frac{h}{2} \left( f\left(x_{i-1}\right) + f\left(x_{i}\right) \right) \\
#     &=& \frac{h}{2} \left( f(x_{0}) + 2 \sum_{i=1}^{n-1}f(x_{i}) + f(x_{n}) \right)
#     \end{eqnarray*}
#     <img src="../../images/cap4_trapecio_compuesto.png" width="300"/>
#     </center>
# 
# * **Fórmula de Simpson compuesta**:
#     <center>
# 
#     \begin{eqnarray*}
#     \int_a^b f(x)\,dx = \sum_{i=1}^{n/2} \int_{x_{2i-2}}^{x_{2i}} f(x)\, dx &\approx& \sum_{i=1}^{n/2} \frac{2h}{6} \left(f\left(x_{2i-2}\right) + 4f\left(x_{2i-1}\right) + f\left(x_{2i}\right) \right) \\
#     &=& \frac{2h}{6} \left( f(x_{0}) + 4\sum_{i=1}^{n/2} f(x_{2i-1}) + 2\sum_{i=1}^{n/2-1}f(x_{2i}) + f(x_{n}) \right)
#     \end{eqnarray*}
#     <img src="../../images/cap4_simpson_compuesto.png" width="300"/>
#     </center>
# 
# ## Programación en `Numpy`
# 
# Podéis ver la programación de estos métodos en la Sección {ref}`sec_PythonIntegracion`. 
# Por favor, no dejéis de mirar con calma la forma en que estas fórmulas compuestas se implementan en una línea, jugando con el comando `np.sum`, lo que nos permite evitar por completo los bucles. Queda un ejercicio fantástico para el manejo de los arrays en `Python`... 

# ## Más información
# 
# Y ahora os damos alguna referencia para que, si os apetece, ampliéis vuestro conocimiento sobre integración numérica:
# * En la wiki: https://es.wikipedia.org/wiki/Integraci%C3%B3n_num%C3%A9rica.
# * En esta página del Departamento de Matemáticas de la Universidad de Oviedo: https://www.unioviedo.es/compnum/laboratorios_py/Inte/Integrales.html.
