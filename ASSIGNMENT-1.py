# Dictionary Operations
student_dict = {"name": "Alice", "age": 21, "course": "Cybersecurity"}
print("Original Dictionary:", student_dict)

# Add new key-value
student_dict["grade"] = "A"
# Update value
student_dict["age"] = 22
# Delete key-value
del student_dict["course"]
print("Updated Dictionary:", student_dict)
print("Keys:", student_dict.keys())
print("Values:", student_dict.values())

# Tuple Operations
marks_tuple = (85, 90, 78, 92, 85)
print("\nOriginal Tuple:", marks_tuple)
print("First element:", marks_tuple[0])
print("Slice (1:4):", marks_tuple[1:4])
print("Length:", len(marks_tuple))
print("Max:", max(marks_tuple))
print("Min:", min(marks_tuple))
print("Count of 85:", marks_tuple.count(85))
print("Index of 92:", marks_tuple.index(92))

# List Operations
subjects_list = ["Math", "Physics", "Chemistry"]
print("\nOriginal List:", subjects_list)

# Append
subjects_list.append("Biology")
# Insert
subjects_list.insert(1, "English")
# Remove
subjects_list.remove("Physics")
# Sort
subjects_list.sort()
# Reverse
subjects_list.reverse()
print("Updated List:", subjects_list)
