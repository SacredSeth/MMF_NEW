# Functions
def not_blank(question):
    """checks that a user has not left a response blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You cannot leave this blank, Please enter a response\n")


# Main
# initialize ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You Have sold all {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets")
