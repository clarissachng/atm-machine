#Function for main page
def MainPage():
  attempts = 3
  quitProgram = False
  while attempts > 0:
    print("Please enter '0' if you wish to quit the program")
    pin2 = int(input("Enter your PIN number:\n"))
    if user['pin'] == pin2:
      print("PIN number accepted!")
      SelectTransaction()  
    elif pin2 == 0:
      quitProgram = True
      print("Program End *Please do ignore the following statement!*")
      break
    else:
      print("Invalid PIN")
      attempts -= 1
      print(f"You have {attempts} attempts left\n")
      continue
  print("You have no more attempts and your card has been retained")

# Function for select transaction
def SelectTransaction():
  print("Select a transaction:\n")
  print("Enter '1' for Balance Enquiry")
  print("Enter '2' for Withdrawal")
  print("Enter '3' for Deposit")
  print("Enter '4' to Quit\n")
  answer = int(input("Selection:"))
  if answer == 1:
    BalanceEnquiry()
  elif answer == 2:
    WithdrawMoney()
  elif answer == 3:
    Deposit()
  # Returns to the Main Page with the message prompt to quit the program
  elif answer == 4:
    quitProgram = True
  else:
    print("Please enter a correct value shown")
  return 

# Function for balance enquiry
def BalanceEnquiry():
    print(f"Your balance is £{user['balance']}\n")
    return 

# Function for money withdrawal
def WithdrawMoney():
    while True:
        withdrawAmount = int(input("Enter the amount of money you want to widthdraw: \n"))
        if withdrawAmount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - withdrawAmount
            print(f"£{withdrawAmount} successfully widthdrawn. Your remaining balance is £{user['balance']}\n")
            return False

# Function for money deposit
def Deposit():
  depositAmount = int(input("Enter the amount of money you want to deposit: \n"))
  user['balance'] = user['balance'] + depositAmount
  print(f"£{depositAmount} successfully deposited. Your balance is £{user['balance']}\n")
  return 


# Welcome message
print("Welcome to ABCD Bank")

import random 
user = {'pin': 1234, 'balance':random.randint(100,1000)}

MainPage()