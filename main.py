class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if color=="rojo":
            self.color="rojo"
        elif color=="verde":
            self.color="verde"
        elif color=="amarillo":
            self.color="amarillo"
        elif color=="negro":
            self.color="negro"
        elif color=="blanco":
            self.color="blanco"

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if tipo=="electrico":
            self.tipo="electrico"
        elif tipo=="gasolina":
            self.tipo="gasolina"

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        cantAsientos=0
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                cantAsientos+=1
        return cantAsientos
    
    def verificarIntegridad(self):
        registroGeneral=self.registro
        asientosOriginales=True
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None and self.asientos[i].registro!=registroGeneral:
                asientosOriginales=False
                break
        if registroGeneral==self.motor.registro and asientosOriginales:
            return "Auto original"
        else:
            return "Las piezas no son originales"