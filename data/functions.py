'''
 Store functions for cleaning data in here.
'''
#create a function for assigning default values of cylinders for each car type.
def cyl(x):
    if x in ['SUV','convertible','coupe','mini-van','offroad','van']:
        return 6
    elif x == 'bus':
        return 10
    elif x == 'hatchback':
        return 4
    elif x in ['pickup','truck']:
        return 8
    elif x == ['sedan','wagon']:
        return 5
    else:
        return 6 #this is for 'other' type