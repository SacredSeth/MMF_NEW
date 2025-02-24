import pandas
import random

# main
# list to hold ticket details
name_list = ["A", "B", "C", "D", "E"]
ticket_cost_list = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge_list = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': name_list,
    'Ticket Price': ticket_cost_list,
    'Surcharge': surcharge_list
}

# create dataframe
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate totals
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out grand totals
grand_total = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

print(mini_movie_frame.to_string(index=False))

# choose a random winner
winner = random.choice(name_list)

# find index of winner
winner_index = name_list.index(winner)

# retrieve ticket price and surcharge
winner_ticket_price = ticket_cost_list[winner_index]
winner_surcharge = surcharge_list[winner_index]

# find total won
total_won = winner_ticket_price + winner_surcharge

# announce winner
print(f"The lucky winner is {winner}. Their ticket worth ${total_won:.2f} is free!")
