numpad = ((1,2,3),
          (4,5,6),
          ("*",0,"#"))
for rows in numpad :
    for num in rows :
        print(num ,end=" ")
    print()

#to print a particular 2 use row[] and coloum[] as below
print(numpad[0][1])