# def add(a,b):
#     sum= a+b
#     print(sum)
# add(1,2)

# def add(*args):
#     sum = args
#     print(sum)
# add(1+2+2)


# def operation(n, **kwargs):
#     n+=kwargs['n1']
#     print(n)
#
# operation(2, n1=2,n2=3) #output is a dictionary


# class Car():
#     def __init__(self, **kwargs):
#         self.make = kwargs.get('make') #syntax to access dict
#         self.model = kwargs.get('model')
# car = Car(make='Nissan', model='GT-R')
# print(car.make, car.model)

# class Car():
#     def __init__(self, *args):
#         self.make = args[0] #syntax to access tuple
#         self.model = args[1]
# car = Car('Nissan','GT-R')
# print(car.make, car.model)

# class House:
#     def __init__(self, **kwargs):
#         self.rooms = kwargs.get('rooms', 'three') #default
# flat = House(rooms=3)
# print(flat.rooms)