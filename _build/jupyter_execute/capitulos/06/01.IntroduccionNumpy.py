#!/usr/bin/env python
# coding: utf-8

# # Introducción
# 
# O traballo con números é unha das cuestións comúns e centais en calquere disciplina científica e en particular en enxeñaría de datos. Debido á súa importancia existen unha gran cantidade de librarías dedicadas á implementación de métodos eficientes para manipular números e funcións. Incluso existen linguaxes e entornos de programación especialmente deseñados para este propósito, tales como a linguaxe Fortran ou Matlab/Octave.
# 
# Para a linguaxe Python, que será  a que usaremos no presente curso de *Cálculo Multivariable*, a libraría **NumPy** (http://www.numpy.org/) é a máis amplamente usada para cálculos numéricos.  Esta librería usar un amplo abano de estruturas de datos e funcións para os cálculos numéricos. Neste guión de prácticas, revisaranse algunhas destas funcionalidades. 
# 
# **NumPy** é unha librería enorme e ten funcionalidades moi extensas. Este guión de prácticas soamente reprensenta unha introducción moi breve. Para descrubrir máis funcionalidades e como utilizala con moitos outros propósitos, a mellor fonte de información en liña son os buscadores, e en particular a comunidade http://stackoverflow.com/.
# 
# Para empregar directamente este guión de prácticas dende unha instalación de Python con *Anaconda*, basta con facer clic na aplicación 'Jupyter notebook' que xa está instalada por defecto (para máis detalles: https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html).
# 
# 
# ## Obxectivos
# 
# - Traballar con obxectos e métodos
# - Introduccion aos vectores unidimensionais de números (`numpy.array`) 
# - Aplicar operacións numéricas elementais
# - Manipulación de vectores numéricos (indexado, troceado, etc)
# - Exercicio: eficiencia de **Numpy** en funcións vectorizadas e non vectorizadas

# # Importar o módulo **NumPy**
# 
# Para ter dispoñible **NumPy** no código, débese primeiro importar o seu módulo. Para facer isto, fíxose unha costume moi extendida, importar **Numpy** usando o atallo '`np`': 

# In[3]:


import numpy as np


# # Programación orientada a obxectos
# 
# Como todos os módulos de Python, a libraría **Numpy** está implementada seguindo unha estratexía de programación orientada a obxectos. Polo tanto, calquera estrutura de datos en Python, incluso a máis simple, débese entender como un obxecto que pertence a unha clase, e todas as operaciós que podemos facer con estes obxectos, son métodos implementados sobre esa clase de obxectos. Incluso un número, é un obxecto dunha clase:

# In[4]:


a = 3.3
print(a)
print(type(a))
isinstance(a,float)


# Para comprobar os atributos e os métodos que podemos aplicar sobre un obxecto en particular, podemos empregar a función `dir()`, que nos devolve unha lista cos seus nomes. Como se pode ver na lista, podemos distinguir dos tipos de atributos e métodos: aqueles que van co prefixo e sufixo `__*__` e aqueles que non. Os do primeiro tipo, denóminanse **privados** e habitualmente fan referencia aos cálculos máis básicos que se poden realizar dentro da clase á que pertence o obxecto.

# In[3]:


dir(a)


# Por exemplo, podemos comprobar un número real é maior que outro de dous xeitos diferentes: usando o operador lóxico `>` ou ben usando o seu método privado `__ge__`: 

# In[5]:


a=6.4; b=5.3
print(a.__gt__(b))
print(a > b)


# En calquera caso, en Python tanto os métodos privados como públicos empréganse do mesmo xeito. Por exemplo:

# In[5]:


a=3.4
print(a.is_integer())
print(a.__int__())
print(np.int(a))


# > ** NOTA **: Neste curso non imos a traballar nin será necesario a implementación de código usando unha programación orientada ao obxecto. Pero o que si será necesario será tomar consciencia de cando se usan obxectos de diferentes clases e que atributos e métodos teñen definidos en cada caso

# # Vectores de números
# 
# En Python existen multitude de formas de gardar datos numéricos (ou non) como poden ser a estrutura lista ou tupla. En particular, as listas poden conter unha secuencia finita de números ordeados (e usando un índice para acceder a cada un dos elementos da lista). Ademais, son o suficiente flexibles como para conter datos de diferente natureza (combinacións de números enteiros, reais, listas de listas, etc).
# 
# Pero esta flexibilidade das listas en Python fai que a seu rendemento computacional sexa moi limitado. Na maioría de apliacións científicas en matemáticas e enxeñaría de datos, os problemas reais involucran operacións sobre enormes conxuntos de datos e polo tanto a velocidade computacional é moi importante para estos grandes problemas. Para traballar de forma eficiente con estos problemas, **Numpy** proporciona funcións especializadas e estruturas de datos para o cálculo numérico eficiente. En particular, para o caso de arranxos de números dun mesmo tipo (perdendo parte da flexibilidade das listas pero gañando eficiencia computacional).

# ## Vectores unidimensionais
# 
# Un vector unidimensional é unha colección ordeada de números que se pode acceder mediante un índice (co que se preserva a orde). Por defecto, os vectores en **Numpy** son vectores fila.

# ### Creación de vectores e indexado 
# 
# Para crear un vector **Numpy** de lonxitude 10 e inicializado con ceros, empregaríase a función `np.zeros()`:

# In[6]:


u = np.zeros(10)
print(u)
print(type(u))


# O tipo por defecto dos número que conteñen os vectores en **Numpy** é `float64` (que é o tipo gardado en `np.float`). De querer usar outros tipos, habería que empregar o argumento opcional `dtype`. O tipo dos números que contén un vector pódese comprobar accedendo ao atributo `dtype` dos vectores **Numpy**:

# In[7]:


print(u.dtype)
w = np.zeros(5, dtype=np.int)
print(w)
print(type(w))
print(w.dtype)


# O que non é posible por exemplo é engadir un valor cadea de texto (de tipo `string`) a un obxecto `numpy.ndarray`, xa que todas os elementos do vector deben ser do mesmo tipo (ou dun tipo que admita unha conversión) e deben ter tamén o mesmo tamaño. Para comprobar o tamaño dun vector, pódese usar a función `len`:

# In[8]:


print(len(u))
v = np.zeros(10, dtype=np.int)
print(u + v) # Implicitamente faise unha conversión de tipo de int64 a float64
print(u + w) # ERRO: Os vectores non teñen o mesmo tamaño!


# Unha forma máis específica de comprobar a dimensión dun vector é usar `u.shape`, que nos devolve unha tupla coas dimensións do vector:

# In[9]:


print(u.shape)


# `shape` nos informa sobre o tamaño do vector en *cada* dirección. No caso dos vectores, soamente hai unha única dirección, mentres que en conxuntos de datos con múltiples índices (matrices, ou tensores $n$-dimensionais) `shape` nos informaría do tamaño destas estrutura de datos en cada dirección. Por exemplo, para crear unha matriz de ceros de tipo enteiro de tamaño $2\times 3$:

# In[10]:


A =  np.zeros((2,3), dtype=np.int)
print(A)
print(A.shape)


# We can change the entries of an array using indexing,

# In[11]:


print(u)
u[0] = 10.0
u[3] = -4.3
u[9] = 1.0
print(u)


# > **NOTA IMPORTANTE **: Hai que lembrar que os valores dos índices comezan en cero!
# 
# Evidentemente, existen outras maneiras de crear vectores, como por exemplo o uso da función `ones` para crear un vector que contén soamente 'uns':

# In[12]:


w = np.ones(5)
print(w)
print(w.dtype)


# ou un vector de valores aleatorios:

# In[13]:


w = np.random.rand(6)
print(w)


# ou tamént un vector de números de tipo `numpy.array` a partir dunha lista Python de números:

# In[14]:


u = [4.0, 8.0, 9.0, 11.0, -2.0]
v = np.array(u)
print(v)


# Existen outros dous métodos para crear vectores de números que nos serán de utilidade ao longo do curso (e en particular cando teñamos que pintar funcións nunha ou en varias variables):
# - `numpy.arange` 
# - `numpy.linspace`
# 
# A función `arange` crea un vector con valores enteiros consecutivos (de forma semellante á función de Python `range`). Para crear o vector fila $\vec{u}=(0, 1, 2, 3, 4, 5)$ usando `arange`:

# In[15]:


u = np.arange(6)
print(u)
print(type(u))
print(u.dtype)


# Podemos comprobar que o número $6$ non está incluido xa que o rango de valores comeza en $0$ e o vector soamente posúe seis elementos. Para cambiar o valor numérico no que comeza o vector:

# In[16]:


u = np.arange(2, 6)
print(u)


# A función `linspace` crea un vector de números equiespaciados cun un valor inicial e final (ambos incluídos) e cun tamaño determinado:

# In[17]:


w = np.linspace(0., 100., 6)
print(w)
print(w.dtype)


# Esta función `linspace` xunto coa función `meshgrid` usarase de forma extensiva para pintar funcións de unha e de varias variables ao longo deste curso.

# ### Funcións e aritmética sobre vectores
# 
# Os vectores en **NumPy** soportan as operacións aritmética básica tales como o produto, sumas e restas:

# In[18]:


a = np.array([1.0, 0.2, 1.2])
b = np.array([2.0, 0.1, 2.1])
print(a)
print(b)

# Suma de a e b
c = a + b
print(c)


# e no caso do producto dos seus elementos por un valor escalar,

# In[19]:


c = 10.0*a
print(c)


# e elevar as súas compoñentes a unha potencia:

# In[20]:


a = np.array([2, 3, 4])
print(a**2)


# Tamén se poden aplicar as funcións de cálculo usual a cada unha das súas compoñentes:

# In[21]:


# Crear un vector [0, π/2, π, 3π/2]
a = np.array([0.0, np.pi/2, np.pi, 3*np.pi/2])
print(a)

# Calcular o seno de cada compoñente do vector
b = np.sin(a)
print(b)


# O anteior código calcula o seno de cada coeficiente do vector `a`. Debemos remarcar que a función que se está a usar é `np.sin`, que depende directamente do módulo **Numpy**. O uso de calquera outra implementación da función noutros módulos (por exemplo no módulo **Math**), podería dar lugar a erro.

# Evidentemente, tamén poderíamos calcular o seno de cada coeficiente do vector, accedendo a cada un dos elementos mediante o seu índice e facendo os cálculos no interior dun bucle `for`:

# In[24]:


b = np.zeros(len(a))
for i in range(len(a)):
    b[i] = np.sin(a[i])

print(b)


# Neste caso o programa é máis longo e difícil de ler. Ademais, en moitos casos será máis lento. Á manipulación de vectores e calquera dos cálculos realizados entre eles sen acceder aos índices nos referiremos como 'vectorización'. Cando sexa posible, empregar vectorización incrementará o rendemento e velocidade dos códigos de cálculo. No exercicio final deste guión, analizarase o rendemento deste tipo de técnicas.

# # Troceado de vectores
# 
# Cando se traballa con vectores de números, é habitual ter que extraer un subconxunto destes para crear un novo vector. Por exemplo, obter os tres primeiros coeficientes dun vector ou no caso de matrices, restrinxir os cálculos á súa segunda columna. Este tipo de operacións é o que se denomina troceado de vectores (ou en inglés *array slicing*). 
# 
# Imos a explorar isto mediante varios exemplos, comezando por traballar cun vector de valores aleatorios:

# In[25]:


a = np.random.rand(5)
print(a)


# No que segue, imos a facer varias operacións de troceado:

# In[26]:


# Usar ':' implica o conxunto enterio no rango dos índices, é dicir, dende 0 ata (lonxitude-1)
b = a[:]
print("Troceado usando '[:]' {}".format(b))

# Usar '1:3' implica os índices 1 -> 3 (sen incluir a 3)
b = a[1:3]
print("Troceado usando '[1:3]': {}".format(b))

# Usar '2:-1' implica os índices 2 -> o segundo dende o final (sen incluílo)
b = a[2:-1]
print("Troceado usando '[2:-1]': {}".format(b))

# Usar '2:-2' implica os índices 2 -> o terceiro dende o final (sen incluílo)
b = a[2:-2]
print("Troceado usando '[2:-2]': {}".format(b))


# > **NOTA**: o uso de índice `-1`, correspóndese co último elemento do vector. Do mesmo xeito, o índice `-2` está vinculado ao segundo elemento comezando polo final, etc. Este convenio de referenciar índices dende o final dun vector é moi útil xa co uso destes índices negativos, pódese facer referencia aos últimos coeficientes dun vector sen ter que facer referencia expresa ao tamaño do vector.

# Se o que se quere é trocear un vector dende o comezo ou dende o final do mesmo, hay que empregar a sintaxe de índices con '`:`'

# In[27]:


# Usar ':3' implica usar índices dende o comezo ata 3 (sen incluir o índice 3)
b = a[:3]
print("Troceado usando '[:3]': {}".format(b))

# Usar '4:' imlica os índices dende 4 -> ata o final
b = a[4:]
print("Troceado usando '[4:]': {}".format(b))

# Usar ':' implica todos os índices dende o comezo ata o final
b = a[:]
print("Troceado usando '[:]': {}".format(b))


# O troceado tamén se pode aplicar sobre matrices:

# In[28]:


B = np.array([[1.3, 0], [0, 2.0]])
print(B)

# Extraer a segunda fila
row = B[1, :]
print(row)

# Extraer a primeira columna (almacenada nun vector fila)
col = B[:, 0] 
print(col)


# Existe moitas outras estratexias e sintaxe relacionada co troceado de vectores, que quedan fora do alcance desta introdución breve a **Numpy**. Para unha información máis detallada, pódese consultar: https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

# # Exercicio: aceleración con Numpy no cálculo de normas de vectores
# 
# A norma euclídea (ou módulo) dun vector $\vec{x}=(x_{0},\ldots,x_{n-1})\in\mathbb{R}^{n}$ ven dada por 
# 
# $$
# \| x \| = \sqrt{\sum_{i=0}^{n-1} x_{i} x_{i}}
# $$
# 
# onde $x_{i}$ é o $i$-ésimo coeficiente de $\vec{x}$. En resumo, a súa norma non é máis que o cálculo do produto interior por si mesmo, seguido polo cálculo dunha raíz cadrada. Para calcular o valor da norma, pódense seguir diferentes estratexias: a primeira delas pode ser usar un bucle para recorrer todos os coeficientes do vector e sumar o cadrado de cada coeficiente. Logo coller a suma de todas estas cantidades e calcular a raíz cadrada.
# 
# Para avaliar o rendemento computacional desta implementación, collerase un vector de lonxitude 10 millóns e calcularemos o tempo de cálculo:

# In[29]:


# Crear un vector NumPy con 10 millóns de valores aleatorios
x = np.random.rand(10000000)
print(type(x))


# In[30]:


def compute_norm(x):
    norm = 0.0
    for xi in x:
        norm += xi*xi
    return np.sqrt(norm)

get_ipython().run_line_magic('time', 'norm = compute_norm(x)')
print(norm)


# O tempo de cálculo que nos interesa é o que aparece baixo a etiqueta '`Wall time`'.
# 
# > ** NOTA **: Os detalle de como a etiqueta `%time` traballa neste guión non é de importancia neste curso. Debemos indicar que esta forma de proceder é unicamente válida para consolas ou ficheiros que se executen baixo [I]Python e entornos de servidores Jupyter. Esta forma de traballar é moi compact e conveniente para medir o tempo que se require para completar a execución dunha liña de código.

# ### **Exercicio 1.1** 
# Usando a mesma implementación baseada nun bucle, accede a cada elemento do vector polo seu índice comezando dende o primeiro ata o último. Fai o mesmo cun bucle que acceda en orde inverso, dende o último ata o primeiro.

# In[31]:


# O TEU CÓDIGO AQUÍ


# ### **Exercicio 1.2** 
# Trata de empregar funcións **Numpy** para definir unha función que evite o bucle sobre os coeficientes do vector e que non acceda elemento a elemento no vector (versión vectorizada).

# In[32]:


# O TEU CÓDIGO AQUÍ


# ### **Exercicio 1.3** 
# Compara os tempos de cálculo das catro implementacións para diferentes dimensións do vector $\vec{x}$, de tamaños $10$, $10^3$, $10^5$, $10^7$. A partir destes tempos de cálculo: que se pode deducir como conclusión?

# In[33]:


# O TEU CÓDIGO AQUÍ

