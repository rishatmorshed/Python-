def greet(name, subject, dept= "CS"):   #Here department is default argument
    print("Hello", name)
    print(f"Are you from {dept} department?")
    print(f"Do you teach {subject}?")
greet("Rishat", "Python") 