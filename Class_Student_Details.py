# Student Info
class Student_details:
    # Student Attributes
    def __init__(self, fullname, student_ID, gender, address, city, country, region, email, phone_number ):
        self.fullname = input("Enter your first and last name")
        self.student_ID = input("Enter you Student_ID")
        self.gender = input("Enter you gender")
        self.address = input("Enter your address")
        self.city = input("Enter your city")
        self.country = input("Enter your country")
        self.region = input("Enter your region")
        self.email = input("Enter your email")
        self.phone_number = ("Enter your phone_number")

 
    def Student_Info(self):
        print("Full name is ", self.fullname)
        print("The Student_ID is", self.student_ID)
        print("The student gender is", self.gender)
        print("The address is ", self.address)
        print("The city is ", self.city)
        print("The country is ", self.country)
        print("The region is ", self.region)
        print("The email is ", self.email)
        print("The phone number is ", self.phone_number)

        
student1 = Student_details("Helia Cruz", 11245, "Female", "123 Main St", "Houston", "USA", "America", "fgghe@hhhf.com", 2011144458)

info = student1.Student_Info()

print(info)


        
                   


