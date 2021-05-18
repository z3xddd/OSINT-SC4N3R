#!/usr/bin/env python3
#
# OsInT Sc4N3r - Tool for automated recon process on bug bounty
# @author: Israel C. dos Reis [@z3xddd]

from os import popen, geteuid, sysconf
from time import sleep

class OsInT_Sc4N3r(object):
    def __init__(self, domain):
        self.domain = domain
    
    def validate_run_as_root(self):
        if not geteuid() == 0:
            print("[-] Please run this script as root... [-]")
            exit()
        else:
            pass

    def portscan(self):
        portscan_command = 'nmap -v -Pn -O -sV -p- '+self.domain+' > results/result_portscan_'+self.domain+'.txt'
        print("[*] Portscan execute process starting... [*]")
        print(popen(portscan_command).read())
        print('[+] Portscan scan finished... See details on results/result_portscan_'+self.domain+'.txt [+]')

    def enumerate_subdomains_assetfinder(self):
        enumerate_command = 'assetfinder -subs-only '+self.domain+' >> results/result_assetfinder_'+self.domain+'.txt'
        print("[*] Assetfinder execute process starting... [*]")
        print(popen(enumerate_command).read())
        print('[+] Assetfinder scan finished... See details on results/result_assetfinder_'+self.domain+'.txt [+]')

    def enumerate_webservers(self):
        enumerate_command = 'cat results/result_assetfinder_'+self.domain+'.txt | httpx --silent > results/result_httpx_'+self.domain+'.txt'
        print("[*] Httpx execute process starting... [*]")
        print(popen(enumerate_command).read())
        print('[+] Httpx scan finished... See details on results/result_httpx_'+self.domain+'.txt [+]')
   
    def nuclei_attack(self):
        attack_command = 'nuclei -l results/result_httpx_'+self.domain+'.txt -t ../nuclei-templates/ > results/result_nuclei_'+self.domain+'.txt'
        print("[*] Nuclei attack execute process starting... [*]")
        print(popen(attack_command).read())
        print('[+] Nuclei attack finished... See details on results/result_nuclei_'+self.domain+'.txt [+]')
    

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
                                                                                 by: Israel C. dos Reis [@z3xddd]
    """)
user_domain_input = str(input("[+] Enter domain to scan >>  [ EX: domain.com.br ]  "))
domain_to_scan = OsInT_Sc4N3r(user_domain_input)
domain_to_scan.validate_run_as_root()
domain_to_scan.portscan()
domain_to_scan.enumerate_subdomains_assetfinder()
domain_to_scan.enumerate_webservers()
domain_to_scan.nuclei_attack()
