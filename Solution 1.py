#Solution 1 
n = int(input("Enter the number of rows : "))

#pattern1
for i in range(1,n+1):
    print(("  "*(n-i)) + ("* "*i))     
print()

#pattern2
asciiVal = 65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(asciiVal), end=" ")
        asciiVal+=1
    print()
