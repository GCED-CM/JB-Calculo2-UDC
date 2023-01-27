#!/usr/bin/env python
# coding: utf-8

# # Boletín IV:  Integración de funciones de una variable
# 
# ## Ejercicios básicos
# 
# 1. Demuestra que $\displaystyle{\,\,8-\frac14\sqrt{1-4x^2}}$ es una primitiva de  $\displaystyle{\,\,\frac{x}{\sqrt{1-4x^2}}}.$ ¿Es su única primitiva? En caso afirmativo justifica el porqué, en caso negativo encuentra otra.
# 
# 2. Calcula:
# 
#     $$
#     \begin{array}{lll}
#     \text{$a)$ } \displaystyle{\int x^3\,\cos \left(x^4+2\right) \, dx} & \qquad
#     \text{$b)$ } \displaystyle{\int \ln(x) \, dx} & \qquad
#     \text{$c)$ }  \displaystyle{\int \cos (x)\,\cos\left(sen(x)\right) \, dx}  \\
#     \\
#     \text{$d)$ } \displaystyle{\int x^2\,(4x^3+7)^9 \, dx} & \qquad
#     \text{$e)$ } \displaystyle{\int e^x\,sen (2x+5) \, dx} & \qquad
#     \text{$f)$ } \displaystyle{\int \frac{x}{1+x^4}\, dx }
#     \end{array}
#     $$
# 
# 3. Sea la función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por $f(x) = x^3 -2$. Consideramos la partición $P=\{-2,-1,1,4\}$. Elige la opción correcta.
#     
#     $$
#     \begin{array}{lll}
#     \\
#     \text{$a)$ $L(f,P)=-19$,     $U(f,P)=181$  }    & \qquad
#     \text{$b)$ $L(f,P)= 19$,     $U(f,P)=181$}    \\
#     \\
#     \text{$c)$ $L(f,P)=-1$,      $U(f,P)=181$ }   & \qquad
#     \text{$d)$ $L(f,P)=-1$,      $U(f,P)=191$}
#     \end{array}
#     $$
#     
# 4. Sea $f$ una función continua en $x \in [2,4]$, de la que sabemos que $\underset{x \in [2,4]}{\min} f(x) = 3$ y $\underset{x \in [2,4]}{\max} f(x) = 6$.
# 
#     *  ¿Puede valer $15$ unidades de superficie el área de la figura limitada por el eje $OX$, la gráfica de $y = f(x)$,  y las rectas $x = 2$ y $x = 4$?
#     *  ¿Entre qué valores puede oscilar el área anterior?
#      
# 
# 5.  Si $f$ y $g$ son funciones continuas, halla:
#   
#     * $f(4)\,\,$ si $\displaystyle{\,\int_0^x f(t) \,  = x \, \cos (\pi x)},$
# 
#     * $g(1)\,\,$ si $\displaystyle{\,\int_{x^2}^{x^3} g(t) \,  = x \, \cos (\pi x)}.$
# 
# 6.  Halla los extremos relativos de la función $F(x) = \displaystyle{\int_1^x \frac{sen( t)}{t} \, }$, con $x > 1$.
# 
# 7.  Halla una función $f$ y un número real $a$ tales que:
# 
#     $$
#     6+\int_{a}^x{\frac{f(t)}{t^2}}\, =2\sqrt{x,}\qquad \quad x>0.
#     $$
# 
# 8. Halla el área de la figura limitada por las rectas $y = x$, $y = 2x$ e $y = 4$.
# 
# 9.  Sea la función dada por:
# 
#     $$
#     f(x) = \begin{cases}
#     sen^2(x)          \, & \quad  \text{si } x \in [0,\pi] \\   \quad \\
#                   \dfrac{x}{\pi-x^2} \, & \quad  \text{si } x \in (\pi,2\pi]
#     \end{cases}
#     $$
#   
#     * ¿Es $f$ integrable en $[0,\, 2\pi]$? Razona la respuesta.        
#     * Calcula el área limitada por el grafo de $f$, $x=0$, $x=2\pi$ e $y=0$.
#     
#     
# 10. Maruja conduce a una velocidad $v_M(t)= \displaystyle{90+15\cos\left(\frac{\pi}{2}t\right)\,\mathrm{km/h}}$ y Pepe lo hace a una velocidad 
# 
#     $$
#     v_P(t)=85+2t\,\mathrm{km/h},
#     $$
# 
#     donde $t$ mide el tiempo en horas. Supongamos que Maruja y Pepe están en el mismo lugar cuando $t=0.$ Calcula $\displaystyle{\int_0^5{(v_M(t)-v_P(t))\,\,}}$ y $\displaystyle{\int_0^{10}{(v_M(t)-v_P(t))\,\,}}.$ 
#     Interpreta las integrales anteriores en términos de una carrera entre Maruja y Pepe. 
# 
# 11. En un circuito eléctrico se ha medido la corriente en distintos instantes de tiempo, obteniendo el cuadro siguiente:
#     | $t_k$      |    2   |    4   |    6   |
#     |------------|:------:|:------:|:------:|
#     | $i(t_k)$   |    3   |    5   |    9   |
# 
#     Aproxima la carga eléctrica del circuito, $q = \displaystyle{\int_2^6 i(t) \, },$ mediante las fórmulas del punto medio, trapecio, Simpson y la fórmula del trapecio compuesta con paso $h=2.$
# 
# 
# 12.  Halla el área limitada por la gráfica de $f(x) = xe^{-2x}$ y el eje $OX$ en el intervalo $[0 , \infty)$.
# 
# 13.  Halla el valor de la integral $\displaystyle{\int_0^1 x^2 \ln (x) \, dx}.$
# 
# 14.  Calcula $\displaystyle{\int_0^{\infty} \frac{1}{\sqrt{x} (x+1)} \, dx}$
# 
# 15.  Una esfera de madera de radio $R = 10\,$cm se recubre de una capa de acero de $1\,$cm de espesor. Calcula, mediante integración, el volumen de acero necesario.
# 
# 16.  En procedimientos de diagnosis médica por imagen (como, por ejemplo, la resonancia magnética), se toman numerosos datos para obtener mediante cálculos computacionales una imagen tridimensional que permita visualizar la parte del cuerpo que se estudia. El proceso es similar al empleado para calcular el volumen de un sólido usando áreas de secciones perpendiculares a un eje. Supongamos que el siguiente cuadro indica el valor del área de unas cuantas secciones de un tumor, tomadas a una distancia de un milímetro entre cada dos imágenes:
#      | $x (cm)$    |   0  | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
#       |-------------|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
#       | $A(x)(cm^2)$|   0  | 0.1 | 0.4 | 0.3 | 0.6 | 0.9 | 1.2 | 0.8 | 0.6 | 0.2 | 0.1 |
# 
#       * Estima el valor  del volumen del tumor en el intervalo $[0,\, 1],$ calculando las sumas superior e inferior para la partición dada en en el cuadro.
#       * Estima el volumen del tumor usando la fórmula del punto medio compuesta. 
#       * Estima el volumen del tumor usando la fórmula  del trapecio compuesta.
#           
# 
# 17.  Calcula el valor del área comprendida entre la gráfica de la función $f(x)=sen(x)$ y el eje $OX$ limitada
# por las rectas $x=0$ y $x=\pi$ **utilizando integración numérica**. Utiliza para ello las fórmulas del punto
# medio compuesto, trapecio compuesto y Simpson compuesto tomando como nodos los puntos $0$, $\frac{\pi}{4}$,
# $\frac{\pi}{2}$, $\frac{3\pi}{4}$ y $\pi$ (distribuidos en 2 o 4 subintervalos, según proceda). Compara los resultados
# obtenidos con el valor exacto de la integral.
# 
# 18.  Sea la función $f(x) = \sqrt{-x \ln (x)}$ definida en los puntos $x$ para
# los cuales $-x \ln(x) \geq 0$.  Calcula el volumen del sólido generado al rotar todo su dominio alrededor del eje $OX$.
# 
# 19.  Comprueba que $f(x)=\frac23 e^x+e^{-2x}$ es una solución de la ecuación diferencial $y'+2y = 2 e^x.$
# 
# 20. Halla la solución general de la ecuación diferencial:  $y^{\prime} x = y \ln (y)$.
# 
# 21. Resuelve el siguiente problema de valor inicial:
#     
#     $$
#       \left\{
#         \begin{array}{c}
#           \displaystyle \cos(y)\,\frac{dy}{dt}= \frac{-t\,sen(y)}{1+t^2}  \\
#                 y(1)= \frac{\pi}{2}
#         \end{array}
#       \right.
#     $$
# 
# 
# 22.  Resuelve la ecuación diferencial:  $\displaystyle{y^{\prime} - \frac{y}{x-2} = 2 (x-2)^2}$.
# 
# 23.  Resuelve la ecuación diferencial: $y^{\prime} + y = sen(x) $ con la condición inicial $y(\pi)=1$.
# 
# 24.  Resuelve el siguiente problema de valor inicial:
# 
#       $$
#         \left\{
#           \begin{array}{c}
#             \displaystyle y^{\prime }\,+ \,2y = e^{3x}  \\
#                   y(0)= \frac{2}{5}
#           \end{array}
#         \right.
#       $$
#       Calcula $\displaystyle\lim_{x\rightarrow \infty}{y(x)}$.
# 
# 25.  La cantidad de medicamento en un órgano dentro del cuerpo humano sigue la ecuación
# 
#       $$
#       \frac{dx}{dt}=\text{velocidad de entrada} - \text{velocidad de salida,}
#       $$
#       donde $x(t)$ es la cantidad de medicamento en el instante $t.$ Recordemos que la velocidad de entrada o salida es igual al producto de la concentración del medicamento (a la entrada o a la salida, respectivamente)
#       multiplicada por la velocidad del flujo sanguíneo.
# 
#       Queremos que un medicamento llegue a un riñón que tiene un volumen de 120 cm$^3$, por lo que se lo suministramos al flujo sanguíneo con una concentración de 0.2 g/cm$^3$. Sabemos que dicho flujo circula a una velocidad constante de 3 cm$^3$/s.
# 
#       * Calcula $x(t)$ en cualquier instante si sabemos que al principio no había vestigio alguno del medicamento.
#       * ¿En qué momento habrá $12\,$g. de medicamento en el riñón?
# 
# 
# 26.  Un célebre actor de cine contrae fiebres virulentas mientras rueda una película en áfrica. A consecuencia de ello, el actor fallece a las 8:00 a.m. en la habitación del hotel donde se aloja, con una temperatura corporal en el momento de la muerte de 40$^{o}$ Celsius. El jefe de seguridad del hotel descubre el cuerpo sin vida dos horas después de su muerte (a las 10:00 a.m.) y avisa a la policía y al forense, que se personan a mediodía (12:00 a.m.). Sabemos que la ley de Newton de enfriamiento de los cuerpos establece que:
#     
#       $$
#       T'(t)=k\,\left(T(t)-T_\mathrm{amb}\right),
#       $$
#       
#       donde $T(t)$ denota la temperatura del cuerpo (en grados Celsius) transcurrido un tiempo  $t$ (medido en horas), $T_\mathrm{amb}$ es  la temperatura ambiente y $k$ es una constante. Supondremos que la habitación del hotel estaba a una temperatura constante de 20$^{o}$ Celsius y tomaremos $k=-0.1$:
# 
#       * Determina la temperatura del cadáver cuando lo descubre el jefe de seguridad.
#       * Determina la temperatura del cadáver cuando llega el forense.
# 
# 27.  Razona la veracidad o falsedad de:
# 
#       $$
#       \int_1^4 {\frac{1}{3-x}\, dx}=-\ln|x-3|\Big]_{1}^{4}= -\ln(4-3)+\ln|1-3|=-\ln(1)+\ln(2)=\ln(2).
#       $$
# 
# 28. Sea $g(x)=\frac{{x}^{2}-1}{x}$:
# 
#     * Halla $\displaystyle{\int_a^e g(x) \, dx}$, siendo $a$ un número real mayor que cero.
#     * Calcula $\displaystyle{\int_0^e g(x) \, dx}$.
# 
# 29. Calcula:
# 
#     * $\displaystyle\int_0^{\ln(5)}  \frac{e^{x} \sqrt{e^{x}-1}}{e^{x}+3 } \, dx$, 
#     * $\displaystyle \int_1^x \frac{\sin( t)}{t}$,
#     * $\displaystyle\int_0^1 \frac{x}{\sqrt{1+{x}^{2}}} \, dx$,
#     * $\displaystyle\int_0^{\pi/4} x^2\cos(x) \, dx$,
#     * $\displaystyle\int_0^{\pi/4} \arctan(x) \, dx$.
#     
# 

# ## Ejercicios complementarios
# 

# 1. ¿En qué se transforma la siguiente integral al realizar el cambio de variable $\sin(3x)=t$?  
# 
#       $$
#       \int{\frac{\cos(3x)}{\sqrt{5+\sin(3x)}}\,}dx\,
#       $$ 
#         
#       
# 2. Resuelve la integral $\displaystyle \int{\frac{dx}{\sqrt{5x+8}}}$ mediante un cambio de variable.
#       
# 3.  Sea la función 
# 
#       $$
#       f : \mathbb{R} \longrightarrow \mathbb{R}
#       $$ 
#       dada por $f(x) = 3 - x^2$. Consideramos la partición $P=\{-2,-1,1,3\}$. Elige la opción correcta.
#       
#       $$
#       \begin{array}{lll}
#       \\
#       \text{$a)$ $L(f,P)=9$,     $U(f,P)=12$  }    & \qquad
#       \text{$b)$ $L(f,P)= 9$,     $U(f,P)=10$}    \\
#       \\
#       \text{$c)$ $L(f,P)=-9$,      $U(f,P)=10$ }   & \qquad
#       \text{$d)$ $L(f,P)=-9$,      $U(f,P)=12$}
#       \end{array}
#       $$
# 
# 4. Sea la función $f$ dada por:
# 
#       $$
#       f(x) = \begin{cases} 1 \, , \quad \quad & \text{si } x \in [0,1] \\ 1+x \, , \quad  \quad & \text{si } x \in (1,2] .
#       \end{cases}
#       $$
#       Se define $S(x_0)$ como el área limitada por la gráfica de $f$, el eje $OX$ y
#       la recta $x=x_0$ (con $x_0 \in [0,2])$.
# 
#       * Razona, sin construir la función, la continuidad de $S$.  
#       * Obtén $S(x_0)$ para cada $x_0$ perteneciente al intervalo $[0,2]$.   
#       * Supón que se repite el procedimiento con la función $S$ en lugar de $f$, construyéndose de esta forma la función $A$, donde $A(x_0)$ es el área limitada por la gráfica de $S$, el eje $OX$ y la recta $x = x_0$.  Razona, sin construir la función, la derivabilidad de $A$ y obtén, además, $A(x_0)$ para todo $x_0$ perteneciente al intervalo $[0,2]$.
# 
# 5. Sea la función $F$ dada por:
# 
#       $$
#       F(x) = \int_{\pi/2}^{g(x)} \, f(t) \, dt,
#       $$
#       donde $f(t) = (1-sen^3 (t)) \, e^t$ \, y \, $g(x) = \frac{\pi}{2} + e^x$.
# 
#       * Determina los puntos críticos de $F$ en el intervalo $[1\, ,\, \ln(5\pi)]$.   
#       * Sin calcular $F''$, clasifica los puntos críticos y determina los extremos absolutos de $F$ en $[1,\,\ln(5\pi)]$.
#         
# 6. Sea $f$ una función continua en $[0,\,\infty),$ tal que $f(0)\neq 0$. Elige la opción correcta:
# 
#    * $F(x)=\displaystyle\int_0^{x^2}{f(t)\,dt}$ es una función derivable y $F^{\prime}(x)=2xf(x^2)$       
#    * $F(x)=\displaystyle\int_0^{x^2}{f(t)\,dt}$ es una función derivable y $F^{\prime}(x)=2xf(x^2)-f(0)$
#    * $F(x)=\displaystyle\int_0^{x^2}{f(t)\,dt}$ es una función continua pero no es derivable
#    * ninguna de las otras respuestas es correcta
# 
# 
# 7. Consideramos la función $f$ dada por $f(x) = 3 + 6\cos (2x)$.
# 
#       * Calcula una primitiva de $f$, $F$, tal que $F(0)= -1$. Comprueba que $F'=f$.   
#       * Halla razonadamente los extremos absolutos y relativos de $F$ en $[0,\,2\pi]$
# 
# 8. El valor de $\displaystyle\int_{-\frac{\pi}{4}}^0{\sin^3(x)\cos(x)\, dx}\,\,$ es:
#       
#       * $\displaystyle{-\frac{1}{16}} \,$          
#       * $\displaystyle{\,\,\,\,\frac{1}{16}}\, $   
#       * $\displaystyle{\,\,\,\,\infty} \,$         
#       * $\,\,\,-2$
#       
# 9.  El valor de $\displaystyle\int_{\frac{\pi}{2}}^{\pi}{\frac{\cos(3x)}{\sqrt{5+\sin(3x)}}\,dx}\,\,$ es:
#     
#       * $\displaystyle{\infty}$, porque el denominador se anula en ese intervalo    
#       * $\displaystyle{2-\sqrt{5}}  \,$
#       * $\displaystyle{2(\sqrt{5}-2)}  \,$                                           
#       * $\displaystyle{\frac{2}{3}(\sqrt{5}-2)}$ 
#       
# 10.  Sea $f(x) = x (x-a)$, $a > 0$, y $V_f$ el volumen engendrado al girar en torno al eje $OX$ la región
# del plano limitada por dicha función y las rectas $y=0$ y $x=c,\,$ $c \geq a > 0$.  Halla $c$ para que $V_f$ sea igual al volumen del cono engendrado por el triángulo de vértices $(0,0)$, $(c,0)$ y $(c,f(c))$ al girar en torno al eje $OX$.
# 
# 11.  Calcula el volumen del cuerpo de revolución que se obtiene al girar, en torno al eje $OX$, la intersección de los círculos \, $x^2 + y^2 \leq 16$ \, y \, $(x-3)^2 + y^2 \leq 25$.
# 
# 12.  Halla el volumen del sólido generado al girar alrededor del eje $OX$ el recinto limitado por los semiejes positivos, la parábola $y = -x^2+2x+3$ y la recta $y = 2-2x/3$.
# 
# 13.  Sea $Q(t) = \cos (\pi t)$ la carga eléctrica de un circuito en un instante de tiempo $t$.
# 
#       * Aproxima el valor de la carga en $t=0.25$ mediante el polinomio de Lagrange, $P_1$, relativo a $Q$ y a los instantes de tiempo $0$ y $0.5$.  
#       * Calcula el polinomio de Lagrange, $P_2$, relativo a $Q$ y a los instantes $0.5$ y $1$.  
#       * Aproxima la integral definida $\displaystyle\int_0^{1} Q(t) \,  dt$ empleando los polinomios anteriores.  
#       * Aproxima la integral anterior mediante la fórmula del trapecio compuesta con $h=0.5$.
#  
# 14.  El valor aproximado de la integral $\displaystyle{\int_{\pi/4}^{3\pi/4}{\mbox{cotan}(x)\,}dx\,\,}$  usando el método de Simpson (simple) es:
#       
#       * $\displaystyle 0$      
#       * $\displaystyle-\frac{\pi}{12}$   
#       * $\displaystyle\frac{\pi}{12}$   
#       * es una integral impropia porque la función cotangente tiene una asíntota vertical en $[\pi/4,\, 3\pi/4]$
#       
# 15.    Calcula la recta, $r$, tangente a la función $f(x)={x}^{2}-2x+1$ por el punto $(3,f(3))$. A continuación, dibuja la región del plano $R$ limitada por la gráfica de $f$, la recta $r$ y el semieje positivo $OX$ y calcula la superficie de dicha región.   
# 
# 16. Halla el área de la figura limitada por la curva $y=\tan(x)$, el eje $OY$y la recta $y=1$. Calcula también el volumen generado al hacer girar la figura anterior alrededor del eje $OX$. 
# 
# 17.  Calcula la superficie del plano limitada por la gráfica de $y=\ln(\frac{1}{x})$, la recta $x=\frac{1}{2}$ y la recta $x=2$.
# 
# 18.  Sea $\displaystyle f(x)=ax+b+\frac{8}{x}$, donde $a$ y $b$ son dos números reales.
#       * Calcula $a$ y $b$ para que la gráfica de $f$ pase por el punto $(-2,-6)$ y tenga en $x=-2$ una tangente horizontal.
#       * Para los valores de $a$ y $b$ obtenidos en el apartado anterior, calcula el área limitada por la gráfica de $f$ y las rectas $x=1$, $x=2$ e $y=0$.  
#     
# 19.  El área del recinto limitado por $y=ln(x)$ y el eje  de abscisas entre $x=\displaystyle{\frac12}$ y $x=2$ está dada por:
# 
#       * $\displaystyle\int_{1/2}^2 {|\ln(x)| \, dx}$             
#       * $\displaystyle\int_{1/2}^2 {\ln(x)\, dx}$             
#       * $\displaystyle\left|\int_{1/2}^2 {\ln(x)\, dx}\right|$   
#       * $\displaystyle\pi \,\int_{1/2}^2{(\ln(x))^2\, dx}$
# 
# 20.  El volumen de revolución generado al girar, alrededor del eje OX, la superficie comprendida entre las curvas  $y=x^2$ e $y = \sqrt{x}$ se calcula así:
# 
#       * $\displaystyle\pi\,\int_0^{\infty}{\left[ (x^2)^2-(\sqrt{x})^2 \right]}\, dx $   
#       * $\displaystyle\pi\,\int_0^{1}{\left[ (x^2)^2-(\sqrt{x})^2 \right]}\, dx $               
#       * $\displaystyle\pi\int_0^{1}{\left[ (\sqrt{x})^2 - (x^2)^2 \right]}\, dx $              
#       * $\displaystyle\int_0^{1}{\left[ (\sqrt{x}-x^2)^2 \right]}\, dx $
# 
# 21.  Calcula el volumen que genera la curva $g(x) = \dfrac{1}{x-1}$ al girar alrededor del eje $OX,$ para $0 \leq x \leq 2$.
# 
# 22.  La integral $\displaystyle\int_0^5{\frac{1}{\sqrt{25-5x}}}\, dx$:
# 
#       * es impropia de tercer tipo
#       * es impropia de segundo tipo porque la función integrando no está acotada superiormente en $x=5$ 
#       * es impropia de segundo tipo porque la función integrando no está acotada inferiormente en $x=5$
#       * es impropia de primer tipo porque la función integrando no está acotada superiormente en $x=5$
# 
# 23. ¿Cuál es la solución del siguiente problema de valor inicial?
# 
#       $$
#       \left\{
#       \begin{array}{c}
#             \displaystyle{y^{\prime } = 2 y^{2} } \\
#                   y(0)= \displaystyle{\frac{1}{2}}
#       \end{array}
#       \right.
#       $$
#             
# 24.  ¿Cuál es la solución del siguiente problema de valor inicial?
# 
#       $$
#       \left\{ 
#       \begin{array}{l}
#         \displaystyle {y' + \cos(x) y = \cos(x)} \\
#             \displaystyle{ y(0)= 0 \, .}
#       \end{array}\right.
#       $$
# 
# 25. Calcula la solución general de la siguiente ecuación diferencial ordinaria: 
# 
#       $$
#       v^\prime = v + t\,e^t.
#       $$ 
# 
# 26.  Del  problema de valor inicial
# 
#       $$
#       \begin{cases} \displaystyle{y^\prime = -y^2} \\ \displaystyle{y(0)=\frac12} \end{cases}
#       $$
#       podemos obtener la información siguiente:
# 
#       * ninguna de las siguientes afirmaciones es correcta
#       * la solución de ese problema de valor inicial es una función $y$  que es creciente y tal que $\displaystyle{y^\prime(0)=-\frac14}$
#       * la solución de ese problema de valor inicial es $\displaystyle y= \frac1{2-x}$  
#       * la solución de ese problema de valor inicial es una función decreciente. Además, la función $g$ dada por $\displaystyle g(x)=\frac{1}{2}-\frac{x}{4}$ es la recta tangente a la función solución del p.v.i. en el punto de abscisa $x=0$.  
# 
# 29.  Sea la ecuación diferencial ordinaria $\displaystyle y^\prime = x^2y$, donde $y$ es una función de $x.$ Entonces:
# 
#       * la solución general es $\displaystyle y=k\,e^{-x^3/3}$, donde $k$ es constante de integración  
#       * la solución general es $\displaystyle y= k\,e^{x^3/3}$, donde $k$ es constante de integración         
#       * no puedo hallar la solución porque no es una ecuación diferencial ordinaria separable ni tampoco lineal 
#       * la solución general es $\displaystyle y= \frac{x^3}{3}\,y+k$, donde $k$ es constante de integración
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
