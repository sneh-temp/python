nums=list()

while True:
    try:
        num=(input("Enter a number: "))
        if num=='done':
            break
        else:
            num=int(num)
            nums.append(num)
    except:
        print("Invalid input")
        break

print(nums)
print("\nMaximum number in",nums,"is",max(nums))
print("Minimum number in",nums,"is",min(nums))