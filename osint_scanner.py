#!/usr/bin/env python3
#
# OsInT Sc4N3r - Tool for automated recon process on bug bounty
# by: Israel Comazzetto dos Reis [@z3xddd]

from os import popen
from time import sleep

class OsInT_Sc4N3r(object):
    def __init__(self, domain, logs):
        self.domain = domain
        self.logs = logs
    
    def enumerate_subdomains(self):
        print("[*] Enumeration subdomains process starting... [*]")
        if self.logs == 'Y' or self.logs == 'y':
            enumerate_command = 'echo '+self.domain+' | haktrails subdomains >> results/result_haktrails_'+self.domain+'.txt'
            print("[*] Haktrails execute process starting... [*]")
            sleep(2)
            popen(enumerate_command)
            print('[+] Haktrails scan finished... [+]')
        elif self.logs == 'N' or self.logs == 'n':
            enumerate_command = 'echo '+self.domain+' | haktrails subdomains'
            print("[*] Haktrails execute process starting... [*]")
            sleep(2)
            popen(enumerate_command)
            print('[+] Haktrails scan finished... [+]')
        else:
            print("[-] Unknown Option [-]")

print("""\

:'#######:::'######::'####:'##::: ##:'########:::::'######:::'######::'##::::::::'##::: ##::'#######::'########::
'##.... ##:'##... ##:. ##:: ###:: ##:... ##..:::::'##... ##:'##... ##: ##:::'##:: ###:: ##:'##.... ##: ##.... ##:
 ##:::: ##: ##:::..::: ##:: ####: ##:::: ##::::::: ##:::..:: ##:::..:: ##::: ##:: ####: ##:..::::: ##: ##:::: ##:
 ##:::: ##:. ######::: ##:: ## ## ##:::: ##:::::::. ######:: ##::::::: ##::: ##:: ## ## ##::'#######:: ########::
 ##:::: ##::..... ##:: ##:: ##. ####:::: ##::::::::..... ##: ##::::::: #########: ##. ####::...... ##: ##.. ##:::
 ##:::: ##:'##::: ##:: ##:: ##:. ###:::: ##:::::::'##::: ##: ##::: ##:...... ##:: ##:. ###:'##:::: ##: ##::. ##::
. #######::. ######::'####: ##::. ##:::: ##:::::::. ######::. ######:::::::: ##:: ##::. ##:. #######:: ##:::. ##:
:.......::::......:::....::..::::..:::::..:::::::::......::::......:::::::::..:::..::::..:::.......:::..:::::..::
                                                                   
#################################################################################################################                                                                   
                                                                   Tool for automated recon process on Bug Bounty
                                                                                                      by: @z3xddd
    """)
user_domain_input = str(input("[+] Enter domain to scan >>  [ EX: domain.com.br ]  "))
user_log_input = str(input("[+] Store the output in a text file? [ Write (Y) / (y) or (N) / (n) ] >>  "))
domain_to_scan = OsInT_Sc4N3r(user_domain_input, user_log_input)
domain_to_scan.enumerate_subdomains()
