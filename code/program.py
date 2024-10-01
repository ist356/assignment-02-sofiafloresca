'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

import json
import packaging
parsed = []
with open("data/packaging.txt")as packages:
    for line in packages.readlines():
        parsed.append(packaging.parse_packaging(line.strip()))
        package = packaging.parse_packaging(line.strip())
        unit = packaging.get_unit(package)
        total_units = packaging.calc_total_units(package)
        print(f"{line} => total units: {total_units} {unit}")
        with open ("data/packaging.json", "w") as f:
            json.dump(parsed, f, indent = 4)