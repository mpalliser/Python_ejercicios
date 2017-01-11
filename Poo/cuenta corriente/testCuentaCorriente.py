# coding=utf-8
import pytest
from cuentaCorriente import CuentaCorriente


if __name__ == '__main__':
    userMariano = CuentaCorriente("Mariano", "Palliser Muñoz", "calle infanta elisabet", "662221000", "43164435J", "500")
    print(userMariano)

    ingresoSaldo = userMariano.ingresarDinero(500)
    retirarSaldo = userMariano.retirarDinero(700)
    print(userMariano)
    print(userMariano.saldoNegativo())