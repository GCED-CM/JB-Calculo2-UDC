#!/usr/bin/env python
# coding: utf-8

# # Definición de derivada y propiedades básicas
# 
# ## Definición de derivada
# 
# Vamos a introducir este nuevo concepto mediante un ejemplo. Para ello copiamos 
# el célebre experimento de Galileo en la torre de Pisa y nos preguntamos:
# 
# Supongamos que dejamos caer una pelota desde lo más alto de un edificio de 
# $300$ m. ¿Cuál será la velocidad de la pelota después de 5 segundos?
# 
# Galileo llegó a la conclusión de que el espacio recorrido es directamente proporcional
# al cuadrado del tiempo transcurrido, según la fórmula
# 
# $$
# s(t)=4.9 t^2,
# $$
# 
# fórmula que se acerca mucho a la realidad... siempre que despreciemos el rozamiento
# ejercido por el aire.
# 
# Entonces, ¿cómo hallamos la velocidad en $t=5$ segundos? Podemos hacer una 
# velocidad promedio:
# 
# $$
# \begin{array}{rcl}
# \text{Velocidad promedio} &=& \dfrac{\text{distancia recorrida}}
# {\text{tiempo transcurrido}}, \\
# && \\
# v(5)\approx \dfrac{s(5.1)-s(5)}{0.1} &=& \dfrac{4.9(5.1)^2-4.9\, 5^2}{0.1}
# =49.49\; m/s,
# \end{array}
# $$
# 
# o, mejor todavía, 
# 
# $$
# v(5)\approx \frac{s(5.01)-s(5)}{0.01}=\frac{4.9(5.01)^2-4.9(5)^2}{0.01}
# =49.049\; m/s.
# $$
# 
# Realmente, lo que estamos haciendo es aproximar la pendiente de la recta tangente 
# a la función $s$ en el punto $t=5$.
# Recordemos, antes de nada, que la **pendiente** de una recta es la tangente del
# ángulo que forma con el eje $OX$, como se muestra en la siguiente figura:
# 
# <img src="../../images/cap_deriv_pendiente_recta.png" width="400"/>
# 
# 

# Si ahora queremos calcular la pendiente de la recta tangente a una función $f$ 
# en un punto $x_0$, lo que haremos será calcular las pendientes de las rectas 
# secantes a $f$ por dos puntos próximos, $x_0$ y $x$, y hacer que $x$ se 
# acerque a $x_0$ (es decir, tomar el *límite cuando $x\to x_0$*). La 
# ilustración gráfica de este proceso se muestra en la siguiente figura 
# (con la que, por cierto, puedes jugar en el siguiente link: https://www.desmos.com/calculator/piskepauzm): 
# 
# <img src="../../images/cap_deriv_definicion_derivada.png" width="400"/>
# 
# ````{prf:definition} 
# :label: def_derivada
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. Definimos la **derivada de $f$ en $x_0$**
# como el límite, si existe,
# 
# $$
# f'(x_0):=\lim_{x\to x_0}\dfrac{f(x)-f(x_0)}{x-x_0}=\lim_{h\to 0}\dfrac{f(x_0+h)-f(x_0)}{h}.
# $$
# 
# ````
# ````{prf:remark} 
# :label: remark_derivada
# :nonumber: 
# 
# 1. Aquí ya vemos la utilidad de no incluir el punto $x_0$ (en este caso, 
# el punto $h=0$) en la definición de límite. En la expresión 
# $\displaystyle\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$ no podemos hacer nada si 
# $h=0$, ya que tendríamos una división entre $0$. Pero, afortunadamente, 
# justo el punto $h=0$ no se incluye en la definición de límite (recordemos eso 
# de $0<|h-0|<\delta$...).
# 
# 2. El cociente $\frac{f(x)-f(x_0)}{x-x_0}$ mide la variación de la función 
# respecto a la variación de la variable. Por ese motivo a $f'(x_0)$ se le denomina, 
# en ocasiones, coeficiente de variación de $f$, o razón de cambio de la función 
# $f$, en el punto $x_0$. 
# 
#     Es decir, la derivada de una función en un punto indica la variación instantánea 
#     de la función en ese punto. Por ejemplo, la aceleración, que es la variación de 
#     velocidad, se escribe matemáticamente como $\frac{dv}{dx}$, es decir, 
#     la derivada de la velocidad respecto al tiempo. 
# 
#     Que la derivada sea la variación instantánea de una variable dependiente, 
#     $y$, respecto a otra variable independiente, $x$, será fundamental cuando
#     veamos los modelos matemáticos en ecuaciones diferenciales.
# 
# 3. Ahora ya podemos calcular la ecuación de la recta tangente utilizando la
# fórmula punto-pendiente,
# 
#     $$
#     y-y_{0}=m\left(x-x_{0}\right) \Longrightarrow y=y_{0}+m\left(x-x_{0}\right).
#     $$ 
# 
#     En este caso, $\left(x_{0},y_{0}\right)=\left(x_{0},f\left(x_{0}\right)\right)$, 
#     $m=f'\left(x_{0}\right)$. Y la recta tangente,
# 
#     $$
#     y=f\left(x_{0}\right)+f'\left(x_{0}\right)\left(x-x_{0}\right).
#     $$
# 
# ````
# 
# 

# ## Derivadas laterales
# 
# Ahora, como estamos definiendo la derivada como un límite, podemos hablar de derivada
# por la izquierda y derivada por la derecha.
# 
# ````{prf:definition} Derivadas laterales
# :label: def_derivadas_laterales
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. Definimos
# 
# * **derivada por la izquierda** de $f$ en $x_0$ como
# 
#     $$
#     f'(x_0^{-}):=\lim_{h\to 0^{-}}\frac{f(x_0+h)-f(x_0)}{h},
#     $$
# 
# * **derivada por la derecha** de $f$ en $x_0$ como
# 
# $$
# f'(x_0^{+}):=\lim_{h\to 0^{+}}\frac{f(x_0+h)-f(x_0)}{h}.
# $$
# 
# ````
# ````{prf:property} 
# :label: prop_derivadas_laterales
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. $f$ es derivable en $x_0$ si y sólo si es
# derivable por la izquierda y por la derecha en $x_0$ y ambas derivadas coinciden.
# ````
# 
# El **ejemplo** más típico de función no derivable es la
# función valor absoluto, que no es derivable en el $0$. Veámoslo, calculando sus
# derivadas parciales.  Recordemos que
# 
# $$
# |x|=\left\{\begin{array}{ll}
# -x &\quad \mbox{si }x<0, \\
# x &\quad\mbox{si }x\geq 0.
# \end{array}\right.
# $$
# 
# Entonces,
# 
# \begin{eqnarray*}
# &&f'\left(0^{-}\right)=\lim_{h\to 0^{-}}\frac{|h|-|0|}{h}=\lim_{h\to 0^{-}}\frac{-h}{h}=-1, \\
# &&f'\left(0^{+}\right)=\lim_{h\to 0^{+}}\frac{|h|-|0|}{h}=\lim_{h\to 0^{+}}\frac{h}{h}=1.
# \end{eqnarray*}
# 
# Entonces $f'\left(0^{-}\right)\not=f'\left(0^{+}\right)$, por lo que la función valor absoluto no es
# derivable en $0$. 
# 
# Gráficamente, podemos darnos cuenta de lo que pasa si recordamos la gráfica de la
# función valor absoluto: 
# 
# <img src="../../images/cap_deriv_valor_absoluto.png" width="400"/>
# 
# El punto $x=0$ es un punto anguloso para
# esta curva, es decir, un punto en el que la pendiente de la curva varía bruscamente.
# Pasa de ser $-1$ a la izquierda de $0$ a ser $1$ a su derecha. Al producirse esta
# variación brusca la función no puede ser derivable en el $0$.  
# 
# Aquí podéis ver **otro ejemplo** completo: 
# * https://existelimite.blogspot.com/2013/02/derivabilidad-de-una-funcion-definida.html.

# ## Propiedades de la derivación
# 
# Veamos ahora algunas propiedades importantes de la función derivada.
# 
# ````{prf:property}  
# :label: prop_derivable_continua
# :nonumber: 
# 
# Sea $f(a,b)\rightarrow\mathbb{R}$, $x_0\in\mathbb{R}$. Si $f$ es derivable en $x_0$, entonces $f$ es
# continua en $x_0$.
# ````
# 
# Esta propiedad se puede resumir en 
# 
# $$
# \mathrm{derivable}\,\Rightarrow\, \mathrm{continua}.
# $$
# 
# Conviene saber leerla correctamente. Según la relación lógica
# 
# $$
# \left[\textrm{a}\Rightarrow\textrm{b}\right]\Leftrightarrow\left[\textrm{no b}\Rightarrow\textrm{no a}\right],
# $$
# 
# esta propiedad es lo mismo que  
# 
# $$
# f  \mbox{ no continua en } x_0\Rightarrow f \mbox{ no derivable en }x_0. 
# $$
# 
# Ésta es la forma más habitual de aplicación. Si nos preguntan si determinada
# función es derivable en algún punto, lo primero que debemos hacer es comprobar si es
# continua. Si efectivamente lo es, debemos comprobar si se cumple la definición de
# derivada, pero si no es continua ya habremos acabado, porque en ese caso no podrá ser
# derivable.
# 
# ````{prf:property}  Derivadas elementales
# :label: prop_derivadas_elementales
# :nonumber: 
# 
# 1. $\displaystyle \dfrac{d}{dx} \left(x^{n}\right) = nx^{n-1}$,
# 2. $\displaystyle \dfrac{d}{dx} \left(\ln x\right) = \dfrac{1}{x}$, 
#    
#    $\displaystyle  \dfrac{d}{dx} \left(\log_{a}x\right) = \dfrac{1}{x}\log_{a} e$,
# 3. $\displaystyle \dfrac{d}{dx} \left(e^x\right) = e^x$,
#    
#     $\displaystyle \dfrac{d}{dx} \left(a^x\right) = a^x\ln a$,
# 4. $\displaystyle \dfrac{d}{dx} \left(\sin x\right) = \cos x$,
#    
#    $\displaystyle \dfrac{d}{dx} \left(\cos x\right) = -\sin x$,
# 5. $\displaystyle  \dfrac{d}{dx} \left(\tan x\right) = \dfrac{1}{\cos^2 x}$,
# 6. $\displaystyle \dfrac{d}{dx} \left(\arcsin x\right) = \dfrac{1}{\sqrt{1-x^2}}$, 
#    
#     $\displaystyle \dfrac{d}{dx} \left(\arccos x\right) = \dfrac{-1}{\sqrt{1-x^2}}$,
# 7.  $\displaystyle \dfrac{d}{dx} \left(\arctan x\right) = \dfrac{1}{1+x^2}$.
# 
# ````
# 
# ````{prf:property} Propiedades aritméticas de la derivada 
# :label: prop_aritmetica_derivada
# :nonumber: 
# 
# Sean $f,g:(a,b)\rightarrow\mathbb{R}$, dos funciones derivables en un punto $x_0\in(a,b)$. Entonces
# 
# 1. para cualquier $\lambda\in\mathbb{R}$, la función $\lambda f$ es derivable en $x_0$ y 
# 
#     $$
#     \left(\lambda f\right)'(x_0)=\lambda f'(x_0),
#     $$
# 
# 2. $f\pm g$ es derivable en $x_0$ y 
# 
#     $$
#     \left(f\pm g\right)'(x_0)=f'(x_0)\pm g'(x_0),
#     $$
# 
# 3. $fg$ es derivable en $x_0$ y 
# 
#     $$
#     \left(fg\right)'(x_0)=f'(x_0)g(x_0)+f(x_0)g'(x_0),
#     $$
# 
# 4. si $g(x_0)\not= 0$, entonces $\dfrac{f}{g}$ es derivable en $x_0$ y 
# 
#     $$
#     \left(\frac{f}{g}\right)'(x_0)=\frac{f'(x_0)g(x_0)-f(x_0)g'(x_0)}{g(x_0)^2}.
#     $$
# 
# ````
# 
# ````{prf:property} Regla de la cadena 
# :label: prop_regla_cadena
# :nonumber: 
# 
# Consideramos las funciones $f:(a,b)\rightarrow\mathbb{R}$, derivable en $x_0\in(a,b)$, y
# $g:f(a,b)\to\mathbb{R}$, derivable en $f(x_0)$. Entonces la función composición $g\circ f$ es
# derivable en $x_0$ y además
# 
# $$
# \left(g\circ f\right)'(x_0)=g'\left(f(x_0)\right)f'(x_0).
# $$
# 
# ````
# 
# Veamos algunos ejemplos de aplicación de estas reglas:
# 
# 1. Derivar $\ln\left(\cos x\right)$. 
# 
#     El resultado es
# 
#     $$
#     \left(\ln\left(\cos x\right)\right)'=\frac{1}{\cos x}\left(\cos x\right)'=\frac{-\sin x}{\cos x}.
#     $$
# 
#     Pensemos qué es lo que hemos hecho: 
#     
#     Estamos componiendo la función $f(x)=\cos x$ con
#     $g(x)=\ln x$. Esto es sencillo de comprobar, ya que
# 
#     $$
#     \left(g\circ f\right)(x)=g\left(f(x)\right)=g\left(\cos x\right)=\ln\left(\cos x\right).
#     $$  
# 
#     Entonces, según la regla de la cadena, $\left(g\circ f\right)'(x)=g'\left(f(x)\right)f'(x)$. 
#     
#     Ahora, $f'(x)=-\sin x$ y $g'(x)=\frac{1}{x}$, por lo que $g'(\cos x)=\frac{1}{\cos x}$, lo que
#     nos permite obtener el resultado anunciado.
# 
# 2. Veamos un ejemplo de aplicación un poco más complicado. 
# 
#     \begin{eqnarray*}
#     \left(\textrm{atan}\left(\frac{\sin x}{1+\cos x}\right)\right)'&=&\frac{1}{1+\frac{\sin^2 x}{\left(1+\cos
#     x\right)^2}} \frac{\left(\cos x\right)\left(1+\cos x\right)+\sin^2 x}{\left(1+\cos x\right)^2}=\\
#     &=&\frac{\cos x+\cos^2 x+\sin^2 x}{\left(1+\cos x\right)^2+\sin^2 x} 
#     =\frac{1+\cos x}{1+\cos^2 x+2\cos x+\sin^2 x}= \\
#     &=&\frac{1+\cos x}{2+2\cos x}=\frac{1}{2},
#     \end{eqnarray*}
# 
#     donde hemos utilizado en dos ocasiones que $\sin^2 x+\cos^2 x=1$.
# 
# 

# ## Derivación de algunos casos especiales.
# 
# ### Derivación de la función inversa.
# 
# Sea $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Supongamos que $f$ es derivable en $x_0$ y que $f(x_0)\not=0$. 
# Entonces $f^{-1}$, si existe, es derivable y
# 
# $$
# \left(f^{-1}\right)'\left(f(x_0)\right)=\frac{1}{f'(x_0)},
# $$
# 
# o, lo que es lo mismo, 
# 
# $$
# \left(f^{-1}\right)'\left(y_0\right)=\frac{1}{f'\left(f^{-1}(y_0)\right)}.
# $$ 
# 
# Destaquemos que estamos relacionando la derivada de la función inversa con $1$ partido
# por la derivada de la función inversa. Esto es bastante sorprendente, porque a estas
# alturas ya debemos saber que $f^{-1}\not=\frac{1}{f}$.
# 
# Veamos un **ejemplo**. Si consideramos la función $y=f(x)=\cos x$, la función
# inversa es el arco-coseno, $f^{-1}(y)=\arccos y$. Derivando directamente,
# 
# $$
# \left(f^{-1}\right)'(y)=\left(\arccos\, y\right)'=-\frac{1}{\sqrt{1-y^2}}.
# $$
# 
# Vamos a ver si esta expresión coincide con la que obtenemos aplicando la fórmula
# que expusimos al pincipio. En este caso
# 
# $$
# \left(f^{-1}\right)'\left(f(x)\right)=\frac{1}{f'(x)}=-\frac{1}{\sin x}=-\frac{1}{\sqrt{1-\cos^2
# x}}=-\frac{1}{\sqrt{1-y^2}},
# $$
# 
# donde, en la última igualdad, hemos utilizado la definición inicial de la función: $y= f(x)=\cos x$.
# 
# ### Derivación implícita
# 
# Una ecuación implícita es una ecuación de la forma
# 
# $$
# F(x,y)=0,
# $$ 
# 
# es decir, una ecuación donde $x$ e $y$ aparecen mezclados y donde no es posible
# (generalmente) separar la $y$ para llegar a una ecuación explícita,
# 
# $$
# y=f(x). 
# $$
# 
# Un ejemplo de ecuación implícita sería
# 
# $$
# \cos(xy)+xy^2=0.
# $$ 
# 
# Si a partir de una ecuación implícita queremos conocer el valor de la derivada de $y$
# respecto a $x$, $y'=\frac{dy}{dx},$ derivaremos término a término, utilizando las
# reglas habituales de derivación, pero teniendo en cuenta que en los términos donde
# aparezca $y$, o algo que dependa de $y$, al derivar aplicando la regla de la cadena
# obtendremos la correspondiente expresión multiplicada por $y'$. Esto no sucede si el
# término depende de $x$, ya que cuando derivamos respecto a $x$ aparecería la derivada
# de $x$ respecto a la misma $x$, $\frac{dx}{dx}$, que es $1$. Veamos algún ejemplo
# sencillo:
# 
# * $\displaystyle \left(x^3\right)'=3x^2\frac{dx}{dx}=3x^2$,
# * $\displaystyle \left(y^3\right)'=3y^2\frac{dy}{dx}=3y^2y'$,
# * $\displaystyle \left(cos(2y)\right)=-\sin(2y)2\frac{dy}{dx}=-2\sin(2y)y'$.
# 
# Entonces, en una derivada más complicada (utilizando la regla de derivación del
# producto),
# 
# \begin{eqnarray*}
# \cos(xy)+xy^2=0&\stackrel{\mathrm{derivando}}{\Rightarrow}
# &-\sin(xy)\left(y+xy'\right)+y^2+2xyy'=0 \\
# &\Rightarrow& y'\Big(2xy-x\sin(xy)\Big)=y\sin(xy)\Rightarrow
# y'=\frac{y\sin(xy)}{2xy-x\sin(xy)}.
# \end{eqnarray*}
# 
# Como podemos ver, el resultado final es el valor de $y'$ en función de $x$ y de $y$.
# Generalmente no es posible obtener el valor de $y'$ solamente en función de $x$.
# 
# Puedes mirar en los siguientes links, si quieres entender esto mejor:
# * https://es.wikipedia.org/wiki/Funci%C3%B3n_impl%C3%ADcita
# * https://www.fisicalab.com/apartado/derivacion-implicita
# * https://es.snapxam.com/calculators/calculadora-derivacion-implicita (¡Calculadora para derivar funciones implícitas! Si es que hay de todo en internet...)
# * https://es.khanacademy.org/math/ap-calculus-ab/ab-differentiation-2-new/ab-3-2/a/implicit-differentiation-review
# 
# ### Derivación logarítmica
# 
# Supongamos que tenemos una expresión del tipo
# 
# $$
# y=f(x)^{g(x)}
# $$
# y queremos derivarla. Como tenemos una función que depende de $x$ tanto en la base como
# en el exponente no lo podemos hacer directamente. Entonces aplicamos logaritmos y de la
# expresión anterior resulta
# 
# $$
# \ln y=\ln\left(f(x)^{g(x)}\right)\Rightarrow\ln y=g(x)\ln\left(f(x)\right),
# $$
# y ahora hacemos una derivación implícita para obtener
# 
# \begin{eqnarray*}
# &&\frac{1}{y}y'=g'(x)\ln\left(f(x)\right)+g(x)\frac{1}{f(x)}f'(x)\Rightarrow
# y'=y\left(g'(x)\ln\left(f(x)\right)+\frac{g(x)f'(x)}{f(x)}\right) \\
# &&\Rightarrow y'=f(x)^{g(x)}\left(g'(x)\ln\left(f(x)\right)+\frac{g(x)f'(x)}{f(x)}\right).
# \end{eqnarray*} 
# 
# Veámoslo sobre un **ejemplo**:
# 
# \begin{eqnarray*}
# y=\left(x^3-5\right)^{\sin x}&\stackrel{\mathrm{(logaritmos)}}{\Rightarrow}&\ln
# y=\sin(x)\ln\left(x^3-5\right) \\
# &\stackrel{\mathrm{(derivamos)}}{\Rightarrow}&\frac{1}{y}y'=\cos(x)\ln\left(x^3-5\right)+\frac{
# \sin(x)3x^2}{x^3-5} \\
# &\Rightarrow& y'=y\left(\cos(x)\ln\left(x^3-5\right)+\frac{\sin(x)3x^2}{x^3-5}\right) \\
# &\Rightarrow& y'=\left(x^3-5\right)^{\sin(x)}\left(\cos(x)\ln\left(x^3-5\right)+\frac{\sin(x)3x^2}{x^3-5}\right).
# \end{eqnarray*}
# 
# Aquí tienes más información y otros ejemplos:
#  * https://lasmatematicas.eu/derivacion-logaritmica/
#  * https://es.snapxam.com/calculators/calculadora-diferenciacion-logaritmica

# ## Regla de l'Hôpital
# 
# Nos queda todavía un punto que debemos resolver: 
# Cuando aplicamos las propiedades aritméticas de los límites nos podemos encontrar una *desagradable* sorpresa si alguna de las partes involucradas tiene como límite $+\infty$ o $-\infty$.
# Por ejemplo, si recordamos que $\displaystyle\lim_{x\to x_{0}} \left(f(x)+g(x)\right) = \lim_{x\to x_{0}} f(x) + \lim_{x\to x_{0}} g(x)$, si ahora suponemos que $\displaystyle\lim_{x\to x_{0}} f(x) = 4$, y $\displaystyle\lim_{x\to x_{0}} g(x) = + \infty$, ¿cómo sumamos $4$ y $+\infty$?
# 
# Hay algunas reglas que nos ayudan a hacer estas operaciones con límites que involucran + o -$\infty$ o, también, al $0$ (en ocasiones, a esto se llama **aritmética del infinito**). Puedes mirar aquí la tabla: http://asignaturas.topografia.upm.es/matematicas/primero/Apuntes/Funciones/Operaciones%20con%20limites%20infinitos.pdf, nosotros la resumimos a continuación:
# 
# ````{prf:property} Operaciones con límites infinitos
# :label: prop_aritmetica_infinito
# :nonumber: 
# 
# * Suma:
#   * $\lambda + \infty = +\infty$, $\forall \lambda\in\mathbb{R}$,
#   * $\lambda - \infty = -\infty$, $\forall \lambda\in\mathbb{R}$,
#   * $+\infty+\infty = +\infty$,
#   * $-\infty-\infty=-\infty$.
# * Multiplicación:
#   * $\lambda*\pm\infty=\pm\infty$, $\forall \lambda >0$,
# 
#       $\lambda*\pm\infty=\mp\infty$, $\forall \lambda <0$,
#   * $(+\infty)(+\infty) = (-\infty)(-\infty) = +\infty$, 
#     
#       $(+\infty)(-\infty) = (-\infty)(+\infty) = -\infty$. 
# * División:
#   * $\displaystyle\frac{\lambda}{\pm\infty} = 0$, $\forall \lambda\in\mathbb{R}$, $\lambda\neq 0$,
#   * $\displaystyle\frac{\lambda}{0^{+}} = +\infty$, $\displaystyle\frac{\lambda}{0^{-}} = -\infty$, $\forall \lambda > 0$,
#     
#     $\displaystyle\frac{\lambda}{0^{+}} = -\infty$, $\displaystyle\frac{\lambda}{0^{-}} = +\infty$, $\forall \lambda < 0$,
#   * $\displaystyle\frac{+\infty}{0^{+}}=+\infty$ (en otros casos, se aplica la regla de los signos),
#   * $\displaystyle\frac{0}{\pm\infty}=0$.
#   
#   [**Nota**: Diremos que $\displaystyle\lim_{x\to x_0} f(x) = 0^{+}$ si la función se acerca a $0$ por valores positivos, es decir, desde la derecha.]
# * Potencias:
#   * $\displaystyle 0^{+\infty} = 0$,
#   
#     $\displaystyle 0^{-\infty} = +\infty$,
#   * $\displaystyle\left(+\infty\right)^{+\infty} = +\infty$,
#   * $\displaystyle \left(+\infty\right)^{-\infty} = 0$,
#   * $\displaystyle \left(-\infty\right)^{+\infty} = \not\exists\,$.
# ````
# 
# En todo caso, volvemos a recordar que **no estamos operando con números reales y con símbolos**. 
# Al decir, por ejemplo, que $5 + \infty = +\infty$ lo que realmente queremos decir es que si sumamos una función que, en un punto determinado, tiene como límite $5$ con otra función que, en el mismo punto, tiene como límite $+\infty$, el resultado tendrá como límite $+\infty$.  
# 
# Sin embargo, hay algunas operaciones con límites infinitos que no siempre dan el mismo resultado. Son las llamadas **indeterminaciones**. A saber:
# 
# ````{prf:property} Indeterminaciones
# :label: prop_indeterminaciones
# :nonumber: 
# 
# * $\displaystyle \frac{0}{0} = $ INDETERMINADO,
# * $\displaystyle \frac{\pm\infty}{\pm\infty} = $ INDETERMINADO,
# * $\displaystyle 0\left(\pm\infty\right) = $ INDETERMINADO,
# * $+\infty - \infty  = $ INDETERMINADO,
# * $-\infty + \infty  = $ INDETERMINADO,
# *  $\displaystyle 1^{\pm\infty} = $ INDETERMINADO,
# * $\displaystyle 0^{0}  = $ INDETERMINADO,
# * $\displaystyle \left(\pm\infty\right)^{0}  = $ INDETERMINADO.
# ````
# 
# **¡Cuidado!** Cuando decimos *INDETERMINADO* no queremos decir que no exista el límite, si no que el resultado puede variar según los casos. 
# Por ejemplo, hay veces que al dividir una función que converja a $+\infty$ entre otra función que también converja a $+\infty$ el límite del cociente será $5$, 
# pero en otros casos ese cociente convergerá a $0$, o a $+\infty$, o a... 
# 
# Como no podemos dar un resultado *a priori* tendremos que estudiar caso a caso. ¿Cómo se hace eso? No siempre funciona, pero en muchos casos podemos echar mano de la **Regla de l'Hôpital**.
# 
# ````{prf:theorem} Regla de l Hôpital 
# :label: th_lhopital
# :nonumber: 
# 
# Sea $x_{0}\in\mathbb{R}$ y $f$ y $g$ funciones derivables en $\left(x_{0}-r, x_{0}\right)\cup\left(x_{0}, x_{0}+r\right)$. 
# 
# Si $\displaystyle \lim_{x\to x_{0}} f(x) = \displaystyle\lim_{x\to x_{0}} g(x) = 0$ y $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$ entonces 
# $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)}$ y 
# 
# $$
# \displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)} = \displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}.
# $$
# 
# ````
# 
# ````{prf:remark}  
# :label: rm_lhopital
# :nonumber:
# 
# * El recíproco no es cierto: $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)} \not\Rightarrow \exists\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$.
# * El enunciado del teorema también es válido si $\displaystyle \lim_{x\to x_{0}} f(x) = \pm\infty$ y  $\displaystyle\lim_{x\to x_{0}} g(x) = \pm \infty$ y/o $x_{0}=\pm\infty$.
# * Si en la expresión $\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$ se vuelve a producir una indeterminación del tipo $\frac{0}{0}$ o $\frac{\infty}{\infty}$ 
#   (y se cumplen el resto de hipótesis), se puede volver a aplicar l'Hôpital.
# * Las indeterminaciones $0\,\infty$, $+\infty-\infty$, $0^{0}$, $\infty^{0}$ o $1^{\infty}$ se pueden convertir en indeterminaciones resolubles con l'Hôpital.
# 
# ````
# 
# **Curiosidad histórica:** La hoy conocida como *Regla de l'Hôpital* debe su nombre a Guillaume de l´Hôpital, marqués de Saint Mesme, que fue un matemático aficionado del siglo XVII, 
# y que publicó el famoso teorema en un libro en 1696. 
# Sin embargo, el resultado realmente fue fruto del trabajo de Johann Bernoulli (hermano pequeño del más famoso Jacob Bernoulli, uno de los más grandes matemáticos de la historia), 
# quien trabajaba para dicho marqués y que vio como éste robaba su idea. Podéis ver más jugosos detalles de este salseo matemático aquí (cortito y en castellano, a ver si os animáis): 
# https://emis.univie.ac.at//journals/DM/v1/art7.pdf.  
