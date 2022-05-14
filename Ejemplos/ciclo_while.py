def ciclo_while1(n):
  
  i=1
  while i<=10:
   print(i,"x",n,"=",i*n)
   i=i+1
2
def ciclo_while2(n):
  
  i=0
  while i<=10:
    i+=1
    print(i,"x",n,"=",i*n)
   
    if i*n==10:
     break
def ciclo_while3(n):
  
  i=0
  while i<=10:
    i+=1
    if (i*n)/2==0:
     continue
    print(i,"x",n,"=",i*n)
    
    
   
    