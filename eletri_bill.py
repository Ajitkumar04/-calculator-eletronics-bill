def amount():
  input("what' your name?")
  units=int(input("how many units of eletricity did you use?"))
  bill_amount= units*8
 # print(bill_amount)
  if bill_amount>500:
    print(bill_amount+100)
  else:
    print(bill_amount)
amount()
   

