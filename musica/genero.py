from flask import Flask, render_template, Blueprint
from . import db 

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name, genreId FROM genres
        ORDER BY genres ASC	 
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina =  render_template("genero.html", generos=lista_de_resultados)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres 
        WHERE genreid = ?		 
        """
    resultado = base_de_datos.execute(consulta, (id,))
    genero = resultado.fetchone()

    consulta2 = """
        """

    resultado = base_de_datos.execute(consulta, (id,))
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("detalle_genero.html", genero=genero,
                                        canciones=lista_de_resultados)
    return pagina