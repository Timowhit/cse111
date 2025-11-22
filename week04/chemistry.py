import re

def make_periodic_table():
    periodic_table_dict = {
        'H':["Hydrogen", 1.008],
        'He': ["Helium", 4.0026],
        'Li': ["Lithium", 6.94],
        'Be': ["Beryllium", 9.0122],
        'B': ["Boron", 10.81],
        'C': ["Carbon", 12.011],
        'N': ["Nitrogen", 14.007],
        'O': ["Oxygen", 15.999],
        'F': ["Fluorine", 18.998],
        'Ne': ["Neon", 20.180],
        'Na': ["Sodium", 22.990],
        'Mg': ["Magnesium", 24.305],
        'Al': ["Aluminum", 26.982],
        'Si': ["Silicon", 28.085],
        'P': ["Phosphorus", 30.974],
        'S': ["Sulfur", 32.06],
        'Cl': ["Chlorine", 35.45],
        'Ar': ["Argon", 39.948],
        'K': ["Potassium", 39.098],
        'Ca': ["Calcium", 40.078],
        'Sc': ["Scandium", 44.955908],
        'Ti': ["Titanium", 47.867],
        'V': ["Vanadium", 50.9415],
        'Cr': ["Chromium", 51.9961],
        'Mn': ["Manganese", 54.938044],
        'Fe': ["Iron", 55.845],
        'Co': ["Cobalt", 58.933194],
        'Ni': ["Nickel", 58.6934],
        'Cu': ["Copper", 63.546],
        'Zn': ["Zinc", 65.38],
        'Ga': ["Gallium", 69.723],
        'Ge': ["Germanium", 72.630],
        'As': ["Arsenic", 74.921595],
        'Se': ["Selenium", 78.971],
        'Br': ["Bromine", 79.904],
        'Kr': ["Krypton", 83.798],
        'Rb': ["Rubidium", 85.4678],
        'Sr': ["Strontium", 87.62],
        'Y': ["Yttrium", 88.90584],
        'Zr': ["Zirconium", 91.224],
        'Nb': ["Niobium", 92.90637],
        'Mo': ["Molybdenum", 95.95],
        'Tc': ["Technetium", 98.0],
        'Ru': ["Ruthenium", 101.07],
        'Rh': ["Rhodium", 102.90550],
        'Pd': ["Palladium", 106.42],
        'Ag': ["Silver", 107.8682],
        'Cd': ["Cadmium", 112.414],
        'In': ["Indium", 114.818],
        'Sn': ["Tin", 118.710],
        'Sb': ["Antimony", 121.760],
        'Te': ["Tellurium", 127.60],
        'I': ["Iodine", 126.90447],
        'Xe': ["Xenon", 131.293],
        'Cs': ["Cesium", 132.90545196],
        'Ba': ["Barium", 137.327],
        'La': ["Lanthanum", 138.90547],
        'Ce': ["Cerium", 140.116],
        'Pr': ["Praseodymium", 140.90766],
        'Nd': ["Neodymium", 144.242],
        'Pm': ["Promethium", 145.0],
        'Sm': ["Samarium", 150.36],
        'Eu': ["Europium", 151.964],
        'Gd': ["Gadolinium", 157.25],
        'Tb': ["Terbium", 158.92535],
        'Dy': ["Dysprosium", 162.500],
        'Ho': ["Holmium", 164.93033],
        'Er': ["Erbium", 167.259],
        'Tm': ["Thulium", 168.93422],
        'Yb': ["Ytterbium", 173.04],
        'Lu': ["Lutetium", 174.9668],
        'Hf': ["Hafnium", 178.49],
        'Ta': ["Tantalum", 180.94788],
        'W': ["Tungsten", 183.84],
        'Re': ["Rhenium", 186.207],
        'Os': ["Osmium", 190.23],
        'Ir': ["Iridium", 192.217],
        'Pt': ["Platinum", 195.084],
        'Au': ["Gold", 196.96657],
        'Hg': ["Mercury", 200.59],
        'Tl': ["Thallium", 204.38],
        'Pb': ["Lead", 207.2],
        'Bi': ["Bismuth", 208.98040],
        'Po': ["Polonium", 209.0],
        'At': ["Astatine", 210.0],
        'Rn': ["Radon", 222.0],
        'Fr': ["Francium", 223.0],
        'Ra': ["Radium", 226.0],
        'Ac': ["Actinium", 227.0],
        'Th': ["Thorium", 232.0377],
        'Pa': ["Protactinium", 231.03588],
        'U': ["Uranium", 238.02891],
        'Np': ["Neptunium", 237.0],
        'Pu': ["Plutonium", 244.0],
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

def compute_molar_mass(composition):
    periodic_table = make_periodic_table()
    mass = 0.0
    for element, count in composition.items():
        mass += periodic_table[element][1] * count
    return mass

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol]
        total_mass += atomic_mass * quantity
    return total_mass

def parse_formula(formula):
    # Regex to match elements and their counts
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    composition = {}
    for (element, count) in matches:
        if element not in make_periodic_table():
            raise ValueError(f"Unknown element: {element}")
        count = int(count) if count else 1
        composition[element] = composition.get(element, 0) + count
    return composition

def main():
    formula = input("Enter the chemical formula: ").strip()
    sample_mass = float(input("Enter the mass of compound in grams: "))
    try:
        composition = parse_formula(formula)
        molar_mass = compute_molar_mass(composition)
        print(f"Molar mass of {formula}: {molar_mass:.3f} g/mol")
        moles = sample_mass / molar_mass
        print(f"Number of moles: {moles:.4f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()