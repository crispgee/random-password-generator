import random
import string

def password_generator(length = 12):
          characters = string.ascii_letters + string.digits +string.punctuation
          password=''.join(random.choice(characters) for i in range(length))
          
          print(password)
          
           
        
password_generator()                     