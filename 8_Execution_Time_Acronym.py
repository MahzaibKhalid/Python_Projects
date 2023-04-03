from time import time

start = time()

word= "University Management Technology"
text = word.split()
a=''
for i in text:
    a = a+str(i[0]).upper()
    
print(a)

end = time()
exe_Time= end-start

print("Execution Time:",exe_Time)

