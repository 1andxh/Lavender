# Create a program that will:

# Store personal details (like name, age, and favorite colors) in variables and dictionaries.
name  = input("enter name: ")
age = int(input("enter age: "))
favorite_color = input("what's your favorite color(s): ").split(",")
personal_details ={"name":name,
          "age" :age,
          "favourite color": favorite_color
          }

print(personal_details)

# Store a list of friends' names.
friends = []
store_names = input("Enter friends name: ")
friends.extend(store_names.split())
print(f"you stored these names as friends: {friends}")

# Allow a user to update their personal information, like age and favorite color.
update_age = int(input("Enter age to update details: "))
personal_details["age"] = update_age 
update_color = input("Enter new color to update: ")
personal_details["favourite color"] = update_color
print(f"Personal details updated!")

# remove a friend fromt the list
remove_friend = input("Who do you want to remove?: ")
friends.remove(remove_friend)
print(f"you removed {remove_friend}, \nfriends left; {friends}\n")

# Display the updated information in an organized format.
print("UPDATE INFORMATION")
print(f"Updated age: {update_age}")
print(f"Updated color: {update_color}")
print(f"Current details: \n{personal_details}")
