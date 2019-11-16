# import re
#
# mystr = '''this is khushiiii 27
# she is owner of the multinational company
# she is best rapper 01234-5678
# nd famous over the world
# '''
#
# # findall , search , split , sub , finditer
# # print(r"\n")
#
# # patt = re.compile(r'khushi')
# # patt = re.compile(r'.') #. means any character
# # patt = re.compile(r'.is') # any char nd is in string
# # patt = re.compile(r'^this') #string starts with this
# # patt = re.compile(r'world$') #string ends with world
# # patt = re.compile(r'hi*')  #0 or 1 or more i
# # patt = re.compile(r'hi{3}') #exact 3 i
# # patt = re.compile(r'hi+')
# # patt = re.compile(r'khushi| rapper')
#
# # special sequences
# # patt = re.compile(r'\Athis') #Begining of string this
# # patt = re.compile(r'27')
# # patt = re.compile(r'\bkhushi')
# # patt = re.compile(r'world\b')
# patt = re.compile(r'\d{5}-\d{4}')
#
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# =============================================================================

import re
my_phone_numbers = '''
+91-8888669733
+91-8796201556
+91-8605647578
+91-9595775710
+96-92700801955
+88-96894967666
+98-97301103411
'''
numbers=re.compile(r'91-\d{10}')
matches=numbers.finditer(my_phone_numbers)
for match in matches:
    print(match)