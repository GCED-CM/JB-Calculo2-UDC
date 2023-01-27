#!/usr/bin/env python
# coding: utf-8

# # Introducción a **NumPy**
# 
# Hasta ahora, dentro de Python, hemos trabajado con el módulo **SymPy**, que nos permite manejar cálculo simbólico, definir nuevas funciones, calcular límites o, como veremos más adelante, derivar e integrar funciones.
# 
# Sin embargo, las posibilidades de Python para el cálculo matemático no acaban, ni mucho menos, aquí. Ahora giraremos nuestra cabeza para buscar una herramienta que convierta a Python en una especie de super-calculadora, con enormes posibilidades a la hora de realizar grandes operaciones repetitivas con números, vectores o matrices. Nosotros le sacaremos el máximo jugo en la programación de los métodos numéricos que estudiaremos en esta materia pero, por supuesto, sus posibilidades son mucho mayores. 
# 
# Yendo al grano, os vamos a presentar la librería **NumPy** (http://www.numpy.org/) que es la más utilizada para cálculos numéricos. Esta librería permite utilizar un enorme abanico de estructuras de datos y funciones para los cálculos numéricos. En esta sección os mostraremos algunas de estas funcionalidades. 
# 
# **NumPy** es una librería enorme y tiene posibilidades muy extensas, por lo que sólo pretendemos realizar una introducción muy breve. Para descubrir nuevas funcionalidades y como utilizarla con muchos otros propósitos, la mejor fuente de información en línea son los buscadores, y, en particular, la comunidad http://stackoverflow.com/.
# 
# ## Objetivos
# 
# - Trabajar con objetos y métodos.
# - Introducción a los vectores unidimensionales de números (`numpy.array`).
# - Aplicar operacines numéricas elementales.
# - Manipulación de vectores numéricos (indexado, troceado, *etc.*).
# - Ejercicio: eficiencia de **NumPy** en funciones vectorizadas y no vectorizadas. 

# **Importar el módulo NumPy**
# 
# Antes de nada, para tener disponible **NumPy** en el código, debemos primero importarlo. Para hacer esto, es habitual importar **NumPy** utilizando el alias `np`: 

# In[1]:


import numpy as np


# ## Programación orientada a objetos
# 
# Como todos los módulos de Python, la librería **NumPy** está implementada siguiendo una estrategia de programación orientada a objetos. Por lo tanto, cualquier estructura de datos en Python, incluso la más simple, se debe entender como un objeto que pertenece a una clase, y sobre ella podemos realizar todas las operaciones implementadas sobre esta clase de objetos. Incluso un número es un objeto de una clase: 

# In[2]:


a = 3.3
print(a)
print(type(a))
isinstance(a,float)


# Para comprobar los atributos y los métodos que podemos aplicar sobre un objeto en particular, podemos emplear la función `dir()`, que nos devuelve una lista con sus nombres. Como se puede ver en la lista, podemos distinguir dos tipos de atributos y métodos: aquéllos que van con prefijo y sufijo `__*__` y aquéllos que no. Los del primer tipo se denominan **privados** y habitualmente hacen referencia a los cálculos más básicos que se pueden realizar dentro de la clase a la que pertenece el objeto. 

# In[4]:


dir(a)


# Por ejemplo, podemos comprobar si un número real es mayor que otro de dos maneras diferentes: utilizando el operador lógico `>` o bien usando su método privado `__ge__`: 

# In[5]:


a=6.4; b=5.3
print(a.__gt__(b))
print(a > b)


# En cualquier caso, en Python tanto los métodos privados como los públicos se utilizan de la misma manera. Por ejemplo:

# In[5]:


a=3.4
print(a.is_integer())
print(a.__int__())
print(np.int(a))


# > **NOTA**: En este curso no vamos a trabajar ni será necesaria la implementación de código utilizando una programación orientada a objetos. Pero lo que sí será necesario es tomar conciencia de cuándo se utilizan objetos de diferentes clases y qué atributos y métodos tiene definido cada caso. 

# ## Vectores de números
# 
# En Python existen multitud de formas de guardar datos numéricos (o no) como pueden ser la estrutura lista o tupla. En particular, las listas pueden contener una secuencia finita de números ordenados (y utilizando un índice para acceder a cada uno de los elementos de la lista). Además, son lo suficientemente flexibles como para contener datos de diferente naturaleza (combinación de números enteros, reales, listas de listas, *etc.*).
# 
# Pero esta flexibilidad de las listas en Python hace que su rendimiento computacional sea muy limitado. En la mayoría de las aplicaciones científicas en matemáticas (con sus aplicaciones a las diferentes partes de la ingeniería informática, inteligencia artificial, ciencia de datos,...), los problemas reales necesitan operaciones sobre enormes conjuntos de datos y, por tanto, la velocidad computacional es muy importante para estos grandes problemas. Para trabajar de forma eficiente con estos problemas, **Numpy** proporciona funciones especializadas y estructuras de datos adecuadas. En particular, para el caso de conjuntos de números de un mismo tipo (perdiendo parte de la flexibilidad de las listas, pero ganando eficacia computacional).  
# 
# **Vectores unidimensionales**: Un vector unidimensional es una colección ordenada de números a los que se puede acceder mediante un índice (con lo que se preserva el orden). Por defecto, los vectores en **NumPy** son vectores fila.
# 
# **Creación de vectores e indexado**: Para crear un vector **Numpy** de longitud 10 e inicializado con ceros, se utilizaría la función `np.zeros()`:

# In[3]:


u = np.zeros(10)
print(u)
print(type(u))


# El tipo por defecto de los números que contienen los vectores en **NumPy** es `float64` (que es el tipo guardado en `np.float`). Si queremos usar otros tipos, tendríamos que utilizar el argumento opcional `dtype`. El tipo de los números que contiene un vector puede comprobarse accediendo al atributo `dtype` de los vectores **NumPy**:

# In[4]:


print(u.dtype)
w = np.zeros(5, dtype=np.int)
print(w)
print(type(w))
print(w.dtype)


# Lo que no es posible, por ejemplo, es añadir un valor del tipo cadena de texto (es decir, de tipo `string`) a un objeto `numpy.ndarray`, ya que todos los elementos del vector deben ser del mismo tipo (o, al menos, de un tipo que admita una conversión) y deben tener también el mismo tamaño. Para comprobar el tamaño de un vector, se puede usar la función `len`:

# In[5]:


print(len(u))
v = np.zeros(10, dtype=np.int)
print(u + v) # Implicitamente se hace una conversión de tipo de int64 a float64
print(u + w) # ERROR: ¡Los vectores no tienen el mismo tamaño!


# Una forma más específica de comprobar la dimensión de un vector es usar `u.shape`, que nos devuelve una tupla con las dimensiones del vector:

# In[9]:


print(u.shape)


# `shape` nos informa sobre el tamaño del vector en *cada* dirección. En el caso de los vectores, solamente hay una única dirección, mentres que en conjuntos de datos con múltiples índices (matrices, o tensores $n$-dimensionales), `shape` nos informaría del tamaño de estas estructuras de datos en cada dirección. Por ejemplo, para crear una matriz de ceros de tipo entero de tamaño $2\times 3$:

# In[10]:


A =  np.zeros((2,3), dtype=np.int)
print(A)
print(A.shape)


# Podemos cambiar las entradas de un vector utilizando la indexación,

# In[11]:


print(u)
u[0] = 10.0
u[3] = -4.3
u[9] = 1.0
print(u)


# > **NOTA IMPORTANTE**: Hay que recordar que en Python los valores de los índices empiezan en 0.
# 
# Evidentemente, existen otras maneras de crear vectores, como, por ejemplo, el uso de la función `ones` para crear un vector que contenga solamente *unos*:

# In[12]:


w = np.ones(5)
print(w)
print(w.dtype)


# o un vector de valores aleatorios:

# In[13]:


w = np.random.rand(6)
print(w)


# o también un vector de números de tipo `numpy.array` a partir de una lista Python de números:

# In[14]:


u = [4.0, 8.0, 9.0, 11.0, -2.0]
v = np.array(u)
print(v)


# Existen otros dos métodos para crear vectores de números que nos serán de utilidad a lo largo del curso (y, en particular, cuando tengamos que pintar funciones con **Matplotlib**):
# - `numpy.arange` 
# - `numpy.linspace`
# 
# La función `arange` crea un vector con valores enteros consecutivos (de forma semejante a la función de Python `range`). Por ejemplo, para crear el vector fila $\vec{u}=(0, 1, 2, 3, 4, 5)$ usando `arange`,

# In[15]:


u = np.arange(6)
print(u)
print(type(u))
print(u.dtype)


# Podemos comprobar que el número $6$ no está incluido ya que el rango de valores comienza en $0$ y el vector solamente posee seis elementos. Para cambiar el valor numérico en el que comienza el vector:

# In[16]:


u = np.arange(2, 6)
print(u)


# La función `linspace` crea un vector de números equiespaciados con un valor inicial y final (ambos incluidos) y con un tamaño determinado:

# In[17]:


w = np.linspace(0., 100., 6)
print(w)
print(w.dtype)


# Esta función `linspace`, junto con la función `meshgrid`, se usará de forma habitual para pintar funciones con **Matplotlib** a lo largo de este curso.

# ## Funciones y aritmética sobre vectores
# 
# Los vectores en **NumPy** soportan las operaciones aritméticas básicas (producto, sumas, restas, *etc.*):

# In[18]:


a = np.array([1.0, 0.2, 1.2])
b = np.array([2.0, 0.1, 2.1])
print(a)
print(b)

# Suma de a e b
c = a + b
print(c)


# y el producto de todos sus elementos por un valor escalar,

# In[19]:


c = 10.0*a
print(c)


# y elevar todas sus componentes a una potencia:

# In[20]:


a = np.array([2, 3, 4])
print(a**2)


# También se pueden aplicar las funciones de cálculo usual a cada una de sus componentes:

# In[6]:


# Crear un vector [0, π/2, π, 3π/2]
a = np.array([0.0, np.pi/2, np.pi, 3*np.pi/2])
print(a)

# Calcular el seno de cada componente del vector
b = np.sin(a)
print(b)


# El código anterior calcula el seno de cada coeficiente del vector `a`. Debemos remarcar que la función que se está usando es `np.sin`, que depende directamente del módulo **NumPy**. El uso de cualquier otra implementación de la función en otros módulos (por ejemplo, en el módulo **Math**), podría dar lugar a error.
# 
# Evidentemente, también podríamos calcular el seno de cada coeficiente del vector, accediendo a cada uno de los elementos mediante su índice y haciendo los cálculos en el interior de un bucle `for`:

# In[24]:


b = np.zeros(len(a))
for i in range(len(a)):
    b[i] = np.sin(a[i])

print(b)


# En este caso el programa es más largo y difícil de leer. Además, en muchos casos será más lento. La manipulación de vectores y cualquiera de los cálculos realizados entre ellos sin acceder a los índices suelen conocerse como **vectorización**. Cuando sea posible emplearla, la vectorización incrementará el rendimiento y la velocidad de los códigos de cálculo. En el ejercicio final de este guión, se analizará el rendimiento de este tipo de técnicas.

# ## Troceado de vectores
# 
# Cuando se trabaja con vectores de números, es habitual tener que extraer un subconjunto de estos para crear un nuevo vector. Por ejemplo, obtener los tres primeros coeficientes de un vector o, en el caso de matrices, restringir los cálculos a su segunda columna. Este tipo de operaciones es el que se denomina troceado de vectores (o, en inglés, *array slicing*). 
# 
# Vamos a explorar esto mediante varios ejemplos, trabajando con un vector de valores aleatorios:

# In[6]:


a = np.random.rand(5)
print(a)

# Usar ':' implica el conjunto entero en el rango de los índices, es decir, desde 0 hasta (longitud-1)
b = a[:]
print("Troceado usando '[:]' {}".format(b))

# Usar '1:3' implica los índices 1 -> 3 (sin incluir a 3)
b = a[1:3]
print("Troceado usando '[1:3]': {}".format(b))

# Usar '2:-1' implica los índices 2 -> el segundo desde el final (sin incluirlo)
b = a[2:-1]
print("Troceado usando '[2:-1]': {}".format(b))

# Usar '2:-2' implica los índices 2 -> el tercero desde el final (sin incluirlo)
b = a[2:-2]
print("Troceado usando '[2:-2]': {}".format(b))


# > **NOTA**: el uso del índice `-1`, se corresponde con el último elemento del vector. Del mismo modo, el índice `-2` corresponde al penúltimo elemento, *etc.*. Este convenio de referenciar índices desde el final de un vector es muy útil, ya que con el uso de estos índices negativos se puede hacer referencia a los últimos coeficientes de un vector sin tener que hacer referencia expresa a su tamaño (o, incluso, sin conocerlo explícitamente).

# Si lo que se quiere es trocear un vector desde el principio o desde el final del mismo hay que utilizar la sintaxis de índices con '`:`'

# In[8]:


# Usar ':3' implica usar índices desde el principio hasta 3 (sin incluir el índice 3)
b = a[:3]
print("Troceado usando '[:3]': {}".format(b))

# Usar '4:' implica los índices desde 4 -> hasta el final
b = a[4:]
print("Troceado usando '[4:]': {}".format(b))

# Usar ':' implica todos los índices desde el comienzo hasta el final
b = a[:]
print("Troceado usando '[:]': {}".format(b))


# El troceado también se puede aplicar a matrices:

# In[9]:


B = np.array([[1.3, 0], [0, 2.0]])
print(B)

# Extraer la segunda fila
row = B[1, :]
print(row)

# Extraer la primera columna (almacenada en un vector fila)
col = B[:, 0] 
print(col)


# Existen muchas otras estrategias y sintaxis relacionada con el troceado de vectores, que quedan fuera del alcance de esta introdución breve a **NumPy**. Para una información más detallada, se puede consultar: https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

# ## Ejercicio: aceleración con NumPy en el cálculo de normas de vectores
# 
# La norma euclídea (o *módulo*) de un vector $\vec{x}=(x_{0},\ldots,x_{n-1})\in\mathbb{R}^{n}$ viene dada por 
# 
# $$
# \| x \| = \sqrt{\sum_{i=0}^{n-1} x_{i} x_{i}},
# $$
# 
# donde $x_{i}$ es el $i$-ésimo coeficiente de $\vec{x}$. En resumen, su norma no es más que el cálculo del producto interior del vector por sí mismo, seguido por el cálculo de una raíz cuadrada. Para calcular el valor de la norma se pueden seguir diferentes estrategias: la primera de ellas puede ser usar un bucle para recorrer todos los coeficientes del vector y sumar el cuadrado de cada coeficiente, luego tomar la suma de todas estas cantidades y calcular su raíz cadrada.
# 
# Para evaluar el rendimiento computacional de esta implementación, vamos a coger un vector moderadamente grande (10 millones) y vamos a calcular el tiempo de cáculo:

# In[8]:


# Crear un vector NumPy con 10 millones de valores aleatorios
x = np.random.rand(10000000)
print(type(x))


# In[9]:


def compute_norm(x):
    norm = 0.0
    for xi in x:
        norm += xi*xi
    return np.sqrt(norm)

get_ipython().run_line_magic('time', 'norm = compute_norm(x)')
print(norm)


# El tiempo de cálculo que nos interesa es el que aparece bajo la etiqueta '`Wall time`'.
# 
# > **NOTA**: Los detalle de como la etiqueta `%time` trabaja en este guión no son de importancia en este curso. Debemos indicar que esta forma de proceder es únicamente válida para consolas o ficheiros que se ejecuten bajo [I]Python y entornos de servidores Jupyter. Esta forma de trabajar es muy compacta y conveniente para medir el tiempo que se requiere para completar la ejecución de una línea de código.

# **Ejercicio 1:** 
# Usando la misma implementación basada en un bucle, accede a cada elemento del vector por su índice, comenzando desde el primero hasta el último. Haz lo mismo con un bucle que acceda en orde inverso, desde el último hasta el primero.

# In[31]:


# ESCRIBE AQUÍ TU CÓDIGO


# **Ejercicio 2:** 
# Trata de emplear funciones **NumPy** para definir una función que evite el bucle sobre los coeficientes del vector y que no acceda elemento a elemento al mismo (es decir, haz una versión vectorizada del cálculo de la norma euclídea).

# In[32]:


# ESCRIBE AQUÍ TU CÓDIGO


# **Ejercicio 3:** 
# Compara los tiempos de cálculo de las cuatro implementaciones para diferentes dimensiones del vector $\vec{x}$, de tamaños $10$, $10^3$, $10^5$, $10^7$. A partir de estos tiempos de cálculo: ¿qué se puede deducir como conclusión?

# In[33]:


# ESCRIBE AQUÍ TU CÓDIGO

