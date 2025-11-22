from formula import parse_formula

def make_periodic_table():
    periodic_table_dict = {
        'H':["Hydrogen", 1.00794],
        'He': ["Helium", 4.002602],
        'Li': ["Lithium", 6.941],
        'Be': ["Beryllium", 9.012182],
        'B': ["Boron", 10.811],
        'C': ["Carbon", 12.0107],
        'N': ["Nitrogen", 14.0067],
        'O': ["Oxygen", 15.9994],
        'F': ["Fluorine", 18.9984032],
        'Ne': ["Neon", 20.1797],
        'Na': ["Sodium", 22.98976928],
        'Mg': ["Magnesium", 24.305],
        'Al': ["Aluminum", 26.9815386],
        'Si': ["Silicon", 28.0855],
        'P': ["Phosphorus", 30.973762],
        'S': ["Sulfur", 32.065],
        'Cl': ["Chlorine", 35.453],
        'Ar': ["Argon", 39.948],
        'K': ["Potassium", 39.0983],
        'Ca': ["Calcium", 40.078],
        'Sc': ["Scandium", 44.955912],
        'Ti': ["Titanium", 47.867],
        'V': ["Vanadium", 50.9415],
        'Cr': ["Chromium", 51.9961],
        'Mn': ["Manganese", 54.938045],
        'Fe': ["Iron", 55.845],
        'Co': ["Cobalt", 58.933195],
        'Ni': ["Nickel", 58.6934],
        'Cu': ["Copper", 63.546],
        'Zn': ["Zinc", 65.38],
        'Ga': ["Gallium", 69.723],
        'Ge': ["Germanium", 72.64],
        'As': ["Arsenic", 74.9216],
        'Se': ["Selenium", 78.96],
        'Br': ["Bromine", 79.904],
        'Kr': ["Krypton", 83.798],
        'Rb': ["Rubidium", 85.4678],
        'Sr': ["Strontium", 87.62],
        'Y': ["Yttrium", 88.90585],
        'Zr': ["Zirconium", 91.224],
        'Nb': ["Niobium", 92.90638],
        'Mo': ["Molybdenum", 95.96],
        'Tc': ["Technetium", 98],
        'Ru': ["Ruthenium", 101.07],
        'Rh': ["Rhodium", 102.9055],
        'Pd': ["Palladium", 106.42],
        'Ag': ["Silver", 107.8682],
        'Cd': ["Cadmium", 112.411],
        'In': ["Indium", 114.818],
        'Sn': ["Tin", 118.71],
        'Sb': ["Antimony", 121.76],
        'Te': ["Tellurium", 127.6],
        'I': ["Iodine", 126.90447],
        'Xe': ["Xenon", 131.293],
        'Cs': ["Cesium", 132.9054519],
        'Ba': ["Barium", 137.327],
        'La': ["Lanthanum", 138.90547],
        'Ce': ["Cerium", 140.116],
        'Pr': ["Praseodymium", 140.90765],
        'Nd': ["Neodymium", 144.242],
        'Pm': ["Promethium", 145],
        'Sm': ["Samarium", 150.36],
        'Eu': ["Europium", 151.964],
        'Gd': ["Gadolinium", 157.25],
        'Tb': ["Terbium", 158.92535],
        'Dy': ["Dysprosium", 162.5],
        'Ho': ["Holmium", 164.93032],
        'Er': ["Erbium", 167.259],
        'Tm': ["Thulium", 168.93421],
        'Yb': ["Ytterbium", 173.054],
        'Lu': ["Lutetium", 174.9668],
        'Hf': ["Hafnium", 178.49],
        'Ta': ["Tantalum", 180.94788],
        'W': ["Tungsten", 183.84],
        'Re': ["Rhenium", 186.207],
        'Os': ["Osmium", 190.23],
        'Ir': ["Iridium", 192.217],
        'Pt': ["Platinum", 195.084],
        'Au': ["Gold", 196.966569],
        'Hg': ["Mercury", 200.59],
        'Tl': ["Thallium", 204.3833],
        'Pb': ["Lead", 207.2],
        'Bi': ["Bismuth", 208.9804],
        'Po': ["Polonium", 209],
        'At': ["Astatine", 210],
        'Rn': ["Radon", 222],
        'Fr': ["Francium", 223],
        'Ra': ["Radium", 226],
        'Ac': ["Actinium", 227],
        'Th': ["Thorium", 232.03806],
        'Pa': ["Protactinium", 231.03588],
        'U': ["Uranium", 238.02891],
        'Np': ["Neptunium", 237],
        'Pu': ["Plutonium", 244],
        'Am': ["Americium", 243.0],
        'Cm': ["Curium", 247.0],
        'Bk': ["Berkelium", 247.0],
        'Cf': ["Californium", 251.0],
        'Es': ["Einsteinium", 252.0],
        'Fm': ["Fermium", 257.0],
        'Md': ["Mendelevium", 258.0],
        'No': ["Nobelium", 259.0],
        'Lr': ["Lawrencium", 266.0],
        'Rf': ["Rutherfordium", 267.0],
        'Db': ["Dubnium", 270.0],
        'Sg': ["Seaborgium", 271.0],
        'Bh': ["Bohrium", 270.0],
        'Hs': ["Hassium", 277.0],
        'Mt': ["Meitnerium", 278.0],
        'Ds': ["Darmstadtium", 281.0],
        'Rg': ["Roentgenium", 282.0],
        'Cn': ["Copernicium", 285.0],
        'Fl': ["Flerovium", 289.0],
        'Lv': ["Livermorium", 293.0],
        'Ts': ["Tennessine", 294.0],
        'Og': ["Oganesson", 294.0],
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0.0
    
    for element_data in symbol_quantity_list:
        symbol = element_data[0]
        quantity = element_data[1]
        atomic_mass = periodic_table_dict[symbol][1]
        total_mass += atomic_mass * quantity
    
    return total_mass

def main():
    periodic_table_dict = make_periodic_table()
    formula = input("Enter the molecular formula of the sample: ").upper()
    sample_mass = float(input("Enter the mass in grams of the sample: "))
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    print(f"{molar_mass:.5f} grams/mole")
    number_of_moles = sample_mass / molar_mass
    print(f"{number_of_moles:.5f} moles")

if __name__ == "__main__":
    main()