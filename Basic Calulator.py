#Basic Calulator
print("Welcome to the basic calculator ")

print("1 = Addition")
print("2 = Subtraction")
print("3 = Multipication ")
print("4 = Division")
print("5 = Persentage")

a= input("Enter Your Operation : ")

if a == "1": 

    num1= int(input("Enter the first number : "))
    num2= int(input("Enter the second number : "))
    
    print("Here the sum of two numbers : ", num1+num2 )

elif  a == "2": 

    num1= int(input("Enter the first number : "))
    num2= int(input("Enter the second number : "))
    
    print("Here the Subtracion of two numbers : " , num1-num2)

elif a == "3":

    num1= int(input("Enter the first number : "))
    num2= int(input("Enter the second number : "))

    print("Here the Multiplication of two numbers : " , num1*num2)

elif a == "4":

    num1= int(input("Enter the first number : "))
    num2= int(input("Enter the second number : "))

    print("Here the Division of two numbers : " , num1/num2)

elif a == "5":
    t=int(input("Enter the Total Numbers : "))
    g=int(input("Enter the Given Numbers : "))
    print("Here is the Persentage : " , g/t*100)
