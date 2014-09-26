class netlist_element():
    def __init__(self,typeof):
        self.typeof = typeof
    def __str__(self):
        return(self.typeof)


class subcircuit(netlist_element):
    def __init__(self, name, nets, instances):
        self.name = name;
        self.nets = nets;
        self.instances = instances;
        netlist_element.__init__(self,'subcircuit')
    def __str__(self):
        insts = {}
        for i in self.instances:
            insts[i.name] = i.reference
        return(self.typeof + " " + self.name + "(" + str(self.nets) + "):" + str(insts))

class instance(netlist_element):
    def __init__(self, name, pins, reference, attributes):
        self.name = name;
        self.pins = pins;
        self.reference = reference;
        self.attributes = attributes;
        netlist_element.__init__(self,'instance')
    def __str__(self):
        return(self.typeof + " " + self.name + "@" + self.reference + str(self.attributes))

class net:
    def __init__(self, name):
        self.name = name
        self.nettype = 'standard'
 
