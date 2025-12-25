num1 = input ("Input num1: ")
num2 = input ("Input num2: ")
if num1.isdigit() and num2.isdigit() :
   num1=int(num1)
   num2=int(num2)
   result=num1*num2
   print (f" {num1} * {num2}  = {result} ")
else:
   print ("Incorrect input")
