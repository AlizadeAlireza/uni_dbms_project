

class Abilitiy:
    # a = "for student"
    def available_courses(self):
        pass
    def show_informations(self):
        pass
    def select_course(self):
        pass
    def remove_course(self):
        pass
    def total_average(self):
        pass
    def term_average(self):
        pass

class AdminAbility(Abilitiy):
    def remove_default_course(self):
        pass
    def add_course(self):
        pass
    def add_student(self):
        pass

class StudentAbility(Abilitiy):
    pass

# b = StudentAbility()
# print(b.a)