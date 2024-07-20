with open('abc.txt','r') as file:
 print(file.read())
  
with open("mpx","w") as f:
 f.write("This ")

import os
os.remove("mpx")