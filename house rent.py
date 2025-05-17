# inputs we need from the users
# total rent
# Total food orderred for snaking
# electricity units spend
# charge per unit
# person living in rom /flat

# output
# total amnount you' ve to pay is

rent = int(input("Enter your hostel/flat rent="))
food = int(input("Enter the amnount of foof ordered"))
electruicity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of persons living in room/flat ="))

total_ball = electruicity_spend * charge_per_unit

ouput = (food + rent + total_ball) // persons

print("Each person will pay = ", ouput)

