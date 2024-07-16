# class myclass:
#     def __init__(self,name):
#         self.name=name
#
#     def show_name(self):
#         print("name: ",self.name)
#
# if __name__=='__main__':
#
#     obj=myclass("subbu")
#     obj.show_name()
#
# class myclass1:
#     def __init__(self):
#         self.instance_var=25
#
# obj=myclass1()
# print(obj.instance_var)
#
# class myclass2:
#     def __init__(self,name):
#         self.name=name
#
#     def show_name(self):
#         print("name",self.name)
#
#     def Updated_name(self,n_name):
#         self.name=n_name
#
#
# obj=myclass2("omkar")
# obj.show_name()
#
# obj.Updated_name("hari")
# obj.show_name()
#
#
# class abc:
#     country="india"
#
#     def __init__(self,name):
#         self.name=name
#     def show_name(self):
#         print("name",self.name)
#
# print(abc.country)
# obj=abc("muthu")
# obj.show_name()
#
# class bcd:
#     city="pune"
#
#     @classmethod
#     def class_method(cls):
#         print("classmethod: ",cls.city)
#     @staticmethod
#     def static_method():
#         print("this is static method")
# # bcd.class_method()
# # bcd.static_method()
#
# # obj=bcd()
# # obj.class_method()
# # obj.static_method()
#
# class MyClass:
#     pass
#
# obj = MyClass()
# print("Class name:", obj.__class__.__name__)
# print("Module name:", obj.__module__)
# print("Class name:", obj.__class__)

#
# class parent:
#     def parent_method(self):
#         print("parentmethod")
# class chlid(parent):
#     def chlid_method(self):
#         print("chlidmethod")
#
# obj=chlid()
# obj.chlid_method()
# obj.parent_method()


class Player:
    def __init__(self,name):
        self.name=name

class Team:
    def __init__(self):
        self.players=[]

    def add_players(self,player):
        self.players.append(player)
        #print("".join(str(self.players)))


player1=Player("vishnu")
player2=Player("Sudha")
team=Team()
team.add_players(player1)
team.add_players(player2)
print(team.players)
