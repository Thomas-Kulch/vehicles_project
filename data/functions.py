#Store functions for cleaning data in here.

#create a function for assigning default values of cylinders for each car type.
def cyl(x):
    if x == 'SUV':
        return 6
    elif x == 'bus':
        return 10
    elif x == 'convertible':
        return 6
    elif x == 'coupe':
        return 6
    elif x == 'hatchback':
        return 4
    elif x == 'mini-van':
        return 6
    elif x == 'offroad':
        return 6
    elif x == 'pickup':
        return 8
    elif x == 'sedan':
        return 5
    elif x == 'truck':
        return 8
    elif x == 'van':
        return 6
    elif x == 'wagon':
        return 5
    else:
        return 6 #this is for 'other' type