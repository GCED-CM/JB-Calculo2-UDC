#!/usr/bin/env python
# coding: utf-8

# # Introducción a Sympy
# 
# Ademais das variables numéricas existen as variables simbólicas que permiten calcular
# límites, derivadas, integrais etc., como se fai habitualmente nas clases de matemáticas.
# Para poder facer estas operacións, habituais nun curso de Cálculo, é preciso ter instalada a libraría **Sympy**.
# 
# Ao contrario que o módulo **Math** ou o módulo **Numpy** que acabamos de revisar na práctica anterior, o módulo **Sympy** non traballa cunha estrutura de datos baseado en números (xa sexan de tipo enteiro ou dobre) senón que traballa con obxectos que posúen atributos e métodos que tratan de reproducir o comportamento matemático de variables, funcións, rexións, ecuacións, etc. coas que se traballa habitualmente nas disciplinas da álxebra e o cálculo diferencial e integral.
# 
# Para empregar directamente este guión de prácticas dende unha instalación de Python con *Anaconda*, basta con facer clic na aplicación 'Jupyter notebook' que xa está instalada por defecto (para máis detalles: https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html).
# 
# ## Obxectivos:
# 
# - Uso de variables simbólicas
# - Suposicións e requerimentos das variables 
# - Manipulación de expresións sinxelas en varias variables
# 
# 
# ## Instalación e carga do módulo
# Para facer que estea dispoñible o módulo **Sympy**, hai que instalalo usando a ferramente `pip` (ou `conda` se estades a usar entornos de traballo diferenciados). No caso do uso de *Microsoft Azute Notebooks* (https://notebooks.azure.com/), empregaríase a seguinte instalación:

# In[1]:


get_ipython().system('pip -q install sympy')


# Para dispoñer do módulo **Sympy** e importalo para o resto do guión de prácticas, usaremos:

# In[2]:


import sympy as sp


# ## Variables simbólicas
# Para traballar en modo simbólico é necesario definir variables simbólicas e para facer
# isto usaremos o función `sp.Symbol`. Vexamos algúns exemplos do seu uso:

# In[3]:


x = sp.Symbol('x') # define a variable simbólica x
y = sp.Symbol('y') # define a variable simbólica y
f = 3*x + 5*y # agora temos definida a expresion simbólica f
print(f)

a, b, c = sp.symbols('a:c') # define como simbólicas as variables a, b, c.
expresion = a**3 + b**2 + c
print(expresion)


# Por claridade na implementación e nos cálculos, será habitual que o nome da variable simbólica e o nome do obxecto **Sympy** no que se alamacena coincidan, pero isto non ter porque ser así:

# In[4]:


a = sp.Symbol('x')
print(a)
a.name


# Debemos ter claso que agora as variables `x` ou `y` definidas antes non son números, nin tampouco pertencen aos obxectos definidos co módulo **Numpy** revisado na práctica anterior. Todas as variables simbólicas son obxectos da clase `sp.Symbol` e os seus atributos e métodos son completamente diferentes aos que aparecían ás variables numéricas e vectores de **Numpy**:

# In[5]:


print(type(x))
dir(x)


# Con **Sympy** pódense definir constantes enteiras ou números racioanais (todas de forma simbólica) de xeito doado usando o comando `sp.Integer` ou `sp.Rational`. Por exemplo, podemos definir a constante simbólica $1/3$. Se fixeramos o mesmo con números representados por defecto en Python, obteríamos resultados moi diferentes. Observa tamén a diferenza que existe entre o tipo
# de dato asignado no espazo de traballo

# In[6]:


a = sp.Rational('1/3')
b = sp.Integer('1')/sp.Integer('3')
c = 1/3
d = 1.0/3.0
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Outra forma sinxela de manexar valores constante mediante obxectos do módulo **Sympy** é usar a función `sp.S`. Unha vez feitos todos os cálculos simbólicos, se precisamos obter o valor numérico, empregaríase a función `sp.N` ou ben directamente `float`:

# In[7]:


a = sp.S(2)
b = sp.S(6)
c = a/b
d = sp.N(c)
e = float(c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(c)
print(d)
print('{0:.15f}'.format(e))


# Ao longo do curso usaremos asiduamente dous números reais que podes definir como constantes simbólicas: $\pi$ e o numéro $e$. Do mesmo xeito, para operar con variables ou constantes simbólicas, debemos empregar funcións que sexan capaces de manipular este tipo de obxectos, todas elas implementadas no módulo **Sympy** (por exemplo, `sp.sin`, `sp.cos`, `sp.log`, etc)

# In[8]:


p=sp.pi # definición da constante pi
print(sp.cos(p))

e = sp.E # definición do número e
print(sp.log(e))


# ## Suposicións sobre as variables
# 
# Cando se define unha variable simbólica se lle pode asignar certa información adicional sobre o tipo de valores que pode acadar, ou as suposicións que se lle van a aplicar. Por exemplo, podemos decidir antes de facer calquera cálculo se a variable toma valores enteiros ou reais, se é positiva ou negativa, maior que un certo número, etc. Este tipo de información engádese no momento da definición da variable simbólica como un argumento opcional.

# In[9]:


x = sp.Symbol('x', nonnegative = True) # A raíz cadrada dun número non negativo é real
y = sp.sqrt(x)
print(y.is_real)

x = sp.Symbol('x', integer = True) # A potencia dun número enteiro é enteira
y = x**sp.S(2)
print(y.is_integer)

a = sp.Symbol('a')
b = sp.sqrt(a)
print(b.is_real)

a = sp.Symbol('a')
b = a**sp.S(2)
print(b.is_integer)


# Posto que os cálculos simbólicos son consistentes en **Sympy**, se poden tamén facer comprobacións sobre se algunhas desigualdades son certas ou non, sempre e cando se teña coidado nas suposicións que se fagan ao definir as variables simbólicas

# In[10]:


x = sp.Symbol('x', real = True)
p = sp.Symbol('p', positive = True)
q = sp.Symbol('q', real = True)
y = sp.Abs(x) + p # O valor absoluto
z = sp.Abs(x) + q
print(y > 0)
print(z > 0)


# ## Manipulación de expresións simbólicas

# Do mesmo xeito que o módulo **Sympy** nos permite definir variables simbólicas, tamén podemos definir expresións matemáticas a partir destas e manipulalas, factorizándoas, expandíndoas, simplificalas, ou mesmo imprimilas dun xeito similar a como o faríamos con lápiz e papel

# In[11]:


x,y = sp.symbols('x,y', real=True)
expr = (x-3)*(x-3)**2*(y-2)
expr_long = sp.expand(expr) # Expandir expresión

print(expr_long) # Imprimir de forma estándar
sp.pprint(expr_long) # Imprimir de forma semellante a con lápiz e papel

expr_short = sp.factor(expr)
print(expr_short) # Factorizar expresión

expr = -3+(x**2-6*x+9)/(x-3)
expr_simple = sp.simplify(expr) # Simplificar expresión
sp.pprint(expr)
print(expr_simple)


# Dada unha expresión en **Sympy** tamén se pode manipulala, substituindo unhas variables simbólica por outras ou mesmo reemprazando as variables simbólicas por constantes. Para facer este tipo de substitucións emprégase a función `subs` e os valores a utilizar na substitución veñen definidos por un diccionario de Python:

# In[12]:


x,y = sp.symbols('x,y', real=True)
expr = x*x + x*y + y*x + y*y
res = expr.subs({x:1, y:2}) # Substitutición das variables simbólicas por constantes
print(res)

expr_sub = expr.subs({x:1-y}) # Subsitución de variable simbólica por unha expresión
sp.pprint(expr_sub)
print(sp.simplify(expr_sub))


# ## Algunos ejercicios
# 
# ### **Exercicio 2.1** 
# Define a expresión dada pola suma dos termos seguintes:
# $$
# a+a^2+a^3+\ldots+a^N,
# $$
# onde $a$ é unha variable real arbitraria e $N$ e un valor enteiro positivo.

# In[13]:


# O TEU CÓDIGO AQUÍ


# ### **Exercicio 2.2** 
# Cal é o valor exacto da anterior expresión cando $N=15$ e $a=5/6$? Cal é valor numérico en coma flotante?

# In[14]:


# O TEU CÓDIGO AQUÍ

