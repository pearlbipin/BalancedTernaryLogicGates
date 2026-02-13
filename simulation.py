# --- TERNARY LOGIC GATES IMPLEMENTATION ---
# Based on research by Pearl Bipin Pulickal, Yash Jesus Diniz, and Dr. Trilochan Panigrahi

# 1-Input Logic Gates
def ternary_NOT(a):
    if a == 1:
        return -1
    elif a == -1:
        return 1
    else:
        return 0

def ternary_BUFFER(a):
    return a

# 2-Input Logic Gates
def ternary_AND(a, b):
    # Functions as an input minimizer
    if a == 1 and b == 1:
        return 1
    elif a == -1 or b == -1:
        return -1
    else:
        return 0

def ternary_OR(a, b):
    # Functions as an input maximizer
    if a == -1 and b == -1:
        return -1
    elif a == 1 or b == 1:
        return 1
    else:
        return 0

def ternary_NAND(a, b):
    return ternary_NOT(ternary_AND(a, b))

def ternary_NOR(a, b):
    return ternary_NOT(ternary_OR(a, b))

def ternary_XOR(a, b):
    # High if sum is +/-1; low if inputs are identical; neutral if any input is neutral
    return ternary_OR(ternary_AND(ternary_NOT(a), b), ternary_AND(a, ternary_NOT(b)))

def ternary_XNOR(a, b):
    return ternary_NOT(ternary_XOR(a, b))

# 3-Input Logic Gates
def ternary_AND_3(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 1
    elif -1 in [a, b, c]:
        return -1
    else:
        return 0

def ternary_OR_3(a, b, c):
    if a == -1 and b == -1 and c == -1:
        return -1
    elif 1 in [a, b, c]:
        return 1
    else:
        return 0

def ternary_NAND_3(a, b, c):
    return ternary_NOT(ternary_AND_3(a, b, c))

def ternary_NOR_3(a, b, c):
    return ternary_NOT(ternary_OR_3(a, b, c))

# --- SIMULATION WRAPPERS ---

def wrapper_one(op, fn):
    """Generates truth tables for 1-input gates."""
    print(f"--- {op} Truth Table ---")
    for a in range(-1, 2):
        print(f"{op} {a} = \t {fn(a)}")
    print()

def wrapper_two(op, fn):
    """Generates truth tables for 2-input gates."""
    print(f"--- {op} Truth Table ---")
    for a in range(-1, 2):
        for b in range(-1, 2):
            print(f"{a} {op} {b} = \t {fn(a, b)}")
    print()

def wrapper_three(op, fn):
    """Generates truth tables for 3-input gates."""
    print(f"--- {op} (3-Input) Truth Table ---")
    for a in range(-1, 2):
        for b in range(-1, 2):
            for c in range(-1, 2):
                print(f"{a}, {b}, {c} {op} = \t {fn(a, b, c)}")
    print()

# --- RUNNING SIMULATIONS ---
if __name__ == "__main__":
    # 1-Input Simulations
    wrapper_one("TNOT", ternary_NOT)
    wrapper_one("TBUFFER", ternary_BUFFER)

    # 2-Input Simulations
    wrapper_two("TAND", ternary_AND)
    wrapper_two("TOR", ternary_OR)
    wrapper_two("TNAND", ternary_NAND)
    wrapper_two("TNOR", ternary_NOR)
    wrapper_two("TXOR", ternary_XOR)
    wrapper_two("TXNOR", ternary_XNOR)

    # 3-Input Simulation Example
    wrapper_three("TAND3", ternary_AND_3)
