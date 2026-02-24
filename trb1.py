salario_mininmo = 1750905
auxilio_transporte = 249095
salud =0.08 *salario_mininmo
pension =0.12 *salario_mininmo
parafiscales =0.09 *salario_mininmo
cesantias =0.083 *salario_mininmo
prima =0.083 *salario_mininmo
vacaciones =0.047 *salario_mininmo
total_auxilio = auxilio_transporte + salud + pension + parafiscales + cesantias + prima + vacaciones + salario_mininmo

print(total_auxilio)
