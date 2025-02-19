# Filename: nested_if_else_statement.py

# Step 1: Get user input
age_str = input("Enter your age: ")
membership_str = input("Are you a member? (Yes/No): ")

# Step 2: Convert input
try:
    age = int(age_str)  # Convert age input to integer
    membership = membership_str.strip().lower()  # Convert membership input to lowercase and remove extra spaces
    
    # Step 3: Use nested if statements
    if age >= 18:
        if membership == "yes":
            print("Access granted.")
        else:
            print("Membership required for access.")
    else:
        print("Access denied. Must be at least 18 years old.")
        
except ValueError:
    print("Invalid age input. Please enter an integer.")
