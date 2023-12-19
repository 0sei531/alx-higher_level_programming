What is OOP (Object-Oriented Programming):
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into reusable and self-contained objects. Objects represent real-world entities, and they encapsulate data (attributes) and behavior (methods). OOP principles include encapsulation, inheritance, and polymorphism, providing a modular and structured way to design and organize code.

"First-class Everything":
In Python, everything is considered an object, and objects are first-class citizens. This means that objects can be assigned to variables, passed as arguments to functions, and returned from functions. Functions, classes, and modules are all first-class entities in Python.

What is a Class:
A class in Python is a blueprint for creating objects. It defines a data structure along with methods that operate on the data. Objects created from a class are instances of that class.

What is an Object and an Instance:
An object is an instance of a class, representing a specific realization of that class. An instance is a concrete occurrence of a class in memory.

Difference Between a Class and an Object or Instance:
A class is a template or blueprint for creating objects, while an object or instance is a specific realization created from that template.

What is an Attribute:
An attribute is a piece of data that belongs to an object or class. Attributes are variables that store information about the object's state.

Public, Protected, and Private Attributes:
In Python, attributes can be public, protected, or private. Public attributes are accessible from anywhere. Protected attributes start with a single underscore and are considered protected but can still be accessed. Private attributes start with a double underscore and are not directly accessible from outside the class.

What is self:
self is a convention in Python that refers to the instance of the class. It is the first parameter in the method definition and allows methods to access and modify the object's state.

What is a Method:
A method is a function defined inside a class. It operates on the data (attributes) of an object and may modify the object's state.

The Special __init__ Method:
__init__ is a special method in Python classes, known as the constructor. It is called automatically when an object is created from the class and is used to initialize the object's attributes.

Data Abstraction, Data Encapsulation, and Information Hiding:

Data Abstraction: The concept of exposing only essential information and hiding the implementation details.
Data Encapsulation: Bundling the data (attributes) and the methods that operate on the data within a class, enforcing access through methods.
Information Hiding: Restricting access to certain details, allowing only what is necessary to be visible.
What is a Property:
A property in Python is a special kind of attribute managed by getter, setter, and deleter methods. It allows controlled access to class attributes.

Difference Between an Attribute and a Property in Python:
An attribute is a variable that holds data, while a property is an attribute that uses getter, setter, and deleter methods to control access and modification.

Pythonic Way to Write Getters and Setters:
The Pythonic way is to use properties rather than explicit getter and setter methods. Decorators like @property, @<attribute>.setter, and @<attribute>.deleter help define properties.

Dynamically Create Arbitrary New Attributes:
New attributes can be dynamically added to an object using the dot notation or the setattr function.

Bind Attributes to Objects and Classes:
Attributes are bound to objects by assigning values to them. Class attributes are shared among all instances, while instance attributes are specific to each instance.

__dict__ of a Class and/or Instance:
__dict__ is a dictionary that holds the namespace of a class or an instance. It contains the mapping of attribute names to their values.

How Does Python Find Attributes:
When an attribute is accessed, Python first looks for it in the instance's namespace (__dict__). If not found, it searches in the class hierarchy.

How to Use getattr Function:
The getattr function is used to get the value of an attribute. It takes the object and the attribute name as arguments.
