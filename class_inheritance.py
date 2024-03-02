# class Animal:
#     def __init__(self):
#         self.eyes = 2
#     def breathe(self):
#         print("exhale and inhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def swim(self):
#         print("it can swim in water")
#     def breathe(self):
#         super().breathe()
#         print("underwater")
#
# tuna = Fish()
# tuna.breathe()
# tuna.swim()

#2nd example:
# class Aircraft:
#     def __init__(self):
#         self.can_fly = True
#     def engine(self):
#         self.type1 = "heavy duty"
#
# class Jet(Aircraft):
#     def __init__(self):
#         super().__init__()
#     def engine(self):
#         super().engine()
#         self.type2 = "super fast"
#         print(f"{self.type1}\n{self.type2}")
# tejas = Jet()
# tejas.engine()

#3rd example:
# class Art:
#     def __init__(self):
#         self.intellectual = True
#     def types(self):
#         self.list1 =["historical", "modern", "contemporary"]
# class Painting(Art):
#     def __init__(self):
#         super().__init__()
#     def forms(self):
#         super().types()
#         self.list2 = ["abstract", "pastel", "oil"]
#         print(self.list1, self.list2)
#
# van_gogh = Painting()
# van_gogh.forms()

# list = ['a','b','c','d','e','f'] #list slicing and reversal
# print(list[::-1])






















