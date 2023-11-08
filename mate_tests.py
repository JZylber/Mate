from mate import Mate, Mateador, ronda_de_mates
from inspect import signature

class TestMate:
    @staticmethod
    def test_inicio():
        mate : Mate = Mate()
        assert not mate.lavado(), f"Un mate no empieza lavado"
    @staticmethod
    def test_cebar():
        mate : Mate = Mate()
        mate.cebar()
        assert not mate.lavado(), f"Si cebo a un mate con 20  cebadas, quedan 19 cebadas y el mate no está lavado"
    @staticmethod
    def test_lavado():
        mate : Mate = Mate()
        for i in range(20):
            assert not mate.lavado(), f"Si cebo {i} veces, el mate todavía no se lavó"
            mate.cebar()
        assert mate.lavado(), f"Si cebo 20 veces a un mate está lavado"
    @staticmethod
    def test_cambio_yerba():
        mate : Mate = Mate()
        for _ in range(20):
            mate.cebar()
        mate.cambiar_yerba()
        assert not mate.lavado(), f"Si cebo 20 veces a un mate, pero luego cambio la yerba, no está lavado"
    @staticmethod
    def test_cambio_yerba_relavado():
        mate : Mate = Mate()
        for _ in range(20):
            mate.cebar()
        mate.cambiar_yerba()
        for i in range(20):
            assert not mate.lavado(), f"Si cebo {i} veces a un mate con yerba nueva, el mate todavía no se lavó"
            mate.cebar()
        assert mate.lavado(), f"Si cambio la yerba, se lava a las 20 cebadas"
    @staticmethod
    def test_cambio_yerba_intermedio():
        mate : Mate = Mate()
        for _ in range(10):
            mate.cebar()
        mate.cambiar_yerba()
        for i in range(20):
            assert not mate.lavado(), f"Si cebo {i} veces a un mate con yerba nueva, el mate todavía no se lavó"
            mate.cebar()
        assert mate.lavado(), f"Si cambio la yerba, se lava a las 20 cebadas, no importa cuantas cebadas quedaron antes de lavar la yerba"



class TestMateador:
    @staticmethod
    def test_inicio():
        constructor = signature(Mateador.__init__)
        assert len(constructor.parameters) == 4, f"El constructor de Mateador debe tener 3 parámetros (excluyendo el self), no {len(constructor.parameters)}"
        mateador : Mateador = Mateador("Estudiante",True,20)
        tomados = mateador.mates_tomados()
        assert tomados == 0, f"Al iniciar, un mateador no tomó ningún mate"
        assert not mateador.gracias(), "Un mateador que tiene 20 mates restantes por tomar no devuelve a gracias True"
    @staticmethod
    def test_acepta_lavados_toma_mate_bueno():
        mateador : Mateador = Mateador("Estudiante",True,20)
        mate :  Mate = Mate()
        #Para que se lave a la siguiente cebada
        for _ in range(19):
            mate.cebar()
        mateador.cebar_y_tomar(mate)
        assert mateador.mates_tomados() == 1, f"El mateador tomó un mate, no {mateador.mates_tomados()}"
        assert mate.lavado(), "El mate no está siendo cebado"
        assert not mateador.gracias(), "El mateador quería tomar 20 mates, no dice gracias luego del primero"
    @staticmethod
    def test_acepta_lavados_toma_mate_lavado():
        mateador : Mateador = Mateador("Estudiante",True,20)
        mate :  Mate = Mate()
        #Para que se lave
        for _ in range(20):
            mate.cebar()
        mateador.cebar_y_tomar(mate)
        assert mateador.mates_tomados() == 1, f"El mateador acepta mates lavados, y por lo tanto tomó un mate, no {mateador.mates_tomados()}"
        assert not mateador.gracias(), "El mateador quería tomar 20 mates, no dice gracias luego del primero"
    @staticmethod
    def test_no_acepta_lavados_toma_mate_bueno():
        mateador : Mateador = Mateador("Estudiante",False,20)
        mate :  Mate = Mate()
        #Para que se lave a la siguiente cebada
        for _ in range(19):
            mate.cebar()
        mateador.cebar_y_tomar(mate)
        assert mateador.mates_tomados() == 1, f"El mate no está lavado, entonces tomó un mate, no {mateador.mates_tomados()}"
        assert mate.lavado(), "El mate no está siendo cebado"
        assert not mateador.gracias(), "El mateador quería tomar 20 mates, no dice gracias luego del primero"
    @staticmethod
    def test_no_acepta_lavados_toma_mate_lavado():
        mateador : Mateador = Mateador("Estudiante",False,20)
        mate :  Mate = Mate()
        #Para que se lave
        for _ in range(20):
            mate.cebar()
        mateador.cebar_y_tomar(mate)
        assert mateador.mates_tomados() == 0, f"El mateador NO acepta mates lavados, y por lo tanto no tomó mate, pero el mateador tomó {mateador.mates_tomados()} mates"
        assert not mateador.gracias(), "El mateador quería tomar 20 mates, no dice gracias luego del primero"
    @staticmethod
    def test_toma_los_20_mates_deseados():
        mateador : Mateador = Mateador("Estudiante",False,20)
        mate :  Mate = Mate()
        #Para que se lave
        for mates_cebados in range(20):
            assert mateador.mates_tomados() == mates_cebados, f"Hasta acá el mateador debe haber tomado {mates_cebados} mates, no {mateador.mates_tomados()} mates"
            assert not mateador.gracias(), f"El mateador quería tomar 20 mates, no dice gracias luego del mate número {mates_cebados}"
            mateador.cebar_y_tomar(mate)
        assert mateador.gracias(), "El mateador tomó los 20 mates deseados y por lo tanto debe decir gracias"
    @staticmethod
    def test_toma_los_15_mates_deseados():
        mateador : Mateador = Mateador("Estudiante",False,15)
        mate :  Mate = Mate()
        #Para que se lave
        for mates_cebados in range(15):
            assert mateador.mates_tomados() == mates_cebados, f"Hasta acá el mateador debe haber tomado {mates_cebados} mates, no {mateador.mates_tomados()} mates"
            assert not mateador.gracias(), f"El mateador quería tomar 15 mates, no dice gracias luego del mate número {mates_cebados}"
            mateador.cebar_y_tomar(mate)
        assert mateador.gracias(), "El mateador tomó los 20 mates deseados y por lo tanto debe decir gracias"

class TestRondaDeMates:
    #Completar acá con los tests de ronda de mates
    pass