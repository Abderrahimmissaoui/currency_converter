import os 
import time
def clear_screen():
  os.system("cls" if os.name =="nt" else "clear" )

dollar=("""
 ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| Moon RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| Moon RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
""")

currency_rates={
  "":dollar,
  "USD":1.0,
  "EUR":0.82, 
  "EGP":30.9,
  "RMB":6.5,
} 
def display():
  clear_screen()
  print("Welcome to the currency converter.\n")
  for currency in currency_rates:
    print(f"{currency} : {currency_rates[currency]}\n")
  print("-----------------------------------------------------------------")  


def currency_converter():
  display()
  from_currency=input("Choose a currency to convert from: ").upper()
  while True:
    amount=float(input("\nEnter the amount: "))
    conformation=input(f"\nYou entered {amount} {from_currency}. Confirm? (Y/N):  ").upper()
    if conformation=='Y':
      break
  display()
  to_currency=input("\nChoose a currency to convert to: ").upper()
  print("\nAnalyzing your request.....please wait")
  time.sleep(2)

  print(f"\nChecking for {to_currency}'s best available.....please wait ")
  time.sleep(2)

  print(f"\nGetting discount price for {from_currency} ......please wait ")
  time.sleep(2)

  print(f"\nPreparing the deal from {from_currency} to {to_currency}......plaese wait ")
  time.sleep(2)

 
  if from_currency in currency_rates and to_currency in currency_rates:
    rate=currency_rates[to_currency]/currency_rates[from_currency]
    new_rate=amount * rate
    display()
    print(f"\nExchange rate 1 {from_currency} = {round(rate,2)} {to_currency}. ")
    print(f"\n{amount} {from_currency} equal {round(new_rate,2)} {to_currency}. ")
    if(input("\nDo you accept this transaction: (Y/N): ")).lower() =="y":
      print(f"\nGetting discount price for {from_currency} ......please wait ")
      time.sleep(2)

      print(f"\nPreparing the deal from {from_currency} to {to_currency}......plaese wait ")
      time.sleep(2)
      print("\nTransaction done successfully.")
      if (input("\nDo you want to perform another conversion? (Y/N): ")).lower() =="y":
        currency_converter()
      else:
        print("\nExiting the program.....")
    else:
      print("\nTransaction canceled.")
      if (input("\nDo you want to perform another conversion? (Y/N): ")).lower() == "y":
        currency_converter()
      else:
        print("\nExiting the program......")
  else:
    print("\nInvalid input.\n")
    time.sleep(3)
    currency_converter()

currency_converter()
    
  