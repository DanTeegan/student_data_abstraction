
# Hides the complexity's from the user.

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __full_name(self):
        print(self.first_name, " ", self.last_name)

    def __roll_call(self):
        print("I am a student")

    def __change_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def test_questions(self):
        pass

