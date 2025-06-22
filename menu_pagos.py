def menu_pagos():
    clear_screen()
    while True:
        clear_screen()
        print("<----- Gestión de Pagos ----->")
        print("1. Registrar pago")
        print("2. Listar pagos")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_pago()
            input("Presione una tecla para continuar...")
        elif opcion == "2":
            listar_pagos()
            input("Presione una tecla para continuar...")
        elif opcion == "3":
            clear_screen()
            break
        else:
            print("Opción no válida. Intente nuevamente.")
