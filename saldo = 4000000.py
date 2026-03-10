saldo = 4000000

print("\n1 Ver saldo\n2 Retirar dinero\n3 Depositar dinero")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print("Su saldo es:", saldo)

elif opcion == 2:
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro <= saldo:
        saldo = saldo - monto_retiro
        print("Se retiró:", monto_retiro)
        print("Su saldo ahora es:", saldo)
    else:
        print("Error, fondos insuficientes")

elif opcion == 3:
    deposito = int(input("Ingrese el valor del depósito: "))
    saldo = saldo + deposito
    print("Su saldo ahora es:", saldo)

else:
    print("Opción inválida")