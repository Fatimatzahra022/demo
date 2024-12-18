import streamlit as st

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit interface
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown menu for selecting an operation
operation = st.selectbox("Select the operation", ("Add", "Subtract", "Multiply", "Divide"))

# Display result after the user selects an operation
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
else:
    result = divide(num1, num2)

# Show the result on the app
st.write(f"Result: {result}")


