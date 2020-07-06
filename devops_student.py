# Hides the complexity's from the user.


from abc import ABC # Used when using abstraction
class Student(ABC):
    # method initializes the abstract method


class Devops(Student):
    def __init__(self, first_name, last_name, stream): # This adds an attribute "stream" to the devops sub class.
        self.first_name = first_name
        self.last_name = last_name
        self.stream = stream

    def full_name(self):
        print(self.first_name, self.last_name)

    def roll_call(self):
        print("I am a Devops Student")
