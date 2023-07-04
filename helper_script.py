admin_username = "admin"
admin_password = "admin"

def department_id():
    department = input("1, fanni /2, ensani/3, tarbiat: " )
    try:
        if department == "1":
            stdeid = "1"
        elif department == "2":
            stdeid = "2"
        elif department == "3":
            stdeid = "3"
        return stdeid
    except:
        print("\nthere is no such DEPARTMENT!")
    
def lesson_type():
    type = input("\n1, amali /2, nazari: " )
    try:
        if type == "1":
            lesson_type = "amali"
        elif type == "2":
            lesson_type = "nazari"
        else:
            print("\nthere is no such lesson type!")

        return lesson_type
        
    except:
        print("\nthere is no such lesson type!")

def help():
    a = "\nthis is a test for our help function to show that." 
    return a

def about():
    a = "\nthis is a test for our about function to show that."
    return a


def student_level():
    level = input(" \nselect the level: 1, bs / 2, phd / 3, ms: ")
    try:
        if level == "1":
            stu_level = "bs"
        elif level == "2":
            stu_level = "phd"
        elif level == "3":
            stu_level = "ms"
        return stu_level
    except:
        return "there is no such DEPARTMENT!"
