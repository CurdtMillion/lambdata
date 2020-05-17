
from pandas import DataFrame

def add_state_names(my_df):
    '''
    Adds a column of state names to accompany a corresponding column of abbrev

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbrevs

    Returns:
        copy of the original dataframe, with another column
    '''
    new_df = my_df.copy()
    names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn'}
    new_df['name'] = new_df['abbrev'].map(names_map)
    return new_df

if __name__ == '__main__':

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    print(df.columns)
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())

    df3 = DataFrame({'a': [1, 2, 3, 4]})
    print(df3.head())

