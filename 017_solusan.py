#########PASSWORD STRENGTH CHECAR
password="Secure3p@ss"


if len(password)<6:
    strength="Weak"
elif len(password)<=10:
    strength="Medium"
else:
    strength="strong"
print("password strength is:",strength)



#password strength is: strong