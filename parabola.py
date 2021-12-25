import matplotlib.pyplot as plt
import numpy as np
from parabolaUtil import *
from PIL import Image


class parabola:
    a1=''
    b1=''
    c1=''
    a2=''
    b2=''
    c2=''

    @staticmethod
    def setuj(na1,nb1,nc1,na2,nb2,nc2):
        parabola.a1 = float(na1)
        parabola.b1 = float(nb1)
        parabola.c1 = float(nc1)
        parabola.a2 = float(na2)
        parabola.b2 = float(nb2)
        parabola.c2 = float(nc2)

    @staticmethod
    def parabola1(x):
        return parabola.a1 * pow(x, 2) + parabola.b1 * x + parabola.c1

    @staticmethod
    def parabola2(x):
        return parabola.a2 * pow(x, 2) + parabola.b2 * x + parabola.c2

    @staticmethod
    def nacrtaj(xmin, xmax):
        if parabola.a1 == 0 or parabola.a2 == 0:
            return "Greska a1 i a2 moraju biti različiti od 0"

        v1 = findVertex(parabola.a1, parabola.b1, parabola.parabola1)
        v2 = findVertex(parabola.a2, parabola.b2, parabola.parabola2)

        x = np.arange(xmin, xmax, 0.001)
        y1 = parabola.parabola1(x)
        y2 = parabola.parabola2(x)
        lineblue, = plt.plot(x, y1, 'b', label='parabola 1')
        linered, = plt.plot(x, y2, 'r', label='parabola 2')
        plt.grid(True)
        plt.xlabel('X osa')
        plt.ylabel('Y osa')
        plt.ylim(min(v1[1], v2[1]) - 10, max(v1[1], v2[1]) + 10)
        plt.legend(handles=[lineblue, linered], loc=2)
        plt.savefig('static/img/plot.png')
        plt.clf()

        rez = findIntersection(parabola.a1, parabola.b1, parabola.c1, parabola.a2, parabola.b2, parabola.c2,
                               parabola.parabola1, parabola.parabola2, v1, v2)
        if rez == -1:
            rez = "beskonacno"
        return str(rez)

    @staticmethod
    def iniciajlizujPar():
        image = Image.open("static/img/plot.png")
        for row in range(image.size[1]):
            for column in range(image.size[0]):
                image.putpixel((column, row), (255,255,255))
        image.save('static/img/plot.png')