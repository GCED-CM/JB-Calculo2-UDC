#!/usr/bin/env python
# coding: utf-8

# (sec:integral_indefinida)=
# # La integral indefinida
# 
# ## Definición de primitiva
# 
# La primitiva de una función es la expresión que se obtiene mediante el proceso opuesto a la derivación. De aquí que la primitiva también se conozca con el nombre de antiderivada. Realmente, una función no tiene una única primitiva, sino que una familia de funciones. Veámoslo con un ejemplo.
# 
# Si tenemos la función $f(x)=x^2$ sabemos que su derivada se obtiene en dos pasos, i) se multiplica la función por el exponente y ii) se disminuye el exponente en una unidad, esto es, $f'(x)=2x$. Entonces, para calcular la primitiva de $f$ procedemos en sentido opuesto, i) se aumenta el exponente en una unidad y ii) se divide por el exponente (nuevo al hacer el paso i)). De este modo obtenemos que $F(x) = \dfrac{x^3}{3}$, podemos comprobar que al aplicar la derivada a $F$ obtenemos nuestra función inicial $f$. 
# 
# Tal y como hemos mencionado, la primitiva no es única, de este modo le podemos añadir cualquier constante a $F(x)$ y su derivada seguirá siendo la función de inicio $f$ (la derivada de una constante era 0). Entonces, para este caso, la familia de primitivas estaría dada por $F(x) = \dfrac{x^3}{3} +C$, donde $C$ es una constante cualesquiera.
# 
# Veamos pues, las definiciones formales de primitiva.
# 
# 
# ````{prf:definition} Primitiva
# :label: def_primitiva 
# :nonumber: 
# Sea $f:I\rightarrow \mathbb{R}$. Se dice que F es una primitiva de $f$ en $I$ si
# 
# $$ F'(x) = f(x), \quad \forall x \in I.$$
# ````
# 
# ````{prf:theorem} 
# :label: th_primitivas
# Si $F$ y $G$ son dos primitivas de una misma función $f$ en un intervalo $I$, entonces,
# 
# $$ \exists k \in \mathbb{R} \mbox{ tal que } F(x)=G(x)+k, \quad \forall x \in I.$$
# ````
# 
# Como consecuencia del anterior teorema, una vez conocida una primitiva $F$ de $f$, ya se pueden obtener todas al sumar únicamente una constante a la primitiva ya conocida.
# ## Definición de primitiva
# 
# La primitiva de una función es la expresión que se obtiene mediante el proceso opuesto a la derivación. De aquí que la primitiva también se conozca con el nombre de antiderivada. Realmente, una función no tiene una única primitiva, sino que una familia de funciones. Veámoslo con un ejemplo.
# 
# Si tenemos la función $f(x)=x^2$ sabemos que su derivada se obtiene en dos pasos, i) se multiplica la función por el exponente y ii) se disminuye el exponente en una unidad, esto es, $f'(x)=2x$. Entonces, para calcular la primitiva de $f$ procedemos en sentido opuesto, i) se aumenta el exponente en una unidad y ii) se divide por el exponente (nuevo al hacer el paso i)). De este modo obtenemos que $F(x) = \dfrac{x^3}{3}$, podemos comprobar que al aplicar la derivada a $F$ obtenemos nuestra función inicial $f$. 
# 
# Tal y como hemos mencionado, la primitiva no es única, de este modo le podemos añadir cualquier constante a $F(x)$ y su derivada seguirá siendo la función de inicio $f$ (la derivada de una constante era 0). Entonces, para este caso, la familia de primitivas estaría dada por $F(x) = \dfrac{x^3}{3} +C$, donde $C$ es una constante cualesquiera.
# 
# Veamos pues, las definiciones formales de primitiva.
# 
# 
# ````{prf:definition} Primitiva
# :label: def_primitiva 
# :nonumber: 
# Sea $f:I\rightarrow \mathbb{R}$. Se dice que F es una primitiva de $f$ en $I$ si
# 
# $$ F'(x) = f(x), \quad \forall x \in I.$$
# ````
# 
# ````{prf:theorem} 
# :label: th_primitivas
# Si $F$ y $G$ son dos primitivas de una misma función $f$ en un intervalo $I$, entonces,
# 
# $$ \exists k \in \mathbb{R} \mbox{ tal que } F(x)=G(x)+k, \quad \forall x \in I.$$
# ````
# 
# Como consecuencia del anterior teorema, una vez conocida una primitiva $F$ de $f$, ya se pueden obtener todas al sumar únicamente una constante a la primitiva ya conocida.

# ## Definición de la integral indefinida
# La integración indefinida es el proceso por el cual se obtienen las primitivas de una función. La notación más habitual para denotar a la integral indefinida de la función $f$ es $\int f(x) \mathrm{d}x$, que es la que utilizamos para su definición.
# 
# ````{prf:definition} Integral indefinida
# :label: def_primitiva 
# :nonumber: 
# 
# Dada una función $f:I\rightarrow \mathbb{R}$, se llama integral indefinida de $f$ al conjunto de todas las primitivas de $f$, y se escribe
# 
# $$\int f(x)\, \mathrm{d}x = \{ F : F'(x)=f(x), \quad \forall x \in I\}.$$
# ````
# 
# Utilizando el {prf:ref}`th_primitivas`, es inmediato deducir que si conocemos una primitiva $F$ de $f$, su integral indefinida será
# 
# $$\int f(x) \, \mathrm{d}x = \{ F(x) +k, \quad \forall k \in \mathbb{R}\}.$$
# 
# Entre las propiedades de la integral está la linealidad, es decir:
# 
# ````{prf:property} Linealidad de la integración indefinida
# :label: prop_linealidad_int_indef 
# :nonumber: 
# Sean las funciones $f:I\rightarrow \mathbb{R}$ y $g:I\rightarrow \mathbb{R}$ entonces se verifica 
# 
# * $\displaystyle\int \left( f(x)+ g(x)\right) \, \mathrm{d}x = \int f(x) \, \mathrm{d}x + \int g(x) \, \mathrm{d}x$,
# * $\displaystyle\int \alpha f(x) \, \mathrm{d}x  = \alpha \int f(x) \, \mathrm{d}x, \quad \forall \alpha \in \mathbb{R}$.
# ````
# 
# Veamos ahora cuáles son algunas integrales inmediatas.
# 
# ````{prf:property} Integrales inmediatas
# :label: prop_integrales_inmediatas 
# :nonumber: 
# 
# * $\displaystyle\int x^m \, \mathrm{d}x = \dfrac{1}{m+1}x^{m+1} + C, \quad m \neq -1$,
# * $\displaystyle \int \dfrac{1}{x} \, \mathrm{d}x = \ln|x| + C$,
# * $\displaystyle \int e^x \, \mathrm{d}x = e^x + C; \quad \int a^x \, \mathrm{d}x = \dfrac{a^x}{\ln a} + C, \quad a>0, a\neq1$,
# * $\displaystyle \int \sin(x) \, \mathrm{d}x = -\cos(x) + C; \quad \int \cos(x) \, \mathrm{d}x = \sin(x) + C$,
# * $\displaystyle \int \dfrac{1}{\cos^2(x)} \, \mathrm{d}x = \tan(x) + C$,
# * $\displaystyle \int \dfrac{1}{1+x^2} \, \mathrm{d}x = \arctan(x) + C$,
# * $\displaystyle \int \dfrac{1}{\sqrt{1-x^2}} \, \mathrm{d}x = \arcsin(x) + C$.
# ````
# 
# ¿Te apetece practicar un poco con las llamadas *integrales inmediatas*? Aquí puedes hacerlo: 
# * https://www.matesfacil.com/ejercicios-resueltos-integrales-inmediatas.htm
# * https://thales.cica.es/rd/Recursos/rd97/Problemas/54-1-p-INM.HTML

# ## Principales métodos para obtener las integrales indefinidas
# Los métodos más comunes para obtener la integral indefinida de una función son la integración por partes, la integración por cambio de variable y la integración por descomposición de fracciones racionales.
# 
# ### Integración por partes
# La integración por partes se utiliza para hallar de forma más sencilla la integral de algunas funciones $f$ que son producto de otras dos. Veamos el enunciado de este método.
# 
# ````{prf:property} Integración por partes para la integral indefinida
# :label: prop_integracion_ind_partes 
# :nonumber: 
# Si $u'$ y $v'$ son funciones continuas, se verifica que
# 
# $$ \int u(x)v'(x) \, \mathrm{d}x = (uv)(x) - \int v(x)u'(x)\, \mathrm{d}x,  $$
# o bien
# 
# $$ \int u dv = uv - \int v du.  $$
# ````
# 
# Es conveniente utilizar este método para los productos de:
# * polinomio (actúa como $u$) contra exponencial (actúa como $dv$), 
# * polinomio ($u$) contra seno o coseno ($dv$),
# * inversa de trigonométrica o logarítmica ($u$) contra polinomio ($dv$),
# * exponencial ($u$ o $dv$) contra seno o coseno ($dv$ o $u$).
# 
# Veamos un ejemplo para aplicar el método de integración por partes.
# 
# ````{prf:example} 
# :label: ex_indefinida_partes 
# :nonumber: 
# 
# Calcular la integral indefinida $\int xe^{x-1} \,\mathrm{d}x$.
# 
# Debemos tener en cuenta que queremos simplificar el integrando de forma que la nueva integral a calcular sea directa o al menos más sencilla que la inicial. Entonces nos interesará considerar $u=x$ y $dv=e^{x-1}dx$, donde tras derivar e integrar obtenemos $du = dx$ y $v=e^{x-1}$, respectivamente. De este modo
# 
# $$ \int xe^{x-1} \,\mathrm{d}x = xe^{x-1} - \int e^{x-1} dx,  $$
# 
# donde la integral que nos queda por calcular ya es directa
# 
# $$ \int xe^{x-1} \,\mathrm{d}x = xe^{x-1} -  e^{x-1} + C = (x-1)e^{x-1} + C.  $$
# ````
# 
# Veamos algún ejemplo más donde podemos utilizar este método.
# 
# ````{prf:example} 
# :label: ex_indefinida_partes_2
# :nonumber: 
# 
# Obtén las siguientes integrales indefinidas:
# 
# * a) $\int e^x \sin(x) \,\mathrm{d}x$ 
# 
#     Para este caso consideramos $u=\sin(x)$ y $dv=e^x dx$. Por tanto $ du = \cos(x)$ y $v = e^x$ y al aplicar la integración por partes obtenemos
# 
#     $$ \int e^x \sin(x) \,\mathrm{d}x = e^x \sin(x) - \int e^{x} \cos(x) dx.  $$
# 
#     Ahora debemos volver a utilizar la integración por partes para resolver la nueva integral que aparece en el lado derecho. Tomamos $u=\cos(x)$ y $dv=e^x dx$ de donde $ du = -\sin(x)$ y $v = e^x$ y por tanto
# 
#     \begin{eqnarray*}
#     \int e^x \sin(x) \,\mathrm{d}x &=& e^x \sin(x) - \int e^{x} \cos(x) dx \\
#     &=& e^x\sin(x) -e^x\cos(x) - \int e^{x} \sin(x) dx. 
#     \end{eqnarray*}
# 
#     Al aplicar por segunda vez la integración por partes hemos obtenido la misma integral que teníamos al inicio por lo que podemos obtener su valor despejándola de la igualdad anterior
# 
#     $$ 2\int e^x \sin(x) \,\mathrm{d}x = e^x\sin(x) -e^x\cos(x).$$
# 
#     Por tanto obtenemos
# 
# 
#     $$ \int e^x \sin(x) \,\mathrm{d}x = \dfrac{ e^x}{2}\left(\sin(x) -\cos(x)\right) +C.$$
# 
# * b) $\int \ln(x) \,\mathrm{d}x$ 
# 
#     Consideramos $u=\ln(x)$ y $dv=dx$. Entonces $du=\dfrac{1}{x}$ y $v=x$, de donde obtenemos que
# 
#     $\int \ln(x) \,\mathrm{d}x = x\ln(x) - \int 1dx = x\ln(x) -x +C = x(\ln(x) -1) +C. $
# ````
# 
# Aquí puedes encontrar ejemplos para practicar: 
# * https://www.matesfacil.com/resueltos-integracion-por-partes.htm
# * https://thales.cica.es/rd/Recursos/rd97/Problemas/54-1-p-PART.HTML

# ### Integración por cambio de variable
# Este método de integración se podría decir que es lo opuesto a la regla de la cadena en derivación. Lo que pretendemos al utilizar este método es convertir la función a integrar en algo más sencillo.
# 
# ````{prf:property} Integración por cambio de variable
# :label: prop_integ_cambio_variable 
# :nonumber: 
# 
# Sean $f:[a,b] \rightarrow \mathbb{R}$ integrable y $\varphi:[\alpha,\beta] \rightarrow \mathbb{R}$ inyectiva, con derivada continua y tal que $\varphi([\alpha,\beta])\subset [a,b]$. Entonces se verifica que
# 
# $$\int f(x) \,\mathrm{d}x =  \int f(\varphi(t))\varphi'(t) \,\mathrm{d}t. $$
# ````
# 
# Veamos algún ejemplo donde se aplica el cambio de variable.
# 
# ````{prf:example} 
# :label: ex_indefinida_cambio_variable 
# :nonumber: 
# 
# * a) Para calcular $\displaystyle\int \dfrac{(\ln(x))^3}{x}  \,\mathrm{d}x $ podemos considerar $t = \ln(x)$ y obtenemos 
#   (al derivar la anterior expresión) que $dt=\dfrac{dx}{x}$. Por tanto, al hacer el cambio de variable en la integral inicial obtenemos
# 
#     $$\int \dfrac{(\ln(x))^3}{x}  \,\mathrm{d}x = \int t^3 \,\mathrm{d}t,$$
# 
#     que ya es una integral directa:
# 
#     $$\int t^3 \,\mathrm{d}t = \dfrac{t^4}{4} + C.$$
# 
#     Finalmente, deshacemos el cambio de variable para obtener que
# 
#     $$\int \dfrac{(\ln(x))^3}{x}  \,\mathrm{d}x = \dfrac{(\ln(x))^4}{4} + C.$$
# 
# 
# * b) Para calcular $\displaystyle\int \dfrac{1}{1+\sqrt{x}}  \,\mathrm{d}x $ podemos considerar $t = \sqrt{x}$ de donde obtenemos que 
#   $dt=\dfrac{dx}{2\sqrt{x}} = \dfrac{dx}{2t}$. O lo que es lo mismo $dx = 2t dt$, que al hacer el cambio de variable obtenemos
# 
#     $$\int \dfrac{1}{1+\sqrt{x}}  \,\mathrm{d}x = \int \dfrac{2t}{1+t} \,\mathrm{d}t,$$
# 
#     que todavía no es una integral inmediata. Por lo que podemos hacer otro cambio de variable, sea $z= 1+t$ entonces $dz=dt$ y
# 
#     $$ \int \dfrac{2t}{1+t} \,\mathrm{d}t = \int \dfrac{2z-2}{z} \,\mathrm{d}z = \int 2 \,\mathrm{d}z-\int \dfrac{2}{z} \,\mathrm{d}z = 2z -2\log|z| +C.$$
# 
#     Ahora debemos deshacer los dos cambios de variable realizados anteriormente, empezamos por el último
# 
#     $$ \int \dfrac{2t}{1+t} \,\mathrm{d}t = 2t+2 -2 \ln|t+1| +C,$$
# 
#     y terminamos por el primer cambio
# 
#     \begin{eqnarray*}
#     \int \dfrac{1}{1+\sqrt{x}}  \,\mathrm{d}x &=& 2\sqrt{x} +2 -2\ln|\sqrt{x}+1| +C \\
#     &=& 2\left(1+\sqrt{x} -\ln(\sqrt{x}+1)\right) +C,
#     \end{eqnarray*}
# 
#     donde el valor absoluto se ha eliminado al ser $\sqrt{x}+1>0$.
# ````
# 
# Aquí puedes practicar:
# * https://www.matesfacil.com/resueltos-integracion-por-sustitucion.htm
# * https://thales.cica.es/rd/Recursos/rd97/Problemas/54-1-p-SUST.HTML

# ### Integración por descomposición de fracciones racionales
# Este método se utiliza para integrar funciones racionales $f(x)=\dfrac{p_m(x)}{q_n(x)}$ en las cuales el grado del numerador ($m$) es menor que el grado del denominador ($n$). Esto siempre es posible ya que de no ser el caso, se puede efectuar la división, esto es, si $m\ge n$ entonces $\dfrac{p_m(x)}{q_n(x)} = c_r(x) + \dfrac{r_s(x)}{q_n(x)}$  donde el cociente es un polinomio que se puede integrar directamente y la nueva función a integrar por este método se corresponde con el resto de la división partido del divisor $\dfrac{r_s(x)}{q_n(x)}$ verificándose que $s<n$. 
# 
# ````{prf:property} 
# :label: prop_integ_racionales 
# :nonumber: 
# 
# Si tenemos una función racional tal que $f(x)=\dfrac{p_m(x)}{q_n(x)}$ con $m<n$, y $\displaystyle q_n(x)=a_{n_a}(x)\prod_{i=1}^{R} (x-\alpha_i)^{s_i}$, donde $\alpha_i$ son las distintas raices reales de multiplicidad $s_i$ de $q_n(x)$, con $i=1,2,\dots,R$ y $a_{n_a}(x)$ un polinomio sin raices reales con $n_a<n$ tal que $n_a +s_1+s_2 +\dots+s_R = n$. Entonces tenemos que
# 
# \begin{eqnarray*}
# \dfrac{p_m(x)}{q_n(x)} &=& \dfrac{b_{n_b}(x)}{a_{n_a}(x)} + \dfrac{k_1}{x-\alpha_1} + \dots+ \dfrac{k_{s_1}}{(x-\alpha_1)^{s_1}} + \\
# && + \dots + \dfrac{k_{n_{r-1}+1}}{x-\alpha_r} + \dots+ \dfrac{k_{n_{r-1}+s_r}}{(x-\alpha_r)^{s_r}},
# \end{eqnarray*}
# 
# donde $n_b < n_a$ y $n_{r-1}=s_1+s_2+\dots+s_{r-1}$. En este caso la integral de $f$ se puede descomponer en
# 
# \begin{eqnarray*}
# \int f(x) \,\mathrm{d}x &=&  \int \dfrac{b_{n_b}(x)}{a_{n_a}(x)}\,\mathrm{d}x  + \int \dfrac{k_1}{x-\alpha_1}\,\mathrm{d}x  + \dots+ \int \dfrac{k_{s_1}}{(x-\alpha_1)^{s_1}} \,\mathrm{d}x + \\
# && + \dots + \int \dfrac{k_{n_{r-1}+1}}{x-\alpha_r}\,\mathrm{d}x  + \dots+ \int \dfrac{k_{n_{r-1}+s_r}}{(x-\alpha_r)^{s_r}} \,\mathrm{d}x .
# \end{eqnarray*}
# ````
# 
# Veamos algún ejemplo práctico.
# 
# ````{prf:example} 
# :label: ex_integ_racionales 
# :nonumber: 
# 
# * **Ejemplo 1:** Calcular $\int \dfrac{2x}{x^3 -x^2 +x -1} \,\mathrm{d}x$.
# 
#     Podemos descomponer el denominador en $(x^2+1)(x-1)$ y por tanto
# 
#     $$\dfrac{2x}{x^3 -x^2 +x -1}= \dfrac{ax+b}{x^2+1}+\dfrac{k_1}{x -1},$$
# 
#     donde debemos obtener los valores de los parámetros $a, \ b$ y $k_1$. Para ello realizamos la suma
# 
#     $$\dfrac{ax+b}{x^2+1}+\dfrac{k_1}{x -1} = \dfrac{(a+k_1)x^2 + (b-a)x +(k_1-b)}{(x^2+1)(x-1)}.$$
# 
#     Como queremos que el denomidador coincida con el original tenemos que $(a+k_1)x^2 + (b-a)x +(k_1-b)=2x$. Por tanto se debe verificar que $a+k_1 = 0$, $b-a = 2$ y $k_1-b=0$, de donde obtenemos que $b=k_1=1$ y $a=-1$. Entonces
# 
#     \begin{eqnarray*}
#     \int \dfrac{2x}{x^3 -x^2 +x -1} \,\mathrm{d}x &=& \int \dfrac{-x+1}{x^2+1}\,\mathrm{d}x+\int \dfrac{1}{x -1}\,\mathrm{d}x \\
#     &=&  \int \dfrac{1}{x^2+1}\,\mathrm{d}x - \int \dfrac{x}{x^2+1}\,\mathrm{d}x+\int \dfrac{1}{x -1}\,\mathrm{d}x. 
#     \end{eqnarray*}
# 
#     Donde las últimas 3 integrales ya son directas (en la segunda se podría hacer un cambio de variable si no se ve claramente). De este modo obtenemos
# 
#     $$\int \dfrac{2x}{x^3 -x^2 +x -1} \,\mathrm{d}x =  \arctan(x) -\dfrac{1}{2}\ln(x^2+1) + \ln|x-1| + C. $$
# 
# * **Ejemplo 2:** Calcular $\int \dfrac{x^2+3x+2}{x^3-3x^2+4} \,\mathrm{d}x$.
# 
#     En este caso $x^3-3x^2+4=(x+1)(x-2)^2$, por tanto 
# 
#     $$\dfrac{x^2+3x+2}{x^3-3x^2+4}= \dfrac{k_1}{x +1} + \dfrac{k_2}{x -2} + \dfrac{k_3}{(x -2)^2}.$$
# 
#     Realizando la suma de fracciones obtenemos
# 
#     \begin{eqnarray*}
#     \dfrac{k_1}{x +1} &+& \dfrac{k_2}{x -2} + \dfrac{k_3}{(x -2)^2} = \\
#     &&\dfrac{(k_1+k_2)x^2 + (k_3 -k_2 -4k_1)x + (k_3-2k_2+4k_1)}{(x+1)(x-2)^2}.
#     \end{eqnarray*}
# 
#     Para que coincidan los numeradores se debe verificar que $k_1+k_2=1$, $k_3 -k_2 -4k_1=3$ y $k_3-2k_2+4k_1=2$ de donde obtenemos que $k_1=0$, $k_2=1$ y $k_3=4$. Entonces
# 
#     $$\int \dfrac{x^2+3x+2}{x^3-3x^2+4} \,\mathrm{d}x = \int \dfrac{0}{x +1} \,\mathrm{d}x + \int\dfrac{1}{x -2} \,\mathrm{d}x+ \int\dfrac{4}{(x -2)^2} \,\mathrm{d}x,$$
# 
#     donde las integrales de la derecha ya son directas, nótese que $\dfrac{4}{(x -2)^2}=4(x-2)^{-2}$, y, por tanto, 
# 
#     $$\int \dfrac{x^2+3x+2}{x^3-3x^2+4} \,\mathrm{d}x  = \ln|x-2| -\dfrac{4}{x-2}+ C.$$
# ````

# In[ ]:




