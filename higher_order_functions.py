#calculator app example to showcase higher order functions and how they are called

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def calc (n1,n2,func):
    return func(n1,n2)
print(calc(2,3,add))
#     func_map = {
#         'add': add,
#         'subtract': sub,
#         'multiply': mul,
#         'divide': div
#     }
#     return func_map[func](n1,n2)
#
# num1 = int(input("enter n1\n"))
# num2 = int(input("enter n2\n"))
# func = input("enter function\n")
# print(f"output is:{calc(num1, num2, func)}")
