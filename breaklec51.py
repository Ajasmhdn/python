list1=['hi','hello','Namaste']
list2=['Ajas','bheem','Raju']
for item in list1:
    for name in list2:
        print(item,name)
        if item=='hello' and name=='bheem':
            pass
    print('out of the inner loop')
print('out of the outer loop')