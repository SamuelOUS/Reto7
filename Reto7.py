from dataclasses import dataclass
from typing import Union

class person:
    def __init__(self,Name,Age,Size,Hair_color):
        self.Name:str = Name
        self.Age:int = Age
        self.Size:float = Size
        self.Hair_color:str = Hair_color
    def Walk(self, distance: Union[int,float]):
        print(f"{self.Name}a caminado {distance}")

    def Eat(self, food: str):
        print(f"{self.Name}a consumido {food}")

    def talk(self,language: str):
        print(f"{self.Name}habla {language}")


class Teacher(person):

    def Teach(self, subject):
        print(f"El profesor {self.Name} dicta {subject}")




class Student(person):

    def Study(self, subject):
        print(f"El estudiante {self.Name} estudia {subject}")


S1 = Student("Samuel", 15, 1.78, "black")
T1 = Teacher("Tomas", 58, 1.72, "black")
T1.Teach("Matematicas")
S1.Study("Matematicas")



















































