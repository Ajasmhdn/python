set1={'Ram',"Gokul","suni",'Charan'}
set2={"Charan",'shiva','ramanan',"Gokul"}
set3={'nana',"dheedi"}
set1.symmetric_difference_update(set3)
print(set1)
print(set1^set2^set3)
#print(set1.difference(('Mohan','Ram')))
#print(set1-set2)