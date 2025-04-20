from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDAO

print('***CLIENTES***')
opcion = None
while opcion != 5:
    print(f'''MENÚ:
    1. Listado
    2. Agregar
    3. Editar
    4. Eliminar
    5. Salir''')
    opcion = int(input('Selecciona opción (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** LISTADO ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre_var = input('Nombre: ')
        apellido_var = input('Apellido: ')
        membresia_var = input('Membresía: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3:
        id_cliente_var = int(input('Id a editar: '))
        nombre_var = input('Nombre: ')
        apellido_var = input('Apellido: ')
        membresia_var = input('Membresía: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    elif opcion == 4:
        id_cliente_var = int(input('Id a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')
else:
    print('Salimos de la app...')