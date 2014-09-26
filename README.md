spectre_python
==============

Simple and most probably incomplete parser to read spectre netlists into
a data structure for further use.

Up to now supported: instances and subcircuits, parameters:

```
subckt BUFFER A Z gnd gnds vdd vdds
M1 (Z net0 vdd vdds) mypmos w=5 l=1
M2 (net0 A vdd vdds) mypmos w=5 l=1
M3 (Z net0 gnd gnds) mynmos w=2 l=1
M4 (net0 A gnd gnds) mynmos w=2 l=1
ends BUFFER

subckt INVERTER A Z gnd gnds vdd vdds
M1 (Z A vdd vdds) mypmos w=5 l=1
M3 (Z A gnd gnds) mynmos w=2 l=1
ends INVERTER

I1 (net0 net1 0 gnds! vdd! vdds!) BUFFER
I2 (net1 net2 0 gnds! vdd! vdds!) INVERTER
```

```python
import parse_netlist

# read a netlist file
file = open('sample_netlist','r')
sample = file.read()

# parse the netlist
parsed_netlist = parse_netlist.parse_spectre(sample)

# print the top level objects
for obj in parsed_netlist:
    print(obj)

# access to parameters in an instance within a subcircuit
print parsed_netlist[0].instances[0].parameters['w']
```

Example output:
```
subcircuit BUFFER(['A', 'Z', 'gnd', 'gnds', 'vdd', 'vdds']):{'M4': 'mynmos', 'M1': 'mypmos', 'M3': 'mynmos', 'M2': 'mypmos'}
subcircuit INVERTER(['A', 'Z', 'gnd', 'gnds', 'vdd', 'vdds']):{'M1': 'mypmos', 'M3': 'mynmos'}
instance I1@BUFFER{}
instance I2@INVERTER{}
5
```
