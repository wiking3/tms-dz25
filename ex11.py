try:
  num_str = float(input("Enter an integer number: "))
  if num_str.is_integer():
     number = int(num_str)
     result = number ** 2
     print(f" {result} ")
  else:
     print(f" float value")   

except ValueError:
  print(f"Error") 
