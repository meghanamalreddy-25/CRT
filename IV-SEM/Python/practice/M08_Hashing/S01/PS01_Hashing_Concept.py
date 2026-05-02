'''a=10
b='meghana'
c=3.454

print(hash(a))
print(hash(b))
print(hash(c))'''

'''size=7
table=[None]*size
a=[50,700,80,50,40,100]
for key in a:
    hash_key=key%size
    table[hash_key]=key
print(table)'''



'''3.
a=[1,2,2,1,2,1]
freq={}
for x in a:
    freq[x] = freq.get(x,0)+1
    max_ele=max(freq, key=freq.get)
print(max_ele)
'''
'''4.
a=[1,2,2,1,2,1]
freq={}
for x in a:
    freq[x] =freq.get(x,0)+1
for x in a:
    if freq[x] == 1:
        print(x)
        break'''
 '''5.       
a='meghana'
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)'''

from collections import Counter
a=[1,2,2,1,2,1]
b=[1,4,3,2,1,1]
print(Counter(a)==Counter(b))

    
    
