fn="te.txt"
Mydict={}
f1=open(fn, "r")       
for l in f1:
        name, dept, cgpa =l.split("\t")
        Mydict[name]=[dept,cgpa]
f1.close
print(Mydict)
name=str(input("Enter the name for CGPA change :"))
dept, cgpa = Mydict[name]

cgpa=str(input("CGPA :"))
Mydict[name]=[dept, cgpa]

f1=open(fn, "w")      
for x,y in Mydict.items():
        std=str(x)+"\t"+str(y[0])+"\t"+str(y[1])
        print(std, end="\n", file=f1)
f1.close

f1=open(fn, "r")       
for l in f1:
        name, dept, cgpa =l.split("\t")
        print(name, dept, float(cgpa), end="\n")
f1.close
