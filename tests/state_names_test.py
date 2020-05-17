import unittest
from pandas import DataFrame

from my_lambdata.state_names import add_state_names

# OBJECTIVE: test the add_state_names() function

class TestStateNames(unittest.TestCase):

    def test_add_state_names(self):

        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        result = add_state_names(df)

        # after we invoke the function
        # expect that it has one more column and same amnt rows
        # expect that certain column names exist before and some after
        
        breakpoint()
        # df.columns
        #self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()