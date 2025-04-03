# Dictionary containing chatbot responses for user inputs
responses = {
    # Basic Responses
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer your questions. Try asking about something more specific!",
    "default": "I'm sorry, I didn't understand that. Could you rephrase?",

    # COMP 248 Responses
    "if_statement": "An if statement in Java executes a block of code if a specified condition is true.",
    "for_loop": "A for loop in Java is used to execute a block of code a specified amount of times.",
    "variable": "A variable in Java is a container that stores data values.",
    "else_statement": "An else statement in Java executes a block of code if the same condition is false.",
    "while_loop": "A while loop in Java executes a block of code as long as a specified condition is true.",
    "switch_statement": "A switch statement in Java selects one of many code blocks to be executed.",
    "method": "A method in Java is a block of code that is executed when it is called.",
    "array": "An array in Java is a collection of variables that are accessed with an index number.",
    "string": "A string in Java is a sequence of characters.",
    "int": "Int is a data type in Java that stores whole numbers.",
    "double": "Double is a data type in Java that stores floating point numbers.",
    "access_modifier": "An access modifier in Java specifies the accessibility of a class, method, or variable.",
    "return_type": "A return type in Java specifies the data type that a method returns.",
    "parameter": "A parameter in Java is a value that is passed into a method.",
    "constructor": "A constructor in Java is a special method that is called when an object is created.",
    "object": "An object in Java is an instance of a class.",
    "class": "A class in Java is a blueprint for creating objects.",
    "inheritance": "Inheritance in Java allows one class to inherit the properties and methods of another class.",
    "interface": "An interface in Java is a reference type that can contain only constants, method signatures, default methods, static methods, and nested types.",
    "package": "A package in Java is a namespace that organizes a set of related classes and interfaces.",
    "import": "An import statement in Java is used to import classes from other packages.",
    "exception": "An exception in Java is an event that disrupts the normal flow of the program's instructions.",
    "try_catch": "A try-catch block in Java is used to handle exceptions.",
    "finally": "A finally block in Java is used to execute important code such as closing a file or releasing resources.",
    "overloading": "Method overloading in Java allows a class to have multiple methods with the same name but different parameters.",
    "overriding": "Method overriding in Java allows a subclass to provide a specific implementation of a method that is already provided by its superclass.",
    "static": "The static keyword in Java is used to create variables and methods that belong to the class rather than instances of the class.",
    "final": "The final keyword in Java is used to restrict the user from changing the value of a variable, method, or class.",
}

# Dictionary containing regular expressions to match user input to predefined intents
patterns = {
    # Basic patterns
    "greet": r"\b(hello|hi|hey|greetings|howdy)\b",
    "bye": r"\b(bye|goodbye|farewell|see you)\b",
    "help": r"\b(help|assist|support|guide)\b",

    # Java concept patterns
    "if_statement": r"\b(if statement|conditional|if condition|if then)\b",
    "for_loop": r"\b(for loop|for statement|for iteration)\b",
    "variable": r"\b(variable|var|variables|value storage)\b",
    "else_statement": r"\b(else statement|else condition|else block)\b",
    "while_loop": r"\b(while loop|while statement|do while)\b",
    "switch_statement": r"\b(switch statement|switch case|case statement)\b",
    "method": r"\b(method|function|procedure|subroutine)\b",
    "array": r"\b(array|arrays|list of data|data structure)\b",
    "string": r"\b(string|text|character sequence)\b",
    "int": r"\b(int|integer|whole number)\b",
    "double": r"\b(double|float|floating point|decimal)\b",
    "access_modifier": r"\b(access modifier|public|private|protected|access control)\b",
    "return_type": r"\b(return type|return value|method return)\b",
    "parameter": r"\b(parameter|argument|input|param)\b",
    "constructor": r"\b(constructor|initializer|new object|instantiation)\b",
    "object": r"\b(object|instance|class instance)\b",
    "class": r"\b(class|blueprint|object template)\b",
    "inheritance": r"\b(inheritance|extends|subclass|parent class|child class)\b",
    "interface": r"\b(interface|contract|abstract type)\b",
    "package": r"\b(package|namespace|code organization)\b",
    "import": r"\b(import|include|using)\b",
    "exception": r"\b(exception|error handling|error catch|runtime error)\b",
    "try_catch": r"\b(try catch|exception handling|catch block|try block)\b",
    "finally": r"\b(finally block|cleanup|resource release)\b",
    "overloading": r"\b(overloading|same name different parameters|method overload)\b",
    "overriding": r"\b(overriding|override|reimplement|polymorphism)\b",
    "static": r"\b(static|class variable|class method)\b",
    "final": r"\b(final|constant|immutable|cannot change)\b",
}
