for i in range(0, augstums):
    for j in range(0, garums):
        
   
for i in range(0, garums):
    for j in range(0, garums):
        print('#', end=" ")
    print()

print()


augstums = 5  
for i in range(0, augstums):
    for j in range(0, augstums * 2):
        if i == j or j == (augstums * 2 - i - 1):
            print('#', end="")
        else:
            print(' ', end="")
    print()

            

