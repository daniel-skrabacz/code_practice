print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3
mass = weight/2.34
# Write an if statement below:

if planet == 1:
  print('Venus!')
  print(mass*0.91)
elif planet == 2:
  print('Mars')
  print(mass*0.38)
elif planet == 3:
  print('Jupiter')
  print(mass*2.34)
elif planet == 4:
  print('Saturn')
  print(mass*1.06)
elif planet == 5:
  print('Uranus')
  print(mass*0.92)
elif planet == 6:
  print('Neptune')
  print(mass*1.19)
