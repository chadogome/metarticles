import yaml

class MetaItem(object):

    def __init__(self):
        self.id = ""
        self.name = ""
        self.alternates = []
        self.description = ""

    def createFromDict(self, data):
        self.id = data['id']
        self.name = data['name']
        self.alternates = data['alternates']
        self.description = data['description']


item = MetaItem()
print(yaml.dump(item))