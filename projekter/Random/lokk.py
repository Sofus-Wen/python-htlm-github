import sys

yes = ['yes', 'y', 'ye', "ja", "Ja", "j"]
no = {'no', 'n', "nej", "nope"}


x = input("Vil du svare: ")
if x == yes:
   print ("Godt...")
elif x == no:
   print("Ok....")
else:
   print("Skriv ja eller nej")

choice = input().lower()
if choice in yes:
   return True
elif choice in no:
   return False
else:
   sys.stdout.write("Please respond with 'yes' or 'no')
