student_data= {
    "id1": {"name": "Alice", "class": "V", "subject integration": "Maths,science,english"},
    "id2": {"name": "Bob", "class": "V", "subject integration": "Maths,science,english"},
    "id3": {"name": "Charlie", "class": "V", "subject integration": "Maths,science,english"},
    "id4": {"name": "Alice", "class": "V", "subject integration": "Maths,science,english"}
    }
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = details["name"] + details["class"] + details["subject integration"]
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
   print(k, ":", v)