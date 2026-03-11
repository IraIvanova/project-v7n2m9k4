from colorama import Fore

def console(message, type="message"):
    if type == "error":
        print(f"{Fore.LIGHTRED_EX}{message}")

    elif type == "success":
        print(f"{Fore.LIGHTGREEN_EX}{message}")

    else:
        print(f"{Fore.LIGHTYELLOW_EX}{message}")