admin_username = "admin"
admin_password = "admin"

def department_id():
    department = input("fanni / ensani/ tarbiat " )
    try:
        if department == "fanni":
            stdeid = "1"
        elif department == "ensani":
            stdeid = "2"
        elif department == "tarbiat":
            stdeid = "3"
        return stdeid
    except:
        return "there is no such DEPARTMENT!"
    

def help():
    a = "\nthis is a test for our help function to show that." 
    return a

def about():
    a = "\nthis is a test for our about function to show that."
    return a