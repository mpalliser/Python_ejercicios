class CuentaCorriente:

    def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.nif = nif
        self.saldo = saldo
        
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.nombre, self.apellidos, self.direccion, self.telefono, self.nif, self.saldo)
    
    def ingresarDinero(self, saldoIngresado):
        self.saldo = int(self.saldo) + saldoIngresado
        str(self.saldo)

    def retirarDinero(self, saldoRetirado):
        self.saldo = int(self.saldo) - saldoRetirado
        str(self.saldo)

    def saldoNegativo(self):
        if self.saldo < 0:
            return True
        else:
            return False