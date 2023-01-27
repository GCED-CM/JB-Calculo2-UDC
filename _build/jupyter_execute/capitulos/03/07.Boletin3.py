#!/usr/bin/env python
# coding: utf-8

# # Boletín III: Cálculo diferencial de funciones de una variable 
# 
# ## Ejercicios básicos
# 
# 1. Sea $f$ la función dada por $f(x)=5x^2.$
# 
#     a. Utiliza la definición de derivada para demostrar que $f'(x)=10x.$
#     
#     b. Calcula la ecuación de la recta tangente a la gráfica de $f$ en $\displaystyle{x=\frac12}.$
# 
# 2. Sea $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     2x - 1             & \quad \text{si } x \leq -1 \\
#     ( x+1)^3 + 2x & \quad \text{si } x > -1
#     \end{cases}
#     $$
# 
#     Averigua si es derivable en $x = -1$.
# 
# 3. Sea $f$ la función dada por
#    
#     $$
#     f(x)=
#     \begin{cases}
#     \displaystyle{x+x^2 \sin\left(\frac 1x\right)} & \text{  si  } x\neq 0 \\
#             0 & \text{  si  } x = 0
#     \end{cases}
#     $$
# 
#     1. Obtén la expresión de $f'(x)$ para $x\neq 0$.  
#     2. Calcula $f' (0)$ usando la definición de derivada; es decir, como límite del cociente incremental.  
#     3. Comprueba que el valor obtenido en el apartado [3.2] no coincide con el resultado de sustituir $x$ por cero en la expresión hallada en [3.1]. Razona el porqué de estos resultados distintos.  
#     
#     
# 4. Considera la función $f$ dada por:
#    
#     $$
#     f(x) =
#     \begin{cases}
#     \displaystyle{\frac{1-e^{-x}}{x} }            & \quad \text{si } x \neq 0 \\
#     1 & \quad \text{si } x = 0
#     \end{cases}
#     $$
# 
#     1. Calcula $f'(x)$ en todos los puntos en los que exista.  
#     2. Calcula $\displaystyle{\lim _{x\rightarrow -\infty}{f(x)}}$, $\displaystyle{\lim _{x\rightarrow \infty}{f(x)}}$ y el conjunto $\textrm{Im}(f)$.  
#    
# 5. Escribe el método de Newton--Raphson para aproximar $\sqrt[3]{2}$ partiendo de $x_0 = 1$. Calcula los dos primeros iterantes.  
# 
# 6. Para aproximar el valor de la solución  de la ecuación $x^3+2x-2=0,$ en el intervalo $[-2,\, 2],$ vamos a usar el método de Newton-Raphson.
#    
#     1. Plantea el algoritmo de Newton-Raphson para este caso.  
#     2. Calcula las dos primeras iteraciones usando ese algoritmo. Para ello usa como aproximación inicial el valor $x_0=0$.  
#     
# 7. Sea $f(x) = \displaystyle \arctan \left( \frac{\sin (x)}{1 + \cos (x)} \right )$. Calcula la recta tangente a la gráfica de $f$ en $x = 0$. 
#     
# 8. Sea la función $f$ dada por $f(x) = (4x+1)^{(2+ \sin (x^2))}$.  Calcula su derivada en cualquier punto.  
#    
# 9.  Si consideramos la función $f:\mathbb{R}\rightarrow \mathbb{R}$ dada por
# 
#     $$
#     f(x)=\displaystyle{\left\{ \begin{array}{ccl}
#                             \displaystyle{\frac{\sin^2(3x)}{3x^2}} & si & x\neq 0 \\
#                                 \\
#                             \displaystyle{\frac13 }& si & x=0
#                             \end{array}
#     \right. }, 
#     $$ 
#     elige la opción correcta: 
#     
#     1. $\displaystyle\lim _{x\rightarrow 0}f(x)=\frac{1}{3} $. 
#     2. No se puede calcular  $\displaystyle{\lim _{x\rightarrow 0}{f(x)}}$.
#     3. $\displaystyle{\lim _{x\rightarrow 0}{f(x)}}=3$.
#     4. Es continua en $\mathbb{R}$    
#     
# 10. Calcula los valores de $a$ y $b$ para que
# 
#     $$
#     \displaystyle{\lim_{x\rightarrow 0}\frac{ax^2+bx+1-e^{2x}}{\sin(x^2)}=1}
#     $$
#   
# 11. Sea la función $f$ dada por $\displaystyle f(x) = \frac{1}{2} x |x|$. ¿Cuál es la clase de $f$?  
#     
# 12. Consideramos la función $f$ dada por
# 
#     $$
#     f(x) =
#     \begin{cases}
#     \sin (x) \, \qquad \text{ si } x \in (-\infty,0) \\
#                 \arctan (x) \,\qquad \text{ si } x \in [0,1] \\
#                 \pi x^3 / 4 \, \qquad \text{ si } x \in (1,+\infty)
#     \end{cases}
#     $$
#     1. Esboza la representación gráfica de $f$.  
#     2. Determina la clase de $f$ en $\mathbb{R}$.  
#     3. Calcula, si es posible, la recta tangente a $f$ en el punto $x_0 = 0$.  
#     4. Determina un conjunto de números reales en el que $f$ sea de clase infinito.
#     
# 13. Sea $f$ la función dada por
#     
#     $$
#     f(x) =
#     \begin{cases}
#     \sqrt{x} + 1    & \quad  \text{si } x \in (0,1) \\
#     \alpha x^2 + \beta x + 1   & \quad  \text{si } x \in [1,2)
#     \end{cases}
#     $$  
# 
#     1.  Determina $\alpha$ y $\beta$ para que $f$ sea derivable en $(0,2)$.
#     2.  ¿Qué condiciones deben verificar $\alpha$ y $\beta$ para que $f$ tenga un mínimo relativo en el punto $x=1$?  
#     
# 14.  Calcula los extremos relativos, y absolutos si existen, de la función definida en el 
#     intervalo $\left [ -\frac{1}{2} , \frac{3}{2} \right ]$ por $f(x) = x^2 - 2|x| + 2$.
#       
# 15. Considera la función $f:\mathbb{R} \rightarrow \mathbb{R}$ dada por $\displaystyle{f(x)=\frac{|x|}{e^{x-1}}}$.
#     1.  Estudia la continuidad y derivabilidad de la función.  
#     2.  Esboza la gráfica de $f$. Para ello calcula sus extremos relativos, puntos de inflexión y asíntotas. Determina también su(s) intervalo(s) de concavidad y/o convexidad.    
#     3. Determina los extremos absolutos de $f$.    
# 
# 16. Demuestra que la ecuación $x^4-4\,x^3-1=0$ tiene una única raíz en el intervalo $[4,5]$.   
#     Plantea el método de Newton-Raphson para resolver la ecuación del apartado anterior. Partiendo de $x_0=4$, obtén la aproximación $x_1$ a mano y la aproximación $x_7$ utilizando `Python`.  
#     
# 17.  ¿En qué intervalo es creciente la función $f$ dada por $f(x)=x^3e^x$? ¿Es cóncava o convexa en ese intervalo? Esboza su gráfica.  
# 
# 18. Halla la condición que debe cumplir $\lambda$ para que el polinomio $x^4 + x^3 + \lambda x^2$ sea cóncavo en algún intervalo. Determina ese intervalo en función de $\lambda$.  
# 
# 19.  Encuentra un polinomio cúbico sin extremos locales pero con  punto de inflexión y tangente horizontal en $P=(1,\, 20)$.  
# 
# 20. Esboza la gráfica de una función cuya pendiente sea siempre positiva y creciente. ¿Conoces alguna función elemental que sea ejemplo de esta situación? <br>  Esboza la gráfica de una función cuya pendiente sea siempre positiva y decreciente. ¿Conoces alguna función elemental que sea ejemplo de esta situación?  
#      
# 21. Un rectángulo cuya base está en el eje de abscisas tiene sus dos vértices superiores en la parábola $y = 12 - x^2$. ¿ Cuál es la mayor área que puede tener ese rectángulo? Indica sus dimensiones.  
# 
# 22. Sabiendo que $p(x)=5+(x+1)^2+3(x+1)^3$ es el polinomio de Taylor de tercer orden centrado en $x_0=-1$ de una función $f,$ calcula $f(-1),$ $f^\prime (-1)$ y $f^{\prime \prime}(-1).$ Justifica la respuesta.  
# 
# 23. Consideramos la función $f$ definida mediante $f(x)=\ln(1+x)$.
#     1.  Calcula el polinomio de McLaurin (es decir, el polinomio de Taylor con $x_0=0$) de orden dos relativo a $f$.  
#     2.  Utiliza este polinomio para aproximar el valor de $\ln(1.1)$, acotando el error cometido.  
#   
# 24. Construye el polinomio de Taylor, $p$, de primer orden para la función $g(x) = \sin (x)$, centrado en el punto $x_0 = \pi/2$.
# 
#     Ahora considera la función $f$ definida como sigue:
#         
#     $$
#     f(x) =
#     \begin{cases} \sin (x) \quad  & \quad \quad \text{si } x \leq \pi/2 \\
#                         p(x) \quad    & \quad \quad \text{si } x > \pi/2
#     \end{cases}
#     $$
#     siendo $p$ el polinomio construido en el apartado anterior. ¿Cuál es la clase de $f$ en $\mathbb{R}$?  
# 
# 25. Determina el polinomio de Taylor de orden dos de la función $f(x)= \arcsin(x)$ relativo al punto $x_{0}=0$. <br> Utiliza el polinomio anterior para obtener, de forma aproximada, el ángulo cuyo seno es $\frac{1}{10}$.  
#     
# 
# 26. Sea la función dada por
#     
#     $$
#     \begin{array}{cccl}
#     f: & \mathcal{D}om(f) \subset \mathbb{R} & \longrightarrow & \mathbb{R} \\
#     &        x                    & \rightsquigarrow & f(x) = \dfrac{x^2}{e^x}
#     \end{array}
#     $$
# 
#     1.  Calcula el dominio de $f.$  
#     2.  Calcula los extremos absolutos de $f$ en el intervalo $[0,10]$, justificando previamente su existencia.  
#     3.  Calcula los extremos absolutos de $f$ en su dominio.
# 
# 
# 
# 
# 

# ## Ejercicios complementarios
#   
# 1.  Si la recta tangente a la gráfica de la función $y = f(x)$ en el punto $(4,3)$
#     pasa por el punto $(0,2)$, calcula el valor de la función $f$ y su derivada en el punto cuya
#     abscisa es $x = 4$.  
# 
# 2. Aproxima la solución de $x^3 - x - 1 = 0$ en $[1.3,\, 1.4]$ mediante el método de Newton-Raphson, partiendo de $x_0 = 1$ y realizando tres iteraciones.  
# 
# 3. Encuentra los números $a$ y $b$ tales que $\,\,\displaystyle{\lim_{x\rightarrow 0}{\frac{\sqrt{ax+b}-2}{x}}=1}.$  
# 
# 4. Calcula el límite:
#    
#     $$
#     \displaystyle{\lim_{x\rightarrow 0} \dfrac{(1+x)^{\frac{1}{x}} - e}{x}.}
#     $$ 
# 
# 5.  Se considera la función $f: \mathbb{R} \longrightarrow \mathbb{R}$ dada por:  
# 
#     $$
#     f(x)=
#     \begin{cases}
#     \displaystyle{\dfrac{1-\cos (x)}{x^2}} & \text{  si  } x\neq 0 \\
#             \lambda  & \text{  si  } x = 0
#     \end{cases}
#     $$
#     a. Calcula el valor de $\lambda$ para el cual $f$ es derivable en $x=0$.  
#     
#     b. Calcula $f^{\prime \prime}(0)$ para el valor de $\lambda$ hallado en el apartado anterior.  
#   
# 6.   Sea $f: \mathbb{R} \to \mathbb{R}$ definida como $ f(x) =
#     \begin{cases} 
#         \displaystyle 1 - \frac{x^2}{2} & \text{ si } x < 0 \\
#         \cos (x) & \text{ si } x \geq 0
#     \end{cases}
#     $. <br> ¿Cuántas veces es $f$ derivable en $x_{0}=0$?
# 
# 7. Comprueba que la función $F$, dada por $F(x) = \dfrac{1}{4} x^2 - \ln x$, tiene un  mínimo relativo, $x_{\min}$, en el intervalo $(1,3)$.  
#     Utiliza el algoritmo de dicotomía, partiendo de $a = 1$ y $b = 3$, para aproximar $x_{\min}$ con un error menor que $\frac{1}{7}$.  
#   
# 8. Consideramos la ecuación \, $x e^{-x} = e^{-3}$.
# 
#     1. Comprueba que tiene exactamente dos soluciones en $\mathbb{R}$.  
#     2. Plantea el método de Newton-Raphson a partir de un punto en el intervalo $[2,5]$. Calcula $x_2$ a partir de $x_0 = 2$. 
#   
# 9.   Se desea construir un arco que describa la curva dada por $f(x) = \sqrt{1-x^2}$.  Para facilitar la construcción, se propone aproximar dicha función por un polinomio de Taylor de segundo orden centrado en $a = 0$.  Calcula dicho polinomio y aproxima $f(1)$.  
# 
# 10. Durante la tos, el diámetro de la tráquea disminuye. La velocidad $v$ del aire en la tráquea durante la tos viene relacionada con el radio, $r,$ mediante la ecuación:
# 
#     $$
#     v = Ar^2 (r_0-r) \quad , \qquad A > 0
#     $$
#     donde $r_0$ es el radio en estado de relajación.  
# 
#     1. Halla el radio de la tráquea cuando la velocidad es máxima, así como esta velocidad.  
#     2. Justifica la existencia de un mínimo. Calcúlalo.  
#     
# 11. Halla el radio y la altura de una lata cilíndrica de refresco de
#       $33$ cm$^3$ que minimice la cantidad de material utilizado para su construcción (supón que el grosor del material empleado es uniforme en toda la lata y despreciable).  
#       
# 12. Sea la función real $f$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases} \dfrac{\sin( x)}{x} - 1 \quad  & \quad \quad \text{si } x < 0 \\ & \\
#                         x^3 e^{-x^2} \quad           & \quad \quad \text{si } x \geq 0 \, .
#     \end{cases}
#     $$
#     1.  Estudia la derivabilidad de $f$ en $\mathbb{R}$.  
#     2. Calcula el polinomio de Taylor de segundo orden de la función $f$ en un entorno de $x_0 = 1$.    
#     3. Determina razonadamente los extremos absolutos de $f$ en $[0,+\infty)$.  
#     
# 13. Sea la función $f$ dada por:
# 
#     $$
#         f(x) =
#     \begin{cases} \dfrac{\sin (x)}{x} \, & \quad \quad \text{si } x < 0 \\
#                             2 - \cos(x) \,        & \quad \quad \text{si } x \geq 0 \, .
#     \end{cases}
#     $$  
#     1. Estudia la continuidad de $f$ en $\mathbb{R}$.  
#     2. Determina, si existe, $f'(0)$.  En caso afirmativo, razona si $f$ es de clase uno en $\mathbb{R}$.  
#     3. Calcula el polinomio de Taylor de segundo grado de $f$ en $x = -\pi$.  
# 
# 
# 14. Llamamos $f(x) = \sqrt{x+1}$.  
#     1. Halla el polinomio de Taylor de cuarto orden de $f$ en $x = 0$.  
#     2. Aproxima $\sqrt{1.02}$ con el polinomio de Taylor de segundo grado y acota el error cometido.
#   
# 15.  Obtén el polinomio de McLaurin (Taylor, con $x_{0}=0$) de orden menor o igual que $n$ relativo a $f(x) = (1-x)^{\alpha}$, con $\alpha \in \mathbb{R}$.
# 
# 16. Construye el polinomio de Taylor de grado menor o igual que $3$ para la función $f(x)=x^2 - 2x + 1$ en un entorno del punto $x_{0} = 1$.  
# 
# 17.  Determina los extremos absolutos de la función $f(x)=|16-x^2|$ en el intervalo $[-5,8]$.  
# 
# 18. Queremos aproximar una raíz de la ecuación   $x^3 -x^2 + 2 = 0$.  
#     1. Justifica la existencia de raíces de la función $f$ dada por $f(x)=x^3 -x^2 + 2$ en el intervalo $[-2,3]$.  
#     2. Partiendo de $x_0=2$ calcula, mediante el algoritmo de Newton, $x_1$. Utiliza dos cifras decimales correctas en tus cálculos.  
#   
