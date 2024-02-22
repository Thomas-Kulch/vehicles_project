'''
 Store functions for cleaning data in here.
'''
#function for assigning default values of cylinders for each car type.
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

#function for year ranges for car's models
def year_range(x):
    if 1920 <= x <= 1940:
        return '1920-1940'
    elif 1940 < x <= 1960:
        return '1941-1960'
    elif 1960 < x <= 1980:
        return '1961-1980'
    elif 1980 < x <= 2000:
        return '1981-2000'
    elif 2000 < x <= 2020:
        return '2001-2020'
    else:
        return 'unknown'


#function for condition based on odometer reading
def condition(x):
    if 0 <= x <= 200:
        return 'new'
    elif 200 < x <= 5000:
        return 'like new'
    elif 5000 < x <= 20000:
        return 'good'
    elif 20000 < x <= 50000:
        return 'used'
    elif 50000 < x <= 100000:
        return 'very used'
    else:
        return 'heavily used'

#alternative method for filling the NaN cylinders. I will grab the median cylinder from the dataframe grouped by model and model_year and use that value. 
#this still leaves a few NaN values, so I will use this along with my original function.

#this creates some values like 5.5 and 7 cylinder engines which do not exist in cars.
def cylinder_estimation(df):
    # Calculate median cylinders grouped by car model and model year
    median_cylinders = df.groupby(['model', 'model_year'])['cylinders'].transform('median')

    # Fill NaN values with the calculated median
    df['cylinders'] = df['cylinders'].fillna(median_cylinders)
    
    return df
