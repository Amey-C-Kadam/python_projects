
import re

def register():
  
  db= open('db.txt','r')
  email=input('Enter email id -')
  password=input('Enter password - ')
  password1=input('Confirm password - ')

  if password!=password1:
    print('Your password does not match')
  else:
    if 5>len(password) or len(password)>16:
      print('Enter password in the range of 5 to 16 character')
    elif not re.search('[a-z]',password):
      print('Password must have lowercase character') 
    elif not re.search('[A-Z]',password):
      print('password must have upper case character')
    elif not  re.search('[0-9]',password):
      print('password must have integer ' )
    elif not  re.search('[@#$%^&*!]',password):
      print('password must have atleast 1 special character ')
    elif '@' and '.' not in email:
      print('email must have @ and . ')
    elif '@.'  in email:
      print('@. or .@ not allowed')
    elif '@gmail.com' in email:
      print('Enter valid email ')
    elif not (re.search('[a-z]',email[0]) or re.search('[A-Z]',email[0])):
      print('email cannot start with special character or integer ')
    else:
      db=open('db.txt','a')
      db.write(email+'   '+password+ '\n')
      print('You are successfully registered')


def login():
  db= open('db.txt','r')
  email=input('Enter email id -')
  password=input('Enter password - ')
  d=[]
  e=[]
  
  for i in db:
        a,b = i.split("   ")
        b = b.strip()
        d.append(a)
        e.append(b)
  data = dict(zip(d,e))
  if email in d:
    if password in e:
      print('login Successfull!')
    else:
      print('Enter correct password ')
      login()
  else:
    print('Please Register ')
    register()


def forget_password():
  db= open('db.txt','r')
  email=input('Enter email id -')
  
  d=[]
  e=[]
  
  for i in db:
        a,b = i.split("   ")
        b = b.strip()
        d.append(a)
        e.append(b)
  data = dict(zip(d,e))
  print(f'The password is {data.get(email)}')
  
def choice():
  user=input('login  signup  forget_password - ')
  if user=='login':
    login()
  if user=='signup':
    register()
  if user=='forget_password':
    forget_password()

choice()