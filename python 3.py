print("Hello")
print("Hello World")

# -> comment

# python interpreter is written in C language
# every line executed in python interpreter is
#   1 statement 
#   2 expression

"Adithi"
"""Adithi"""

100 + 200
_+ 200 # _ is the previous answer

a = "a"
type(a)

# four bacis data types in python
# 1 string
# 2 integer
# 3 float
# 4 complex

# these four are similar to the C interpreter therefore these are considered as the basic

# primitives are inbuild variables that doesnt depend on anything that means those are logics of interpreter 

isinstance("a",int)
isinstance("b", str)

a = 255
print(id(a))

a = 200
print(id(a))

a = 4864121894184121333
print(a+1)
 27  
Class_3_printFunctionalities.py
@@ -0,0 +1,27 @@
# python are platform independent inspiration from linux
# interpreter are platform dependent

print(1)

print(1, 2, 3, "jatin", 3.4, 1 + 5j, sep=",")

print("Hello")
print("World!")

print("Hello", end=":")
print("World!")

# print has accept can take infinite numberof arguments and prints with space
# print after every execution new line character is added

print("a")
print("b")
print("c")

print("a", end=" ")
print("b", end=" ")
print("c")

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep="-")