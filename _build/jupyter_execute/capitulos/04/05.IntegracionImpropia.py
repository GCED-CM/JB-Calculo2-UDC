#!/usr/bin/env python
# coding: utf-8

# # Integración impropia
# 
# Anteriormente hemos definido la integral de Riemann de funciones acotadas en intervalos acotados.  Aunque parezca paradójico, en algunas ocasiones también es posible calcular la integral de una función no necesariamente acotada en intervalos no necesariamente acotados; por ejemplo:
# \begin{equation*}
# \int_1^{\infty} \frac{dx}{x^3} \, , \qquad \qquad \int_{-1}^{1} \frac{dx}{x^2} \, .
# \end{equation*}

# Estas integrales se denominan **impropias** y pueden clasificarse en:
# - de primera especie, si la función está acotada pero el intervalo es infinito,
# - de segunda especie, si el intervalo es finito pero la función no está acotada en el intervalo,
# - de tercera especie, cuando ni la función ni el intervalo de integración están acotados.

# ## Integrales impropias de primera especie
# 
# En estas integrales, **la función es acotada pero el intervalo de integración es infinito**.  
# 
# Sea $f: [a,+\infty) \rightarrow \mathbb{R}$ integrable en $[a, b]$ para cualquier $b \geq a$.  Entonces, se define:
# \begin{equation*}
# \int_a^{+\infty} f(x) \, dx = \underset{b \rightarrow +\infty}{\lim} \int_a^b f(x) \, dx \, .
# \end{equation*}
# Su cálculo tiene dos partes:
# 1. Calculamos la integral definida en un intervalo finito.
# 2. Hacemos que el extremo superior del intervalo tienda a infinito.
# 
# Veamos un ejemplo:
# \begin{equation*}
# I = \int_0^{+\infty} e^{-2x} \, dx \, .
# \end{equation*}
# La función del integrando está acotada y tiene una primitiva inmediata, pero el intervalo de integración no está acotado por la derecha.  Por lo tanto, vamos a calcular nuestra integral impropia como
# \begin{align*}
# I = \int_0^{+\infty} e^{-2x} \, dx &= \underset{b \rightarrow +\infty}{\lim} \int_0^{b} e^{-2x} \, dx = \\
#   &= \underset{b \rightarrow +\infty}{\lim} \left[ -\frac{1}{2} e^{-2x} \right]_0^b
#    = \underset{b \rightarrow +\infty}{\lim} \left( -\frac{1}{2} \right) \left[ e^{-2b} - 1 \right]
#    = -\frac{1}{2} \left[ 0 - 1 \right] = \frac{1}{2} \, .
# \end{align*}
# 
# Hemos obtenido un resultado finito.  En estos casos, decimos que **la integral impropia es convergente**. 
# 

# De forma similar podemos resolver una integral impropia donde el intervalo no está acotado por la izquierda.
# 
# Si $f: (-\infty, b] \rightarrow \mathbb{R}$ es integrable en $[a, b]$ para cualquier $a \leq b$, se define:
# \begin{equation*}
# \int_{-\infty}^b f(x) \, dx = \underset{a \rightarrow -\infty}{\lim} \int_a^b f(x) \, dx \, .
# \end{equation*}
# 
# Por ejemplo,
# \begin{equation*}
# \int_{-\infty}^{-3} \frac{dx}{x^2} \, dx = \underset{a \rightarrow -\infty}{\lim} \int_a^{-3} \frac{dx}{x^2} \, dx
#    = \underset{a \rightarrow -\infty}{\lim} \left[ -\frac{1}{x} \right]_a^{-3}
#    =  \underset{a \rightarrow -\infty}{\lim} \left[ \frac{1}{3} + \frac{1}{a} \right]
#    = \frac{1}{3} \, ,
# \end{equation*}
# o bien
# \begin{equation*}
# \int_{-\infty}^1 e^{-x} \, dx = \underset{a \rightarrow -\infty}{\lim} \int_a^1 e^{-x} \, dx
#    = \underset{a \rightarrow -\infty}{\lim} \left[ -e^{-x} \right]_a^1
#    = \underset{a \rightarrow -\infty}{\lim} \left[ -e^{-1} + e^{-a} \right] = +\infty \, .
# \end{equation*}
# En el primer caso estamos, de nuevo, ante una integral convergente (porque el resultado es finito), mientras que la segunda integral es **divergente**.

# Si el intervalo no está acotado en ninguno de sus extremos, debemos descomponer la integral en dos integrales impropias donde -en cada una de ellas- solo uno de los extremos no está acotado:
# \begin{align*}
# \int_{-\infty}^{+\infty} \frac{dx}{x^2+1} 
#     &= \int_{-\infty}^c \frac{dx}{x^2+1} + \int_c^{+\infty} \frac{dx}{x^2+1} = \\
#     &= \underset{a \rightarrow -\infty}{\lim} \int_a^c \frac{dx}{x^2+1} 
#      + \underset{b \rightarrow +\infty}{\lim} \int_c^b \frac{dx}{x^2+1} \\
#     &= \underset{a \rightarrow -\infty}{\lim} \left[ \arctan (x) \right]_a^c 
#      + \underset{b \rightarrow +\infty}{\lim} \left[ \arctan (x) \right]_c^b \\ 
#     &= \left[ \arctan (c) - \underset{a \rightarrow -\infty}{\lim} \arctan (a) \right]
#      + \left[ \underset{b \rightarrow +\infty}{\lim} \arctan (b) - \arctan (c) \right] \\
#     &= \arctan (c) - \left( -\frac{\pi}{2} \right) + \frac{\pi}{2} - \arctan (c) = \pi \, .
# \end{align*}
# Si la integral está bien planteada, el resultado será independiente del punto $c$ introducido.
# 
# ````{prf:remark} 
# :label: rem_impropia 
# :nonumber: 
# En este caso, **si una de las integrales en la descomposición es divergente, toda la integral se dice divergente**, independientemente de lo que le pase a la otra integral. 
# ````

# ## Integrales impropias de segunda especie
# 
# Decimos que **una integral impropia es de segunda especie cuando el intervalo de integración es finito pero la función a integrar, $f$, no está acotada en algún punto del intervalo**:
# \begin{equation*}
# \underset{x \rightarrow c}{\lim} f(x) = \pm \infty \qquad \text{ con } c \in [a,b] \, .
# \end{equation*}
# 
# En estos casos debemos tener la precaución de tomar límites en un entorno del punto (o puntos) donde la función deja de estar acotada.
# 
# Por ejemplo, consideremos la integral
# \begin{equation*}
# \int_2^4 \frac{dx}{\sqrt{x-2}} \, .
# \end{equation*}
# Podemos comprobar que el integrando, $f(x) = \frac{1}{\sqrt{x-2}}$, tiende a infinito cuando $x$ tiende a $2$; como este punto es, precisamente, el extremo izquierdo del intervalo, basta con calcular la integral en el intervalo $[c, 4]$ y hacer que $c$ tienda a $2$:
# \begin{align*}
# \int_2^4 \frac{dx}{\sqrt{x-2}} &= \underset{c \rightarrow 2}{\lim} \int_c^4 (x-2)^{-1/2} \, dx = \\
#     &= \underset{c \rightarrow 2}{\lim} \left[ \frac{(x-2)^{1/2}}{1/2} \right]_c^4
#      = 2 \underset{c \rightarrow 2}{\lim} \left[ \sqrt{4-2} - \sqrt{c-2} \right] = 2 \sqrt{2} \, .
# \end{align*}
# Se hace de manera similar si la función tiende a infinito cuando nos acercamos al límite derecho del intervalo:
# \begin{align*}
# \int_2^4 \frac{dx}{(x-4)^{1/3}} &= \underset{c \rightarrow 4}{\lim} \int_2^c (x-4)^{-1/3} \, dx 
#    = \underset{c \rightarrow 4}{\lim} \left[ \frac{(x-4)^{2/3}}{2/3} \right]_2^c \\
#    &= \frac{3}{2} \underset{c \rightarrow 4}{\lim} \left[ (c-4)^{2/3} - (2-4)^{2/3} \right]
#    = -\frac{3}{2} 2^{2/3} \, .
# \end{align*}
# 
# Y si el punto donde la función tiende a infinito está en el interior del intervalo de integración, basta con descomponer la integral en una suma de otras dos como las que acabamos de describir. Por ejemplo:
# \begin{align*}
# \int_1^4 \frac{dx}{(x-2)^{1/3}} &= \int_1^2 \frac{dx}{(x-2)^{1/3}} + \int_2^4 \frac{dx}{(x-2)^{1/3}} \\
#      &=\underset{b \rightarrow 2}{\lim} \int_1^b (x-2)^{-1/3} \, dx 
#                                  + \underset{a \rightarrow 2}{\lim} \int_a^4 (x-2)^{-1/3} \, dx  \\
#     &= \underset{b \rightarrow 2}{\lim} \left[ \frac{(x-2)^{2/3}}{2/3} \right]_1^b
#      + \underset{a \rightarrow 2}{\lim} \left[ \frac{(x-2)^{2/3}}{2/3} \right]_a^4  \\
#     &= \frac{3}{2} \underset{b \rightarrow 2}{\lim} \left[ (b-2)^{2/3} - (1-2)^{2/3} \right]
#      + \frac{3}{2} \underset{a \rightarrow 2}{\lim} \left[ (4-2)^{2/3} - (a-2)^{2/3} \right]  \\
#     &= \frac{3}{2} \left[ 0 - 1 \right] + \frac{3}{2} \left[ 2^{2/3} - 0 \right] 
#      = \frac{3}{2} \left(\sqrt[3]{4} - 1 \right) \, .
# \end{align*}
# 

# ## Integrales impropias de tercera especie
# 
# En este grupo incluimos las **integrales en las que tanto el intervalo como la función no están acotadas**.  
# 
# Para resolverlas, basta con combinar las técnicas que hemos visto en las secciones anteriores.
# 
# Veamos un ejemplo:
# \begin{equation*}
# \int_1^{+\infty} \frac{dx}{(x-4)^{2/5}} \, .
# \end{equation*}
# Vemos que el intervalo de integración es infinito y, además, la función a integrar no está acotada en $x = 4$.  
# 
# Para resolverla, la descomponemos en:
# - una integral entre $1$ y $4$ (impropia de segunda especie),
# - una integral entre $4$ y $6$ (impropia de segunda especie),
# - una integral entre $6$ y $+\infty$ (impropia de primera especie).
# 
# Hemos escogido el punto $6$ como podríamos haber escogido cualquier otro en $(4, +\infty)$.  De esta manera,
# \begin{align*}
# \int_1^{+\infty} \frac{dx}{(x-4)^{2/5}} &= \int_1^4 \frac{dx}{(x-4)^{2/5}} 
#        + \int_4^6 \frac{dx}{(x-4)^{2/5}} + \int_6^{+\infty} \frac{dx}{(x-4)^{2/5}} \\
#     &= \underset{b \rightarrow 4}{\lim} \int_1^b (x-4)^{-2/5} \, dx 
#      + \underset{a \rightarrow 4}{\lim} \int_a^6 (x-4)^{-2/5} \, dx \\
#     & \hphantom{=} + \underset{c \rightarrow +\infty}{\lim} \int_6^c (x-4)^{-2/5} \, dx \\
#     &= \underset{b \rightarrow 4}{\lim} \left[ \frac{(x-4)^{3/5}}{3/5} \right]_1^b
#      + \underset{a \rightarrow 4}{\lim} \left[ \frac{(x-4)^{3/5}}{3/5} \right]_a^6
#      + \underset{c \rightarrow +\infty}{\lim} \left[ \frac{(x-4)^{3/5}}{3/5} \right]_6^c \\
#     &= \dfrac{5}{3} \left[ \underset{b \rightarrow 4}{\lim} \left( (b-4)^{3/5} - (-3)^{3/5} \right) 
#                          + \underset{a \rightarrow 4}{\lim} \left( (6-4)^{3/5} - (a-4)^{3/5} \right) \right. \\
#     & \hphantom{= \dfrac{5}{3}} \left. + \underset{c \rightarrow +\infty}{\lim} \left( (c-4)^{3/5} - 2^{3/5} \right) \right]  \\
#     &= \dfrac{5}{3} \left[ 0 + 3^{3/5} + 2^{3/5} - 0 
#                     + \underset{c \rightarrow +\infty}{\lim} (c-4)^{3/5} - 2^{3/5} \right] = +\infty \, .
# \end{align*}
# Por lo tanto, en este ejemplo, estamos ante una integral divergente.
# 
# Recordamos que basta con que uno de los trozos sea divergente para que toda la integral sea considerada del mismo modo.

# ## Más información
# 
# Puedes encontrar más información, y algunos ejemplos/ejercicios en
# * https://es.wikipedia.org/wiki/Integral_impropia
# * https://es.khanacademy.org/math/ap-calculus-bc/bc-integration-new/bc-6-13/a/improper-integrals-review
# 
# ## Otros ejercicios
# 
# Además de los ejercicios que puedes encontrar en los boletines, te recomendamos que eches un vistazo a
# * https://www.ehu.eus/~mtpalezp/mundo/ana1/EJERCICIOSINTEGRALIMPROPIA.pdf
# * https://existelimite.blogspot.com/search/label/Integraci%C3%B3n%20impropia (son un poco más difíciles de lo habitual, pero... ¡tú puedes!).
