from http.client import CONTINUE

import os

shutdown=input("do you want to shutdown?(yes/no)")
if shutdown =='no':
    CONTINUE
else:
    os.system("shutdown /s /t 1")
