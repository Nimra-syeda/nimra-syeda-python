

#Section 1
name = "Nimra"
age = 25
height = 5.5
is_student =True


print(name,type(name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))


# Section 2

name = input("\nWhat's your Name?:")
year_born = int(input("Please enter the year you wear born: "))
current_year = 2026
age = current_year - year_born
name_1 = name.strip().capitalize()

print(f"Hello,{name_1}! You are approximately {age} years old.")

# Section 3

number_1 =float(input("\nEnter the number:" ))
number_2 =float(input("Enter the another number:"))
product = number_1 * number_2
print()
print(f"{number_1}*{number_2} = {product:}")

#Section 4
item = "Programming Fundamentals Book"
price = 69.99
quantity = 4
total = price * quantity
print()
print("="* 25)
print("\t RECEIPT")
print("="*25)
print(f"Item: {item}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print("-"*25)
print(f"Total: {total}")
print("="*25)

#Section 5

hometown = input("\nEnter your hometown: ")
hometown_1 =hometown.strip().capitalize()
hobby = input("What's your hobby:")
hobby_1 =hobby.strip().capitalize()
fun_fact =input("One fun fact about you: ")
fun_fact_1 =fun_fact.strip().capitalize()


print()
print("╔══════════════════════════════╗")
print(f"\tPROFILE :{name_1}")
print("╚══════════════════════════════╝")
print(f"Hometown: {hometown_1}")
print(f"Hobby: {hobby_1}")
print(f"Fun fact: {fun_fact_1}")
print(f"Age:  {age}")
