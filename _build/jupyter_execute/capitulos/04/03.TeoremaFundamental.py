#!/usr/bin/env python
# coding: utf-8

# # Teorema Fundamental del Cálculo
# 
# ## Enunciado del teorema
# 
# Calcular el valor de una integral definida empleando geometría o límites de las sumas de Riemann para particiones infinitamente refinadas, es, en general, una tarea complicada. En esta sección presentamos el teorema fundamental del cálculo, que nos da un medio para calcular muchas integrales. De hecho, reducirá el problema de integración al cálculo de primitivas, es decir, al problema inverso de la derivación.
# 
# ````{prf:theorem} Teorema fundamental del Cálculo
# :label: th_fundamental 
# :nonumber: 
# Sea $f \in {\cal R}[a,b]$.  Para $a \leq x \leq b$, sea: 
# 
# $$F(x) = \int_a ^x f(t) \,dt .$$
# Entonces, $F \in {\cal C}[a,b]$.  Además, si $f$ es continua en $[a,b]$, entonces $F$ es derivable en $[a,b]$
# y $F^{\,\prime} (x) = f(x)$, $\forall x \in [a,b]$.
# 
# También puede enunciarse de la siguiente manera:
# 
# Si $f : I \longrightarrow \mathbb R$ es continua en $I$, entonces tiene primitivas en $I$; 
# una de ellas es la integral definida $F$ dada por:
# 
# $$F(x) = \int_a ^x f(t) \,dt,$$
# donde $a \in I$ *es cualquiera*.
# ````
# 
# Sería bueno que practicaras un poco en el cálculo de $F$ para casos sencillos. Aquí tienes un par de ejemplos detallados:
# 
# * https://existelimite.blogspot.com/2012/11/un-ejercicio-sobre-el-teorema.html
# * https://existelimite.blogspot.com/2012/12/un-ejercicio-en-flashback-sobre-el.html
# 
# ## Primera consecuencia: derivación de una función integral
# 
# Vamos a *jugar* un poco con este teorema. Empezamos con un ejercicio en 4 partes:
# 
# **EJERCICIO:** 
# 
# 1. Sea $F(x)= \displaystyle \int_{1}^{x} t^2\sin(t)\, dt$. Calcula $F'(x)$.
# 
#     Según el teorema fundamental, como la función que está dentro de la integral, $f(t)=t^2\sin(t)$, es continua, la derivada de $F$ en $x$ coincide con el valor del integrando en ese punto:
# 
#     $$
#      F'(x) = f(x) = x^2\sin(x).
#     $$
# 2. Sea $F(x)= \displaystyle \int_{1}^{x^3} t^2\sin(t)\, dt$. Calcula $F'(x)$.
# 
#     En este caso, tenemos que combinar el teorema fundamental con la regla de la cadena para obtener:
# 
#     $$
#      F'(x) = F'(x^3)3x^2 = f(x^3)3x^2 = \left(x^{3}\right)^{2}\sin(x^{3}) 3x^2 = 3x^{8}\sin(x^{3}).
#     $$
# 3. Sea $F(x)= \displaystyle \int_{\ln(x)}^{1} t^2\sin(t)\, dt$. Calcula $F'(x)$.
# 
#     Ahora, en primer lugar le damos la vuelta a la integral (cambiando su signo) para que la parte variable quede en la parte superior, 
# 
#     $$
#     F(x) = \int_{\ln(x)}^{1} t^2\sin(t)\, dt = - \int_{1}^{\ln(x)} t^2\sin(t)\, dt = \int_{1}^{\ln(x)} - t^2\sin(t)\, dt,
#     $$
#     y ahora actuamos como en el apartado anterior:
# 
#     $$
#      F'(x) = F'(\ln(x))\frac{1}{x} = -(\ln(x))^2\sin(\ln(x))\frac{1}{x} = -\frac{(\ln(x))^2}{x}\sin(\ln(x)). 
#     $$
# 4. Sea $F(x)= \displaystyle \int_{\ln(x)}^{x^3} t^2\sin(t)\, dt$. Calcula $F'(x)$.
#    
#     Primero utilizamos la aditividad en intervalos:
# 
#     $$
#     F(x)= \displaystyle \int_{\ln(x)}^{x^3} t^2\sin(t)\, dt = \int_{\ln(x)}^{1} t^2\sin(t)\, dt + \int_{1}^{x^3} t^2\sin(t)\, dt,
#     $$
#     y, a continuación, juntando los resultados de los anteriores apartados:
# 
#     $$
#     F'(x) = 3x^{8}\sin(x^{3}) - \frac{(\ln(x))^2}{x}\sin(\ln(x)).
#     $$
# 
# Estas cuentas, hechas para un caso particular, se pueden generalizar fácilmente:
# 
# ````{prf:property} 
# :label: prop_fundamental 
# :nonumber: 
# Sea la función $F$ dada por la integral definida:
# 
# $$
# F(x) = \int_{a(x)}^{b(x)} f(t) \, dt.
# $$
# Entonces, la derivada de $F$ con respecto a $x$ viene dada por: 
# 
# $$
# F^{\,\prime}(x) = f(b(x)) \, b^{\prime}(x) - f(a(x)) \, a^{\prime}(x). 
# $$
# ````
# 
# Esto abre un mundo de posibilidades. Por ejemplo, si conocemos la derivada podemos buscar los puntos críticos, estudiar la concavidad/convexidad o, incluso, ¡calcular el polinomio de Taylor para funciones definidas a partir de una integral!
# 
# Puede ser buena idea practicar un poco:
# 
# * https://existelimite.blogspot.com/2012/12/calculo-de-la-derivada-de-f-mediante-el.html
# * https://existelimite.blogspot.com/2017/01/examen-de-enero-de-2017-aplicacion-del.html
# * https://existelimite.blogspot.com/2014/02/calculo-de-extremos-de-f-mediante-el.html

# ## Segunda consecuencia: Regla de Barrow
# 
# ````{prf:property} Regla de Barrow
# :label: prop_Barrow 
# :nonumber: 
# Si $f \in {\cal R}[a,b]$ y existe una primitiva $F$ de $f$ en $[a,b]$, entonces: 
# 
# $$
# \int_a ^b f(x) \,dx = \left. \begin{array}{c} \, \\ \, \end{array} F(x) \right|_a^b = F(b) - F(a).
# $$
# ````
# 
# ````{prf:proof} 
# Pese a que no es muy habitual en este curso, al ser muy sencilla y creemos que didáctica, vamos a mostrar la demostración de esta propiedad... aunque sólo para el caso más fácil: supondremos que $f$ es una función continua.
# 
# Supongamos entonces que podemos calcular una primitiva, $F$, para nuestra función $f$ (con las técnicas aprendidas (ejem...) en el instituto o en la Sección {ref}`sec:integral_indefinida`). 
# 
# Por otra parte, gracias al Teorema Fundamental del Cálculo, conocemos otra primitiva de $f$:
# 
# $$
# G(x) = \int_a ^x f(t) \,dt.
# $$
# 
# Como también sabemos que dos primitivas distintas de una misma función se diferencian en una constante, resulta que: $F(x) = G(x) + C$. Entonces:
# 
# \begin{eqnarray*}
# F(b) - F(a) &=& \left(G(b)+C\right) - \left(G(a)+C\right) = G(b) - G(a) = \int_{a}^{b} f(t)\, dt - \int_{a}^{a} f(t)\, dt \\
# &=& \int_{a}^{b} f(t)\, dt - 0 = \int_{a}^{b} f(t)\, dt.
# \end{eqnarray*}
# ````
# 
# La Regla de Barrow (insistimos: una consecuencia directa del Teorema Fundamental del Cálculo) une la integración de Riemann (algo puramente geométrico) con el cálculo de primitivas (una operación aritmética): 
# para calcular el área por debajo de una función positiva basta calcular una primitiva de ésta, evaluarla en los dos extremos y restar. Veamos un
# 
# ````{prf:example} 
# :label: ex_Barrow 
# :nonumber: 
# Calcula el área bajo la curva $y=\cos x$ en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.
# 
# **Solución:**
# 
# $$
# A = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos x \, dx = \sin x \lvert_{-\frac{\pi}{2}}^{\frac{\pi}{2}} = \sin\left(\frac{\pi}{2}\right) - \sin\left(-\frac{\pi}{2}\right) = 1 - (-1) = 2.
# $$
# Así, el área de la región son dos unidades cuadradas.
# ````
# 
# ## Integración por partes en la integral de Riemann
# 
# ````{prf:property} 
# :label: prop_fundamental 
# :nonumber: 
# 
# Si $F$ y $G$ son dos funciones derivables en $[a,b]$, y se tiene: 
# 
# $$\begin{cases} F^{\,\prime} = f \\ G^{\,\prime} = g \end{cases} \hspace{20mm} \text{en } [a,b],
# $$ 
# siendo $f$ y $g$ integrables en $[a,b]$, entonces 
# 
# $$
# \int_a ^b F(x) \,g(x) \,dx = F(b) \,G(b) - F(a) \,G(a) - \int_a ^b f(x) \,G(x) \,dx.
# $$
# ````
