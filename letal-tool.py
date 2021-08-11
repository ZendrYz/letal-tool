#########################IMPORTS###############################
import os
from colorama import Fore
from urllib.request import urlopen
import json
import socket
import webbrowser
import random
import string
import requests
import random
import socket


os.system("cls")

# ctypes.windll.kernel32.SetConsoleTitle("Tool de Letal Net")


def main():
    print(Fore.BLUE + """
                             #LetalNet               
  _         _        _   _   _      _   
 | |    ___| |_ __ _| | | \ | | ___| |_ 
 | |   / _ \ __/ _` | | |  \| |/ _ \ __|
 | |__|  __/ || (_| | | | |\  |  __/ |_ 
 |_____\___|\__\__,_|_| |_| \_|\___|\__|
                                        
""")

    print(Fore.WHITE + "Tool de Letal Net")
    print(Fore.WHITE + "Versión 1.1 | Coded by ZendrYz")
    print()
    print(Fore.GREEN + "[1] CANAL DE KRYSSI$")
    print(Fore.GREEN + "[2] TIK TOK DE LETAL NET")
    print(Fore.GREEN + "[3] CONSEGUIR IP DE UN DOMINIO")
    print(Fore.GREEN + "[4] GEOLOCALIZACIÓN POR IP")
    print(Fore.GREEN + "[5] GEN + CHECKER DE NITRO")

    menu = input(Fore.WHITE + "Inserte una opción >> ")

    if menu == "1":

        webbrowser.open(
            "https://www.youtube.com/channel/UCbpIrs3r8mLoMIi-BGvZFbA", new=2, autoraise=True)
        os.system("cls")
        main()

    if menu == "2":

        webbrowser.open(
            "https://www.tiktok.com/@letalnet?lang=es&is_copy_url=1&is_from_webapp=v1", new=2, autoraise=True)
        os.system("cls")
        main()

    if menu == "3":

        os.system("cls")
        ip2 = input(
            Fore.RED + "[Letal Net TOOL] Inserte aqui la URL de la web >> " + Fore.GREEN)

        print()
        ip = socket.gethostbyname(str(ip2))
        print(Fore.YELLOW + "La direccion IP es >> " + Fore.BLUE + str(ip))

        print()
        menu2331 = input(
            Fore.WHITE + "Presione la tecla intro para volver al menu...")

        os.system("cls")

        main()

    if menu == "4":

        os.system("cls")

        ip = input(Fore.RED + '[Letal Net TOOL] Coloca la IP a rastrear >> ')

        url = "http://ip-api.com/json/"

        response = urlopen(url + ip)

        data = response.read()

        values = json.loads(data)
        print("\n")
        print(Fore.BLUE + "IP: " + values['query'])
        print("\n")
        print(Fore.BLUE + "Ciudad: " + values['city'])
        print("\n")
        print(Fore.BLUE + "ISP: " + values['isp'])
        print("\n")
        print(Fore.BLUE + "Pais: " + values['country'])
        print("\n")
        print(Fore.BLUE + "Zona horaria: " + values['timezone'])
        print("\n")
        print(Fore.BLUE + "Zip code: " + values['zip'])
        print("\n")

        input(Fore.WHITE + "Geolocalización completada. Presiona la tecla intro para continuar...")

        os.system("cls")
        main()

    if menu == "5":
         os.system("cls")
         num = input(
            Fore.RED + '[Letal Net TOOL] Teclea cuantos codigos desea generar y checkear. Para verlos mejor se te creará un archivo llamado Nitro Codes.txt donde los podrás ver con más claridad >> ')

         f = open("Nitro Codes.txt", "w", encoding='utf-8')

         for n in range(int(num)):
          y = ''.join(random.choice(string.ascii_uppercase +
                    string.digits + string.ascii_lowercase) for _ in range(24))
         f.write('https://discord.gift/')
         f.write(y)
         f.write("\n")

         with open("Nitro Codes.txt") as f, open('Valid Codes.txt', 'w', encoding="UTF-8") as valid:
          for line in f:
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + \
                nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 0:
                print(" Valid | {} ".format(line.strip("\n")))
                valid.write(url)
                valid.write("\n")
                break
            else:
                print(" Invalid | {} ".format(line.strip("\n")))
                break

                os.system("cls")

                main()
       
    else:
        os.system("cls")
        print(Fore.RED + "¡Has introducido un numero incorrecto!")
        print()
        menu22331 = input(
            Fore.WHITE + "Presiona la tecla intro para volver al menu...")

        os.system("cls")

        main()


os.system("cls")
main()
