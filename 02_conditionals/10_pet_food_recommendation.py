# Pet Food Recommendation

species = input("Enter the species of pet: ").lower()
age = int(input("Enter the age of the pet: "))

if species == "dog":
    if age < 2:
        food = "Puppy food"
elif species == "cat":
    if age > 5:
        food = "Senior cat food"
else:
    print("Provide pet food recommendation only for Dogs and Cats only.")
    

print("Food for ", species,  "of age ", age, "is ", food)

