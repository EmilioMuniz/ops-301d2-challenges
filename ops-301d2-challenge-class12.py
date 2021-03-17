#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class12.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/16/2021    
# Purpose:                  Using Psutil in python.

# Declaration of variables:


# Declaration of functions:

# Main
import psutil
print("User Mode:")
print(psutil.cpu_times("user"))
print("Kernel Mode:")
print(psutil.cpu_times("system"))
print("Idle Mode:")
print(psutil.cpu_times("idle"))
print("Nice Mode:")
print(psutil.cpu_times("nice"))
print("I/O Wait:")
print(psutil.cpu_times("iowait"))
print("IRQ:")
print(psutil.cpu_times("irq"))
print("Soft IRQ")
print(psutil.cpu_times("softirq"))
print("Steal Mode:")
print(psutil.cpu_times("steal"))
print("Guest Mode:")
print(psutil.cpu_times("guest"))
print("All Done.")

# End
# References: https://psutil.readthedocs.io/en/latest/
