# Oppgave 4

# Funksjoner
def lNH3(T):
    return 0.00868*T**2 - 1.66*T + 87.4
def lNaCl(T):
    return 0.000295*T**2 + 0.00554*T + 35.7

# Halveringsmetoden
def h(a,b,f,g,tol=1E-6):
    m = (a+b)/2
    while lNH3(m)/lNaCl(m) > tol:
        if lNH3(a) < lNaCl(a):
            b = m
        if lNH3(b) > lNaCl(b):
            a = m
    while lNH3(m)/lNaCl(m) < tol:
        if lNH3(a) < lNaCl(a):
            b = m
        if lNH3(b) > lNaCl(b):
            a = m