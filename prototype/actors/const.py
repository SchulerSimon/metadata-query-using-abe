'''
This file is here to define a common ground for researcher and patient interaction

All the attributes need to be CAPITAL and must not contain underscore, 
otherwise the implementation will not work.

complexity: to distinguish 2^n attributes, one needs 2n bits. 
the consequence is if the attribute count > 6 (n>=4) its worth to create a binary 
representation (maybe this is not all there is to it, it might be, that having shorter 
policies is better than having less attributes. TODO:timeit)
'''

# ethnicity: 3 bit is enought for the moment.
eb0 = 'ETHNICITYBIT0'
eb1 = 'ETHNICITYBIT1'
eb2 = 'ETHNICITYBIT2'
enb0 = 'ETHNICITYNOTBIT0'
enb1 = 'ETHNICITYNOTBIT1'
enb2 = 'ETHNICITYNOTBIT2'

asian = [eb0, enb1, enb2]
european = [enb0, eb1, enb2]
north_american = [enb0, enb1, eb2]
south_american = [eb0, eb1, enb2]
australian = [eb0, enb1, eb2]
persian = [enb0, eb1, eb2]
arabic = [eb0, eb1, eb2]

# age: 2^7 = 128, should be sufficciant for the age of a human person.
# a[,n]b0 is defined as MSBit
# they follow the rule ab0 = age_bit_0 to ab6 = age_bit_6
# and anb0 = age_not_bit0 to anb6 = age_not_bit_6
abx = 'AGEBIT'
anbx = 'AGENOTBIT'

# desease: 3 bit is enought for a prototype
db0 = 'DESEASEBIT0'
db1 = 'DESEASEBIT1'
db2 = 'DESEASEBIT2'
dnb0 = 'DESEASENOTBIT0'
dnb1 = 'DESEASENOTBIT1'
dnb2 = 'DESEASENOTBIT2'

cancer = [dnb0, dnb1, dnb2]
autism = [db0, dnb1, dnb2]
diabetes = [dnb0, db1, dnb2]
alzheimers = [db0, db1, dnb2]
tuberculosis = [dnb0, dnb1, db2]
desease_6 = [db0, dnb1, db2]
desease_7 = [dnb0, db1, db2]
desease_8 = [db0, db1, db2]


# all of it encoded into a dictionary
bit_dict = {
    # ethnicity
    'asian': asian,
    'european': european,
    'north_american': north_american,
    'south_american': south_american,
    'north_american': north_american,
    'australian': australian,
    'persian': persian,
    'arabic': arabic,
    # desease
    'cancer': cancer,
    'autism': autism,
    'alzheimers': alzheimers,
    'tuberculosis': tuberculosis,
    'desease_6': desease_6,
    'desease_7': desease_7,
    'desease_8': desease_8
}
