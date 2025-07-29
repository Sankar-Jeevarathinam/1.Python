class AssignmentFunctions():
    def Subfields():
        List = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]        
        print("Sub-fields in AI are:")
        for string in List:
            print(string)
            
    def OddEven():
        i = int(input("Enter a Number:")) 
        if ((i%2)==1):
            print(i, " is Odd Number")
        else:
            print(i, " is Even Number")

    def Elegible():
        gender = input("Your Gender:")
        age = input("Your Age:")
        if (gender == "Male" and int(age)>=21):
            print("Elegible")
        elif (gender == "Female" and int(age)>=18):
            print("Elegible")
        else:
            print("Not Elegible")

    def percentage():
        Sub1 = int(input("Subject1 ="))
        Sub2 = int(input("Subject2 ="))
        Sub3 = int(input("Subject3 ="))
        Sub4 = int(input("Subject4 ="))
        Sub5 = int(input("Subject5 ="))
        Total = Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:", Total)
        print("Percentage:", Total/5)

    def triangle():
        H1 = int(input("Height:"))
        B1 = int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle", H1*B1/2)
        Hi1 = int(input("Height1:"))
        Hi2 = int(input("Height2:"))
        B =  int(input("Breadth:"))
        print ("Perimeter formula: Height1+Height2+Breadth")
        print ("Perimeter of Triangle:", Hi1+Hi2+B)
    