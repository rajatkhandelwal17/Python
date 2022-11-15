# DICTIONARY IS TYPE IN WHICH WE USE CURLY BRACKETS {}
# HERE WE HAVE TO TAKE TWO THINGS, KEYS AND VALUES
# THE KEYS SHOULD BE IMMUTABLE AND UNIQUE AND WE CAN USE STRINGS/ NUMBERS ETC.

data = {
    1: "NAVIN",
    2: "KIRAN",
    3: "HARSH"
}
print(data)
print(data[1], data[2], data[3])

# ANOTHER METHOD OF ACCESSING GETTING VALUES 
print(data.get(1))
print(data.get(4))
print(data.get(4, 'NOT FOUND')) # Value found then print otherwise printn't found

# ANOTHER METHOD OF CREATING DICTIONARY
keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JavaScript']
data = dict(zip(keys,values))
print(data)
print(data['Kiran'], data['Navin'], data['Harsh'])

# ADDING ONE MORE VALUE TO DICTIONARY
data['Monika'] = "CS"
print(data)

# DELETING DATA FROM DICTIONARY
del data['Harsh']
print(data)