# Written by: Hu Bowen (S10255800)
# Date: 2 July 2023
# Class: CSF02

# Functions to calculate printer charges with gst

def calculate_charge(pages: int) -> float:
    charge = 0.0

    if pages <= 100:
        charge = pages * 0.03
    elif pages <= 300:
        charge = 100 * 0.03 + (pages - 200) * 0.02
    else:
        charge = 100 * 0.03 + 200 * 0.02 + (pages - 300) * 0.01

    return charge

def calculate_gst(charge: float) -> float:
    return charge * 1.07

# Runner code
print("{:10} {:>10} {:>20}".format("Pages", "Charge($)", "Include gst($)"))
for pages in range(0, 501, 50):
    charge = calculate_charge(pages)
    inc_gst = calculate_gst(charge)

    print("{:<10} {:10.2f} {:20.2f}".format(pages, charge, inc_gst))
