import random
digits = '0123456789'
l_letters = 'abcdefghijklmnopqrstuvwxyz'
u_letters = l_letters.upper()
l_special = '!#$%&*+-=?@^_.'
misspell = 'il1Lo0O'

chars = [] #valid password characters

def is_valid_int(input):
    if input.isdigit() and int(input)>0 and int(input)==float(input):
        return True
    else:
        return False

def check_bool(input):
    if input.lower()=='y':
        return 1
    elif input.lower()=='n':
        return 0
    else:
        return -1

def user_request(question='',type='u_int',default_answer=''):
    result=''
    if type=='u_int':
        while not is_valid_int(result):
            result=input(question+' (default '+str(default_answer)+'): ') or default_answer
        result=int(result)
    elif type=='bool':
        while check_bool(result) < 0:
            result = input(question+' y/n (default '+str(default_answer)+'): ') or default_answer
        result = check_bool(result)
    else:
        raise ValueError
    return result

def gen_pswd(length=8, chars=[chr(i) for i in range(ord('A'), ord('z')+1)]):
    psw=''
    for _ in range(length):
        psw+=random.choice(chars)
    return psw


#################################################
print('<<<SAFE PASSWORDS GENERATOR>>>')
gen_amount = int(user_request('Enter amount of passwords to generate','u_int','5'))
gen_length = int(user_request('Enter password length','u_int','8'))
use_digits = user_request('Use digits [0-9]','bool','y')
use_upper = user_request('Use uppercase letters [A-Z]','bool','y')
use_lower = user_request('Use lowercase letters [a-z]','bool','y')
use_special = user_request('Use special chars [!#$%&*+-=?@^_]','bool','y')
exclude_misspell = user_request('Exclude characters that can be mixed up [il1Lo0O]','bool','n')

if use_digits:
    chars+=list(digits)
if use_upper:
    chars+=list(u_letters)
if use_lower:
    chars+=list(l_letters)
if use_special:
    chars+=list(l_special)
if exclude_misspell:
    for c in misspell:
        while c in chars:
            del chars[chars.index(c)]

pswds=[]
for _ in range(gen_amount):
    pswds.append(gen_pswd(gen_length,chars))
print('Your passwords:')
print(*pswds,sep='\n')

