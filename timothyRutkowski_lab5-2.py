# Timothy Rutkowski 03/21/2024 timothyRutkowski_lab5-2.py

# This program will accept input values of a piece of property,
# calculate the amount of tax due based on the input values,
# and loop until the user decides to end the program.

# Define constants
assessed_value_rate = float(0.6)
tax_rate = float(0.0086)

# Initialize globally
property_value = 0
assessed_value = 0
property_tax = 0

# Main function of program
def main():
    while True:
        input_data()
        calc_assessed_value()
        calc_property_tax()
        print_results()
        
        while True:
            user_select = int(input('\nWould you like to calculate taxes for another property? \n1 = Yes\t 0 = No: '))
            if user_select not in {1, 0}:
                print('\nInvalid Input: Please enter 1 or 0')
            else:
                break
            
        if user_select == 0:
            print('\nThank you for using the Property Tax Calculator')
            break
    

# Function to accept input value
def input_data():
    global property_value
    property_value = float(input('\nPlease input the actual value of the property: '))

# Function for calculating assessed value
def calc_assessed_value():
    global assessed_value, property_value
    assessed_value = float(property_value * assessed_value_rate)

# Function to calculate property tax    
def calc_property_tax():
    global property_tax, assessed_value
    property_tax = float(assessed_value * tax_rate)

# Function to print results   
def print_results():
    formatted_assessed_value = "${:,.2f}".format(assessed_value)
    formatted_property_tax = "${:,.2f}".format(property_tax)
    print('\nAssessed Value:', formatted_assessed_value)
    print('Property Tax:', formatted_property_tax)
        
# Call the main function
main()