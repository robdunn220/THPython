# Basic dictionary instantiation
team = {'name': 'Michigan', 'mascot': 'Wolverines', 'rank': 4}

# Returns value with key 'name'
print(team['name'])

# Returns all keys
print(team.keys())

# Returns all values
print(team.values())

# Returns all keys or values (whichever is specified), sorted alphabetically. Only works if all items are same type
print(sorted(team.keys()))
