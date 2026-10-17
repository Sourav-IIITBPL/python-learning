# tuples,int,str,dict,list are internally represented as classes in python.

print(type(("name",33)))
print(type(int))
print(type("you are here"))
print(type({"name":"John","age":33}))
print(type([1,2,3,4]))

class Student:
    def __init__(self,name,scholar,age):      # __init__ is like a constructor in other programming languages. It is called when an object is created.
        self.name = name
        self.scholar = scholar
        self.age = age
    def __str__(self):                        # __str__ is a special method that is called when we try to print an object. It returns a string representation of the object.
        return f"Name: {self.name}, Scholar: {self.scholar}, Age: {self.age}"

def main():
    student1 = Student("John", 12345, 20)
    student2 = Student("Alice", 67890, 22)
    professor1 = Professors("Dr. Smith", "Computer Science", "CS50", "CS50-001")
    professor2 = Professors("Dr. Johnson", "Mathematics", "MATH101", "MATH101-001")

    print(student1)
    print(student2)
    print(professor1)
    print(professor2)

    professor1.name = "Dr. Brown"
    professor1.department = "Data Science"
    professor1.cs.name = "CS51"
    professor1.cs.code = "CS51-001"
    print(professor1)

    professor1.cs = Courses("CS52", "CS52-001")
    print(professor1)



# classes with property and decorators methods 

class Courses:
    def __init__(self, name, code):          # self in class means the current instance of the class. It is used to access variables that belongs to the class. you can use any name instead of self but it is a convention to use self.
        self.name = name
        self.code = code

    @property                                # the getters and setters must be of same name as the variable name. The @property decorator is used to define a getter method for a property. It allows us to access the property like an attribute.
    def name(self):
        return self._name

    @name.setter                             # the @name.setter decorator is used to define a setter method for a property. It allows us to set the value of the property like an attribute.
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value                   # this _name is a private variable. It is a convention to use an underscore before the variable name to indicate that it is private and should not be accessed directly. Instead, we use the getter and setter methods to access and modify the value of the property.

    @property
    def code(self):
        return self._code                    #  this "_code" is different from what is in __init__. It means that this variable is private and is even set during initialization or object creation by setters only.
    
    @code.setter
    def code(self, value):
        if not value:
            raise ValueError("Code cannot be empty")
        self._code = value

    def __str__(self):
        return f"Course Name: {self.name}, Course Code: {self.code}"


class Professors(Courses):

    def __init__(self,name,department,course_name,course_code):
        super().__init__(course_name,course_code)          # super() is used to call the __init__ method of the parent class. It is used to initialize the parent class attributes in the child class.
        self.name = name
        self.department = department
        self.cs = Courses(course_name,course_code)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if not value:
            raise ValueError("Department cannot be empty")
        self._department = value  

    @property
    def cs(self):
        return self._cs

    @cs.setter
    def cs(self, value):
        if not isinstance(value, Courses):
            raise ValueError("cs must be an instance of Courses")
        self._cs = value 

    def __str__(self):
        return f"Professor Name: {self.name}, Department: {self.department}, Course: {self.cs}"


if __name__ == "__main__":
    main()
