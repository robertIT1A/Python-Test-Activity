n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')



n = 5

for i in range(1, n + 1):        # Loop through rows 1 to n
    for j in range(1, i + 1):    # Print numbers from 1 to current row number
        print(j, end=' ')
    print()          # Move to the next line after each row