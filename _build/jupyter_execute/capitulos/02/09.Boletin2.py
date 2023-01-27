#!/usr/bin/env python
# coding: utf-8

# # Boletín 2: Límites, continuidad, Lagrange y dicotomía

# 1. Calcula, si es posible,
#    
#     a. $\displaystyle{\lim_{x\rightarrow 0}{\frac{|2x-1|-|2x+1|}{x}}}$,
# 
#     b. $\displaystyle{\lim_{x\rightarrow 0}{\frac{\sqrt{x^2+4}-2}{x^2}}}$,
#     
#     c. $\displaystyle{\lim_{x\rightarrow 0}{\left (\frac{1}{x}-\frac{1}{|x|}\right)}}$.
# 
# 2. Calcula, si es posible, los siguientes límites:
#    
#     $$
#     \begin{array}{lllll}
#     %\text{$(a)$ } \displaystyle{\lim_{x\rightarrow -\infty} e^x}   &\qquad
#     %\text{$(b)$ } \displaystyle{\lim_{x\rightarrow 0}       e^x}   &\qquad
#     %\text{$(c)$ } \displaystyle{\lim_{x\rightarrow +\infty} e^x}   &\qquad
#     \text{$a)$ } \displaystyle{\lim_{x\rightarrow -\infty} \sqrt[3]{x}}   & \qquad
#     \text{$b)$ } \displaystyle{\lim_{x\rightarrow +\infty} \sqrt{x}}  &\qquad
#     \text{$c)$ } \displaystyle{\lim_{x\rightarrow 0^+}     \sqrt{x}}   &\qquad
#     \text{$d)$ } \displaystyle{\lim_{x\rightarrow -\infty} \sqrt{x}}   \\
#     \\
#     \text{$e)$ } \displaystyle{\lim_{x\rightarrow +\infty} \dfrac{1}{\sqrt{x}}}  & \qquad
#     \text{$f)$ } \displaystyle{\lim_{x\rightarrow 0^+}     \dfrac{1}{\sqrt{x}} }  &\qquad
#     %\text{$j)$ } \displaystyle{\lim_{x\rightarrow +\infty} x^2}   &\qquad
#     \text{$g)$ } \displaystyle{\lim_{x\rightarrow -\infty} x^2 }  &\qquad
#     \text{$h)$ } \displaystyle{\lim_{x\rightarrow +\infty} \left( x^3 - 5x^2 + 8 \right)}
#     \end{array}
#     $$
# 
# 3. El valor, en euros, de un coche $x$ años después de su adquisición (nuevo) viene dado por la función
#    
#     $$
#     v(x)=2000+\frac{60000}{4^{0.25 x}}.
#     $$
#     
#     Se llama *valor residual* del coche a su valor límite cuando el número de años aumenta indefinidamente.
#     
#       a. ¿Cuál fue el precio de compra del vehículo nuevo?
# 
#       b. ¿Cuál será su valor residual?
# 
#       c. ¿Al cabo de cuántos años diferirá su valor en menos de 1000 euros del valor residual? 
#     
# 4. Dibuja, con `Sympy` la gráfica de la curva $y=\sqrt{x^2+1}-x$. 
#    
#     Comprueba, con lápiz y papel y comprobando los resultados en el ordenador, si esta gráfica tiene alguna asíntota y, en caso afirmativo, obtén sus ecuaciones.
# 
# 5. Calcula las asíntotas de las siguientes funciones:
# 
#     a. $\displaystyle{v_{1}(x)= \frac{3x^2-2}{4x^2 +1}}$,
# 
#     b. $\displaystyle{h(t)= \frac{t^2+2}{t -2}}$,
# 
#     c. $\displaystyle{v_{2}(x)= \frac{3x^2-2}{4x^2 -1}}$,   
# 
#     d. $\displaystyle{f(x)=x^\frac{|x|}{x} + \frac{1}{x}}$.
# 
# 6. Considera la  función $f$, dada por $f(x) = \ln(x)$.
#    
#     a. ¿Cuál es su dominio? ¿Cuál es su imagen?
# 
#     b. ¿Cuánto valen $\displaystyle{\lim_{x\rightarrow  +\infty}\ln(x)} \,\,$ y $\displaystyle{\lim_{x\rightarrow 0^+}\ln (x)}$?
# 
#     c. ¿Existe $\displaystyle{\lim_{x\rightarrow -\infty}\ln(x)}$? ¿Por qué?
# 
#     d. ¿Posee $f$ alguna asíntota vertical? En caso afirmativo, ¿cuál es su ecuación?
# 
#     e. Dibuja la gráfica de $f$.
# 
#     f. Utilizando la relación entre la gráfica de una función y la de su inversa, esboza la gráfica de $g(x)=e^x$. 
#     De la observación de esta gráfica deduce la existencia de una asíntota horizontal.
# 
# 7. Vamos a repasar la función arco-tangente ($\arctan$):
# 
#     a. ¿Cuál es el dominio de la función $f(x)=\arctan(x)$? ¿Y su imagen?
# 
#     b. ¿Es cierto que $\dfrac{1}{\tan(x)} = \arctan(x)$? ¿Por qué?
# 
#     c. ¿Cuáles son los ángulos cuya tangente vale $1$?
# 
#     d. ¿Es correcto decir que $\arctan (1)=\dfrac{\pi}{4}+k\pi$, $\,k \in \mathbb{Z}$? ¿Por qué?
# 
# 8. Si la longitud de un animal $t$ días después de su nacimiento es 
# 
#     $$
#     \ell(t)= \frac{300}{1+9\left(0.8\right)^t}
#     $$  
#     ¿cuánto midió al nacer? Obtén una cota superior de su tamaño máximo. 
# 
# 9. Elige la opción correcta: 
#     
#     Para aproximar el valor de la solución de la ecuación  $x^3+2=0$ con un error menor que $0.30$ usando el algoritmo de dicotomía en el intervalo $[-2,\,2]$:
# 
#     a. debemos realizar cuatro iteraciones y las tres primeras son $x_1=0$, $x_2=-1$ y $x_3=-3/2$
# 
#     b. debemos realizar cuatro iteraciones y las tres primeras son $x_1=0$, $x_2=-1$ y  $x_3=-1/2$
# 
#     c. debemos realizar tres iteraciones y las dos primeras son $x_1=0$ y $x_2=-1$
# 
#     d. debemos realizar tres iteraciones y las dos primeras son $x_1=0$ y $x_2=1$.
# 
# 10. ¿Dónde es continua la función $f$ dada por $f(x)=\displaystyle{\frac{e^x+\ln(2x)}{x^2-3}}?$
# 
# 11. Elige la opción correcta:
# 
#     La función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     \sqrt{{x}^{2}-1} \,\,\,\,  \qquad\,  \text{  si  } x \in (-\infty,-1] \\
#                 {x}^{2}+2x+1 \qquad    \text{si } x \in (-1,10] \\
#                 \frac{121}{10}x   \qquad\, \, \, \, \qquad   \text{     si   } x \in (10,+\infty)
#     \end{cases}
#     $$
# 
#     a. No es continua en $x=-1$
# 
#     b. Es continua en $(-\infty,\infty)$
# 
#     c. No es continua en $x=10$
# 
#     d. No es continua en $x=0$
# 
# 12. Estudia la continuidad en $x=0$ de la función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     x e^{-x} \,  \qquad\,\quad  \text{si } x < 0 \\
#                 1 \qquad \qquad \,\,\,\,\,\,   \text{si } x = 0 \\
#                 \sqrt{x^2+1}   \qquad   \text{si } x > 0
#     \end{cases}
#     $$
# 
# 13. Si $a>1$ estudia la continuidad de la función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     {x}^{2} {\cos^2\left(\frac{1}{x}\right)}   \qquad\,\quad  \text{si } x < 0 \\
#                 0 \qquad \qquad \,\,\,\,\,\,\,\,\quad   \text{     si } x = 0 \\
#             \dfrac{x {a}^{x}-x} {\sqrt{1+x}-1}  \qquad   \text{si } x > 0
#     \end{cases}
#     $$
# 
# 14. Demuestra que la ecuación $x + \sin (x) = \dfrac{1}{\sqrt{x}+3}$ tiene al menos una raíz en $[0,\pi]$.
#     
# 15. Justifica la existencia de una solución de la ecuación $e^x+4x=0$ en el intervalo $[-1, 0]$. 
#     Determina el número de iteraciones necesarias para aproximar la solución mediante el método de dicotomía con un
#     error inferior a  una centésima y calcula las tres primeras iteraciones.
#     
# 16. Sea la función $f$ dada por:
# 
#     $$
#     f(x) = \begin{cases}
#     \displaystyle{\frac{x^2}{1+e^{1/x}} - 1}    & \quad  \text{si } x \neq 0 \\
#     \\
#     - 1   & \quad  \text{si } x =0. \end{cases}
#     $$
# 
#     a. Estudia la continuidad de $f$ en $\mathbb{R}.$
# 
#     b. Justifica la existencia de una raíz de $f$ en el intervalo $[0,\, 2].$
#     
#     c. Calcula los dos primeros iterantes del algoritmo de dicotomía, aplicado a $f$ en el intervalo $[0,\,2],$ para aproximar la raíz a la que se refiere el apartado anterior.
# 
# 
# 17.  Mediciones puntuales han determinado que una función $f$ desconocida pasa por $(-2, -16)$, $(0, 0)$, $(1, -1)$ y $(3, 9)$. Calcula, mediante diferencias divididas, una aproximación polinómica de $f$. Utiliza este polinomio para aproximar $f(2)$.
# 
# 18. Calcula el polinomio de interpolación de Lagrange de orden tres relativo a $f(x) = 2^{x+1}-5$ en los puntos $x_0 = 1$, $x_1 = 2$, $x_2 = 3$ y $x_3 = 4$.
#     Utilizando los cálculos previos, calcula una aproximación del número $r = 4 \sqrt{2}-5$ y una aproximación de la raíz de la ecuación $\log_2 (y+5) = 3.5$.
# 
# 19. Utiliza la fórmula de Newton para obtener el polinomio de interpolación de la función $f(x)=\sin(x)$ relativo a los puntos $\displaystyle{ 0, \frac{\pi}{2}, \pi}$ y $\displaystyle{\frac{3\pi}{2} }$. Utilízalo para aproximar el seno de $\displaystyle{\frac{\pi}{4}}$.
# 
# 20. Considera la siguiente tabla de valores, correspondiente a mediciones de una función $f$:
# 
#     | $x_{i}$ | -1 | 0 | 1 | 3 | 4 |
#     | -- | -- | -- | -- | -- | -- |
#     | $f(x_{i})$ | 6 | 3| 6 | 38 | 77|
# 
#     a. Calcula el polinomio $p$ de interpolación de Lagrange de orden $2$ relativo a $f$ en los nodos $\{ 1,3,4 \}$.
# 
#     b. Calcula el polinomio $q$ de interpolación de Lagrange de orden $2$ relativo a $f$ en los nodos $\{ -1,0,1 \}$.
# 
#     c. Aproxima $f(0.25)$  y $f(2)$.
# 
# 21. Elige la opción correcta:
#     
#     Si usamos el polinomio de Lagrange que interpola a los nodos $(-2,-8)$, $(-1, 0)$ y $(1, 4)$, para aproximar el valor en $x=0$ obtenemos:
# 
#     a. -4
# 
#     b. 0
# 
#     c. 4
# 
#     d. con el polinomio de Lagrange que interpola esos nodos no se puede aproximar el valor en $x=2$.
# 
# 22. Elige la opción correcta:
# 
#     El coeficiente de grado $1$ del polinomio de Lagrange que interpola los datos de la siguiente tabla
# 
#     | $x_{i}$ | -2 | -1 | 1 | 0 |
#     | -- | -- | -- | -- | -- |
#     | $y_{i}$ | 4 | 4 | 10 | 6 |
# 
#     a. es 0
# 
#     b. es 1
# 
#     c. es 3
# 
#     d. no existe ese polinomio.   
# 
# 23. **Razona** la veracidad o falsedad de las siguientes afirmaciones:
#     
#     a.  Sea $f:[0,2]\rightarrow \mathbb{R}$ continua y tal que $f(1)=0$. Entonces, por el teorema de Bolzano debe ser $f(0)f(2)<0$.
# 
#     b. Existe un punto $x \in (0,1)$ tal que $\displaystyle{e^{x}=\frac{3}{2}}$.
# 
#     c. La función $g$ dada por $\,g(x)=\dfrac{16}{{a}^2+2abx+{b}^2{x}^2}\,$, donde $a$ y $b$ son dos números reales no nulos, es continua siempre que $x$ difiera de $\,\frac{-a}{b}$.
# 
#     d. La función $h$ dada por $\displaystyle{ h(x)=\frac{1}{1+e^{-1/x}} }$ no tiene límite en $0$.
# 
#     e. La gráfica de la función $\dfrac{{x}^{3}}{{(x+1)}^2}$ se corta con su asíntota oblícua en un punto de abscisa comprendida entre $-1$ y $0$.
#     
#     f. Todo polinomio $p$ verifica $p(x+y)=p(x) + p(y)$.
