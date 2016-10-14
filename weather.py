# Create a dictionary with key-value pairs of month:average temps

weather = {'January': 57, 'February': 57, 'March': 63, 'April': 70, 'May': 77, 'June': 81, 'July': 82, 'August': 82, 'September': 79, 'October': 73, 'November': 66, 'December': 59}

# create a global value to hold the average temp
# create an empty dictionary to store info on the warmest month

average = 70
warmest = dict()

# create a function to calculate the country's average temp

def ave_temp(year):
    total = 0
    for temp in year:
        total += year[temp]
    ave = total / len(weather)
    print("The average yearly temperature in Cairo, Egypt is " + str(ave) + " degrees F!")

# create a function that uses a new dictionary that compares the global average variable
# with each monthly average, months with temps higher than average will be added to the
# new dictionary. Print the new dictionary

def above(month):
    global average
    for temp in month:
        if month[temp] > average:
            warmest[temp] = (month[temp])
    print warmest

# call each function and pass the dictionary

ave_temp(weather)
above(weather)
