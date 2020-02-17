import re

string2work = "ABCDCDC"

print(len(re.findall('(?=CDC)', string2work)))