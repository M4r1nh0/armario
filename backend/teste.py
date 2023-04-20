import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
john = table.find_one(name='John Doe')
#print(table, john)
ver = []
for row in table:
    list(row)
    ver.append(row)
print(ver)