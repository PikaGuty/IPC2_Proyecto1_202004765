from MOrto import MOrto
from NOrtogonal import NodoOrtogonal


Matriz = MOrto()
Matriz.insertar(NodoOrtogonal(1,0,0))
Matriz.insertar(NodoOrtogonal(1,1,0))
Matriz.insertar(NodoOrtogonal(4,2,0))
Matriz.insertar(NodoOrtogonal(2,3,0))
Matriz.insertar(NodoOrtogonal(3,4,0))
Matriz.insertar(NodoOrtogonal(6,5,0))
Matriz.insertar(NodoOrtogonal(5,6,0))

Matriz.insertar(NodoOrtogonal(11,0,1))
Matriz.insertar(NodoOrtogonal(11,1,1))
Matriz.insertar(NodoOrtogonal(41,2,1))
Matriz.insertar(NodoOrtogonal(21,3,1))
Matriz.insertar(NodoOrtogonal(31,4,1))
Matriz.insertar(NodoOrtogonal(61,5,1))
Matriz.insertar(NodoOrtogonal(51,6,1))

print(Matriz.obtener(3,1).arriba.derecha.getDato())

Matriz.recorrer()

