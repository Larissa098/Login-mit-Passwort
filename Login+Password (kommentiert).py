# Das Programm fragt sie nach ihrem Benutzernamen und Passwort
x=input("geben sie bitte ihr Benutzername ein: ")
z=input("Bitte geben sie ihr Passwort ein: ")


########################################################################################################
# Falls der Benutzername Anna_Müller und das Passwort coolheit ist, wird "Herzlich Willkommen Anna" ausgegeben. 
if x == "Anna_Stöckli"and z =="coolheit": 
    print("Herzlich Willkommen Anna")
#Falls der Benutzername Max_Meyer und das Passwort hallo123 ist, wird "Herzlich Willkommen Max" ausgegeben. 
elif x == "Max_Meyer"and z =="hallo123":
    print("Herzlich Willkommen Max")
# Falls keiner dieser Benutzernamen/Passwörter eingegeben wurden,wird ein Fehler ausgegeben. 
else: 
    print("Benutzername und/oder Passwort nicht korrekt")
########################################################################################################
