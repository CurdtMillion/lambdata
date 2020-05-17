
from pandas import DataFrame

class DataProcessor():
    def __init__(self, something_else):
        '''
        Params: something_else (pandas.DataFrame) has a column cal
        '''
        self.df = something_else

    def add_state_names(self):
    '''
    Adds a column of state names to accompany a corresponding column of abbrev
    '''
    names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn'}
    self.df['name'] = self.df['abbrev'].map(names_map)

if __name__ == '__main__':

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names()
    print(processor.df.head())
