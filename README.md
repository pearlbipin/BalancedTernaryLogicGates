# Ternary Logic Gates: Advancing Computing with -1, 0, 1 Base

This repository contains the software simulation and mathematical implementation of digital logic gates using a **balanced ternary system**. Unlike traditional binary systems that rely on two states (0 and 1), this research explores the efficiency and expanded information density of a three-state paradigm.

## Core Research Logic

The balanced ternary base utilized in this project consists of three distinct states:

 
**+1 (High):** Represents a strong positive signal or high-energy state.

 
**0 (Neutral):** Represents no signal or thermal equilibrium.


**-1 (Low):** Represents a negative signal or low-energy state.



## Logic Gate Implementations

The gates are implemented using mathematical modeling where primary gates function as input minimizers or maximizers:


**Ternary AND (TAND):** Output is the minimum of the inputs ().



**Ternary OR (TOR):** Output is the maximum of the inputs ().



**Ternary NOT (TNOT):** Performs logical negation by inverting the state ().



**Ternary NAND (TNAND):** A universal building block defined as .



## Repository Contents

* `ternary_logic.py`: Core Python library containing the gate definitions and truth table generators.
* `simulations/`: Scripts demonstrating 2-input and 3-input gate behaviors.
* `papers/`: Original research manuscripts detailing the theoretical derivations.

## Universality & Applications

The research successfully demonstrates that the **TNAND gate** is functionally complete within the ternary framework, meaning any logical function can be synthesized using combinations of TNAND gates alone. Practical applications for this logic include:


**Increased Data Density:** Reducing the number of required gates for complex operations.



**Power Efficiency:** Potential for reduced power consumption in hardware through memristor integration.



**AI & Quantum Computing:** Foundations for Ternary Neural Networks (TNNs) and qutrit algorithms.



## Citation

If you use this code or research in your work, please cite the original paper:

> Pulickal, P. B., Diniz, Y. J., & Panigrahi, T. (2024). *Ternary Logic Gates: Advancing Computing with -1, 0, 1 Base.* 
