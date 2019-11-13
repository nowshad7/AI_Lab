#Finding number of lines in a file fn

def num_of_lines(fn):
        c=0
        for l in open(fn):
                c=c+1     
        return c

"""
Displaying all lines of student file fn each containing name,
department and cgpa separated by tabs
"""

def display_file(fn):
        f1=open(fn, "r")     
        for l in f1:
                name, dept, cgpa =l.split("\t")
                print(name, dept, float(cgpa), end="\n")
        f1.close

"""
Displaying ln lines of student file fn each containing name,
department and cgpa separated by tabs
"""

def display_file_lines(fn,ln):
        f1=open(fn, "r")     
        for i in range(ln):
                l=f1.readline()
                name, dept, cgpa =l.split("\t")
                print(name, dept, float(cgpa), end="\n")
        f1.close

