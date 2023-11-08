# Mate : Cultura Popular

## Introducción

El título hace referencia a la icónica banda de punk/reggae argentina, Todos tus Muertos: https://www.youtube.com/watch?v=__OZv9zn5oM

## Consigna

### Mate

Vamos a construir el mate. Para eso, declarar una clase Mate que tenga las siguientes características:
 - No tome parámetros en su constructor. Al iniciarse, un mate puede ser cebado 20 veces sin lavarse.
 - Tenga un método `cebar`.
 - Tenga un método `lavado`, que devuelva `True` si el mate está lavado, `False` si no.
 - Tenga un método `cambiar_yerba`, que devuelva el mate a su estado inicial con 20 cebadas nuevas. No importa si está lavado o le quedan cebadas, al cambiar la yerba siempre se vuelve a las 20 cebadas

Para probar pueden correr los tests con el comando `python -m pytest test_mate.py::TestMate`

### Mateador

Ahora vamos a modelar a los tomadores de mate. Construir una clase `Mateador` que tenga las siguientes características:

- El constructor toma 3 parámetros:
  1. Un nombre (`string`).
  2. Si acepta mates lavados (`bool`).
  3. Cantidad de mates a tomar (`int`).
 - Un método `cebar_y_tomar`, que tome a un mate de parámetro, lo cebe, y lo tome. Si el mate está lavado y el mateador no acepta mates lavados, no debe cebarlo ni tomarlo (si el mateador acepta lavados lo toma igual).
 - Un método `mates_tomados` que devuelva el número de mates tomados.
 - Un método gracias que devuelva `True` si tomó todos los mates deseados (el pasado en el constructor),`False` si no.

Para probar pueden correr los tests con el comando `python -m pytest test_mate.py::TestMateador`

### Ronda de Mates

¡Ahora queda armar una ronda de mates! Construir una función, `ronda_de_mates`, que tome una lista de mateadores (lista de objetos mateadores) y un mate. Debe funcionar de la siguiente forma:
- Se va pasando el mate en el orden de la lista, y cada mateador ceba y toma. Las reglas anteriores se
mantienen, si el mate está lavado y el mateador no acepta lavados, no lo toma.
- Cada mateador toma solo los mates deseados, no más ni menos.
- Al reiniciar la ronda, si el mate está lavado, se cambia la yerba.
- La función termina cuando todos los mateadores toman todos los mates y se termina la vuelta.
- La función retorna la cantidad de vueltas que se dieron.

Para este punto, no solo deben hacer la función si no además escribir casos de test. En el archivo `test_mate` completar dentro de la clase `TestRondaDeMates` tests para esta función. 
Como mínimo incluyan estos casos:
- Una ronda donde todos los mateadores van a tomar la misma cantidad de mates
- Una ronda donde los mateadores toman números distintos de mates.
- Una ronda donde haya al menos un mateador que no tome mates lavados, el mate se lave en algún momento y el mateador en cuestión saltee esa ronda.

**TIP:** Como *no* pueden acceder a los estados intermedios de `ronda_de_mates`, vean que sus casos afecten la cuenta final del total de vueltas.