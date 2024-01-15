

attempt = 3
while attempt >= 1 :
    
    password = input("Ingresa una contraseña que inicie con un numero: ")
    password_char = password[0]
    
    if password_char.isdigit() == True:
    
        password_ver = input("Ingresa nuevamente la contraseña: ")
        
        if password == password_ver:
            print("Contraseña correcta :) ")
            break
        else:
            print("Las contraseñas no coinciden")
            attempt -= 1
            # print(attempt, "flag de attempt")
            if attempt == 0: #este lo tuve que poner por que me daba 4 intentos, lo cual esta raro por que mi condicion original era while attempt > 0, entonces al llegar a 0 ya no deberia entrar el cliclo de nuevo, pero entraba una 4ta vez
                break
            else:                
                password_ver = input("Ingresa nuevamente la contraseña nuevamente: ")
                if password == password_ver:
                    print("Contraseña correcta :) ")
                    break
                else:
                    print("Las contraseñas no coinciden")
                    attempt -= 1
                    # print(attempt, "flag de attempt")
    else:
        print("La contraseña debe comenzar con un numero")
        attempt -= 1                 
             
print("Fin del programa")            