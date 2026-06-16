pattern=input()
text=input()
d=(int(input()))


for i in range (len(text)-len(pattern)):
  c=0

  for j in range (len(pattern)):
    if pattern[j]!=text[i+j]:
      c+=1

  if(c<=d):
    print(i,end=" ")    
    
