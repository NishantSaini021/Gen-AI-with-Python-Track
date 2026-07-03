# Task 2: Categories (Sets)
# 1. From your products list, create a set of categories called categories_set.
# 2. Demonstrate adding a new category to the set and show that duplicates are ignored.
# 3. Show how to check whether a category exists in the set (print a boolean result).
# Extra (Optional): Show how to get the total number of unique categories using a set.

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Office",
    "Audio"
]

categories_set = set(categories)

print("Categories Set:")
print(categories_set)

categories_set.add("Networking")
categories_set.add("Electronics")

print("After Adding Categories:")
print(categories_set)

print("Is 'Audio' present?", "Audio" in categories_set)

#Extra:
print("Total Unique Categories:", len(categories_set))