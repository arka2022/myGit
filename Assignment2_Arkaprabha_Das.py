#Q2.b:

print('Diamond Pattern')
n=5
#diamond patter with full of stars
#top hill(removing last row)
for i in range(n-1):
   #left triangle(decrease space, increase *)
   for j in range(i,n):
      print(' ',end=' ')
   for j in range(i+1):
      print('*',end=' ')
   #right triangle(increasing *)
   for j in range(i):
      print('*',end=' ')
   print()
#bottom hill

for i in range(n):
   #left triangle(increasing space, decreasing *)
   for j in range(i+1):
      print(' ',end=' ')
   for j in range(i,n):
      print('*',end=' ')
   #right side triangle(decreasing *)
   for j in range(i+1,n):
      print('*',end=' ')
   print()

print('TopHill pattern')


#Q2.c:
   # Tophill
n=5
   #leftTriangle(decreasing space, increasing *)
for i in range(n):
      for j in range(i,n):
         print(' ',end=' ')
      for j in range(i):
         if(j==0):
            print('*',end=' ')
         else:
            print(' ',end=' ')
      for j in range(i+1):
         if(j==i):
            print('*',end=' ')
         else:
            print(' ',end=' ')

      print()
print(('* '*2*n)+'* ')



#@Q2.c:

n=5
for i in range(n):
   for j in range(i):
      print(' ',end=' ')
   for j in range(i,n):
      if(j==i or i==0 or j==n-1):
           print('*',end=' ')
      else:
         print(' ',end=' ')

   print()
