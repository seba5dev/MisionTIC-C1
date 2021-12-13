ht = (int(input("Horas trabajadas: ")))
vh = (int(input("Valor hora: ")))

def horas_normales():
    if(ht > 40):
        return 40*vh
    else:
        return ht*vh

def horas_extra(): 
    if(ht > 40):
        return (ht - 40) * 1.5 * vh
    else:
        return 0

def sueldo_bruto():
    return horas_normales() + horas_extra()

sb = sueldo_bruto()

def dcto_parafiscales():
    return sb * 0.09

def dcto_salud():
    return sb * 0.04

def dcto_pension():
    return sb * 0.04

def suma_descs():
    return dcto_parafiscales() + dcto_salud() + dcto_pension()

def sueldo_neto():
    return sb - suma_descs()

def prima():
    return sb * 0.0833

def cesantias():
    return sb * 0.0833

def intcesantias():
    return sb * 0.01

def vacaciones():
    return sb * 0.0417


print(horas_normales())
print(horas_extra())
print(sueldo_bruto())
print(dcto_parafiscales())
print(dcto_salud())
print(dcto_pension())
print(suma_descs())
print(sueldo_neto())
print(prima())
print(cesantias())
print(intcesantias())
print(vacaciones())