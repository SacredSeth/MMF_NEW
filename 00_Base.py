# Imports
import pandas
import random


# Functions
def num_check(question, datatype=int, low=0, high=None, exit_code="xxx"):
    """ Function to make sure user inputs an integer / float that is within parameters """

    # check if parameters are set
    if low is not None and high is None:
        ror = f" that is at least {low}"
        check = 0
    elif low is not None and high is not None:
        ror = f" that is between {low} and {high}"
        check = 1
    elif low is None and high is not None:
        ror = f" that at most {high}"
        check = 2
    else:
        ror = ""
        check = 3

    # get correct error message for data type
    if datatype == int:
        err = "Please enter an integer"
    else:
        err = "Please enter a number"

    error = err + ror

    while True:

        # tests for exit code
        test_exit = input(question).lower()

        if test_exit == exit_code or test_exit == exit_code[0]:
            return "exit"

        # try statement for checking that it is of the correct datatype
        try:
            response = datatype(test_exit)

            # Different calculations for set values of low and high
            if check == 0:
                if response >= low:
                    return response
                else:
                    print(error)

            elif check == 1:
                if low <= response <= high:
                    return response
                else:
                    print(error)

            elif check == 2:
                if response <= high:
                    return response
                else:
                    print(error)

            else:
                return response

        except ValueError:
            print(err)


def not_blank(question):
    """checks that a user has not left a response blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You cannot leave this blank, Please enter a response\n")


def string_check(question, ans_list=None, num_letters=1):
    """Checks that the user entered the full word OR the first letter"""

    # set the default value of the list to a list
    if ans_list is None:
        ans_list = ['yes', 'no']

    # make the error message look more readable
    error = ""
    for ite in ans_list:
        if ite != ans_list[-1]:
            error += (ite + " / ")
        else:
            error += ite

    # loop for authenticity
    while True:

        response = input(question).lower()

        for item in ans_list:

            # check for the entire word
            if response == item:
                return item

            # check for the first letter of the response
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {error}\n")


def make_statement(statement, decoration="", lines=1):
    """Decorates headings
    (headings : 3 lines, subheadings : 2 lines, mini headings : 1 line)
    with chosen emoji/ASCII character, only use emoji for single line"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    # prints statement with decorations over a certain number of lines
    if lines == 1:
        return middle
    elif lines == 2:
        return middle + "\n" + top_bottom
    else:
        return top_bottom + "\n" + middle + "\n" + top_bottom


def instructions():
    """Print the instructions with a header"""

    print(make_statement("Instructions", "ℹ️"))

    print('''

For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit)

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).

    ''')


def currency(x):
    """Formats numbers as currency ($x.xx)"""
    return f"${x:.2f}"


# Main

# initialize variables / non-default options for string checker
payment_list = ['cash', 'credit']
MAX_TICKETS = 5
tickets_sold = 0

ticket_cost_list = []
surcharge_list = []
name_list = []

# tickets Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge
CREDIT_SURCHARGE = 0.05

# print heading
print(make_statement("Mini-Movie Fundraiser", "*", 3))

# ask user if they want to see the instructions
print()
want_instructions = string_check("Do you want to see instructions? ")

# display if yes
if want_instructions == "yes":
    instructions()

# loop to sell as many tickets as possible
while tickets_sold < MAX_TICKETS:
    print()

    # check name isn't blank
    name = not_blank("Name: ")

    # check for exit code
    if name == "xxx":
        break
    name_list.append(name)

    # check age is between 12 and 120
    age = num_check("Age: ")

    # check for exit code
    if age == "exit":
        break

    # error / Pricing based on age
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age < 16:
        ticket_price = CHILD_PRICE
    elif age < 65:
        ticket_price = ADULT_PRICE
    elif age < 120:
        ticket_price = SENIOR_PRICE
    else:
        print(f"{name} is too old")
        continue

    # append to a list
    ticket_cost_list.append(ticket_price)

    # ask for payment method
    pay_method = string_check("Payment method: ", payment_list, 2)

    # get surcharge amount
    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # append surcharge to list and get total cost
    surcharge_list.append(surcharge)
    ticket_total = ticket_price + surcharge

    tickets_sold += 1

# end of selling loop

# create dict
mini_movie_dict = {
    'Name': name_list,
    'Ticket Price': ticket_cost_list,
    'Surcharge': surcharge_list
}

# Create data frame
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate total / profit
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# get grand totals
grand_total = mini_movie_frame['Total'].sum()
profit_total = mini_movie_frame['Profit'].sum()

print()
grand_total_string = f"Total Paid: ${grand_total:.2f}"
total_profit_string = f"Total Profit: ${profit_total:.2f}"

# choose a random winner
winner = random.choice(name_list)

# find index of winner
winner_index = name_list.index(winner)

# retrieve ticket price and surcharge
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

lucky_winner_string = f"\nThe lucky winner is {winner}. Their ticket worth ${ticket_won:.2f} is free!"
final_total_string = f"The grand total is now ${(grand_total - ticket_won):.2f}"
final_profit_string = f"The total profit is now ${(profit_total - profit_won):.2f}"


# currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var in add_dollars:
    mini_movie_frame[var] = mini_movie_frame[var].apply(currency)

# print the dataframe
print()
mini_movie_string = mini_movie_frame.to_string(index=False)

print()
# check for amount of sold tickets
if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You have sold all {MAX_TICKETS} tickets", "-")
else:
    num_sold_string = make_statement(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets", "-")

# additional string / headings
heading_string = make_statement("mini Movie Fundraiser", "=")
ticket_details_heading = make_statement("Ticket Details", "-")
raffle_heading = make_statement("Raffle Winner", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "-")
adjusted_explanation = f"We have given away a ticket worth ${ticket_won:.2f} which means \nour" \
                       f"sales have decreased by ${ticket_won:.2f} and our profit \n" \
                       f"decreased by ${profit_won:.2f}"

# list of strings to be outputted / written to file
to_write = [heading_string, "\n",
            ticket_details_heading,
            mini_movie_string, "\n",
            grand_total_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_string,
            final_profit_string, "\n",
            num_sold_string]

# Print area
for item in to_write:
    print(item)

# create file to hold data
file_name = "MMF_ticket_details"
write_to = f"{file_name}.txt"

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
