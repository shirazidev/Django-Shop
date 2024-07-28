import re


# iran mobile

phone_pat = re.compile(r'^(\+98|0)?9\d{9}$')
phone_number = int(input('Enter phone number: '))
if phone_pat.match(str(phone_number)):
    print('Valid phone number')
else:
    print('Invalid phone number')
    

# nat code
nat_code_pat = re.compile(r'\d{10}')
nat_code = int(input('Enter national code: '))
if nat_code_pat.match(str(nat_code)):
    print('Valid national code')
else:
    print('Invalid national code')
    
    
# name 
name_pat = re.compile(r'^[a-zA-Z\u0600-\u06FF\s]+$')
name = str(input('Enter name: '))

if name_pat.match(name):
    print('Valid name')
else:
    print('Invalid name')