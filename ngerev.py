import requests
from concurrent.futures import ThreadPoolExecutor
import os

banner = '''\033[92m
███╗   ██╗ ██████╗ ███████╗██████╗ ███████╗██╗   ██╗
████╗  ██║██╔════╝ ██╔════╝██╔══██╗██╔════╝██║   ██║
██╔██╗ ██║██║  ███╗█████╗  ██████╔╝█████╗  ██║   ██║
██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗██╔══╝  ╚██╗ ██╔╝
██║ ╚████║╚██████╔╝███████╗██║  ██║███████╗ ╚████╔╝ 
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝  ╚═══╝  
\033[97m[ \033[92mCoded By \033[92m'/Mine7 \033[97m||\033[92m  github.com/InMyMine7 \033[97m||\033[92m t.me/InMyMineee \033[97m]    

\033[97m[\033[92m~\033[97m] 1. SINGGEL IP 
\033[97m[\033[92m~\033[97m] 2. LIST IP TXT                                           
'''
def reverse_ip(ip_address):
    url = f"https://reverseip.rei.my.id/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["RequestStatus"] == "success":
            return data["RequestResult"]["ResultDomainList"]
        else:
            return []
    except requests.RequestException as e:
        print(f"An error occurred during the request for IP {ip_address}: {str(e)}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred for IP {ip_address}: {str(e)}")
        return None

def read_ip_addresses_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            ip_addresses = file.readlines()
            ip_addresses = [ip.strip() for ip in ip_addresses if ip.strip()]  # Remove empty lines
        return ip_addresses
    except Exception as e:
        print("An error occurred while reading the file:", str(e))
        return []

def save_to_result_file(ip_address, domains):
    with open("result.txt", "a") as result_file:
        result_file.write(f"Domains for IP {ip_address} are:\n")
        for domain in domains:
            result_file.write(domain + "\n")
        result_file.write("\n")  # Add a blank line after each IP's domains

def process_ip(ip_address):
    domains = reverse_ip(ip_address)
    if domains:
        print("Domains for IP", ip_address, "are:")
        for domain in domains:
            print("\033[97m[\033[92m+\033[97m] " + domain)
        save_to_result_file(ip_address, domains)
        print(f"\033[97m[\033[92m~\033[97m] Results for IP {ip_address} have been saved to result.txt")
    else:
        print("No domains found for the IP address:", ip_address)

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    print(banner)
    source_choice = input("\033[97m[\033[92m~\033[97m] ")
    if source_choice == "1":
        ip_address = input("\033[97m[\033[92m~\033[97m] Enter the IP address to reverse: ")
        process_ip(ip_address)
    elif source_choice == "2":
        file_path = input("\033[97m[\033[92m~\033[97m] Enter the path to the file containing IP addresses (.txt): ")
        ip_addresses = read_ip_addresses_from_file(file_path)
        if ip_addresses:
            with ThreadPoolExecutor(max_workers=5) as executor:
                executor.map(process_ip, ip_addresses)
        else:
            print("No IP addresses found in the specified file.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
