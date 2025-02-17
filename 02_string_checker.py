# Functions
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
# payment_list = ['cash', 'credit']

while 1:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()

# pay_method = string_checker("Payment method: ", payment_list, 2)
# print(f"You are paying with {pay_method}")
