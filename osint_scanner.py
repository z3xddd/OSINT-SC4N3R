#!/usr/bin/env python3
#
# OsInT Sc4N3r - Tool for automated recon process on bug bounty
# by: Israel Comazzetto dos Reis [@z3xddd]

import os
from time import sleep

class OsInT_Sc4N3r(object):
    def __init__(self, domain):
        self.domain = domain
    
    def enumerate_subdomains(self):
        print("[*] Enumeration subdomains process starting... [*]")
        enumerate_command = 'echo '+self.domain+' | haktrails subdomains | notify'
        print("[*] Haktrails execute process starting... [*]")
        sleep(2)
        print(os.popen(enumerate_command).read())
        print("[+] Haktrails scan finished... See details on haktrails_result.txt [+]")
        '''log_haktrails = open('/root/')
                                file_n_err = open('n_err.txt','w')
                        file_n_err.write(arquiv_n_errado)
                        file_n_err.close()'''

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
user_domain_input = str(input("[+] Enter domain to scan >>  "))
domain_to_scan = OsInT_Sc4N3r(user_domain_input)
domain_to_scan.enumerate_subdomains()