def calculator():
  print("Welcome to the calculator!")
  #add
  def add(x,y):
    return x+y
    
  #subtract
  def subtract(x,y):
    return x-y
    
  #divide
  def divide(x,y):
    return x/y
    
  #multiply
  def multiply(x,y):
    return x*y
  
  operations = {
  "+":add, 
  "-":subtract, 
  "/":divide, 
  "*":multiply
  }
  
  num1 = int(input("Enter the first number:"))
  operator = input("Enter the operator:")
  num2 = int(input("Enter the second number:"))
  
  y = True
  while y:
    for key in operations:
      if operator == "+":
        print(add(num1,num2))
      elif operator == "-":
        print(subtract(num1,num2))
      elif operator == "/":
        print(divide(num1,num2))
      else:
        operator == "*"
        print(multiply(num1,num2))
    result = operations[operator](num1,num2)
    print(f"The first number is {num1}, the second number is {num2}, the operator is {operator} and the final result is {result}")
    if input("Type no to start a new calculation or hit yes to continue\n") == "yes":
      num1 = result
      operator = input("Enter the operator:")
      num2 = int(input("Enter the next number:"))
      print(f"The first number is {result}, the second number is {num2}, the operator is {operator} and the final result is {result}")
    else:
      y = False
      print("starting anew")
      calculator() # recursion used here
calculator()
    

