'''
Serializacion (POO)
    -> Permanente 
        - Archivo - Texto -> 'w' | 'r' | 'a' 
        - Serializacion => Binario
                            - byte => 'wb' | 'rb' | 'ab'
                objetos se almacenan
                - Tienda([],[])
                    class Tienda(self, productos, facturas)

import pickle

def serializarTienda(tienda):

    archSerializacion = open('aplicativoT/tienda.dat' , 'wb')
    pickle.dump(tienda, archSerializacion)
    archSerializacion.close()

def deserializarTienda()
    archSerializacion = open('aplicativoT/tienda.dat', 'rb')
    tienda = pickle.load(arcSerializacion)
    archSerializacion.close()

Excepciones

    a = 2
    a = input('Cadena')
    b = a + 2 
    Error

    try - except | else - finally
        try:
            codigo correcto 2/0
        except (name error):
            codigo por si ocurre el error
        except ...

        else:
            ocurre cuando el codico esta bien(se ejecuta)
        finally:
            se ejecuta independientemente de si existe errores.

Crear propios excepciones
    raise (nombre de la excepcion(...))
    -> crear mi excepcion
        Heredar -> clase except

'''