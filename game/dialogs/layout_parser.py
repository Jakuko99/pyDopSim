from lxml import etree

class loadLayout:
    def __init__(self, filename):
        self.layout = etree.parse(filename)
        self.root = self.layout.getroot()

class createLayout:
    def __init__(self):
        self.root = etree.Element("layout")
        self.root.set("version", "1.0")

    def createStation(self, name, **kwargs):
        self.station = etree.SubElement(self.root, "station")
        attrib = etree.SubElement(self.station, "attributes")            
        _name = etree.SubElement(attrib, "name")
        _name.text = str(name)
        if kwargs.get("type"):
            type = etree.SubElement(attrib, "type")
            type.text = kwargs["type"]
        if kwargs.get("pos"):
            s2 = etree.SubElement(attrib, "position")
            x = etree.SubElement(s2, "x")
            x.text = str(kwargs.get("pos")[0])
            y = etree.SubElement(s2, "y")
            y.text = str(kwargs.get("pos")[1])
        
    def addPlatform(self, number, **kwargs):
        platform = etree.SubElement(self.station, "platform")
        _number = etree.SubElement(platform, "number")
        _number.text = str(number)
        if kwargs.get("type"):
            type = etree.SubElement(platform, "type")
            type.text = kwargs["type"]
        if kwargs.get("pos"):
            s2 = etree.SubElement(platform, "position")
            x = etree.SubElement(s2, "x")
            x.text = str(kwargs.get("pos")[0])
            y = etree.SubElement(s2, "y")
            y.text = str(kwargs.get("pos")[1])
    
    def addTrack(self, **kwargs):
        track = etree.SubElement(self.station, "track")        
        if kwargs.get("type"):
            type = etree.SubElement(track, "type")
            type.text = kwargs["type"]
        if kwargs.get("pos"):
            s2 = etree.SubElement(track, "position")
            x = etree.SubElement(s2, "x")
            x.text = str(kwargs.get("pos")[0])
            y = etree.SubElement(s2, "y")
            y.text = str(kwargs.get("pos")[1])

    def addSwitch(self, **kwargs):
        switch = etree.SubElement(self.station, "switch")
        if kwargs.get("orientation"):
            orientation = etree.SubElement(switch, "orientation")
            orientation.text = kwargs["orientation"]
        if kwargs.get("pos"):
            s2 = etree.SubElement(switch, "position")
            x = etree.SubElement(s2, "x")
            x.text = str(kwargs.get("pos")[0])
            y = etree.SubElement(s2, "y")
            y.text = str(kwargs.get("pos")[1])

    def saveLayout(self, filename):
        file = etree.ElementTree(self.root)
        file.write(filename, pretty_print=True)

a = createLayout()
a.createStation("Zilina", pos=[0,0], type="passenger")
a.addPlatform(1, pos=[0,0], type="passenger")
a.addPlatform(2, pos=[0,0], type="passenger")
a.addPlatform(3, pos=[0,0], type="passenger")
a.addTrack(pos=[0,0], type="shunt")
a.addTrack(pos=[0,0], type="shunt")
a.addTrack(pos=[0,0], type="incoming")
a.addTrack(pos=[0,0], type="outgoing")
a.addSwitch(pos=[0,0], orientation="0")
a.addSwitch(pos=[0,0], orientation="180")
a.saveLayout("layout.xml")