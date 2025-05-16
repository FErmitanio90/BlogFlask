from flask import Flask, render_template, request, redirect, url_for
import datetime 
from pymongo import MongoClient

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://Tikididapta:WcBZK31WFm0lhJKK@cluster0.dpd9oe1.mongodb.net/")
app.db = cliente.Otakueva


entradas = [entrada for entrada in app.db.post.find({})]

print(entradas)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        titulo = request.form.get("tit")
        contenido_entrante = request.form.get("content")
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%y")
        parametros = {'titulo': titulo, 'contenido': contenido_entrante, 'fecha': fecha_formato}
        app.db.post.insert_one(parametros)

        existe = app.db.post.find_one(parametros)
        if not existe:
            app.db.post.insert_one(parametros)

        return redirect(url_for('home'))

    entradas = list(app.db.post.find({}))
    return render_template('index.html', entradas=entradas)


if __name__ == "__main__":
    app.jinja_env.cache = {} # Limpia la caché de Jinja
    app.run(debug=True) # Habilita modo de depuración