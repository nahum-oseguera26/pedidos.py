# Estilo de Python Pep8

platillos = [ " Pollo chuco " , " carne azada " , " Chuleta aumada " , " pizza " , " sopa de caracol " ]

pedidos = []


def  imprimir_menu ():
	impresión ( " 1 Mostrar Platillos " )
	imprimir ( " 2 Agregar Pedido " )
	imprimir ( " 3 Imprimir Pedidos " )
	imprimir ( " 4 Eliminar Pedidos " )
	imprimir ( " 5 Salir " )
	imprimir ( " 0 Almacenar pedidos " )
	
	valor =  int ( entrada ( " Escriba el número de la acción que desea realizar " ))
	valor de retorno

def  mostrar_platillos ():
	imprimir ( " Listado de Platillos Disponibles " )

	Para platillo en platillos:
		imprimir (platillos)


def  agregar_pedido ():
	plato =  entrada ( " Escriba el nombre del platillo que desea " )
	cantidad =  int ( entrada ( " Escriba la cantidad de platillos que desea " ))
	mesa =  int ( entrada ( " Escriba el numero de la mesa " ))
	pedido =  " {0} , cantidad: {1} , mesa: {2} " .format (plato, cantidad, mesa)

	pedidos.append


def  mostrar_pedidos ():
	Imprimir ( " Listado de Pedidos Pendientes " )
	
	para el pedido de pedidos:
		de impresión (pedido)

def  eliminar_pedidos ():
	pedidos = []
	Imprimir ( " se eliminaron todos los pedidos " )

def  almacenar ():
	f =  abierto ( " pedidos.txt " , " w + " )
	para el pedido de pedidos:
		f.write

continuar =  Verdadero

mientras continúa:
	accion = imprimir_menu ()
	Si accion ==  1 :
		mostrar_platillos ()
	elif accion ==  2 :
		agregar_pedido ()
	elif accion ==  3 :
		mostrar_pedidos ()
	elif accion ==  4 :
		eliminar_pedidos ()
	elif accion ==  5 :
		continuar =  Falso
	otra cosa :
		imprimir ( " Acción Desconocida " )
