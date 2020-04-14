
n = int(input())
student_marks = {}

for i in range(n):
    line = input().split()
    name ,scores = line[0],line[1:]
    scores = map(float,scores)
    scores1 =(list(scores))
    student_marks[name]= scores1
    #print(student_marks)
qwery_name = input()    
lst =[]
for keys in student_marks.keys():
    #print(keys)
    lst.append(keys)
#print (lst)   
#print(student_marks)
lst1 =[]
for i in lst:
    #print(i,'i')
    #print(qwery_name)
    if (qwery_name==i):
        lst1.append(i)
        marks1=student_marks.get(i)
        #print('suc')        
#print(lst1)
#print(marks1)
avg = float(sum(marks1))/len(marks1)
print("%.2f" % avg)
