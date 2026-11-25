# 1. Create a list of 10 student names (including some repeats)
students = [
    "Alice", "Bob", "Charlie", "David", "Bob",
    "Emma", "Frank", "Alice", "Grace", "Charlie"
]

# 2. Print all 10 names in sorted order
print("All names (sorted):")
print(sorted(students))

# 3. Remove duplicates using a set and print the unique names sorted
unique_students = sorted(set(students))
print("\nUnique names (sorted):")
print(unique_students)
