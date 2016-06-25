
class Exit:
    def __init__(self, xml_source):
        self.dir = xml_source.attrib['dir']
        self.to = xml_source.attrib['to']
        self.text = xml_source.attrib['text']

    @property
    def label(self):
        return '{}: {}'.format(self.dir, self.text)


class Location:
    def __init__(self):
        self.name = ''
        self.text = ''
        self.description = ''
        self.exits = dict()

    def update(self, xml_source):
        self.name = xml_source.attrib['name']
        self.text = xml_source.attrib.get('text', self.text)

        desc = xml_source.find('description')
        if desc and len(self.description) < len(desc.text):
            self.description = desc.text

        for e in xml_source.findall('exit'):
            ex = Exit(e)
            self.exits[ex.dir] = ex
