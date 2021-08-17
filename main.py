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
import ctypes
import socket


os.system("cls")

ctypes.windll.kernel32.SetConsoleTitleW("Tool de Letal Net")


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
    print(Fore.GREEN + "[3] DISCORD DE LETAL NET")
    print(Fore.GREEN + "[4] SCAN DE SUBDOMINIOS")
    print(Fore.GREEN + "[5] CONSEGUIR IP DE UN DOMINIO")
    print(Fore.GREEN + "[6] GEOLOCALIZACIÓN POR IP")
    print(Fore.GREEN + "[7] SUMA DE NUMEROS")
    print(Fore.GREEN + "[8] RESTA DE NUMEROS")
    print(Fore.GREEN + "[9] MULTIPLICACIÓN DE NUMEROS")
    print(Fore.GREEN + "[10] DIVISÓN DE NUMEROS")
    print(Fore.GREEN + "[11] GEN + CHECKER DE NITRO")
    print()

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

        webbrowser.open("https://discord.gg/73pcu7B7V2", new=2, autoraise=True)

        os.system("cls")
        main()

    if menu == "4":
        os.system("cls")

        print()
        print()
        subdomains0 = ["www", "ovh-birdmc", "cpanel", "ns-vps", "d", "t", "short", "jar", "iptables", "ufw", "recuperar", "baneados", "imagenes", "samp", "social", "holo", "donaciones", "shoprp", "wow", "multicraft", "mail", "radio3", "radio2", "fr", "teamdub", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "docker", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "web", "dev", "tv", "deposito", "depositos", "extra", "extras", "bungee1", "torneoyt", "hcf", "uhc5", "uhc4", "uhc3", "uhc2", "uhc1", "uhc", "dedicado5", "dedicado4", "dedicado3", "dedicado2", "ded5", "ded4", "ded3", "ded2", "ded1", "ded", "gamehitodrh", "servidor4", "webmail", "monitor", "servidor001", "servidor10", "servidor9", "servidor8", "servidor7", "servidor6", "servidor5", "servidor4", "servidor3", "hvokfcic7sm", "autodiscover", "tauchet", "hg10", "ping", "hg9", "hg8", "hg7", "hg6", "hg5", "hg4", "hg3", "hg2", "hg1", "tienda", "status", "ayuda", "playstation", "home", "job", "firewall", "rank", "mantenimiento", "beta", "pay", "private", "port", "bb", "stor", "mx5", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1",
                       "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "translations", "staff", "help", "render", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "sv3", "sv2", "sv1",  "vps", "build", "web", "dev", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
        victima0 = input(
            Fore.RED + "[Letal Net TOOL] Inserte el dominio >> " + "" + Fore.GREEN+"")
        print()
        for ejecutar0 in subdomains0:
            ipserver0 = str(ejecutar0)+"."+str(victima0)
            iphost0 = socket.gethostname(str(ipserver0))
            print(Fore.MAGENTA+"[Letal Net TOOL] (21) Subdominios encontrados >> " +
                  Fore.CYAN+""+str(ejecutar0)+"."+str(victima0)+" >> "+Fore.YELLOW+""+str(iphost0))

        menu2332 = input(
            Fore.WHITE + "El scan de subdomains a finalizado, presione intro para volver al menu...")

        os.system("cls")
        main()

    if menu == "5":

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

    if menu == "6":

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

    if menu == '7':
        os.system("cls")
        numero1 = input(Fore.MAGENTA + "[Letal Net TOOL] Introduzca el primer numero >> ")

        numero2 = input(Fore.MAGENTA + "[Letal Net TOOL] Introduzca el siguiente numero >> ")

        res = int(numero1) + int(numero2)

        print("El resultado es: ", + res)
        print('\n')

        menudas = input(
            Fore.WHITE + "Resultado completado. Presiona la tecla intro para continuar...")

        os.system("cls")
        main()

    if menu == "8":
        os.system("cls")
        numero1 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el primer numero >> ")
        numero2 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el siguiente numero >> ")

        res = int(numero1) - int(numero2)

        print("El resultado es: ", + res)
        print('\n')

        menudas = input(
            Fore.WHITE + "Resultado completado. Presiona la tecla intro para continuar...")

        os.system("cls")
        main()

    if menu == "9":
        os.system("cls")
        numero1 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el primer numero >> ")
        numero2 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el siguiente numero >> ")

        res = int(numero1) * int(numero2)

        print("El resultado es: ", + res)
        print('\n')

        menudas = input(
            Fore.WHITE + "Resultado completado. Presiona la tecla intro para continuar...")

        os.system("cls")
        main()

    if menu == "10":
        os.system("cls")
        numero1 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el primer numero >> ")
        numero2 = input(
            Fore.MAGENTA + "[Letal Net TOOL] Introduzca el siguiente numero >> ")

        res = int(numero1) / int(numero2)

        print("El resultado es: ", + res)
        print('\n')

        menudas = input(
            Fore.WHITE + "Resultado completado. Presiona la tecla intro para continuar...")

        os.system("cls")
        main()

    if menu == "11":
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
# si lees esto eri gei jaja
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
