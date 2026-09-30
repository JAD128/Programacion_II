"""
    PROJECT: Evaluación 1 / Grupo 2

    MODULE: empresa_transporte.py

    DESCRIPTION:
    Construir un programa que permita administrar los vehículos de pasajeros
    que se encuentran adscritos a una Empresa de Transporte

    AUTHOR: BYRON ORLANDO CORONEL ZAMBRANO
"""


class VehiculoPasajeros:
    """Un vehículo de pasajeros se caracteriza porque maneja un número único de
    registro, la marca, la capacidad máxima de pasajeros y el número de
    viajes realizado. Hay que tener en cuenta que el número de viajes realizado
    se inicializa en el constructor de forma automática a cero (0) y que la
    capacidad máxima por defecto es de diez (10) pasajeros
    """

    # Método constructor a ser implementado
    def __init__(self, reg, marca, cap, nro):
        self._reg = reg
        self.marca = marca
        self.num_via = cap
        self.nro = nro
        

        # if 0 < cap < 10:
        #     self.cap = cap
        # else:
        #     print('Error, la capacidad del vehiculo esta fuera de rango')
            
    # Método VH # 1
    def __eq__(self, otro_vp):
        """Método de comparación de un vehículo de pasajeros, teniendo en
        cuenta el número único de registro, la marca y la capacidad máxima de
        pasajeros
        """

        otro_vp = []
        otro_vp = VehiculoPasajeros

        v_iguales = True

        if self._reg == otro_vp:
            pass
        elif self.marca == otro_vp:   
            pass
        elif self.cap == otro_vp:
            pass
        else:
           v_iguales == False
        
        if v_iguales == True:
            return f'los Vehiculos son diferentes'
        else:
            return f'Los Vehiculos tienen caracteristicas iguales'
        
        
        """
        ----------
        otro_vp : VehiculoPasajeros
            El otro vehículo de pasajeros con el cual se van a ser las
            comparaciones

        Returns
        -------
        bool
            True si los vehículos de pasajeros son iguales. False en caso
        contrario
        """
        

    # Método VH # 2
    def __repr__(self, reg, marca, cap, num_via):
        def __str__(self) -> str:
            print('Vehiculo'.center(50,'-'))
            return (f'[{self.reg}:{self.marca}:{self.cap}:{self.num_via}')

        pass


class EmpresaTransporte:
    """La Empresa de Transporte se caracteriza por tener un NIT, un nombre, un
    número máximo de vehículos para su flota y el listado de todos los
    vehículos de pasajeros registrados (flota de vehículos de la empresa).
    """

    # Método constructor a ser implementado
    def __init__(self, NIT, nombre, num_flot):
        self.NIT = NIT
        self.nombre = nombre
        self.num_flot = num_flot
        # self.vehiculos = vehiculo
        # if self.vehiculos == 0<[]<10:
        #     pass
        # else:
        #     print('El cupo de la flota esta lleno')

    # Método ET # 1
    def vincular_VP(self, nuevo_vp, cap, reg):
       if 0 < cap < 10:
        nuevo_vp = VehiculoPasajeros
        nuevo_vp.append(self.vehiculos)
        valoreg=[]
       
       
        """Este método intenta registrar un vehículo de pasajeros a la flota de
        vehículos de la empresa. Hay que tener en cuenta que no se podrá
        registrar el mismo vehículo de pasajeros 2 veces o más y que se debe
        comprobar que con el nuevo vehículo no se sobrepase el límite del
        número máximo de vehículos de la flota. Tambien es necesario validar la
        Autenticidad del número de registro único del vehículo a registrar,
        teniendo en cuenta que este número consta de 2 partes:

                "número registro básico-dígito de verificación"

        donde el "dígito de verificación" es un valor igual al resíduo o módulo
        de la suma de los dígitos del número de registro básico entre diez (10)
        Ejm. Si el número de registro de un vehículo es "836-7" entonces para
        validar su AUTENTICIDAD sumamos 8 + 3 + 6 = 17 y a este resultado le
        sacamos el módulo entre 10, obteniendo como valor el 7. Por lo tanto el
        número de registro de identificación "836-7" es AUTÉNTICO.
        """

        for num in reg(0,1,2):
            num == reg
            num.append()
        
        residuo = sum(valoreg) // 10
        if residuo == reg(4):
            print(f'el registro es autentico')
        comprobacion = ()
        if nuevo_vp == self.vehiculos:
            pass
        else:
            comprobacion = False

        if comprobacion:
            print (f' el vehiculo ha sido agregado con exito')
        else:
            print('el vehiculo no se pudo agregar')

        
        """
        Parameters
        ----------
        nuevo_vp : VehiculoPasajeros
            El nuevo vehículo de pasajeros para ser adicionado a la flota de
            vehículos de la empresa

        Returns
        -------
        bool
            True si el nuevo vehículo es registrado por la empresa. False en
            caso contrario
        """
        pass

    # Método ET # 2
    def posicionar_VP(self, nuevo_vp, pos):

        self.nuevo = nuevo_vp
        self.pos = pos

        """Este método intenta ingresar un nuevo vehículo de pasajeros, en una
        determinada posición dentro de la flota de vehículos de la empresa. Al
        igual que en el método anterior, hay que tener en cuenta que no se
        podrá registrar el mismo vehículo de pasajeros 2 veces o más, que no se
        sobrepase el límite del número máximo de vehículos de la flota y
        también será necesario validar la Autenticidad del número de registro
        único del vehículo a registrar

        Parameters
        ----------
        nuevo_vp : VehiculoPasajeros
            El nuevo vehículo de pasajeros para ser adicionado a la flota de
            vehículos de la empresa
        pos : int
            Es el número de la posición en la que se requiere registrar el
            vehículo dentro de la flota, comenzando desde 0

            Ejemplo: Si el tamaño máximo de la flota es de 6 y actualmente
            se tiene 4 vehículos:
                [ 0   1   2   3]
                [🛺, 🚗, 🚙, 🛻]
            Se desea registrar 🚚 en la posición 2, entonces la flota queda:
                [ 0   1   2   3   4]
                [🛺, 🚗, 🚚, 🚙, 🛻]
            Ahora, si se desea registrar 🚐 en la posición 5, la flota queda:
                [ 0   1   2   3   4   5]
                [🛺, 🚗, 🚚, 🚙, 🛻, 🚐]
            Cualquier nuevo registro en una determinada posición ya no es
            posible, porque ya se alcanzó el límite máximo de la flota

        Returns
        -------
        bool
            True si el nuevo vehículo se pudo agregar a la flota en la
            posición determinada. False en caso contrario
        """
        pass

    # Método ET # 3
    def despachar_VP(self, vehiculo_tp):
        """Método que realiza el despacho de un vehículo de pasajeros. Un
        vehículo de pasajeros, cada vez que es despachado, implica que su
        número de viajes de debe incrementar en una unidad

        Parameters
        ----------
        vehiculo_tp : VehiculoPasajeros
            El vehículo de pasajeros al cual se le incrementará su número de
            viajes
        """
        vehiculo_tp 


        """
        Returns
        -------
        VehiculoPasajeros|None
            El vehículo de pasajeros al cual se le incrementó el número de
            viajes o None, cuando el vehículo de pasajeros no pertenece a la
            flota
        """
        pass

    # Método ET # 4
    def mini_flota_marca(self, marca):
        
        FlotaVehiculos = []
        for vehiculo in VehiculoPasajeros:
            vehiculo.append(FlotaVehiculos)

        def __str__(self):
            marcaVe = ()
            for vehiculo in VehiculoPasajeros:
             i=0
             f' vehiculo{i}:{self.vehiculo}'
             i += 1
             
            return marcaVe
        
        """Este método crea una lista con todos los vehículos de pasajeros que
        pertenezcan a la flota y que sean de una determinada marca

            Parameters
        ----------
        marca : str
            El nombre de la marca a buscar en la flota

        Returns
        -------
        Lista Python
            Una lista con los vehículos de pasajeros que sean de la marca
            especificada y que pertenezcan actualmente a la flota
        """
    

    # Método ET # 5
    def desvincular_VP(self, vehiculo_tp):
        print(VehiculoPasajeros)
        int(input(f'Diguite el carro que quiere eliminar?'))
        """Método que permite eliminar un vehículo de pasajeros de la flota
        actual de la empresa

        Parameters
        ----------
        vehiculo_tp : VehiculoPasajeros
            Es el vehículo de pasajeros que se desea desvincular de la empresa

        Returns
        -------
        bool
            True si el vehículo es desvinculado de la flota. False en caso
            contrario
        """
        pass

    # Método ET # 6
    def __len__(self, ):

        """Método que retorna el número de vehículos de pasajeros que se
        encuentran actualmente registrados en la flota de la empresa

        Returns
        -------
        int
            El número actual de vehículos que posee la flota de la empresa
        """
        pass

    # Método ET # 7
    def __str__(self):
       
       
        """Método que retorna la cadena de presentación de la empresa de
        transporte

        Returns
        -------
        str
            Una cadena de presentación en dos líneas de la empresa de
            transporte, utilizando el siguiente formato:
            "Empresa:nombre de empresa transporte/NIT:nit de la empresa
             Máx Vehículos:<número máximo de vehículos>"

            Por ejemplo:
            "Empresa:Team ACME/NIT:123
             Máx Vehículos:<5>"
        """
        pass

    # Método ET # 8
    def la_flota(self):
        """Método que retorna una cadena con todos los vehículos de pasajeros
        pertenecientes a la flota de la empresa

        Returns
        -------
        str
            Una cadena con el siguiente formato:
            "{[presentación_vehículo_0] -> [presentación_vehículo_1] -> [presentación_vehículo_2] -> ... -> [presentación_vehículo_n]}"
            En caso de que la flota no tenga ningún vehículo registrado, se retornará:
            "{}"
        """
        pass

vehiculo_1 = VehiculoPasajeros(123-6, "mazda", 8, 5)
vehiculo_2 = VehiculoPasajeros(496-9, "chevrolet", 6, 3)
vehiculo_3 = VehiculoPasajeros(555-5, "BMW", 5, 6)
vehiculo_1 = EmpresaTransporte


