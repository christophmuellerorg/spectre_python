import parse_netlist

# read a netlist file
file = open('sample_netlist','r')
sample = file.read()

# parse the netlist
parsed_netlist = parse_netlist.parse_spectre(sample)

# print the top level objects
for obj in parsed_netlist:
    print(obj)

print parsed_netlist[0].instances[0].parameters['w']
