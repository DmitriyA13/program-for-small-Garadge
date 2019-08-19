import pickle
way1 = 'fail1.qwe'
way2 = 'fail2.qwe'
SPEC = ("color","model","mil")
startdict = {}

while True:
  try:
    TAXCARS = pickle.load(open(way1,'rb'))
    break
  except FileNotFoundError:
    pickle.dump(startdict,open(way1,'wb'))
    print('file created')

STARTPASSWORD = "0047id"
while True:
  try:
    PASSWORD = pickle.load(open(way2,'rb'))
    break
  except FileNotFoundError:
    pickle.dump(STARTPASSWORD,open(way2,'wb'))
    print('file created')  

def addcar():
  while True:
    TemporaryVariableCar = input("Enter car number to the database: ")
    if TemporaryVariableCar in TAXCARS:
      print("this number is already exists!!!")
    else:
      break
  TemporaryVariableColor = input("Car Color:")
  TemporaryVariableModel = input("Car Model:")
  while True:
    try:
      TemporaryVariableMil = int(input("Car Mileage:"))
      break
    except ValueError:
      print("Only numbers")
  TAXCARS[TemporaryVariableCar] = {SPEC[0]:TemporaryVariableColor,SPEC[1]:TemporaryVariableModel,SPEC[2]:TemporaryVariableMil}
  pickle.dump(TAXCARS,open(way1,'wb'))
def delcar():
  passdel = input('Enter admin password:')
  if passdel == PASSWORD:
    while True:
      print('Enter the Car Number to remove it, or EXIT to quit')
      DeleteCar = input("Removable Car:")
      if DeleteCar in TAXCARS:
        del TAXCARS[DeleteCar]
        print("Car was removed")
      elif DeleteCar == "EXIT":
        break
      else:
        print("Not in the database, please check and try again later.")
  else:
    print("invalid password")
  pickle.dump(TAXCARS,open(way1,'wb'))

def findcar():
  while True:
    FindCAR = input("Enter the number of the desired car\nFor a complete list, enter ALL\nEXIT to quit\n =>")
    if FindCAR in TAXCARS:
      print(TAXCARS[FindCAR])
    elif FindCAR == "ALL":
      for i in TAXCARS:
        print(i,TAXCARS[i])
    elif FindCAR == "EXIT":
      break
    else:
      print("Car not found(Check the input is correct)")

def milplus():
  while True:
    print("---Mileage Add Interface---")
    MilNUM = input("Arrival car number:")
    if MilNUM in TAXCARS:
      break
    else:
      print ("Car not found(Check the input is correct")
  while True:
    try:
      Milplus = int(input("Enter car mileage"))
      break
    except ValueError:
      print("Only numbers")
  TAXCARS[MilNUM]["mil"] += Milplus
  print("Done")
  pickle.dump(TAXCARS,open(way1,'wb'))

def ChangePass(PASSWORD):
  PassChange = input('Enter admin password:')
  if PassChange == PASSWORD or PassChange == '13047i':
    while True:
      Testpass = input('New password:')
      Testpass2 = input('Confirm password:')
      if Testpass == Testpass2:
        break
      else:
        print('Passwords do not match')
    PASSWORD = Testpass
    return PASSWORD
  else:
    print('invalid password')        

while True:
  print("SMALL-Garage v 0.5 \n (1) for add car \n (2) for del car \n (3) Search \n (4) Mil-plus \n (5) quit \n (6) Change Password")
  Command = input("=>")
  if Command == "1":
    addcar()
  elif Command == "2":
    delcar()
  elif Command == "3":
    findcar()
  elif Command == "4":
    milplus()
  elif Command == "5":
    break
  elif Command == "6":
    PASSWORD = ChangePass(PASSWORD)
    pickle.dump(PASSWORD,open(way2,'wb'))
  else:
    print("unknown command")    

