'''# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un 
# método que devuelva el área del rectángulo.

class Rectangulo():
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area_rectangulo(self,base,altura):
        return base*altura
    
Rectangulo1=Rectangulo(4,5)
Rectangulo2=Rectangulo(10,8)
print(Rectangulo1.area_rectangulo(4,5))
print(Rectangulo1.area_rectangulo(10,8))

# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
# La clase debe contener como miembros:
# Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# Un atributo para el estado (lleno o vacío).
# Un atributo n, que indica la cantidad máxima de cebadas.
# Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno,
# se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# Un método beber, que vacía el mate y le resta una cebada disponible. 
# Si se intenta beber un mate vacío, se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. 
# En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class Mate():
    def __init__(self,cebadas_restantes,estado,n):
        self.cebadas_restantes=cebadas_restantes
        self.estado=estado # lleno o vacio
        self.n=n # cantidad maxima de cebadas
    def cebar(Self,estado):
        if estado=="lleno":
            return print("¡Cuidado! ¡Te quemaste!") # el mate esta lleno
        else:
            estado="lleno"
            print("Ahora le agregue agua, el mate esta: ", estado)
            return estado # el mate se lleno de agua
    
    def beber(self, cebadas_restantes,estado,n):
        try:
            if estado=="lleno":
                    print("TOMANDO EL MATE!!!! ")
                    estado="vacio"
                    return estado
        except: 
                print("¡El mate está vacío!, debe cargar de agua el mate!")
                self.beber(estado)
        else:print("Puede tomar su mate")

estado_mate_amigas="vacio"
cebada_restante_amigas=3
limite_cebada_amigas=cebada_restante_amigas

mate_amigas=Mate(cebada_restante_amigas,estado_mate_amigas,limite_cebada_amigas) # cebadas restantes, estado, cant max de cebadas           

quieremate="SI"
while quieremate=="SI":
        print("________________________PROX RONDA DE MATE_________________________________________________")
        print ("El mate tiene: ", cebada_restante_amigas, "cebadas DISPONIBLES" )
        estado_mate_amigas=mate_amigas.cebar(estado_mate_amigas)
        if cebada_restante_amigas == 0 : print("________________ADVERTENCIA!!!!: el mate está lavado!!!!!!!")
        else: cebada_restante_amigas -= 1
        estado_mate_amigas=mate_amigas.beber(cebada_restante_amigas,estado_mate_amigas,limite_cebada_amigas)
        quieremate= input("Quiere seguir tomando mate?? Ingrese si/no: ")
        quieremate= quieremate.upper()
# 3) Botella y Sacacorchos
# Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, 
# o None si está destapada.
# Escribir una clase Sacacorchos que tenga un método destapar:
# que le reciba una botella, le saque el corcho y se guarde una referencia al corcho sacado. 
# Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.

# Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que 
# no haya un corcho.
# Se define una excepción
class MiExcepcion(Exception):
    def __init__(self, mi_mensaje):
        self.mi_mensaje=mi_mensaje

class Corcho():
    def __init__(self,bodega="Alguna Bodega"):
         self.bodega=bodega
class Botella ():
    def __init__(self,corcho):
        self.corcho=corcho
class sacacorchos():
    def __init__(self, estado_sacacorcho): 
        self.estado_sacacorcho=estado_sacacorcho
    
    def destapar(self, botella=Botella):
        if botella.corcho=="corcho":
            if self.estado_sacacorcho=="vacio":
                            print("Estamos sacando el corcho a la botella, SALUD")
                            botella.corcho="None"
                            self.estado_sacacorcho="ocupado"
            else:
                print("El sacacorcho estaba cargado/sucio, ahora lo limpiamos")
                self.limpiar()
                print("ya limpiamos, estamos LISTOS para sacar el corcho a la botella.... SALUD!")
                botella.corcho="None"
        else:
            try: 
                raise MiExcepcion("sale por EXCEPCION: La Botella ya estaba abierta!")
            except MiExcepcion as a:
                print (a.mi_mensaje)
            
                                 
    
    def limpiar(self):
        if self.estado_sacacorcho!="vacio":
                self.estado_sacacorcho="vacio"
        else: print("El sacacorcho esta limpio!!!!")
                        
print("________ probando con una PRIMERA botella!!! TAPADA!")
mi_botella1=Botella("corcho")
mi_sacacorcho=sacacorchos("vacio")
mi_sacacorcho.destapar(mi_botella1)
print("________ probando con una segunda botella!!! destapada!")
mi_botella2=Botella("vacio")
mi_sacacorcho.destapar(mi_botella2)
print("________ probando con una tercer botella!!! para controlar LIMPIEZA!")
mi_botella3=Botella("corcho") 
mi_sacacorcho.destapar(mi_botella3)  '''        

# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante,
# cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida. 
# Cree un método describir_restaurante() que muestre estas piezas de información,
# y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. 
# Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo
# llamado sabores que almacene una lista de los sabores de helado disponibles.
# Escriba también un método que muestre estos valores, cree una instancia de la clase y llame al método.      
print("__________________________")
class Restautante():
    def __init__(self, nombre_resto,tipo_comida):
        self.nombre_resto= nombre_resto
        self.tipo_comida=tipo_comida
    def describir_resto(self):
        print("El Restaurant se llama: ",self.nombre_resto,". Brinda comida tipo: ",self.tipo_comida)
    def abrir_resto(self):
        print("El Restaurant: ", self.nombre_resto, "esta ABIERTO" )
        '''
class Heladeria (Restautante):
    def __init__(self,nombre_resto, tipo_comida, sabores):
        super().__init__ (nombre_resto,tipo_comida)
        self.sabores= sabores
    def mostrando_sabores(self):
        print ("Los sabores de helados disponibles son: ", self.sabores)


mis_sabores=["Vainilla", "Frutilla", "Banana"]

mi_heladeria=Heladeria("Patagonia","Heladeria",mis_sabores )

mi_heladeria.describir_resto()
mi_heladeria.abrir_resto()
mi_heladeria.mostrando_sabores()
#print("El local:", mi_heladeria.nombre_resto, "tiene los siguientes sabores disponibles: ",mi_heladeria.mostrando_sabores())

# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad,
# y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero,
# y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
# Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro personaje,
# al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que devuelva la cantidad cosechada

class Personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad
    def recibir_ataque(self,menos_vida):
        self.vida=self.vida-menos_vida
        if self.vida<=0:
            try:
                MiExcepcion("Te quedaste SIN VIDA EN EL JUEGO!")
            except MiExcepcion as a:
                print(MiExcepcion.mi_mensaje)
    def mover(self,nueva_dir):
        self.posicion=nueva_dir-self.velocidad

class soldado(Personaje):
    def __init__(self, vida, posicion, velocidad,ataque):
         super().__init__(vida, posicion, velocidad)
         self.ataque=ataque
         
    def ataque(self,enemigo):
        print("aqui se debe hacer DAÑO", self.ataque, "al personaje:", enemigo)

class campesino(Personaje):
    def __init__(self, vida, posicion, velocidad,cosecha):
         super().__init__(vida, posicion, velocidad)
         self.cosecha=cosecha
    def cosechar(self):
        return self.cosecha

# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros
# atributos que típicamente se guardan en un perfil de usuario. Escriba un método describir_usuario() 
# que muestre un resumen de la información del usuario. Escriba otro método saludar_usuario() 
# que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

class Usuario():
    def __init__(self, nombre, apellido, edad, domicilio) -> None:
        self.nombre= nombre
        self.apellido=apellido
        self.domicilio=domicilio
        self.edad=edad
    def describir_usuario(self):
        print("Nombre:", self.nombre, "Apellido:", self.apellido, "Domicilio:", self.domicilio)
       
    def saludar (self):
        if self.edad > 40 : print("Buenas noches!!!", self.nombre, "como vas con el curso de Python?")
        else: print(self.nombre, "Sos un CRACK!!! " )

usuario1=Usuario("Eva", "Klarmann", 49, "Ushuaia")
usuario2=Usuario("Leo", "Astorga", 7, "Ushuaia")
usuario3=Usuario("Maria", "Lopez", 33, "Salta")

usuario1.describir_usuario()
usuario1.saludar()
usuario2.describir_usuario()
usuario2.saludar()
usuario3.describir_usuario()
usuario3.saludar()

# 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que
# herede de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene 
# una lista de strings tales como “puede postear en el foro”, “puede borrar un post”, “puede banear usuario”,
# etc. Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador,
# cree una instancia de la clase y llame al método.
privi=["puede postear en el foro","puede borrar un post","puede banear usuario"]
class Administrador (Usuario):
    def __init__(self, nombre, apellido, edad, domicilio,privilegios=list()) -> None:
        super().__init__(nombre, apellido, edad, domicilio)
        self.privilegios=privilegios
    def mostrar_privilegios(self):
        print("Los privilegios del usuario:", self.nombre, "son los siguientes:", self.privilegios)
mi_adm=Administrador("Sergio", "Astorga", 50, "Mexico", privi)
mi_adm.mostrar_privilegios()
mi_adm2=Administrador("Jose", "Astorga", 50, "Mexico") # aqui estoy probando la lista vacia por defecto
mi_adm2.mostrar_privilegios()

# 8 -Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene
# una lista de strings con los privilegios de manera similar a la del ejercicio 7. 
# Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, y haga que una instancia
# de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use el método
# para mostrar privilegios.

class Privilegios():
    def __init__(self, privilegios = list()):
        self.privilegios=privilegios
    def mostrar_privilegios(self):
        print("Los privilegios del usuario:", self.privilegios)
lista=["No trabaja fines de semana", "Ingresa al trabajo a las 10 AM"]
mis_privilegios=Privilegios(lista)

mi_adm3=Administrador("Juanita", "Arce",60,"Salta",mis_privilegios.privilegios)
mi_adm3.mostrar_privilegios()
'''
