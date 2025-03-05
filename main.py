# Imagine Tabia and Ajwa are shopping for fruits 

# Arithmetic Operators
tabia_apples = 5
ajwa_apples = 3

print("Arithmetic Operators:")
print("Total apples:", tabia_apples + ajwa_apples)  # Addition
print("Apples left after eating 2:", tabia_apples - 2)  # Subtraction
print("Apples if Tabia buys 3 times more:", tabia_apples * 3)  # Multiplication
print("Apples shared equally:", tabia_apples / 2)  # Division
print("Remaining apples if divided among 2 people:", tabia_apples % 2)  # Modulus
print("If apples double every day for 3 days:", tabia_apples ** 3)  # Exponentiation
print("Apples per person if divided evenly:", tabia_apples // 2)  # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print("Does Tabia have more apples than Ajwa?", tabia_apples > ajwa_apples)  
print("Do they have the same number of apples?", tabia_apples == ajwa_apples)
print("Does Ajwa have fewer apples than Tabia?", ajwa_apples < tabia_apples)

# Logical Operators
tabia_has_money = True
ajwa_has_money = False

print("\nLogical Operators:")
print("Can both buy oranges?", tabia_has_money and ajwa_has_money)  
print("Can at least one of them buy oranges?", tabia_has_money or ajwa_has_money)  
print("Does Tabia not have money?", not tabia_has_money)

# Bitwise Operators (Think of numbers as secret codes )
tabia_code = 6  # 110 in binary
ajwa_code = 3  # 011 in binary

print("\nBitwise Operators:")
print("Bitwise AND (Common bits):", tabia_code & ajwa_code)  
print("Bitwise OR (At least one bit):", tabia_code | ajwa_code)  
print("Bitwise XOR (Different bits):", tabia_code ^ ajwa_code)  
print("Bitwise NOT (Flip all bits of Tabia's code):", ~tabia_code)  
print("Tabia's code shifted left (×2):", tabia_code << 1)  
print("Tabia's code shifted right (÷2):", tabia_code >> 1)  

# Assignment Operators
print("\nAssignment Operators:")
tabia_money = 100
print("Tabia's money:", tabia_money)
tabia_money += 50  # Tabia gets more money
print("Tabia's money after getting 50 more:", tabia_money)
tabia_money -= 30  # Tabia buys snacks
print("Tabia's money after buying snacks:", tabia_money)

# Identity Operators (Checking if they are the same person)
x = [1, 2, 3]
y = [1, 2, 3]

print("\nIdentity Operators:")
print("Are Tabia and Ajwa the same person?", x is y)  # False, different objects
print("Are they different people?", x is not y)  # True

# Membership Operators
fruit_basket = ["apple", "banana", "mango"]

print("\nMembership Operators:")
print("Does the basket have apples?", "apple" in fruit_basket)  
print("Are there grapes in the basket?", "grape" not in fruit_basket)  

