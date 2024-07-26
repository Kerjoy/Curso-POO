def loop(element):
    for item in element:
        print(f"actual element:{item}")
        
list1 = [1,2,3,4,5]
list2 = "machine"

loop(list2)

"""
Duck typing
Duck Typing is a way of programming in which an object passed into a function or method supports
all method signatures and attributes expected of that object at run time. The object's type itself
is not important. Rather, the object should support all methods/attributes called on it. For this
reason, duck typing is sometimes seen as "a way of thinking rather than a type system".

In duck typing, we don't declare the argument types in function prototypes or methods.
This implies that compilers can't do type checking. What really matters is if the object has the
particular methods/attributes at run time. Duck typing is therefore often supported by dynamic 
languages. However, some static languages are beginning to "mimic" it via structural typing.

Enlaces dinamicos
Enlaces estaticos
El enlace dinámico es un mecanismo por el cual se escoge, en tiempo de ejecución, el método
que responderá a un determinado mensaje. Es útil cuando este no puede ser determinado de forma 
estática, es decir, en tiempo de compilación.

Tipo real
Comportamientos diferentes, asociados a objetos distintos, pueden compartir el mismo nombre;
al llamarlos por ese nombre se utilizará el comportamiento correspondiente al objeto que se esté
usando. O, dicho de otro modo, las referencias y las colecciones de objetos pueden contener
objetos de diferentes tipos, y la invocación de un comportamiento en una referencia producirá
el comportamiento correcto para el tipo real del objeto referenciado
Tipo declarado
"""