import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='daniel', age=38))
john = table.find_one(name='John Doe')
daniel = table.find_one(name='daniel')
#print(table, john)
ver = []
#print(dict(table["id"]))
for row in table:
    #print(daniel)
    daniel = dict(daniel)
    if daniel['id'] == row["id"]:
        print("foi")
    #@if daniel[1] ==
    ver.append(row)
print(ver)
print(daniel['id'])