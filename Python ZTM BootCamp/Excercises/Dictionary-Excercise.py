# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys:
# 'age', 'username', 'weapons', 'is_active' and 'clan'

user = {
    'age': 26,
    'username': 'Samurai',
    'weapons': ['katana', 'shuriken'],
    'is_active': True,
    'clan': 'Kojima'
}

# 2 iterate and print all the keys in the above user.
print(user.keys())

# 3 Add a new weapon to your user
user['weapons'] = 'long sword'

# 4 Add a new key to include 'is_banned'. Set it to false
print(user.update({'is_banned': False}))

# 5 Ban the user by setting the previous key to True
user['is_banned'] = True
# 6 create a new user2 my copying the previous user and update the age value and username value.

new_user2 = user.copy()
new_user2.update({'age': 75, 'username': 'Sam'})
print(user)
print(new_user2)