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


# Main

# initialize variables / non-default options for string checker
payment_list = ['cash', 'credit']

# loop for testing
while 1:
    print()

    # check name isn't blank
    name = not_blank("Name: ")

    # check age is between 12 and 120
    age = num_check("Age: ")

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
