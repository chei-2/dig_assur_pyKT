import re
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

! @ # $ % ^ & * ( ) _ +

300.456.5836
400.444.4444
440.677.8888
888--666--5555
123-456-3433  
555@777@8888

lowkey.com

Mr. Santhu
Mr Sunil
Ms david
Mrs rose
Mr. T

cat
bat
rat
'''
sentence = 'start of the sen and end'

# print("\tTAB")
# print(r"\tTAB")

#pattern = re.compile('ABC')
#pattern = re.compile(r'abc')
#pattern = re.compile(r'\.')
# pattern = re.compile(r'lowkey\.com')
#pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
#pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')???
# pattern = re.compile(r'\S')???
#anchors
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^start')#sentence
#pattern = re.compile(r'end$')#sentence
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}[-@]\d{3}[-@]\d{4}')
# pattern = re.compile(r'[34]00[.]\d{3}[.]\d{4}')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-z]')
#pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
pattern = re.compile(r'M[r|s|rs]\.?\s[A-Za-z]*')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')


matches = pattern.finditer(text_to_search)
#matches = pattern.finditer(sentence)



print(matches)

for match in matches:
    print(match)

#print(text_to_search[1:4])