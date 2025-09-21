# ask positive integer (n)
#Another number (m)
#print all the multiples of (m) that are >= n

n = int(input("Enter a the End Number: "))
m = int(input("Find the Multiples of: "))



for i in range (m, n + 1, m):
    print(i)