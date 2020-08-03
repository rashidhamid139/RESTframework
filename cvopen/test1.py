'''
Dormitory & Dirty room.
Schoolmaster & The classroom.
Listen & Silent.
'''


string1 = 'Dormitory'
string2 = 'Dirty room'.replace(' ', '')


string1  = list(string1)
string2 = list(string2)
string1.sort()
string2.sort()
print(string1, string2)

print(string1 == string2)

