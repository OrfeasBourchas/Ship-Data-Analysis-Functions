def number_of_Trips(df, column, starting_value, lastday):
    """This function add the Trip column to a DataFrame and returns the new DataFrame plus the trip number. 
    The values of the column represents the trip's ID e.g. 1->first trip 2->second trip.

    Calling sequence :

    df_with_trips, N_trips = number_of_Trips(df, 1, 6,'2021-11-19')
    
    Variable explanation:

    Input Variables:
    df: The DataFrame, (type pandas DataFrame)
    column: The column name based on which the trip starts. e.g. Speed THrough Water, Main Engine Power e.t.c.(type Integer),
    starting_value: The lower value, of the column variable, based on which the trip starts. e.g. Speed Through Water > 6(kn).(type Float or Integer),
    last_day: The last day provided as string with the following format 'yyyy-mm-dd'. (type String format yyyy-mm-dd),

    Function Variables:
    dep_date:  The date when the trip starts
    arr_date: The date when the trip ends

    Function flow:

    First it creates the Trip column in the dataframe and initialize it wiht zeros.
    Zeros will be representing the data where the ships is manuvering or the trip is too small to take into consideration.
    Then the trip number variable(trip) is set to zero. The dep_date and arr_date are initialized.
    If the len of the trip is bigger than one day the trip number variable is increased 
    and the values with index betwwen dep_date and arr_date in the column trip are updated with the trip number.
    Next, while the dep_date is earlier than a set datetime the previous step is repeated.


    Author: Orfeas Bourchas
    """
    import pandas as pd
    import numpy as np





    df.insert(len(df.columns), 'Trip', np.zeros(len(df)))
    
    trip = 0
    dep_date = df.index[0]
    arr_date = df.loc[dep_date:][df.loc[dep_date:].iloc[:,column]<starting_value].first_valid_index()
    if len(df.loc[dep_date:arr_date,:])>1440:
        trip +=1
        df.loc[dep_date:arr_date,'Trip'] = trip
    while (dep_date <= pd.to_datetime(lastday)):
        
        dep_date = df.loc[arr_date:][df.loc[arr_date:].iloc[:, column] > starting_value].first_valid_index()
        arr_date = df.loc[dep_date:][df.loc[dep_date:].iloc[:, column] < starting_value].first_valid_index()
        if len(df.loc[dep_date:arr_date,:])>1440:
            trip +=1
            df.loc[dep_date:arr_date,'Trip'] = trip
        
        
    return(df, trip)
