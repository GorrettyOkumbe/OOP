## OBJECT ORIENTED PROGRAMING
---
This directory is all about object oriented programming in python<br/>
Object oriented is the most used programming paradigm in  most designs today, although some designs still would go for for the procedural way.

When I talk of object oriented it means putting things in classes and in python everthing is an object.

	Parts of an  oop in python
	class: It is the template or blue print of an object
			It's general to all objects.
	object: This is the instance of a class(the specific thing)
			Each object is unique in its own way.
	class and instance attributes:
		In a lay mans language I would refer to attributes as variables(`forgive my manners its for easy understanding`)
		class attributes are owned by the class itself and are shared by all instances(objects) of a class.
		They have the same value for all instances and are defined up above all methods, right below the class header.
		Instance attributes are owned by specific instance of a class.


	Objects are instatiated by the __init__() method.
	The __init__(self,....) is special because it gets called automatically when an object is created.
	Each instance method takes `self` as the first parameter, this refers or represents the object.

	Dunder methods
	---
	These are methods that are preceeded with double underscore and end with double_underscore example
	(__len__, __init__, __repr__)just to mention a few.

	There are methods that perform special functions in a class, as mentioned above __init__, instatiates a object		and gets called automatically when an object is created.

	The __repr__ and __str__ return string representation of an object, __repr__ is for the programmer and can be recasted to an object, where as __str__ is beneficial for the user and cannot be recasted back to an object.
	If only one of the two string representations is to be used that is the __repr__.
---
	## ENCAPSULATION
	___
	This is when opertions are done under methods hence they 
