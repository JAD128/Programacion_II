"""
    PROJECT: Evaluación 1 / Grupo 1

    MODULE: gestionar_socios.py

    DESCRIPTION:
    Construir un programa que permita almacenar y manipular la información
    relacionada a socios de un club deportivo

    AUTHOR: PAULA VANESSA LEÓN ERAZO
"""
from datetime import datetime

class SocioClub:
    """Cada socio se caracteriza porque tiene un número de socio, su nombre,
    domicilio y año de ingreso. Tanto el nombre, el domicilio y el año de
    ingreso pueden tener valores por defecto en su inicialización
    """

    # Método constructor a ser implementado
    def __init__(self,numerosocio,nombre,domicilio,añoin):

            self.numerosocio = numerosocio
            self.nombre = nombre
            self.domicilio = domicilio
            self.añoin = añoin

    # Método SC # 1
    def __eq__(self, otro_socio):
        """Método de comparación de un socio, teniendo en cuenta su número de
        socio

        Parameters
        ----------
        otro_socio : SocioClub
            El otro socio con el cual se van a ser las comparaciones

        Returns
        -------
        bool
            True si los socios son iguales. False en caso contrario
        """
        if self.numerosocio == otro_socio:
            return True
        else:
            return False

    # Método SC # 2
    def __repr__(self):
        """Método de presentación del socio del club

        Returns
        -------
        str
            Una cadena con el formato:
                "(numero socio--nombre socio--domicilio--año de ingreso)"
            Ejemplo:
                "(123--Pepito Pérez--Clle 15 # 78-95--1997)"
        """
        return (f'({self.numerosocio}--{self.nombre}--{self.domicilio}--{self.añoin})')


class ClubDeportivo:

    """El club deportivo se caracteriza por tener un nombre, un teléfono y el
    registro de los diferentes socios pertenecientes al club
    """

    # Método constructor a ser implementado
    def __init__(self,nomb,tel):
        self.nombre = nomb
        self.tel = tel
        self.registro = []

    # Método CD # 1
    def registrar_nuevo_socio(self, nuevo_socio):
        """Hay que considerar que no puede haber 2 socios con el mismo número
        de socio

        Parameters
        ----------
        nuevo_socio : SocioClub
            El nuevo socio a ser ingresado al club

        Returns
        -------
        bool
            True si el nuevo socio es admitido. False en caso contrario
        """
        
        for registro in self.registro:
            if registro.numerosocio == nuevo_socio.numerosocio:
                return False  
        self.registro.append(nuevo_socio)
        return True
        try:
            if self.registro != []:
                for regi in self.registro:
                    if not regi.__eq__(nuevo_socio):

                        if regi.numerosocio != nuevo_socio.numerosocio:
                            return True
                        
                return False
            
            elif self.vehiculos == []:
                return True
        except:   
            return



                                    


    # Método CD # 2
    def registrar_nuevo_socio_despues_de(self, nuevo_socio, num_socio):
        """Este método intenta ingresar un nuevo socio al club, en la posición
        que está después de un determinado socio, identificado con un número
        cualquiera. También hay que considerar que no puede haber 2 socios con
        el mismo número de socio

        Parameters
        ----------
        nuevo_socio : SocioClub
            El nuevo socio a ser ingresado al club
        num_socio : str
            Es el número de socio que supuestamente ya hace parte del club

        Ejemplo: Si actualmente existen los siguientes socios:
            <<(👲'789') : (💂'128'), (🧖‍♀️'632'), (👨‍🚒'293')>>
        Se desea registrar (🧑‍🔧'999') después del socio de número '789',
        entonces el club de socios queda:
            <<(👲'789') : (🧑‍🔧'999') : (💂'128'), (🧖‍♀️'632'), (👨‍🚒'293')>>
        Ahora, si se desea registrar (🧑🏾‍💼'444') después del socio de
        número '632', entonces el club de socios queda:
            <<(👲'789') : (🧑‍🔧'999') : (💂'128'), (🧖‍♀️'632'), (🧑🏾‍💼'444'), (👨‍🚒'293')>>
        Ahora, si se desea registrar (👮🏻'555') después del socio de
        número '000' que no existe, entonces el club de socios queda:
            <<(👲'789') : (🧑‍🔧'999') : (💂'128'), (🧖‍♀️'632'), (🧑🏾‍💼'444'), (👨‍🚒'293')>>

        Returns
        -------
        bool
            True si el nuevo socio se pudo agregar al club en una
        posición posterior a un socio existente. False en caso contrario
        """
        for socio in self.registro:
            if not socio.__eq__(nuevo_socio):
                if socio.numerosocio != nuevo_socio.numerosocio:
                    self.registro.insert(num_socio, nuevo_socio)
                    return True
        return False

    # Método CD # 3
    def modificar_domicilio_socio(self, num_socio, nuevo_domicilio):
        """Método que realiza el cambio de domicilio de un socio registrado en
        el club

        Parameters
        ----------
        num_socio : str
            El número de socio al cual se le va a realizar la modificación del
            domicilio
        nuevo_domicilio : str
            El nuevo domicilio del socio

        Returns
        -------
        SocioClub|None
            El socio del club, con la modificación de domicilio realizada OK.
            None en caso de que el socio no exista según el número de socio
            ingresado
        """
        
        for soc1 in self.registro:
            if soc1.numerosocio == num_socio:
                soc1.domicilio = nuevo_domicilio
                return soc1
        return None



        

    # Método CD # 4
    def reporte_antigüedad(self, años_antg):
        """Genera un listado de todos los socios que tengan una antigüedad
        mayor o igual a un número de años determinado.

        Parameters
        ----------
        años_antg : int
            Un valor numérico que representa la cantidad de años de antigüedad

        Returns
        -------
        Lista Python
            Una lista con los socios que cumplen con una angüedad mayor o
            igual a la especificada o en su defecto una lista vacía
        """
        lista_soc = []
        for soc1 in self.registro:
            fechIng = soc1.añoin
            fec = datetime.strptime(str(fechIng), '%Y')
            fechAct = datetime.now()
            añosTraba = int(fechAct.year - fec.year)
            if añosTraba >= años_antg:
                lista_soc.append(soc1)

        return lista_soc

    # Método CD # 5
    def eliminar_socio(self, num_socio):
        """Método que permite dar de baja a un socio dado un número de
        identificación de socio

        Parameters
        ----------
        num_socio : str
            Corresponde al número de identificación del socio a ser eliminado

        Returns
        -------
        bool
            True si el socio es expulsado del club de socios. False en caso
            contrario
        """
        bandera = False
        soc = None
        for soc1 in self.registro:
            if soc1.numerosocio == num_socio and bandera == False:
                soc = soc1
                bandera = True
        if soc != None:
            self.registro.remove(soc)
            return True
        else:
            return False 

    # Método CD # 6
    def __len__(self):
        """Método que calcula y retorna el número de socios actualmente
        registrados en el club

        Returns
        -------
        int
            El número de socios actual del club
        """
        return int(len(self.registro))

    # Método CD # 7
    def __str__(self):
        """Método de presentación del Club Deportivo

        Returns
        -------
        str
            Retorna una cadena de presentación del Club Deportivo, utilizando
            el siguiente formato:
            "Club Deportivo:nombre_club_deportivo
             Teléfono:teléfono_c_d
             Total Socios:numero_socios_c_d
             <<(presentación_socio_0) : (presentación_socio_1) : (presentación_socio_2) : ... : (presentación_socio_n)>>
            "
            En caso de que la lista esté vacía retornar:
            "Club Deportivo:nombre_club_deportivo
             Teléfono:teléfono_c_d
             Total Socios:0
             <<?>>
            "
        """
        nuevacadena = '<<'
        
        if self.registro != []:
            for i in range(len(self.registro)):
                if i != len(self.registro)-1:
                    nuevacadena += f'{self.registro[i]} : '
                else:
                    nuevacadena += f'{self.registro[i]}>>'
        else:
            nuevacadena += f'?>>'
        return f'Club Deportivo:{self.nombre}\nTeléfono:{self.tel}\nTotal Socios:{len(self.registro)}\n{nuevacadena}'

