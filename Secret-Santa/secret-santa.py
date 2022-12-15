# Create a list of the names of the users. This list will be used to randomly select the recipients for each user's gift.
users = ["Elena", "Irene", "Marta", "Sarai", "Nana", "Mery", "Raquel"]

# Use the random module in Python to shuffle the list of users. This will ensure that the order of the users is randomly generated,
# and no user will receive their own name.
import random
random.shuffle(users)

# Create a dictionary that maps each user to their recipient. This will make it easy to look up the recipient for each user.
recipients = {
    'Elena': users[0],
    'Irene': users[1],
    'Marta': users[2],
    'Sarai': users[3],
    'Nana': users[4],
    'Mery': users[5],
    'Raquel': users[6],
}

# Use a for loop to iterate over the list of users, and print out the recipient for each user.
for user in users:
    print(f"{user}'s recipient is {recipients[user]}")

# This program will generate a random order for the users, and then create a dictionary that maps each user to their recipient.
# It will then print out the recipient for each user.