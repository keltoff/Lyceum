import xml.etree.ElementTree as et
from location import Location


class Map:
    def __init__(self):
        self.locations = dict()

    def load(self, filename):
        xml = et.parse(filename)
        for l in xml.findall('location'):
            loc = self.locations.get(l.attrib['name'], Location())
            loc.update(l)
            self.locations[loc.name] = loc

    def __getitem__(self, item):
        return self.locations.get(item, None)
