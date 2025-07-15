# Kyle Segrist
# Chapter 12 lab 1
# 7/15/2025

state_dict = {'Alabama': 'Montgomery',
              'Alaska': 'Juneau',
              'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock',
              'California': 'Sacramento',
              'Colorado': 'Denver',}

total_correct = 0
total_incorrect = 0

for k,v in state_dict.items():
    answer = input(f"What is the capital of {k}? ")
    if answer == state_dict.get(k):
        print("Congratulations, you are correct")
        total_correct += 1
    else:
        print("Sorry, you are not correct")
        total_incorrect += 1

print()
print(f'You answered {total_correct} correct and {total_incorrect} incorrect.')
print()
print('Thanks for playing!')
