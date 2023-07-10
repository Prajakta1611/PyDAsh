#CREATE A LIST FOR ALL NUMBER IN 1-100 THAT ARE DIVIDED BY BOT 3 AND 5.
l=[]
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        l.append(i)
print(l)