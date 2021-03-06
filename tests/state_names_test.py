import unittest
from pandas import DataFrame

from my_lambdata.state_names import add_state_names

# OBJECTIVE: test the add_state_names() function

class TestStateNames(unittest.TestCase):
      
    def test_add_state_names(self):
        # expect that it has one more column and same amnt rows after we invoke the function
        # expect that certain column names exist before and some after

        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        self.assertEqual(list(df.columns), ['abbrev'])
        
        result = add_state_names(df)
        self.assertEqual(list(result.columns), ['abbrev', 'name'])
        self.assertEqual(result.iloc[0]['abbrev'], 'CA')
        self.assertEqual(result.iloc[0]['name'], 'Cali')


if __name__ == '__main__':
    unittest.main()
