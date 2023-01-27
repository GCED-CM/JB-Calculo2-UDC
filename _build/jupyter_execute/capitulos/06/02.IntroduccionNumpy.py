#!/usr/bin/env python
# coding: utf-8

# (sec:introduccion_Numpy)=
# # Introducción a Numpy
# 
# El trabajo con números es una de las cuestiones comunes y centrales en cualquier disciplina científica y en particular en ingeniería de datos. Debido a su importancia existen una gran cantidad de librerías dedicadas a la implementación de métodos eficientes para manipular números y funciones. Incluso existen lenguajes y entornos de programación especialmente diseñados para este propósito, tales como el lenguaje Fortran o Matlab/Octave.
# 
# Para el lenguaje Python, que es el empleado en esta asignatura, la librería **NumPy** (http://www.numpy.org/) es la más ampliamente usada para cálculos numéricos. Esta librería permite usar un amplio abanico de estructuras de datos y funciones para cálculos numéricos. En esta sección, revisaremos algunas de estas funcionalidades. 
# 
# **NumPy** es una librería enorme y tiene funcionalidades muy extensas. En esta sección realizaremos una introducción muy breve. Para descrubrir más funcionalidades y cómo utilizarla con muchos otros propósitos, la mejor fuente de información en línea son los buscadores, y en particular la comunidad http://stackoverflow.com/.
# 
# ## Objetivos
# 
# - Trabajar con objetos y métodos.
# - Introducción a los vectores unidimensionales de números (`numpy.array`). 
# - Aplicar operaciones numéricas elementales.
# - Manipulación de vectores numéricos (indexado, troceado, etc.).
# - Ejercicio: eficiencia de **Numpy** en funciones vectorizadas y no vectorizadas.

# ## Importar el módulo **NumPy**
# 
# Para tener disponible **NumPy** en el código, debemos primero importarlo. Para ello, resulta habitual importar **Numpy** utilizando la abreviatura '`np`': 

# In[108]:


import numpy as np


# Además, para poder trabajar en modo simbólico, será preciso también importar el módulo **Sympy**:

# In[115]:


import sympy as sp


# ## Programación orientada a objetos
# 
# Como todos los módulos de Python, la librería **Numpy** está implementada siguiendo una estrategia de programación orientada a objetos. Por tanto, cualquier estructura de datos en Python, incluso la más simple, se debe entender como un objeto que pertenece a una clase, al que se le pueden aplicar todas las operaciones implementadas sobre esa clase de objetos (a las que se le llaman métodos de la clase). Incluso un número, es un objeto de una clase:

# In[78]:


a = 3.3
print(a)
print(type(a))
isinstance(a,float)


# Para comprobar los atributos y los métodos que podemos aplicar sobre un objeto en particular, podemos utilizar la función `dir()`, que nos devuelve una lista con sus nombres. Podemos distinguir entre dos tipos de atributos y métodos: los **privados** que son los que habitualmente hacen referencia a los cálculos más básicos y en cuyo nombre aparece el prefijo y sufijo `__*__`, y los **públicos**. Teclea `dir(a)` para comprobar los atributos y métodos que podemos aplicar sobre `a`.

# Por ejemplo, podemos comprobar si un número real es mayor que otro de dos formas diferentes: utilizando el operador lógico `>` o bien aplicando su método privado correspondiente `__gt__`: 

# In[80]:


a=6.4; b=5.3
print(a.__gt__(b))
print(a > b)


# En cualquier caso, en Python tanto los métodos privados como los públicos se aplican de la misma manera. Por ejemplo:

# In[81]:


a=3.4
print(a.is_integer())
print(a.__int__())
print(np.int(a))


# > ** NOTA **: En este curso no vamos a trabajar ni será necesaria la implementación de código utilizando una programación orientada a objetos. Pero lo que sí será necesario es ser consciente de las diferentes clases de objetos que se utilicen y de los atributos y métodos definidos sobre cada una de ellas.

# ## Vectores de números
# 
# En Python existen multitud de formas de guardar datos numéricos (o no) como pueden ser la estructura lista o tupla. Las listas en Python presentan una gran flexibilidad (pudiendo contener datos de diferente naturaleza) lo que hace que su rendimiento computacional sea muy limitado. En la mayoría de aplicaciones científicas en matemáticas e ingeniería de datos, los problemas reales involucran operaciones sobre enormes conjuntos de datos y por lo tanto la velocidad computacional es muy importante para estos grandes problemas. Para trabajar de forma eficiente con estos problemas, **Numpy** proporciona funciones especializadas y estructuras de datos para el cálculo numérico eficiente. En particular, para el caso de conjuntos de números de un mismo tipo (perdiendo parte de la flexibilidad de las listas pero ganando eficiencia computacional).

# ## Vectores unidimensionales
# 
# Un vector unidimensional es una colección ordenada de números a los que se puede acceder mediante el índice correspondiente (en el caso de Python, empezando a contar en cero). Por defecto, los vectores en **Numpy** son vectores fila.

# ## Creación de vectores e indexado 
# 
# Para crear un vector **Numpy** que contiene solamente 'ceros' o 'unos', se pueden utilizar, respectivamente, las funciones `np.zeros()` o `np.ones()`. También podemos hacer uso de la función `np.random.rand()` para crear un vector con valores aleatorios:

# In[82]:


u = np.zeros(10) #creamos un vector Numpy de longitud 10 de ceros
v = np.ones(5) #creamos un vector Numpy de longitud 5 de unos
r = np.random.rand(6) #creamos un vector Numpy de longitud 6 con valores aleatorios
print(u)
print(v)
print(r)
print(type(u),type(v),type(r))


# El tipo por defecto de los números que contienen los vectores en **Numpy** es `float64` (que es el tipo guardado en `np.float`). Si queremos usar otros tipos, tendríamos que utilizar el argumento opcional `dtype`. Se puede comprobar el tipo de los números de un vector accediendo al atributo `dtype` de los vectores **Numpy**:

# In[83]:


print(u.dtype,v.dtype,r.dtype)
w = np.zeros(10, dtype=np.int)
print(w)
print(type(w))
print(w.dtype)
print(u + w) # Implícitamente se hace una conversión de tipo de int64 a float64 
print(u + v) # ERROR: Los vectores non tienen el mismo tamaño!


# Podemos cambiar los coeficientes de un vector utilizando la indexación,

# In[11]:


print(u)
u[0] = 10.0
u[3] = -4.3
u[9] = 1.0
print(u)


# > **NOTA IMPORTANTE **: Hai que recordar que en Python los valores de los índices empiezan en cero!
# 
# Evidentemente, existen otras maneras de crear vectores de números de tipo `numpy.array`, como, por ejemplo, aplicando la función `np.array()` a una lista Python de números:

# In[57]:


u = [4.0, 8.0, 9.0, 11.0, -2.0]
v = np.array(u) 
print(v)
print(type(u))
print(type(v))


# Además, existen otros dos métodos para crear vectores de números que nos serán de utilidad a lo largo del curso (y en particular cando tegamos que pintar funciones con **Matplotlib** en una o en varias variables):
# - `numpy.arange` 
# - `numpy.linspace`
# 
# La función `arange` crea un vector con valores enteros consecutivos (de forma semejante a la función de Python `range`). Por ejemplo, podemos crear el vector fila $\vec{u}=(0, 1, 2, 3, 4, 5)$ usando `arange`,

# In[84]:


u = np.arange(6)
print(u)
print(type(u))
print(u.dtype)


# Podemos comprobar que el número $6$ no está incluido ya que el rango de valores comienza en $0$ y el vector solamente posee seis elementos. Sin embargo, podemos especificar el valor numérico en el que comienza y finaliza el vector: 

# In[85]:


u = np.arange(2, 6)
print(u)


# La función `linspace` junto con la función `meshgrid` se usará de forma habitual para pintar funciones de una y varias variables a lo largo de este curso. Esta función `linspace` crea un vector de números equiespaciados con un valor inicial y final (ambos incluidos) y con un tamaño determinado:

# In[86]:


w = np.linspace(0., 100., 6)
print(w)
print(w.dtype)


# Para comprobar el tamaño de un vector, se puede usar la función `len`, aunque una forma más general de comprobar la dimensión del vector w es usar `w.shape`, que nos devuelve una tupla con las dimensiones del vector:

# In[87]:


print(len(w))
print(w.shape)


# `shape` nos informa sobre el tamaño del vector en *cada* dirección. En el caso de los vectores, hay una única dirección, mientras que en conjuntos de datos con múltiples índices (matrices, o tensores $n$-dimensionales) `shape` nos informaría del tamaño de estas estructuras de datos en cada dirección. Por ejemplo, creamos a continuación una matriz de ceros de tipo entero de tamaño $2\times 3$ y comprobamos su tamaño:

# In[88]:


A =  np.zeros((2,3), dtype=np.int)
print(A)
print(A.shape)


# ## Aritmética y funciones sobre vectores
# 
# Los vectores en **NumPy** soportan las operaciones aritméticas básicas (sumas, restas, productos, etc.):

# In[89]:


a = np.array([1.0, 0.2, 1.2])
b = np.array([2.0, 0.1, 2.1])
print(a)
print(b)

# Suma de a y b
c = a + b
print(c)


# y en el caso del producto de sus elementos por un valor escalar,

# In[90]:


c = 10.0*a
print(c)


# y de elevar todas sus componentes a una potencia:

# In[91]:


a = np.array([2, 3, 4])
print(a**2)


# También se pueden aplicar las funciones de cálculo de **Numpy** a cada una de sus componentes:

# In[104]:


# Crear el vector [0, π/2, π, 3π/2]
a = np.array([0.0, np.pi/2, np.pi, 3*np.pi/2])
print(a)

# Calcular el seno de cada componente del vector
b = np.sin(a)
print(b)


# El código aterior calcula el seno de cada componente del vector `a`. Debemos remarcar que la función que se está utilizando es `np.sin`, que depende directamente del módulo **Numpy**. El uso de cualquier otra implementación de la función en otros módulos (por ejemplo, en el módulo **Sympy**), podría dar lugar a error. Sin embargo, se pueden traducir objetos que dependen del módulo **Sympy** a objetos del módulo **Numpy** a través del método `sp.lambdify`:

# In[116]:


x = sp.Symbol('x', real=True) # definimos la variable simbólica x
f = sp.lambdify(x,sp.sin(x),"numpy") # función numpy con la expresión del seno
b = f(a) # Calcular el seno de cada componente del vector
print(b)


# Evidentemente, también se podría calcular el seno de cada componente del vector, accediendo a cada uno de los elementos mediante su índice y haciendo los cálculos en el interior de un bucle `for`:

# In[93]:


b = np.zeros(len(a)) #inicializamos el vector resultante
for i in range(len(a)):
    b[i] = np.sin(a[i])

print(b)


# En este caso el programa es más largo y difícil de leer. Además, en muchos casos será más lento. A la manipulación de vectores y cualquiera de los cálculos realizados entre ellos sin acceder a sus índices suele conocerse como 'vectorización'. Cuando sea posible emplearla, la vectorización incrementará el rendimiento y velocidad de los códigos de cálculo. En el ejercicio final de este guión, se analizará el rendimiento de este tipo de técnicas.

# ## Troceado de vectores
# 
# Cuando se trabaja con vectores de números, es habitual tener que extraer un subconjunto de estos para crear un nuevo vector. Por ejemplo, obtener los tres primeros coeficientes de un vector o, en el caso de matrices, restringir los cálculos a su segunda columna. A este tipo de operaciones se le denomina troceado de vectores (o, en inglés, *array slicing*). 
# 
# Vamos a explorar esto mediante varios ejemplos, empezando mediante un vector de valores aleatorios:

# In[103]:


a = np.random.rand(5)
print(a)

# Usar ':' implica el conjunto entero en el rango de los índices, es decir, desde 0 hasta longitud-1
b = a[:]
print("Troceado usando '[:]' {}".format(b))

# Usar '1:3' implica los índices 1 -> 3 (sin incluir a 3)
b = a[1:3]
print("Troceado usando '[1:3]': {}".format(b))

# Usar '2:-1' implica los índices 2 -> el primero desde el final (sin incluirlo)
b = a[2:-1]
print("Troceado usando '[2:-1]': {}".format(b))

# Usar '2:-2' implica los índices 2 -> el segundo desde el final (sin incluirlo)
b = a[2:-2]
print("Troceado usando '[2:-2]': {}".format(b))

# Usar ':3' implica usar índices dende el principio hasta 3 (sin incluir el índice 3)
b = a[:3]
print("Troceado usando '[:3]': {}".format(b))

# Usar '4:' implica los índices desde 4 -> hasta el final
b = a[4:]
print("Troceado usando '[4:]': {}".format(b))


# > **NOTA**: el uso del índice `-1`, se asocia con el último elemento del vector. Del mismo modo, el índice `-2` está vinculado al segundo elemento empezando por el final, etc. Este convenio de referenciar índices desde el final de un vector es muy útil ya que con el uso de estos índices negativos se puede hacer referencia a los últimos coeficientes de un vector sin tener que hacer referencia expresa a su tamaño.

# El troceado también se puede aplicar a matrices:

# In[95]:


B = np.array([[1.3, 0], [0, 2.0]])
print(B)

# Extraer la segunda fila
row = B[1, :]
print(row)

# Extraer la primera columna (almacenada en un vector fila)
col = B[:, 0] 
print(col)


# Existen muchas otras estrategias y sintaxis relacionadas con el troceado de vectores, que quedan fuera del alcance de esta  breve introducción a **Numpy**. Para una información más detallada, se puede consultar: https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

# ## Ejercicio: aceleración con Numpy en el cálculo de normas de vectores
# 
# La norma euclídea (o módulo) de un vector $\vec{x}=(x_{0},\ldots,x_{n-1})\in\mathbb{R}^{n}$ viene dada por 
# 
# $$
# \| \vec{x} \| = \sqrt{\sum_{i=0}^{n-1} x_{i} x_{i}}
# $$
# 
# donde $x_{i}$ es el $i$-ésimo coeficiente de $\vec{x}$. En resumen, su norma no requiere más que el cálculo del producto interior por sí mismo, seguido por el cálculo de una raíz cuadrada. Para calcular el valor de la norma, se pueden seguir diferentes estrategias: la primera de ellas puede consistir en usar un bucle para recorrer todos los coeficientes del vector y sumar el cuadrado de cada coeficiente, luego coger la suma de todas estas cantidades y calcular la raíz cuadrada.
# 
# Para evaluar el rendimiento computacional de esta implementación, vamos a coger un vector moderadamente grande (con 10 millones de elementos) y calcular su tiempo de cálculo:

# In[96]:


# Crear un vector NumPy con 10 millones de valores aleatorios
x = np.random.rand(10000000)
print(type(x))


# In[97]:


def compute_norm(x):
    norm = 0.0
    for xi in x:
        norm += xi*xi
    return np.sqrt(norm)

get_ipython().run_line_magic('time', 'norm = compute_norm(x)')
print(norm)


# El tiempo de cálculo que nos interesa es el que aparece bajo la etiqueta '`Wall time`'.
# 
# > ** NOTA **: Los detalles de cómo la etiqueta `%time` trabaja en este guión non son de importancia en este curso. Debemos indicar que esta forma de proceder es únicamente válida para consolas o ficheros que se ejecuten bajo [I]Python y entornos de servidores Jupyter. Esta forma de trabajar es muy compacta y conveniente para medir el tiempo que se requiere para completar la ejecución de una línea de código.

# ### **Ejercicio 1** 
# Usando la misma implementación basada en un bucle, accede a cada elemento del vector por su índice comenzando desde el primero hasta el último. Haz lo mismo con un bucle que acceda en orden inverso, desde el último hasta el primero.

# In[98]:


# ESCRIBE AQUÍ TU CÓDIGO


# ### **Ejercicio 2** 
# Trata de emplear funciones **Numpy** para definir una función que evite el bucle sobre los coeficientes del vector y que no acceda elemento a elemento del mismo (versión vectorizada).

# In[99]:


# ESCRIBE AQUÍ TU CÓDIGO


# > ** NOTA **: La función `np.dot(,)` permite calcular el producto interior de dos vectores.

# ### **Ejercicio 3** 
# Compara los tiempos de cálculo de las cuatro implementaciones para diferentes dimensiones del vector $\vec{x}$, de tamaños $10$, $10^3$, $10^5$, $10^7$. A partir de estos tiempos de cálculo: ¿qué se puede deducir como conclusión?

# In[30]:


# ESCRIBE AQUÍ TU CÓDIGO

