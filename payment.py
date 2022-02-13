# Toll management software - Exit / Payment
print("Hello !")

# Ask for the terminal number
nb = input("What is the entry terminal number? ->")

# Calculation of the distance traveled according to the number of the terminal
if nb == "1":
  nk = 50
  price = 1.70
elif nb == "2":
  nk = 30
  price = 1.30
elif nb == "3":
  nk = 110
  price = 2.70
elif nb == "4":
  nk = 80
  price = 2.10
elif nb == "5":
  nk = 220
  price = 3.70
else:
  print("The number indicated is not associated with a terminal")
  quit()

# Price display
print("You have traveled " + str(nk) + "km and you have to pay : " + str(price) + "€")

# Collection of payment method
print("Visa / Mastercard / Cash")
mp = input("How would you like to pay ? ->")

if mp == "Visa":
  print("Follow the instructions on the payment terminal")
elif mp == "Mastercard":
  print("Follow the instructions on the payment terminal")
elif mp == "Espèces":
  print("Insert currency below")
else:
  print("The specified payment method is not supported")
  quit()

# Farewell and opening of the barrier
print("Barrier open - Have a good trip!")
