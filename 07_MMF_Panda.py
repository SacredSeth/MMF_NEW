# Imports
import pandas


# Functions


# Main

# auto lists for testing
names_list = ["A", "B", "C", "D", "E"]
ticket_costs_list = [7.5, 7.5, 10.5, 10.5, 6.5]
surcharge_list = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': names_list,
    'Ticket Price': ticket_costs_list,
    'Surcharge': surcharge_list
}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']

# calculate profit
mini_movie_frame['Profit'] = mini_movie_frame['Total'] - 5

# calculate grand total and profit total
grand_total = mini_movie_frame['Total'].sum()
profit_total = mini_movie_frame['Profit'].sum()

print(mini_movie_frame)
print()
print(f"Total Paid: ${grand_total:.2f}")
print(f"Total Profit: ${profit_total:.2f}")
