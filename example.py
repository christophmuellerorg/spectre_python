import parse_netlist

# read a netlist file
file = open('cells.sp','r')
sample = file.read()

# parse the netlist
parsed_netlist = parse_netlist.parse_hspice(sample)

# print the top level objects
for obj in parsed_netlist:
    print(obj)

print parsed_netlist[0].instances[0].parameters['w']
