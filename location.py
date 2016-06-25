
class Exit:
    def __init__(self, xml_source):
        self.dir = xml_source.attrib['dir']
        self.to = xml_source.attrib['to']
        self.text = xml_source.attrib['text']

    @property
    def label(self):
        return '{}: {}'.format(self.dir, self.text)

class Location:
    def __init__(self, xml_source):
        self.name = xml_source.attrib['name']
        self.text = xml_source.attrib['text']
        self.description = xml_source.find('description').text
        self.exits = {e.attrib['dir']: Exit(e) for e in xml_source.findall('exit')}
