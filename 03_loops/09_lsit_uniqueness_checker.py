# List Uniqueness Checker

items = ["apple", "banana", "orange", "apple", "mango"]  
# add input by user also

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)