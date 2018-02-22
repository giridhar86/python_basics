# Election procedure. planets will give the votes in terms as list. Whoever has highest votes will win. If votes are equal, last element in the list of sorted list in ascending list

planets = ["Mercury", "Venus", "Mercury", "Mars", "Charon", "Jupiter", "Saturn", "Jupiter", "Neptune", "Mars", "Charon"]
dict={}
s = set(planets)
uniq = list(s)
for x in uniq:
    cnt = 0
    cnt = planets.count(x)
    dict[x] = cnt
lst = []  
print (dict)

for x in uniq:
    cnt =0
    for y in uniq:
        if dict[x]>=dict[y]:
            cnt = cnt+1
    if cnt==len(uniq):
        lst.append(x)
print (lst)
lst.sort()
print (lst[-1])

# OUTPUT
# {'Mercury': 2, 'Neptune': 1, 'Charon': 2, 'Jupiter': 2, 'Mars': 2, 'Venus': 1, 'Saturn': 1}
# ['Mercury', 'Charon', 'Jupiter', 'Mars']
# Mercury
