tupleList1 = [('parent','Rashid','Hasib'),
              ('parent','Hasib','Rakib'),
              ('parent','Rakib','Sohel'),
              ('parent','Rakib','Rebeka')]
tupleList2 = [('Rashid','M'),('Hasib','M'),('Rakib','M'),('Sohel','M'),('Rebeka','F')]
found = 0;
X = str(input('Person:'))
print("Brother:",end='')

i = 0
while(i<=3):
    if((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
       for j in range(4):
           if((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][1]) & (tupleList1[j][2] != X)):
               for k in range(5):
                   if((tupleList2[k][0] == tupleList1[j][2]) & (tupleList2[k][1] == 'M')):
                       print(tupleList1[j][2])
                       found = 1
    
    i=i+1   
if(found == 0):
    print('No brother')
