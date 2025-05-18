# class Instructor:
#     def __init__(self):
#         print("Creating new object:")
# Instructor_1 = Instructor()
# Instructor_1.name = "Rishat"
# Instructor_1.address = "Dhaka"
# print(Instructor_1.name)
# Instructor_2 = Instructor()
# Instructor_2.name = "Mahbub"
# Instructor_2.address = "Dhaka"
# print(Instructor_2.name)




################# But we can easily initialize attribute using init function###############

# class instructorInfo:                                       # Creating Class 
#     def __init__(self, instructorName, instructorAddress): # Init function to initialize the attribute of that particular object
#         self.name = instructorName                         # Attribute 1
#         self.address = instructorAddress                   # Attribute 2
#         self.followers = 0                                 #by default all attribute has followers = 0

# info_1 = instructorInfo("Morshed", "Shyamoli")  # Creating Object of above class
# print(info_1.name)
# info_2 = instructorInfo("Rishat", "Dhaka")
# print(info_2.name)


################### Use Methods in a Class ###################

# class instructorInfo:
#     followers = 0                       # Class Object variable
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def display(self, course):               #This is a method in a class
#         print(f"Hello I am {self.name} from {self.address} and I teach {course}")
    
#     def updateFollower(self, follower_name):
#         self.followers += 1
# info_1 = instructorInfo("Morshed", "Shyamoli")
# info_1.display("python")
# info_1.updateFollower("Payal")
# print(info_1.followers)
# info_2 = instructorInfo("Rishat", "Dhaka")
# print(info_2.followers)

########################### Find Circumference of a circle ###########################

class circle:
    pi = 3.14
    def __init__(self, r):
        self.radius = r
        # self.area = circle.pi * r**2
    def circumference(self):
        return 2* circle.pi * self.radius   # bcz pi is a class object attribute
    def area(self):
        return circle.pi * self.radius**2
circle_1 = circle(4)
circle_2 = circle(7)
print(f"Circumference of circle_1 is: {circle_1.circumference()}")
print(f"Circumference of circle-2 is: {circle_2.circumference()}")
print(f"Area of circle_1 is: {circle_1.area()}")


########################### Area of a Rectangle ###########################
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def area(self):
        return self.width * self.length

rectangle_1 = Rectangle(5,5)
print(f"Area of Rectangle_1 is : {rectangle_1.area()}")