from flask import Flask, flash, redirect, session, url_for, render_template, request
from flask_bootstrap import Bootstrap
from forme import *
from normalize import normalize
from parabola import *

app = Flask(__name__)
app.secret_key = 'interesantno'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/zad1', methods=['POST', 'GET'])
def zad1():
    form1 = Zad1Form()
    if request.method == 'POST':
        if form1.validate():
            parabola.setuj(form1.a1.data, form1.b1.data, form1.c1.data, form1.a2.data, form1.b2.data, form1.c2.data)
            rez = parabola.nacrtaj(float(form1.xmin.data), float(form1.xmax.data))
            if rez != "Greska a1 i a2 moraju biti različiti od 0":
                return render_template('zadatak1.html', form=form1, rezultat=rez)
            else:
                flash('Greska a1 i a2 moraju biti različiti od 0')
                return render_template('zadatak1.html', form=form1)
        else:
            flash('Nisu dobro uneti podaci')
            return render_template('zadatak1.html', form=form1)

    else:
        parabola.iniciajlizujPar()
        return render_template('zadatak1.html', form=form1)


@app.route('/zad2', methods=['POST', 'GET'])
def zad2():
    form2 = Zad2Form()
    if request.method == 'POST':
        if form2.validate():
            normalize.setuj(form2.inpMinR.data, form2.inpMaxR.data, form2.outMinR.data, form2.outMaxR.data,
                            form2.inpMinG.data, form2.inpMaxG.data, form2.outMinG.data, form2.outMaxG.data,
                            form2.inpMinB.data, form2.inpMaxB.data, form2.outMinB.data, form2.outMaxB.data)
            normalize.norm_kontr()
            flash('Uspesno odradjena normalizacija')
            return render_template('zadatak2.html', form=form2)
        else:
            flash('Nisu dobro uneti podaci')
            return render_template('zadatak2.html', form=form2)

    else:
        normalize.iniciajlizujNorm()
        return render_template('zadatak2.html', form=form2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9700', debug=True)
