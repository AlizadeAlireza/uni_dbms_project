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
    

