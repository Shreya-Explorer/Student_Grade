import sys
if len(sys.argv) == 6:
  script_name = sys.argv[0]
  m1=int(sys.argv[1])
  m2=int(sys.argv[2])
  m3=int(sys.argv[3])
  m4=int(sys.argv[4])
  m5=int(sys.argv[5])
else:
  script_name = sys.argv[0]
  m1=90
  m2=86
  m3=95
  m4=88
  m5=70

sum=m1+m2+m3+m4+m5
avg=sum/5
if(avg>=90):
  grade='A'
elif(avg>=80):
  grade='B'
elif(avg>=70):
  grade='C'
elif(avg>=60):
  grade='D'
elif(avg>=50):
  grade='E'
else:
  grade='FAIL'
print("Marks 1=",m1)
print("Marks 2=",m2)
print("Marks 3=",m3)
print("Marks 4=",m4)
print("Marks 5=",m5)
print("Average =",avg)
print("Grade =",grade)
  
