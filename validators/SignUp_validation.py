import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def email_check(email):
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False
def phone_num_validate(s):
    c=0
    for i in s:
        if i >='0' and i<='9':
            c+=1
    return c == 11


def fix(username=str):
    s=""
    space=0
    for i in username:
        if i == ' ':
            if space<1:
                space+=1
                s+=i
        else:
            space=0
            s=s+i
    s=s.capitalize()
    return s
    
def name_validate(username=str):
    #should be only lower or upper case letters from a to z
    c=0
    for i in username:
        if i>='a' and i<='z' or i>='A' and i<='Z' or i==' ':
            c+=1
    return c == len(username)