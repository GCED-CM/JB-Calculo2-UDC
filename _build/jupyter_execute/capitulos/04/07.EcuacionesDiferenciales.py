#!/usr/bin/env python
# coding: utf-8

# (sec:edos)=
# # Ecuaciones diferenciales
# 
# ## Primeras definiciones
# 
# ````{prf:definition} 
# :label: def_EDO 
# :nonumber: 
# 
# * Una **ecuación diferencial ordinaria** (E.D.O., o también O.D.E. por sus siglas en inglés *Ordinary Differential Equation*) es una ecuación en la que aparece una función incógnita, $y=y(x)$, y sus derivadas hasta un determinado orden. 
# * Se llama **orden** de una ecuación diferencial ordinaria al mayor índice de las derivadas que intervienen en la ecuación.
# ````
# Veamos algunos ejemplos sencillos, para entrar en calor:
# 
# * EDOs de orden 1:
#     * $y' = x^2 + 1$,
#     * $\log(xy')=e^{xy}$,
#     * $y^2 y' + x^2 y = 2$,
#     * $T' + T = cos(5t)$,
# * EDOs de orden 2: 
#     * $y''+5y'-6y = x^2 + 1$,
#     * $mx'' - sx' = g$. 
# 
# ````{prf:definition} 
# :label: def_variables_dep_indep 
# :nonumber: 
# 
# Dentro de una EDO distinguiremos dos tipos de variables:
# 
# * **Variable independiente**. Es aquélla que, dentro de la relación establecida, no depende de ninguna otra. Suele representarse mediante las letras $x$ o $t$ (aunque esto no es más que una convención).
# * **Variable dependiente**. Es aquélla cuyos valores dependen de los que asumen las variables independientes. Suele representarse con la letra $y$ o con la inicial, muchas veces en mayúscula, de la magnitud que representa ($a$ para la aceleración, $T$ para la temperatura,...). 
# ````
# 
# Fijémonos que, en una EDO con, por ejemplo, $x$ como variable independiente e $y$ como variable dependiente, cuando escribimos:
# 
# * $y$, queremos decir $y(x)$,
# * $y'$, queremos decir $\displaystyle \frac{dy}{dx}$, *etc.*.
# 
# 
# Una vez asentadas estas primeras definiciones, nos vamos a centrar ya, y en lo que sigue en estas notas, en las EDOs de orden 1. Fijamos a continuación la definición:
# 
# ````{prf:definition} Ecuación diferencial ordinaria de primer orden
# :label: def_EDO_orden_uno
# :nonumber: 
# Una ecuación diferencial ordinaria de primer orden es una ecuación diferencial que tiene la forma 
# 
# $$
# y'\,=\,f(x,y)\,,
# $$
# donde la incógnita es la función $y=y(x)$.
# ````
# 
# Casos particulares de la definición anterior son:
# 
# 1. Cuando $f=f(x)$. En este caso, el problema se puede resolver integrando con respecto a la variable independiente $x$: 
# 
# $$
# y(x)=\int f(x)\,dx\,.
# $$
# 
# 2. Cuando $f=f(y)$. En este caso, la EDO se llama **autónoma**. Es un caso muy frecuente en las aplicaciones. Veremos más adelante cómo resolver este tipo de ecuaciones y algunas más generales. 
# 
# ````{prf:definition} Solución de la EDO de primer orden
# :label: def_solucion_EDO 
# :nonumber: 
# 
# Se llama solución de la EDO de primer orden
# 
# $$
# y'=f(x,y)\,,\quad x\in (a,b)\,,
# $$
# a cualquier función $y=y(x)$ tal que $y'(x)=f(x,y(x))$, para $x\in(a,b)$.
# ````
# 
# Veamos un par de ejemplos sencillos: 
# 
# ````{prf:example} 
# :label: ex_EDO 
# :nonumber: 
# 
# 1. Para la siguiente EDO,
# 
#     $$
#     y'=5y\, ,
#     $$
#     la función $y(x)=e^{5x}$ es una solución, puesto que
# 
#     $$
#     y'(x)=5e^{5x}=5y(x)\,.
#     $$
#     Pero... ¡no es la única solución! Fíjate que $y_C(x)=e^{5x+C}$, para cualquier $C\in\mathbb R$, también es solución de la EDO anterior, puesto que
# 
#     $$
#     y'(x)=5e^{5x+C}=5y(x)\,.
#     $$
#     Es decir, la EDO dada tiene en realidad infinitas soluciones: para cada valor de la constante $C$, obtendremos una solución diferente de la EDO.
# 2. Las soluciones de la EDO,
# 
#     $$
#     y'=5x\, ,
#     $$
#     son $\displaystyle y(x) = \frac{5 x^2}{2} + C$.
# 
# ````
# 
# Como acabamos de ver, a través de estos ejemplos, al resolver una EDO de primer orden la solución va a depender de una constante arbitraria que podemos denotar $C$. Para determinar dicha constante, es necesario imponer alguna condición adicional. En física y otras ciencias, dicha condición suele describir el estado inicial del sistema, de ahí el nombre que aparece en la siguiente definición:
# 
# ````{prf:definition} 
# :label: def_CI_y_PI 
# :nonumber: 
# 
# * Una **condición inicial (c.i.)** es una condición adicional sobre la variable dependiente en una EDO:
# 
#     $$
#     y(x_0)=y_0\,.
#     $$
# 
# * Un **problema de valor inicial (P.V.I.)** es el problema que consiste en resolver una EDO junto con una condición inicial: 
# 
#     $$
#     \left\{\begin{array}{lcl}
#     y'&=&f(x,y)\,,\\
#     y(x_0)&=&y_0\,.
#     \end{array}\right.
#     $$
# ````
# 
# ````{prf:example} 
# :label: ex_PVI 
# :nonumber: 
# 
# 1. La única solución del problema de valor inicial
# 
#     $$
#     \left\{\begin{array}{lcl}
#     y'&=& 5y \,,\\
#     y(0)&=& 1 \,,
#     \end{array}\right.
#     $$
#     es $y(x) = e^{5x}$.
# 2. La única solución del problema de valor inicial
# 
#     $$
#     \left\{\begin{array}{lcl}
#     y'&=& 5x \,,\\
#     y(0)&=& 1 \,,
#     \end{array}\right.
#     $$
#     es $\displaystyle y(x) = \frac{5x^2}{2}+1$.
# ````
# 
# Un poco más adelante, en esta misma sección, veremos cómo resolver dos tipos especiales de ecuaciones diferenciales ordinarias de primer orden: las ecuaciones en variables separadas y las ecuaciones lineales de primer orden.

# ## Modelización matemática
# 
# #### Ley de enfriamiento de Newton
# 
# La ley de enfriamiento de Newton (https://es.wikipedia.org/wiki/Ley_del_enfriamiento_de_Newton) establece que cuando la diferencia de temperaturas entre un cuerpo y su medio ambiente no es demasiado grande, la variación en el tiempo de la temperatura del cuerpo es proporcional a la diferencia de la temperatura entre el cuerpo y el medio externo.
# 
# Podemos escribir matemáticamente esta idea como:
# 
# $$ 
# \frac{dT}{dt}\,=\,-k\, (T-T_a)\,,
# $$
# donde $T(t)$ es la temperatura en el instante de tiempo $t$, $T_a$ es la temperatura ambiente y $k>0$ es una constante de proporcionalidad (su valor se determina a partir de los datos del problema). Se trata de una ecuación diferencial ordinaria de primer orden o de orden uno.
# 
# En este caso, para poder determinar la temperatura del sistema de forma unívoca, necesitamos conocer la temperatura en algún instante de tiempo. 
# 
# Así, normalmente, este problema se complementa con una condición inicial: $T(0)=T_0$, donde $T_0$ es la temperatura inicial del cuerpo.
# 
# **Ejercicio propuesto:** 
# 
# 1. Comprobar que la solución general de la EDO 
# 
#     $$
#     \dfrac{dT}{dt}=-k(T-T_a)\,,
#     $$
#     está dada por $T_C(t)=T_a + C\,e^{-kt}$, $C\in\mathbb R$.
# 2. Comprobar que la solución del P.V.I.
# 
#     $$
#     \left\{\begin{array}{rcl}
#     T'&=&-k(T-T_a)\,,\\
#     T(0)&=&T_0\,,
#     \end{array}\right.
#     $$
#     está dada por $T(t)=T_a+(T_0-T_a)e^{-kt}$.
# 
# ### Desintegración radiactica
# 
# Según ChatGPT, *un material radiactivo se desintegra porque tiene núcleos instables de átomos. Estos núcleos emiten partículas y radiación como parte de un proceso conocido como desintegración nuclear. La desintegración nuclear puede ser espontánea, es decir, que ocurre de manera natural, o puede ser provocada por factores externos como la exposición a ciertas formas de energía. La velocidad a la que un material radiactivo se desintegra depende de su propia estructura atómica y de las condiciones externas en las que se encuentra.* 
# 
# Y seguimos preguntándole a ChatGPT por la **ley de desintegración radiactiva** para obtener lo siguiente: *La ley de desintegración radiactiva es una ley científica que describe cómo los núcleos de ciertos elementos radiactivos se desintegran espontáneamente con el tiempo. Según esta ley, la tasa de desintegración de un núcleo radiactivo es proporcional a la cantidad de núcleos presentes en un determinado momento. Esto significa que, si tenemos una cantidad fija de un elemento radiactivo, la tasa a la que se desintegrarán sus núcleos será constante y no cambiará con el tiempo. Esta ley es importante en diversas áreas, como la medicina, la industria y la energía nuclear.*
# 
# Es decir, la velocidad de desintegración depende del número de núcleos y, por tanto, de la cantidad de material presente. Podéis consultar esta ley en la Wikipedia: https://es.wikipedia.org/wiki/Radiactividad. 
# 
# ¡Vamos a enunciar esto con una EDO!
# 
# Llamaremos $N(t)$ al número de núcleos radiactivos en el instante $t$. La ley de desintegración radiactiva dice: *la tasa a la que se desintegrarán sus núcleos será constante y no cambiará con el tiempo*. Como esta tasa es la variación en el número de núcleos, es decir, la derivada de $N$ en función del tiempo, podemos escribir la ecuación diferencial que rige el proceso:
# 
# $$
# \frac{dN}{dt} = -kN \Leftrightarrow N' = -k N.
# $$
# 
# Si conocemos la cantidad inicial de material, $N_{0}$, ya tendremos un problema de valor inicial con el que podremos trabajar:
# 
# $$
# \left\{\begin{array}{lcl}
# \displaystyle\frac{dN}{dt} &=& -kN \\
# N(0) &=& N_{0}
# \end{array} \right.
# $$
# 
# **Ejercicio propuesto:** 
# 
# Comprueba que el tiempo de semidesintegración radiactiva (es decir, el tiempo necesario para que se desintegre la mitad del material inicialmente presente) es
# 
# $$
# t_{0} = \frac{\ln 2}{k}.
# $$
# 
# ### Segunda ley de Newton
# 
# La segunda ley de Newton (también conocida como *principio fundamental de la dinámica*) establece que la aceleración de una partícula es directamente proporcional a la fuerza $F$ que se ejerce sobre ella e inversamente proporcional a su masa $m$, esto es,
# 
# $$
# F=m\,a\,.
# $$
# Como, por definición, 
# 
# $$
# a(t)=x''(t)\,,
# $$
# donde $t$ denota el tiempo y $x(t)$ representa el desplazamiento en el instante $t$, podemos expresar la segunda ley de Newton como sigue:
# 
# $$
# F=m\,x''\,,
# $$
# que no es otra cosa que una ecuación diferencial ordinaria de orden dos para la función desplazamiento: $x=x(t)$.
# 
# ### Caída de un cuerpo en un medio resistente
# 
# Si dejamos caer un cuerpo en un medio con rozamiento, y suponemos, de manera simplificada, que las únicas fuerzas que afectan a ese cuerpo son la de la gravedad y la de fricción, obtenemos el siguiente sistema de fuerzas, en la que consideramos positiva la dirección descendente:
# 
# $$
# F_{\text{total}} = mg - F_{\text{fricción}},
# $$
# donde $m$ es la masa del objeto que cae y $g$ la constante gravitatoria universal (aproximadamente igual a $9.81$).
# 
# Ahora, por un lado pensemos que, según la segunda ley de Newton, $F_{\text{total}} = ma$, y, por otro lado, vamos a aceptar la hipótesis habitual de que la fuerza de fricción es opuesta al movimiento y depende de manera directamente proporcional de la velocidad del móvil,  $F_{\text{fricción}} = kv$.
# 
# Nos quedará la siguiente ecuación, que podemos escribir como una EDO de orden 1 en función de la velocidad del móvil:
# 
# $$
# ma = mg - kv \Leftrightarrow mv' = mg - kv.
# $$
# 
# **Nota:** También podríamos escribir este problema como una EDO de orden dos en función de la distancia recorrida por el objeto que cae:
# 
# $$
# mx'' = mg - kx' \, .
# $$

# ## Uso de `Sympy` para resolver EDOs
# 
# A continuación mostramos cómo se puede utilizar `Sympy` en la resolución de EDOs. 
# 
# Realmente, es muy sencillo. 
# 
# 1. Las variables independientes se definen como símbolos (`sp.Symbol`), mientras que las variables dependientes se definen como funciones (`sp.Function`).  
# 2. Definimos la EDO con el comando `sp.Eq`, destacando la dependencia de la variable dependiente de la independiente. En el siguiente ejemplo, puedes ver cómo en la línea 7 escribimos `v(x)' cada vez que aparece la variable dependiente $v$.
# 3. Las derivadas se escriben, dentro de la definición `sp.Eq` indicando la variable dependiente y la variable dependiente respecto a la que se derivan. En el ejemplo que aparece a continuación, escribimos $v'$ como `v(x).diff(x)`.
# 4. Una vez definida la EDO, la resolvemos con el comando `sp.dsolve`.
# 5. Podemos usar `sp.dsolve` sin más atributos para encontrar la solución general, o podemos incluir una condición inicial, que debemos definir como `ics`, como se puede ver en la penúltima línea del siguiente código.
# 
# Como ejemplo, vamos a calcular la velocidad de un cuerpo con masa $72$ kilogramos, si suponemos que su velocidad inicial es nula y su coeficiente de resistencia al aire es $k=0.2$. 
# 
# Es decir, en función de lo que vimos en la sección anterior, vamos a resolver el problema de valor inicial
# 
# $$
#     \left\{\begin{array}{rcl}
#     72 v'&=& 72*9.81 - 0.2 v\,,\\
#     v(0) &=& 0\,,
#     \end{array}\right.
# $$

# In[8]:


import sympy as sp

# Variable independiente
x = sp.Symbol ('x')
# Variable dependiente (definida como Function)
v = sp.Function ('v')

# Escribimos la EDO 
eq = sp.Eq (72*v(x).diff(x), 72*9.81 - 0.2*v(x))

# Calculamos su solución general (este paso no sería necesario, pero queda como ejemplo)
s_general = sp.dsolve (eq)   
display (s_general)

# Calculamos la solución particular que nos preguntan
s_particular = sp.dsolve (eq, ics={v(0): 0.0}) 
display (s_particular)


# ## EDOs en variables separadas
# 
# ````{prf:definition} Ecuación diferencial en variables separadas 
# :label: def_EDO_separable
# :nonumber: 
# 
# Se dice que la ecuación diferencial
# 
# $$
# y'\,=\,f(x,y) \,\,\Leftrightarrow\,\, \frac{dy}{dx}\,=\,f(x,y)
# $$
# es **separable** o en **variables separadas** si $f$ es de la forma:
# 
# $$
# f(x,y)\,=\,g(x)\,h(y)\,,
# $$
# para ciertas funciones $g$ y $h$.
# ````
# 
# Para resolver una EDO de variables separadas, *separamos* las variables e integramos:
# 
# $$
# \displaystyle
# \frac{dy}{dx}\,=\,g(x)\, h(y) \Rightarrow 
# \displaystyle
# \frac{1}{h(y)}\, dy\,=\, g(x)\, dx
#  \Rightarrow 
# \displaystyle
# \int \frac{1}{h(y)} dy\,=\, \int g(x) dx
# $$ 
# 
# ````{prf:example} 
# :label: ex_EDO_separable
# :nonumber: 
# 
# La EDO $y'=5y$ es autónoma, un caso particular de EDO en variables separadas. Para resolverla, separamos las variables e integramos:
# 
# $$
# \dfrac{dy}{dx}=5y \Rightarrow \dfrac{1}{y}\,dy = 5\,dx\Rightarrow \int\dfrac{1}{y}\,dy =\int 5\,dx\Rightarrow \ln|y|=5x+C\,,
# $$
# donde en el primer paso hemos supuesto que $y\neq 0$.
# Ahora, despejamos $y$ en función de $x$:
# 
# $$
# \ln|y(x)|=5x+C \Rightarrow |y(x)|=e^{5x+C}, \text{ con } C\in\mathbb R. 
# $$
# Notamos que 
# 
# $$
# e^{5x+C}=e^{5x}e^{C}=C'e^{5x}\,,
# $$
# donde $C'=e^C>0$. Entonces, eliminando el valor absoluto, tenemos que:
# 
# $$
# y(x)=Ce^{5x}, \text{ con } C\neq 0\,.
# $$
# 
# Notamos que para $C=0$ también obtenemos una solución de la EDO de partida: la solución $y= 0$, que habíamos eliminado al dividir por $y$ en el primer paso. Esta solución recibe el nombre de **solución singular**. 
# Las soluciones de la EDO son, por tanto, todas las funciones de la forma:
# 
# $$
# y(x)=Ce^{5x}\,,\quad C\in\mathbb R\,.
# $$
# La expresión anterior se denomina la **solución general** de la EDO. Para cada valor de $C$, obtenemos una **solución particular**.
# ````
# 
# ````{prf:example} 
# :label: ex_EDO_separable_2
# :nonumber: 
# 
# Queremos ahora resolver ahora el problema de valor inicial
# 
# $$
# \left\{\begin{array}{rcl}
# y'&=&5y\,,\\
# y(0)&=&3\,.
# \end{array}\right.
# $$
# Ya hemos obtenido la solución general de la EDO: 
# 
# $$
# y(x)=Ce^{5x}\,,\quad C\in\mathbb R\,.
# $$ 
# Entonces, simplemente imponemos la condición inicial, $y(0)=3$. De la expresión de la solución general:
# 
# $$
# y(0)=Ce^{0}=C\,.
# $$
# Luego para que $y(x)=Ce^{5x}$ sea solución del P.V.I. propuesto, $C$ debe ser necesariamente igual a $3$. La solución del P.V.I. es $y(x)=3e^{5x}$.
# ````
# 
# ````{prf:example} 
# :label: ex_EDO_separable_3
# :nonumber: 
# 
# Se desea determinar la temperatura de un cuerpo sabiendo que inicialmente se encuentra a $10ºC$, que al cabo de $2$ horas se encuentra a $15ºC$ y la temperatura exterior es constante e igual a $25ºC$. Para ello, se resuelve el P.V.I. siguiente:
# 
# $$
# \left\{\begin{array}{rcl}
# T'&=&-k(T-25)\,,\\[1ex]
# T(0)&=&10\,.
# \end{array}\right.
# $$
# Comenzamos resolviendo la EDO, que es autónoma, y por tanto, de variables separadas. Para ello, separamos las variables e integramos:
# 
# $$
# \dfrac{dT}{dt}=-k(T-25)\Rightarrow \dfrac{1}{T-25}\,dT=-k\,dt\Rightarrow \int\dfrac{1}{T-25}\,dT=-k\,\int dt\,.
# $$
# Resolviendo las integrales, queda que:
# 
# $$
# \ln|T-25|=-kt+C \Rightarrow |T-25|=e^{-kt+C}=C'e^{-kt}\,,\quad\text{ con }C'>0\,.
# $$
# Entonces,  
# 
# $$
# T(t)-25 = Ce^{-kt}\,,\quad\text{ con }C\neq 0.
# $$
# Notamos que para $C=0$ tenemos también una solución de la EDO: la solución constante $T(t)=25$, que habíamos eliminado en el primer paso, al dividir por $T-25$. En cualquier caso, ésta no es una solución de nuestro P.V.I.
# 
# Para determinar la solución del P.V.I., imponemos la condición inicial $T(0)=10$:
# 
# $$
# 10-25 = Ce^{0}=C\Rightarrow C=-15\,.
# $$
# Luego, la solución del P.V.I. planteado está dada por 
# 
# $$
# T(t)=25-15e^{-kt}\,,\quad t\ge 0.
# $$
# 
# Como además sabemos que al cabo de $2$ horas, el cuerpo está a una temperatura de $15ºC$, podemos determinar con este dato el valor de la constante $k$. Poniendo $t=2$, 
# 
# $$
# 15=25-15e^{-2k}\Rightarrow 15e^{-2k}=10 \Rightarrow e^{-2k}=\dfrac{2}{3}\Rightarrow -2k=\ln\Big(\dfrac{2}{3}\Big)\,,
# $$
# luego
# 
# $$
# k=-\dfrac{1}{2}\ln\Big(\dfrac{2}{3}\Big)\quad\text{ y }\quad T(t)=25-15\Big(\dfrac{2}{3}\Big)^{t/2}\,,\quad t\ge 0. 
# $$
# ````
# 
# ````{prf:example} 
# :label: ex_EDO_separable_4
# :nonumber: 
# 
# Veamos, por último, una EDO en variables separadas que no es autónoma.
# 
# Consideramos la EDO de primer orden
# 
# $$
# xy'=1+y^2\,.
# $$
# Esta EDO se puede escribir de forma equivalente como
# 
# $$
# \dfrac{dy}{dx}=\dfrac{1+y^2}{x}=\dfrac{1}{x}(1+y^2)\,.
# $$
# Se trata, por tanto, de una EDO en variables separadas ($g(x)=\frac{1}{x}$ y $h(y)=1+y^2$). Para resolverla, separamos las variables e integramos:
# 
# $$
# \dfrac{1}{1+y^2}\,dy = \dfrac{1}{x}\,dx\Rightarrow \arctan(y) = \ln|x|+C\,.
# $$
# Despejando, 
# 
# $$
# y(x)=\tan(\ln|x|+C)\,.
# $$
# ````
# 
# **Nota:** Fíjate que en los ejemplos anteriores, siempre es posible comprobar si hemos obtenido la solución correcta... y, si no, podemos usar `Sympy`. Veámosolo, por ejemplo, sobre el último ejemplo:

# In[6]:


import sympy as sp

x = sp.symbols ('x')
y = sp.Function ('y')

# Escribimos la EDO 
eq = sp.Eq (x*y(x).diff(x), 1+ y(x)**2)

# Calculamos su solución general (este paso no sería necesario, pero así completamos el ejercicio)
s_general = sp.dsolve (eq)   
display (s_general)


# ## EDOs lineales de primer orden
# 
# ````{prf:definition} Ecuación diferencial lineal de primer orden 
# :label: def_EDO_lineal
# :nonumber: 
# 
# Una ecuación diferencial lineal de primer orden es una EDO de la forma
# 
# $$
# y'\,+\,p(x)\,y\,=\,q(x)\,,
# $$
# donde $p$ y $q$ son funciones de $x$.
# ````
# 
# Veremos a continuación cómo resolver este tipo de EDOs. 
# 
# Si fuésemos capaces de encontrar una función $\mu(x)$ tal que
# 
# $$
# \mu(x)\,(y'(x)\,+\,p(x)\,y(x))\,=\,(\mu(x)\,y(x))',
# $$ (eq-mu)
# entonces, multiplicando toda la EDO lineal del principio por $\mu(x)$ tendríamos:
# 
# $$
# \mu(x)\left(y'\,+\,p(x)\,y\right) = \mu(x) q(x) \Rightarrow (\mu(x)\,y(x))' = \mu(x) q(x),
# $$
# de donde, integrando, 
# 
# $$
# \mu(x)y(x)=\int\mu(x)q(x)\,dx \Rightarrow y(x) = \frac{\int\mu(x)q(x)\,dx}{\mu(x)},
# $$
# y ya tendríamos el problema resuelto.
# 
# Entonces, el problema se reduce a calcular una función $\mu$ que verifique {eq}`eq-mu`.
# 
# No vamos a detallarlo, pero no es difícil comprobar que esto se cumple si elegimos 
# 
# $$
# \mu(x) = \exp\left({\int p(x)\, dx}\right).
# $$
# La función $\mu$ recibe el nombre de **factor integrante**.
# 
# ````{prf:example} 
# :label: ex_EDO_lineal
# :nonumber: 
# 
# La EDO $y'=5y$, que ya resolvimos en la sección anterior, también se puede considerar una EDO lineal de primer orden. 
# 
# En este caso, $p(x)=-5$ y $q(x)=0$ (¡OJO! para hacer esta identificación, el coeficiente de $y'$ debe ser igual a $1$). Podemos, por tanto, resolver esta EDO por el método que acabamos de describir. 
# 
# Como $p(x)=-5$, el factor integrante será 
# 
# $$
# \mu(x)=e^{-5x}.
# $$ 
# Entonces:
# 
# $$
# y'-5y = 0 \Rightarrow e^{-5x}y' - e^{-5x}y = 0 \Rightarrow \left( e^{-5x}y \right)' = 0 \\
# \Rightarrow e^{-5x} y = C.
# $$
# Entonces, 
# 
# $$
# y(x)=C(e^{-5x})^{-1}=Ce^{5x}\,.
# $$
# Por supuesto, hemos obtenido la misma solución que antes. 
# ````
# 
# ````{prf:example} 
# :label: ex_EDO_separable_2
# :nonumber: 
# 
# Consideramos el problema de valor inicial 
# 
# $$
# \left\{\begin{array}{rcl}
# y'+y&=&\sin(x)\,,\\[1ex]
# y(0)&=&2\,.
# \end{array}\right.
# $$
# La EDO es lineal de primer orden, con $p(x)=1$ y $q(x)=\sin(x)$. 
# 
# Para resolver la EDO, calculamos en primer lugar el factor integrante:
# 
# $$
# \mu(x)=e^{\int 1\,dx}=e^{x}\,.
# $$
# Entonces, multiplicando toda la EDO por $\mu(x)$,
# 
# $$
# y'+y=\sin(x) \Rightarrow e^{x}y'+e^{x}y = e^{x}\sin(x) \Rightarrow \left( e^{x}y \right)' = e^{x}\sin(x)
# \Rightarrow e^{x} y = \int e^{x}\sin(x)dx.
# $$
# 
# Hacemos esta integral utilizando la integración por partes para obtener
# 
# $$
# e^{x} y= \frac{e^x}{2}\left(\sin(x)-\cos(x)\right)+C \Rightarrow y = \dfrac{\sin(x)-\cos(x)}{2}+Ce^{-x} .
# $$
# 
# Acabamos de obtener la solución general de la EDO lineal de primer orden. Queda determinar la solución particular del P.V.I., es decir, el valor de la constante $C$ tal que $y(0)=2$. Imponiendo esta condición inicial, tenemos que:
# 
# $$
# 2=\dfrac{\sin(0)-\cos(0)}{2}+Ce^0=-\dfrac{1}{2}+C\Rightarrow C=\dfrac{5}{2}\,.
# $$
# Por tanto, la solución del P.V.I. propuesto es 
# 
# $$
# y(x)=\frac{1}{2}\left( \sin(x)-\cos(x)+5e^{-x}\right).
# $$
# ````
# 
# Veamos a continuación cómo resolver este último problema aprovechando la potencia de `Sympy`:

# In[5]:


import sympy as sp

x = sp.symbols ('x')
y = sp.Function ('y')

# Escribimos la EDO 
eq = sp.Eq (y(x).diff(x) + y(x), sp.sin(x))

# Resolvemos su solución general (realmente este paso no sería necesario, pero así completamos el ejercicio)
s_general = sp.dsolve (eq)   
display (s_general)

# Calculamos la solución particular que nos preguntan
s_particular = sp.dsolve (eq, ics={y(0): 2.0}) 
display (s_particular)


# ## Referencias
# 
# Para saber más, puedes consultar, por ejemplo, los siguientes enlaces:
# * https://totumat.com/2020/09/16/ecuaciones-diferenciales-ordinarias-de-variables-separables/
# * https://www.ecuacionesdiferenciales.jcbmat.com/id225.htm
# * https://existelimite.blogspot.com/search/label/EDOs
# 
