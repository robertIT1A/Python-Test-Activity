numbers = []
sum = 0
for i in range(1,11):
    number = eval(input("Enter a number: "))
    sum += number
    numbers.append(number)

# pahirap sya

# for Odd and Even
ev = []
od = []
for num  in numbers:  
    if num %  2 == 0:
        ev.append(num)
        ilan_ev = len(ev)
        
    elif num % 2 == 1:
        od.append(num)
        ilan_od = len(od)





print(f"\nYou entered: {numbers}")
print(f"\nEven numbers: {ilan_ev}")
print(f"\nOdd numbers: {ilan_od}")
print(f"\nSum of numbers: {sum}")
print(f"\nMaximum number: {max(numbers)}")
print(f"\nMaximum number: {min(numbers)}")




# numbers.sort() # para maarrange from small to large number
# haba = len(numbers)
# una = haba // 3
# print(f"Maximum number: {numbers[una-1]}")
# print(f"Minimum number: {numbers[una+2]}")







# def number_analyzer():
#     while True:
#         numbers = []

#         # Get 10 numbers from the user
#         for i in range(1, 11):
#             while True:
#                 try:
#                     num = int(input(f"Enter number {i}: "))
#                     numbers.append(num)
#                     break
#                 except ValueError:
#                     print("Invalid input. Please enter an integer.")

#         # Print all numbers entered
#         print("\nYou entered:", numbers)

#         # Initialize counters and sum
#         even_count = 0
#         odd_count = 0
#         total_sum = 0

#         # Analyze numbers
#         for num in numbers:
#             total_sum += num
#             if num % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1

#         # Display results
#         print("Even numbers:", even_count)
#         print("Odd numbers:", odd_count)
#         print("Sum of numbers:", total_sum)
#         print("Maximum number:", max(numbers))
#         print("Minimum number:", min(numbers))

#         # Bonus: Ask user if they want to run again
#         repeat = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
#         if repeat != 'yes':
#             print("Goodbye!")
#             break

# # Run the program
# number_analyzer()

