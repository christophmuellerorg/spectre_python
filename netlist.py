class netlist_element():
    def __init__(self,typeof):
        self.typeof = typeof
    def __str__(self):
        return(self.typeof)


class subcircuit(netlist_element):
    def __init__(self, name, nets, instances):
        self.name = name;

        # dictionarry of net names,
        # key is net name, value is net object
        self.nets = {} #= nets;
        for n in nets:
            self.nets[n] = net(n)
        
        self.instances = instances;
        netlist_element.__init__(self,'subcircuit')

    def __str__(self):
        insts = {}
        for i in self.instances:
            insts[i.name] = i.reference
        return(self.typeof + " " + self.name + "(" + str(self.nets) + "):" + str(insts))

class instance(netlist_element):
    def __init__(self, name, pins, reference, parameters):
        self.name = name;
        self.pins = pins;
        self.reference = reference;
        self.parameters = parameters;
        netlist_element.__init__(self,'instance')
    def __str__(self):
        return(self.typeof + " " + self.name + "@" + self.reference + str(self.parameters))

class net:
    def __init__(self, name):
        self.name = name
        self.nettype = 'standard'
        self.nodes = set()

    def connect(self, pin):
        self.nodes.add(pin)

class pin:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.net = False

    def connect(self,net):
        if not self.net:
            self.net = net
        
class mosfet:
    def __init__(self,name):
        self.name = name
        self.drain = pin('d',self)
        self.gate = pin('g',self)
        self.source = pin('s',self)
        self.bulk = pin('s',self)

class nmos(mosfet):
    def __init__(self,name):
        self.type = 'n'
        mosfet.__init__(self, name)

class pmos(mosfet):
    def __init__(self,name):
        self.type = 'p'
        mosfet.__init__(self, name)
