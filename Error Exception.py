# EXCEPTIONS FOR ERRORS
try:
    age = int(input("How old are you?: "))
    income = 20000
    risk = income / age

except ZeroDivisionError:
     print("Age can not be 0")
except ValueError:
    print("Invalid value")
else:
    print("risk")