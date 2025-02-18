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
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


def instructions():
    """Print the instructions with a header"""

    make_statement("Instructions", "ℹ️")

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


# Main

# initialize variables / non-default options for string checker
payment_list = ['cash', 'credit']
MAX_TICKETS = 5
tickets_sold = 0

make_statement("Mini-Movie Fundraiser", "*", 3)

print()
want_instructions = string_check("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

# loop for testing
while tickets_sold < MAX_TICKETS:
    print()

    # check name isn't blank
    name = not_blank("Name: ")

    # check for exit code
    if name == "xxx":
        break

    # check age is between 12 and 120
    age = num_check("Age: ")

    # check for exit code
    if age == "exit":
        break

    # error / success messages
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask for payment method
    pay_method = string_check("Payment method: ", payment_list, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

# end of selling loop

print()

# check for amount of sold tickets
if tickets_sold == MAX_TICKETS:
    print(f"You have sold all {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets")
