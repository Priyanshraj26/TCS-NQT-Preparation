#!/usr/bin/env python3
"""Generate OOP PDF for TCS NQT Preparation"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.pdf_generator import TCSNQTPDFGenerator

def main():
    pdf = TCSNQTPDFGenerator(
        output_path=os.path.join(os.path.dirname(__file__), '..', '03-Core-CS-Subjects', 'PDFs', 'OOP.pdf'),
        title="Object-Oriented Programming",
        subject="TCS NQT - Core CS Subjects"
    )
    pdf.add_cover_page()

    q = 1

    # =========================================================================
    # SECTION 1: Classes & Objects (10 Questions)
    # =========================================================================
    pdf.add_topic_header("Section 1: Classes & Objects",
        "Constructors, destructors, this pointer, static members, and basic class concepts.")

    pdf.add_question(q, "What is a class in OOP?",
        {'A': 'An instance of an object', 'B': 'A blueprint for creating objects', 'C': 'A type of function', 'D': 'A variable type'},
        "B) A blueprint for creating objects",
        "A class defines the structure (attributes) and behavior (methods) that objects of that type will have.",
        "Easy"); q+=1

    pdf.add_question(q, "Which constructor is called when no arguments are passed during object creation?",
        {'A': 'Parameterized constructor', 'B': 'Copy constructor', 'C': 'Default constructor', 'D': 'Conversion constructor'},
        "C) Default constructor",
        "A default constructor takes no arguments. If no constructor is defined, the compiler provides one.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the purpose of a destructor?",
        {'A': 'To create objects', 'B': 'To initialize objects', 'C': 'To release resources when an object is destroyed', 'D': 'To copy objects'},
        "C) To release resources when an object is destroyed",
        "Destructors are called when an object goes out of scope or is deleted, freeing allocated resources.",
        "Easy"); q+=1

    pdf.add_question(q, "In C++, what does the 'this' pointer refer to?",
        {'A': 'The class itself', 'B': 'The current object', 'C': 'The parent class', 'D': 'The base class'},
        "B) The current object",
        "The 'this' pointer is an implicit pointer available in non-static member functions, pointing to the calling object.",
        "Easy"); q+=1

    pdf.add_question(q, "A static member variable in a class is:",
        {'A': 'Unique to each object', 'B': 'Shared among all objects of the class', 'C': 'Only accessible in constructors', 'D': 'Automatically initialized to null'},
        "B) Shared among all objects of the class",
        "Static members belong to the class, not individual objects. All objects share the same copy.",
        "Medium"); q+=1

    pdf.add_question(q, "Can a static member function access non-static data members?",
        {'A': 'Yes, always', 'B': 'No, it cannot', 'C': 'Only if the object is passed as parameter', 'D': 'Only in the constructor'},
        "C) Only if the object is passed as parameter",
        "Static functions have no 'this' pointer, so they cannot directly access non-static members. An object reference must be passed.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the output when a copy constructor is invoked?",
        {'A': 'A new object identical to the original', 'B': 'A reference to the original object', 'C': 'A null object', 'D': 'A shallow copy only'},
        "A) A new object identical to the original",
        "A copy constructor creates a new object as a copy of an existing object. By default it performs a shallow copy.",
        "Medium"); q+=1

    pdf.add_question(q, "In C++, which keyword is used to define a class?",
        {'A': 'struct', 'B': 'class', 'C': 'object', 'D': 'type'},
        "B) class",
        "The 'class' keyword defines a class. 'struct' can also define a class in C++, but members are public by default.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the difference between a struct and a class in C++?",
        {'A': 'No difference', 'B': 'Struct members are public by default, class members are private', 'C': 'Struct cannot have methods', 'D': 'Class cannot have data members'},
        "B) Struct members are public by default, class members are private",
        "The only difference in C++ is default access: struct = public, class = private.",
        "Medium"); q+=1

    pdf.add_question(q, "How many times is the constructor called when creating an array of 5 objects?",
        {'A': '1', 'B': '5', 'C': '0', 'D': '10'},
        "B) 5",
        "The default constructor is called once for each element in the array, so 5 times for an array of 5.",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 2: Inheritance (12 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 2: Inheritance",
        "Single, multiple, multilevel, hierarchical inheritance, diamond problem, and virtual inheritance.")

    pdf.add_question(q, "Inheritance in OOP represents which relationship?",
        {'A': 'Has-a', 'B': 'Is-a', 'C': 'Uses-a', 'D': 'Part-of'},
        "B) Is-a",
        "Inheritance models an 'is-a' relationship (e.g., Dog is-a Animal). Composition models 'has-a'.",
        "Easy"); q+=1

    pdf.add_question(q, "In multilevel inheritance, class C inherits from B which inherits from A. What can C access?",
        {'A': 'Only B members', 'B': 'Only A members', 'C': 'Both A and B public/protected members', 'D': 'Neither A nor B members'},
        "C) Both A and B public/protected members",
        "In multilevel inheritance, the derived class can access public and protected members of all ancestor classes.",
        "Medium"); q+=1

    pdf.add_question(q, "The diamond problem occurs in:",
        {'A': 'Single inheritance', 'B': 'Multilevel inheritance', 'C': 'Multiple inheritance', 'D': 'Hierarchical inheritance'},
        "C) Multiple inheritance",
        "The diamond problem occurs when a class inherits from two classes that share a common base class, creating ambiguity.",
        "Medium"); q+=1

    pdf.add_question(q, "How is the diamond problem resolved in C++?",
        {'A': 'Using abstract classes', 'B': 'Using virtual inheritance', 'C': 'Using interfaces', 'D': 'Using static members'},
        "B) Using virtual inheritance",
        "Virtual inheritance ensures only one copy of the base class exists, resolving the diamond problem ambiguity.",
        "Medium"); q+=1

    pdf.add_question(q, "Which type of inheritance is NOT supported in Java?",
        {'A': 'Single', 'B': 'Multilevel', 'C': 'Multiple (class)', 'D': 'Hierarchical'},
        "C) Multiple (class)",
        "Java does not support multiple inheritance of classes to avoid the diamond problem. It supports multiple inheritance through interfaces.",
        "Medium"); q+=1

    pdf.add_question(q, "In private inheritance (C++), public members of the base class become:",
        {'A': 'Public in derived class', 'B': 'Protected in derived class', 'C': 'Private in derived class', 'D': 'Inaccessible'},
        "C) Private in derived class",
        "In private inheritance, all public and protected members of the base class become private in the derived class.",
        "Hard"); q+=1

    pdf.add_question(q, "What is hierarchical inheritance?",
        {'A': 'One class inherits from multiple classes', 'B': 'Multiple classes inherit from a single base class', 'C': 'Chain of inheritance', 'D': 'Inheritance with interfaces'},
        "B) Multiple classes inherit from a single base class",
        "Hierarchical inheritance: multiple derived classes inherit from one base class (e.g., Dog, Cat, Bird from Animal).",
        "Easy"); q+=1

    pdf.add_question(q, "In C++, the order of constructor calls in inheritance is:",
        {'A': 'Derived first, then base', 'B': 'Base first, then derived', 'C': 'Random order', 'D': 'Only derived constructor'},
        "B) Base first, then derived",
        "Constructors are called from base to derived. Destructors are called in reverse order (derived first).",
        "Medium"); q+=1

    pdf.add_question(q, "Which keyword is used in Java to inherit a class?",
        {'A': 'inherits', 'B': 'extends', 'C': 'implements', 'D': 'derives'},
        "B) extends",
        "Java uses 'extends' for class inheritance and 'implements' for interface implementation.",
        "Easy"); q+=1

    pdf.add_question(q, "Can a constructor be inherited?",
        {'A': 'Yes, always', 'B': 'No, constructors are not inherited', 'C': 'Only default constructors', 'D': 'Only in Java'},
        "B) No, constructors are not inherited",
        "Constructors are not inherited. Each class must define its own. The base constructor is called via initialization list or super().",
        "Medium"); q+=1

    pdf.add_question(q, "What is the 'super' keyword used for in Java?",
        {'A': 'Access static members', 'B': 'Call parent class constructor/methods', 'C': 'Create new objects', 'D': 'Define interfaces'},
        "B) Call parent class constructor/methods",
        "The 'super' keyword in Java refers to the parent class. super() calls the parent constructor, super.method() calls parent methods.",
        "Easy"); q+=1

    pdf.add_question(q, "In protected inheritance (C++), public members of base become:",
        {'A': 'Public', 'B': 'Protected', 'C': 'Private', 'D': 'Inaccessible'},
        "B) Protected",
        "In protected inheritance, public members of the base class become protected in the derived class.",
        "Hard"); q+=1

    # =========================================================================
    # SECTION 3: Polymorphism (12 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 3: Polymorphism",
        "Compile-time polymorphism (overloading), runtime polymorphism (overriding), virtual functions, and vtable.")

    pdf.add_question(q, "Compile-time polymorphism is achieved through:",
        {'A': 'Virtual functions', 'B': 'Function overloading and operator overloading', 'C': 'Inheritance', 'D': 'Abstract classes'},
        "B) Function overloading and operator overloading",
        "Compile-time (static) polymorphism is resolved at compile time via function overloading, operator overloading, and templates.",
        "Easy"); q+=1

    pdf.add_question(q, "Runtime polymorphism is achieved through:",
        {'A': 'Function overloading', 'B': 'Operator overloading', 'C': 'Virtual functions and function overriding', 'D': 'Templates'},
        "C) Virtual functions and function overriding",
        "Runtime (dynamic) polymorphism uses virtual functions and is resolved at runtime through vtable lookup.",
        "Easy"); q+=1

    pdf.add_question(q, "What is a virtual function in C++?",
        {'A': 'A function with no body', 'B': 'A function that can be overridden in derived class with dynamic dispatch', 'C': 'A static function', 'D': 'A template function'},
        "B) A function that can be overridden in derived class with dynamic dispatch",
        "Virtual functions enable dynamic dispatch - the actual function called depends on the runtime type of the object.",
        "Medium"); q+=1

    pdf.add_question(q, "What is a vtable?",
        {'A': 'A table of variables', 'B': 'A table of function pointers for virtual functions', 'C': 'A vector table', 'D': 'A validation table'},
        "B) A table of function pointers for virtual functions",
        "The vtable (virtual table) is a lookup table of function pointers used to resolve virtual function calls at runtime.",
        "Medium"); q+=1

    pdf.add_question(q, "Can constructors be virtual in C++?",
        {'A': 'Yes', 'B': 'No', 'C': 'Only default constructors', 'D': 'Only copy constructors'},
        "B) No",
        "Constructors cannot be virtual because the vtable is not set up until the constructor completes. Destructors can be virtual.",
        "Medium"); q+=1

    pdf.add_question(q, "Why should destructors be declared virtual in base classes?",
        {'A': 'For better performance', 'B': 'To ensure proper cleanup of derived class objects when deleted via base pointer', 'C': 'It is mandatory', 'D': 'To prevent inheritance'},
        "B) To ensure proper cleanup of derived class objects when deleted via base pointer",
        "Without a virtual destructor, deleting a derived object through a base pointer causes undefined behavior (only base destructor runs).",
        "Hard"); q+=1

    pdf.add_question(q, "What is function overloading?",
        {'A': 'Multiple functions with the same name but different parameters', 'B': 'Redefining a base class function in derived class', 'C': 'A function calling itself', 'D': 'A function with default arguments'},
        "A) Multiple functions with the same name but different parameters",
        "Function overloading allows multiple functions with the same name but different parameter lists (number, type, or order).",
        "Easy"); q+=1

    pdf.add_question(q, "What is function overriding?",
        {'A': 'Same function name with different parameters', 'B': 'Redefining a base class virtual function in derived class with same signature', 'C': 'Calling parent function', 'D': 'Operator overloading'},
        "B) Redefining a base class virtual function in derived class with same signature",
        "Overriding redefines a virtual base function in the derived class with the exact same signature for runtime polymorphism.",
        "Easy"); q+=1

    pdf.add_question(q, "Which operator cannot be overloaded in C++?",
        {'A': '+', 'B': '-', 'C': '::', 'D': '=='},
        "C) ::",
        "The scope resolution (::), member access (.), sizeof, and ternary (?:) operators cannot be overloaded in C++.",
        "Medium"); q+=1

    pdf.add_question(q, "In Java, what annotation is used to indicate method overriding?",
        {'A': '@Override', 'B': '@Overload', 'C': '@Virtual', 'D': '@Super'},
        "A) @Override",
        "@Override annotation helps the compiler verify that the method actually overrides a superclass method.",
        "Easy"); q+=1

    pdf.add_question(q, "A pure virtual function in C++ is declared with:",
        {'A': 'virtual keyword only', 'B': '= 0 at the end', 'C': 'abstract keyword', 'D': 'override keyword'},
        "B) = 0 at the end",
        "A pure virtual function is declared as: virtual void func() = 0; It makes the class abstract.",
        "Medium"); q+=1

    pdf.add_question(q, "What is early binding vs late binding?",
        {'A': 'Early = runtime, Late = compile-time', 'B': 'Early = compile-time, Late = runtime', 'C': 'Both are compile-time', 'D': 'Both are runtime'},
        "B) Early = compile-time, Late = runtime",
        "Early binding resolves function calls at compile time (overloading). Late binding resolves at runtime (virtual functions).",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 4: Encapsulation & Abstraction (8 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 4: Encapsulation & Abstraction",
        "Access modifiers, abstract classes, interfaces, and data hiding.")

    pdf.add_question(q, "Encapsulation is:",
        {'A': 'Inheritance of properties', 'B': 'Bundling data and methods that operate on it, restricting direct access', 'C': 'Function overloading', 'D': 'Multiple inheritance'},
        "B) Bundling data and methods that operate on it, restricting direct access",
        "Encapsulation wraps data and methods into a single unit (class) and controls access via access modifiers.",
        "Easy"); q+=1

    pdf.add_question(q, "Which access modifier makes a member accessible only within the same class?",
        {'A': 'public', 'B': 'protected', 'C': 'private', 'D': 'default'},
        "C) private",
        "Private members are accessible only within the class itself. Protected allows access in derived classes too.",
        "Easy"); q+=1

    pdf.add_question(q, "An abstract class in Java:",
        {'A': 'Cannot have any methods', 'B': 'Can have both abstract and concrete methods', 'C': 'Must have only abstract methods', 'D': 'Cannot be inherited'},
        "B) Can have both abstract and concrete methods",
        "Abstract classes can have abstract methods (no body) and concrete methods (with implementation). They cannot be instantiated.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the difference between an abstract class and an interface in Java?",
        {'A': 'No difference', 'B': 'Abstract class can have state and constructors; interface cannot (pre-Java 8)', 'C': 'Interface supports multiple inheritance; abstract class does not', 'D': 'Both B and C'},
        "D) Both B and C",
        "Abstract classes can have instance variables and constructors. A class can implement multiple interfaces but extend only one class.",
        "Medium"); q+=1

    pdf.add_question(q, "Abstraction focuses on:",
        {'A': 'Hiding implementation details and showing only essential features', 'B': 'Inheriting properties', 'C': 'Creating multiple objects', 'D': 'Data binding'},
        "A) Hiding implementation details and showing only essential features",
        "Abstraction hides complexity by providing a simplified interface. Users see what an object does, not how.",
        "Easy"); q+=1

    pdf.add_question(q, "In Java, can an interface have a constructor?",
        {'A': 'Yes', 'B': 'No', 'C': 'Only default constructor', 'D': 'Only parameterized constructor'},
        "B) No",
        "Interfaces cannot have constructors because they cannot be instantiated and have no instance state to initialize.",
        "Medium"); q+=1

    pdf.add_question(q, "Since Java 8, interfaces can have:",
        {'A': 'Only abstract methods', 'B': 'Default and static methods', 'C': 'Constructors', 'D': 'Instance variables'},
        "B) Default and static methods",
        "Java 8 introduced default methods (with implementation) and static methods in interfaces.",
        "Medium"); q+=1

    pdf.add_question(q, "Which is the best example of encapsulation?",
        {'A': 'Using inheritance', 'B': 'Private data members with public getters/setters', 'C': 'Using virtual functions', 'D': 'Using templates'},
        "B) Private data members with public getters/setters",
        "Making data private and providing controlled access through public getters/setters is the classic encapsulation pattern.",
        "Easy"); q+=1

    # =========================================================================
    # SECTION 5: Design Patterns (10 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 5: Design Patterns",
        "Singleton, Factory, Observer, Strategy, MVC and other common patterns.")

    pdf.add_question(q, "The Singleton pattern ensures:",
        {'A': 'Multiple instances of a class', 'B': 'Only one instance of a class exists', 'C': 'Inheritance of classes', 'D': 'Polymorphic behavior'},
        "B) Only one instance of a class exists",
        "Singleton restricts a class to a single instance and provides a global access point to it.",
        "Easy"); q+=1

    pdf.add_question(q, "Which design pattern creates objects without specifying the exact class?",
        {'A': 'Singleton', 'B': 'Factory', 'C': 'Observer', 'D': 'Strategy'},
        "B) Factory",
        "The Factory pattern uses a factory method to create objects, allowing subclasses to determine the actual type.",
        "Easy"); q+=1

    pdf.add_question(q, "The Observer pattern implements:",
        {'A': 'One-to-one relationship', 'B': 'One-to-many dependency (publish-subscribe)', 'C': 'Many-to-many relationship', 'D': 'No relationship'},
        "B) One-to-many dependency (publish-subscribe)",
        "Observer defines a one-to-many dependency where when one object (subject) changes state, all dependents (observers) are notified.",
        "Medium"); q+=1

    pdf.add_question(q, "The Strategy pattern is used to:",
        {'A': 'Create a single instance', 'B': 'Define a family of algorithms and make them interchangeable', 'C': 'Observe state changes', 'D': 'Build complex objects'},
        "B) Define a family of algorithms and make them interchangeable",
        "Strategy encapsulates algorithms into separate classes, allowing the algorithm to be selected at runtime.",
        "Medium"); q+=1

    pdf.add_question(q, "In MVC architecture, which component handles user input?",
        {'A': 'Model', 'B': 'View', 'C': 'Controller', 'D': 'All of the above'},
        "C) Controller",
        "Controller handles user input, updates the Model, and selects the View. Model manages data, View displays it.",
        "Easy"); q+=1

    pdf.add_question(q, "The Decorator pattern is used to:",
        {'A': 'Create objects', 'B': 'Add responsibilities to objects dynamically', 'C': 'Restrict instantiation', 'D': 'Sort objects'},
        "B) Add responsibilities to objects dynamically",
        "Decorator wraps an object to add new behavior without modifying the original class. It is an alternative to subclassing.",
        "Medium"); q+=1

    pdf.add_question(q, "The Adapter pattern is used to:",
        {'A': 'Create a single instance', 'B': 'Make incompatible interfaces work together', 'C': 'Observe changes', 'D': 'Build objects step by step'},
        "B) Make incompatible interfaces work together",
        "The Adapter pattern converts the interface of a class into another interface that clients expect.",
        "Medium"); q+=1

    pdf.add_question(q, "Which design pattern separates object construction from its representation?",
        {'A': 'Factory', 'B': 'Builder', 'C': 'Prototype', 'D': 'Singleton'},
        "B) Builder",
        "The Builder pattern constructs complex objects step by step, separating construction from representation.",
        "Medium"); q+=1

    pdf.add_question(q, "The Prototype pattern creates new objects by:",
        {'A': 'Using a factory', 'B': 'Cloning existing objects', 'C': 'Direct instantiation', 'D': 'Lazy initialization'},
        "B) Cloning existing objects",
        "Prototype creates new objects by copying (cloning) an existing object, avoiding expensive creation from scratch.",
        "Medium"); q+=1

    pdf.add_question(q, "Design patterns are categorized into:",
        {'A': 'Structural, Behavioral, Functional', 'B': 'Creational, Structural, Behavioral', 'C': 'Abstract, Concrete, Virtual', 'D': 'Static, Dynamic, Hybrid'},
        "B) Creational, Structural, Behavioral",
        "Gang of Four categorized 23 patterns: Creational (object creation), Structural (composition), Behavioral (interaction).",
        "Easy"); q+=1

    # =========================================================================
    # SECTION 6: C++ Specific (15 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 6: C++ Specific OOP",
        "Templates, STL, smart pointers, move semantics, RAII, and other C++ specific features.")

    pdf.add_question(q, "What is a template in C++?",
        {'A': 'A class that cannot be instantiated', 'B': 'A mechanism for generic programming', 'C': 'A type of inheritance', 'D': 'An interface'},
        "B) A mechanism for generic programming",
        "Templates allow writing generic code that works with any data type, resolved at compile time.",
        "Easy"); q+=1

    pdf.add_question(q, "Which STL container provides O(1) average time for insertion and lookup?",
        {'A': 'vector', 'B': 'list', 'C': 'unordered_map', 'D': 'map'},
        "C) unordered_map",
        "unordered_map uses hash table for O(1) average time. map uses balanced BST for O(log n).",
        "Medium"); q+=1

    pdf.add_question(q, "What is RAII in C++?",
        {'A': 'Random Access Indexed Arrays', 'B': 'Resource Acquisition Is Initialization', 'C': 'Runtime Abstraction Interface Implementation', 'D': 'Reference Allocation In Inheritance'},
        "B) Resource Acquisition Is Initialization",
        "RAII ties resource lifecycle to object lifetime. Resources are acquired in constructor and released in destructor.",
        "Medium"); q+=1

    pdf.add_question(q, "Which smart pointer allows exactly one owner?",
        {'A': 'shared_ptr', 'B': 'unique_ptr', 'C': 'weak_ptr', 'D': 'auto_ptr'},
        "B) unique_ptr",
        "unique_ptr has exclusive ownership. It cannot be copied, only moved. shared_ptr allows multiple owners.",
        "Medium"); q+=1

    pdf.add_question(q, "What does std::move() do?",
        {'A': 'Moves memory physically', 'B': 'Casts an lvalue to an rvalue reference enabling move semantics', 'C': 'Deletes the object', 'D': 'Copies the object'},
        "B) Casts an lvalue to an rvalue reference enabling move semantics",
        "std::move() is a cast that enables move semantics by converting an lvalue to an rvalue reference, allowing resource transfer.",
        "Hard"); q+=1

    pdf.add_question(q, "What is the difference between shared_ptr and weak_ptr?",
        {'A': 'No difference', 'B': 'weak_ptr does not increase reference count and can break circular references', 'C': 'shared_ptr is faster', 'D': 'weak_ptr owns the resource'},
        "B) weak_ptr does not increase reference count and can break circular references",
        "weak_ptr observes a shared_ptr without affecting the reference count, preventing circular reference memory leaks.",
        "Hard"); q+=1

    pdf.add_question(q, "The STL vector stores elements in:",
        {'A': 'Linked list', 'B': 'Contiguous memory', 'C': 'Hash table', 'D': 'Binary tree'},
        "B) Contiguous memory",
        "std::vector stores elements in contiguous memory, providing O(1) random access and cache-friendly iteration.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the Rule of Three in C++?",
        {'A': 'A class should have at most 3 members', 'B': 'If a class needs a custom destructor, copy constructor, or copy assignment, it likely needs all three', 'C': 'Use 3 levels of inheritance', 'D': 'Define 3 constructors'},
        "B) If a class needs a custom destructor, copy constructor, or copy assignment, it likely needs all three",
        "The Rule of Three states that if any one of these three special member functions is needed, all three should be defined.",
        "Hard"); q+=1

    pdf.add_question(q, "What is the Rule of Five in C++11?",
        {'A': 'Five design patterns', 'B': 'Rule of Three plus move constructor and move assignment operator', 'C': 'Five levels of access', 'D': 'Five types of inheritance'},
        "B) Rule of Three plus move constructor and move assignment operator",
        "C++11 extends the Rule of Three with move constructor and move assignment operator for efficient resource transfer.",
        "Hard"); q+=1

    pdf.add_question(q, "Which STL container is a FIFO data structure?",
        {'A': 'stack', 'B': 'queue', 'C': 'vector', 'D': 'set'},
        "B) queue",
        "std::queue is FIFO (First In, First Out). std::stack is LIFO (Last In, First Out).",
        "Easy"); q+=1

    pdf.add_question(q, "What is the time complexity of std::map operations (insert, find, delete)?",
        {'A': 'O(1)', 'B': 'O(log n)', 'C': 'O(n)', 'D': 'O(n log n)'},
        "B) O(log n)",
        "std::map is implemented as a balanced BST (typically Red-Black Tree), so all operations are O(log n).",
        "Medium"); q+=1

    pdf.add_question(q, "What keyword in C++ prevents a class from being inherited?",
        {'A': 'static', 'B': 'const', 'C': 'final', 'D': 'sealed'},
        "C) final",
        "The 'final' keyword (C++11) prevents a class from being inherited or a virtual function from being overridden.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the purpose of the 'explicit' keyword in C++?",
        {'A': 'Make methods virtual', 'B': 'Prevent implicit conversions via constructors', 'C': 'Define pure virtual functions', 'D': 'Enable multiple inheritance'},
        "B) Prevent implicit conversions via constructors",
        "'explicit' on a constructor prevents the compiler from using it for implicit type conversions.",
        "Hard"); q+=1

    pdf.add_question(q, "Lambda expressions in C++ are:",
        {'A': 'Named functions', 'B': 'Anonymous function objects', 'C': 'Macros', 'D': 'Templates'},
        "B) Anonymous function objects",
        "Lambdas are anonymous functions: [capture](params){ body }. They create a closure object.",
        "Medium"); q+=1

    pdf.add_question(q, "What does the 'auto' keyword do in C++11?",
        {'A': 'Creates automatic variables on the stack', 'B': 'Deduces the type from the initializer', 'C': 'Makes variables global', 'D': 'Declares a pointer'},
        "B) Deduces the type from the initializer",
        "'auto' lets the compiler deduce the variable type from its initializer: auto x = 5; // int",
        "Easy"); q+=1

    # =========================================================================
    # SECTION 7: Java/General OOP (13 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 7: Java / General OOP",
        "Garbage collection, generics, exception handling, and Java-specific OOP concepts.")

    pdf.add_question(q, "Java uses which type of memory management?",
        {'A': 'Manual memory management', 'B': 'Automatic garbage collection', 'C': 'Reference counting only', 'D': 'Stack-only allocation'},
        "B) Automatic garbage collection",
        "Java's garbage collector automatically reclaims memory from objects that are no longer referenced.",
        "Easy"); q+=1

    pdf.add_question(q, "Which method is called by the garbage collector before destroying an object in Java?",
        {'A': 'destroy()', 'B': 'finalize()', 'C': 'dispose()', 'D': 'close()'},
        "B) finalize()",
        "The finalize() method is called before garbage collection. However, it is deprecated since Java 9.",
        "Medium"); q+=1

    pdf.add_question(q, "What are Java generics used for?",
        {'A': 'Dynamic typing', 'B': 'Type-safe parameterized types', 'C': 'Memory management', 'D': 'Multi-threading'},
        "B) Type-safe parameterized types",
        "Generics provide compile-time type safety: List&lt;String&gt; ensures only strings are stored.",
        "Medium"); q+=1

    pdf.add_question(q, "In Java exception handling, what is the difference between checked and unchecked exceptions?",
        {'A': 'No difference', 'B': 'Checked must be caught or declared; unchecked do not', 'C': 'Unchecked are more severe', 'D': 'Checked are runtime only'},
        "B) Checked must be caught or declared; unchecked do not",
        "Checked exceptions (IOException) must be handled. Unchecked (RuntimeException like NullPointerException) are optional to catch.",
        "Medium"); q+=1

    pdf.add_question(q, "The 'final' keyword in Java can be applied to:",
        {'A': 'Variables only', 'B': 'Methods only', 'C': 'Classes only', 'D': 'Variables, methods, and classes'},
        "D) Variables, methods, and classes",
        "final variable = constant, final method = cannot override, final class = cannot inherit.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the output of: String s1 = \"hello\"; String s2 = \"hello\"; System.out.println(s1 == s2);",
        {'A': 'true', 'B': 'false', 'C': 'Compilation error', 'D': 'Runtime error'},
        "A) true",
        "Both string literals point to the same object in the String Pool, so == returns true for reference comparison.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the purpose of the 'try-with-resources' in Java?",
        {'A': 'Exception handling', 'B': 'Automatic resource management (auto-close)', 'C': 'Multi-threading', 'D': 'Garbage collection'},
        "B) Automatic resource management (auto-close)",
        "try-with-resources automatically closes resources implementing AutoCloseable when the try block exits.",
        "Medium"); q+=1

    pdf.add_question(q, "In Java, all classes implicitly extend:",
        {'A': 'java.lang.Class', 'B': 'java.lang.Object', 'C': 'java.lang.Base', 'D': 'java.lang.Root'},
        "B) java.lang.Object",
        "Every class in Java implicitly extends java.lang.Object, which provides methods like equals(), hashCode(), toString().",
        "Easy"); q+=1

    pdf.add_question(q, "What is method hiding in Java?",
        {'A': 'Making methods private', 'B': 'A static method in subclass with same signature as parent static method', 'C': 'Deleting methods', 'D': 'Method overloading'},
        "B) A static method in subclass with same signature as parent static method",
        "When a subclass defines a static method with the same signature as a parent static method, it hides (not overrides) it.",
        "Hard"); q+=1

    pdf.add_question(q, "Which collection interface does NOT allow duplicate elements in Java?",
        {'A': 'List', 'B': 'Set', 'C': 'Queue', 'D': 'Deque'},
        "B) Set",
        "Set interface (HashSet, TreeSet) does not allow duplicates. List allows duplicates.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the diamond operator (&lt;&gt;) in Java?",
        {'A': 'Bitwise operator', 'B': 'Type inference for generics (Java 7+)', 'C': 'Comparison operator', 'D': 'Lambda operator'},
        "B) Type inference for generics (Java 7+)",
        "The diamond operator allows type inference: List&lt;String&gt; list = new ArrayList&lt;&gt;(); instead of repeating the type.",
        "Medium"); q+=1

    pdf.add_question(q, "An immutable object in Java:",
        {'A': 'Can be modified after creation', 'B': 'Cannot be modified after creation', 'C': 'Is always null', 'D': 'Must be static'},
        "B) Cannot be modified after creation",
        "Immutable objects (like String) cannot change state after creation. They are thread-safe by design.",
        "Easy"); q+=1

    pdf.add_question(q, "What is covariant return type in Java?",
        {'A': 'Return type must be exactly the same when overriding', 'B': 'Overriding method can return a subtype of the original return type', 'C': 'Return type can be any type', 'D': 'No return type needed'},
        "B) Overriding method can return a subtype of the original return type",
        "Since Java 5, an overriding method can return a subclass of the return type declared in the parent method.",
        "Hard"); q+=1

    pdf.generate()
    print(f"Total questions: {q - 1}")

if __name__ == '__main__':
    main()
