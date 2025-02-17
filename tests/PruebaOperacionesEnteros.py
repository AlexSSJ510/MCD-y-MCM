import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.OperacionesEnteros import FaltanParametros


class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numero1 = 18
        operacion = OperacionesEnteros([numero1])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_unaCadena_lanzaExcepcion(self):
        # Arrange
        numero1 = "18a"
        numero2 = 13
        operacion = OperacionesEnteros([numero1, numero2])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularMCD()

    def test_MCM_dosNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 21
        numero2 = 36
        resultadoEsperado = 252
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_tresNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 21
        numero2 = 36
        numero3 = 16
        resultadoEsperado = 1008
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_cuatroNumerosPositivos_retornaMCM(self):
        # Arrange
        numero1 = 21
        numero2 = 36
        numero3 = 16
        numero4 = 4
        resultadoEsperado = 1008
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCM()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numero1 = 21
        operacion = OperacionesEnteros([numero1])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCM()

    def test_MCM_unaCadena_lanzaExcepcion(self):
        # Arrange
        numero1 = "18a"
        numero2 = 13
        operacion = OperacionesEnteros([numero1, numero2])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularMCM()


if __name__ == '__main__':
    unittest.main()
