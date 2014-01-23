from item import MetaItem

def loadCSV(csv_file):
    csv = open(csv_file)
    header = csv.readline().split(',')
    items = []
    for line in csv:
        line = line.split(',')
        data = {}
        data['name'] = line[2]
        data['id'] = line[0]
        data['description'] = line[4]
        data['alternates'] = line[1]
        item = MetaItem()
        item.createFromDict(data)
        items.append(item)
    return items

