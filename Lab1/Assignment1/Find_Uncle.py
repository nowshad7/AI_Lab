tupleList1 = [('parent','Rashid','Hasib'),
              ('parent','Hasib','Rakib'),
              ('parent','Hasib','Jobayer'),
              ('parent','Rakib','Sohel'),
              ('parent','Rakib','Rebeka'),
              ('parent','Jobayer','Selina'),
              ('parent','Jobayer','Imtiyaz')
              ]
tupleList2 = [('Rashid','M'),('Hasib','M'),('Rakib','M'),('Jobayer','M'),('Sohel','M'),('Rebeka','F'),('Selina','F'),('Imtiyaz','M')]


def find_uncle(X):
    found = 0;

    i = 0
    while(i<=6):
        if((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
           for j in range(7):
               if((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][1]) & (tupleList1[j][2] != X)):
                   for k in range(8):
                       if((tupleList2[k][0] == tupleList1[j][2]) & (tupleList2[k][1] == 'M')):
                           return tupleList1[j][2]
                           found = 1
        
        i=i+1   
    if(found == 0):
        return 'No brother'


found = 0
X = str(input('Person:'))
print("Uncle:",end='')
i = 0
while(i<=6):
    if((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
        if(find_uncle(tupleList1[i][1]) != 'No brother'):
            print(find_uncle(tupleList1[i][1]))
            found = 1

    i = i+1    
if(found == 0):
    print('No Uncle')
