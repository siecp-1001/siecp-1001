from distutils.filelist import findall
from email.headerregistry import Address
import re 
doc=" For more details please mail us at: xyz@abc.com,pqr@mno.com"
new_address = re.sub(r'[\w\.-]+@[\w\.-]+',r'xhgf@mno.com',doc);
print(new_address)