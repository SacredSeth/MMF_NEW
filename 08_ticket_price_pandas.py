# Imports
import pandas


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


def currency(x):
    """Formats numbers as currency ($x.xx)"""
    return f"${x:.2f}"


# Main

# initialize variables / non-default options for string checker
payment_list = ['cash', 'credit']
ticket_cost_list = []
surcharge_list = []
name_list = []

# tickets Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge
CREDIT_SURCHARGE = 0.05

# create dict
mini_movie_dict = {
    'Name': name_list,
    'Ticket Price': ticket_cost_list,
    'Surcharge': surcharge_list
}

# loop for testing
for _ in range(5):
    print()

    # check name isn't blank and append to list
    name = not_blank("Name: ")
    name_list.append(name)

    # check age is between 12 and 120
    age = num_check("Age: ")

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

    # append to list
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

    # print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
    #       f"so the surcharge is ${surcharge:.2f}\n"
    #       f"The total cost comes to ${ticket_total:.2f}\n")

# Create data frame
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate total / profit
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Total'] - 5

# get grand totals
grand_total = mini_movie_frame['Total'].sum()
profit_total = mini_movie_frame['Profit'].sum()

# currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var in add_dollars:
    mini_movie_frame[var] = mini_movie_frame[var].apply(currency)

# print the dataframe
print()
print(mini_movie_frame.to_string(index=False))
print()
print(f"Total Paid: ${grand_total:.2f}")
print(f"Total Profit: ${profit_total:.2f}")
