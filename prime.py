n = int(input())
if n<=1:
    print("Not a Prime Number")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n%i==0:
            print("Not a Prime Number")
            break
    else:
        print("It is a Prime Number")
    
