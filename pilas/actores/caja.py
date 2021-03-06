# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor
import pilas


class Caja(Actor):
    """Representa una caja que posee fisica.

    .. image:: images/actores/caja.png

    """

    def __init__(self, x=0, y=0):
        """ Constructor de la Caja.

        :param x: Posición horizontal de la Caja.
        :type x: int
        :param y: Posición vertical del Caja.
        :type y: int
        """
        imagen = pilas.imagenes.cargar('caja.png')
        Actor.__init__(self, imagen)
        self.rotacion = 0
        self.x = x
        self.y = y
        self.radio_de_colision = 25

        self.aprender(pilas.habilidades.RebotarComoCaja)
