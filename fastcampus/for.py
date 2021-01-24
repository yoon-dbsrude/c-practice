a={'a':'apple', 'b':'banana', 'c':'coconut'}
for re in a.keys():
    print(re)

for re in a.keys():
    print(a[re])

for re in a.values():
    print(re)

print('*'*30)

for (key, val) in a.items() :
    print('key is ' + key)    print('value is ' + val)

for(key, val) in a.items():
    print((key, val))