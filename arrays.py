"""scores=[45,90,85,70,60]
for i in range(len(scores)):
    print(f"scores[{i}]={scores[i]}")
for score in scores:
    print(score)
for idx,val in enumerate(scores):
    print(f"Index {idx}->{val}")
doubled=[x+2 for x in scores]"""

#to insert an element
arr = [45,90,85,70,60]
arr.append(23)
arr.insert(4, 88)
arr.extend([60, 40])
new_arr = arr + [20, 50]
print(new_arr)