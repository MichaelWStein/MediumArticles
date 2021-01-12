# Module with diverse functions for dataframe manipulation
# Not necessarily computationally effective

import pandas as pd


# Renaming columns
def df_rename(func_df, old_name, new_name):
    """
    This function receives a dataframe and two lists - one with the old column names, one with the new column names.
    Columns not in the list are not renamed. The dataframe is returned.
    """
    i = 0
    for name in old_name:
        func_df.rename(columns={name: new_name[i]}, inplace=True)
        i += 1

    return func_df


# For the future, see if it would be better to convert to integer with downcast
def df_int(df_func, list_func):
    """
    For the dataframe df_func, all columns provided in list_func are converted to numeric. All fields that cannot
    be converted are set to 0. The dataframe df_func is returned.
    """
    # Convert to float; fields that cannot be converted are set to 'nan'
    for name in list_func:
        df_func[name] = pd.to_numeric(df_func[name], errors='coerce')

    # All nan' are identified and set to zero
    for line in df_func.itertuples():
        for name in list_func:
            if pd.isnull(df_func.at[line.Index, name]):
                df_func.at[line.Index, name] = 0

    return df_func


def column_add(df_func, list_func):
    """
    This function gets a dataframe df_func and a list with column names. It adds the numbers
    for the provided columns per row. Returned is a list with the sums for each column.
    """
    ret_list = []
    for line in df_func.itertuples():
        x = 0
        for name in list_func:
            x = x + df_func.at[line.Index, name]
        ret_list.append(x)
    return ret_list


# Can be done directly in dataframe, but the code can get messy if the lists are long
# In the future may want to provide the option to choose a return if the denominator is zero
def column_frac(df_func, list_func1, list_func2):
    """
    This function gets a dataframe and two lists with column names. It adds the numbers for each of the provided
    lists and then divides the result from the first list by the result of the second list. It returns a list.
    Example: list1 = [a, b] list2 = [c, d] then for each row the element in retlist=(a+b)/(c+d). If the denominator
    is zero, a zero is returned.
    """

    ret_list = []
    for line in df_func.itertuples():
        x = 0
        y = 0
        for name in list_func1:
            x = x + df_func.at[line.Index, name]
        for name in list_func2:
            y = y + df_func.at[line.Index, name]
        if y == 0:
            z = 0
        else:
            z = x / y
        ret_list.append(z)

    return ret_list
