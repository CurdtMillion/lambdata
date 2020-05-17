# lambdata
another attempt at lambdata

## INstallation

'''sh
pip install -i https://test.pypi.org/simple/ another-lambdata==1.2
'''

## Usage

'''py
from my_lambdata.my_mod import enlarge

print('HELLO')

df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.head())

x = 11
print(enlarge(x))

'''
 