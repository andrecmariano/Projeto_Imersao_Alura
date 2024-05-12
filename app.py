from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from cidades import cidades

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", cidades=cidades)

@app.route("/cadastrar-animal", methods=["GET", "POST"])
def cadastrar_animal():
    if request.method == "POST":
        # Obter a cidade selecionada
        cidade = request.form.get("cidade")

        # Verificar se uma imagem foi enviada
        if "imagem" not in request.files:
            flash("Nenhuma imagem foi enviada.", "error")
            return redirect(url_for("cadastrar_animal"))

        # Obter a imagem enviada
        imagem = request.files["imagem"]

        # Verificar se o nome do arquivo é seguro
        if imagem.filename != "":
            filename = secure_filename(imagem.filename)

            # Salvar a imagem na nuvem
            imagem.save(os.path.join("static", "imagens", filename))

            flash("Imagem salva com sucesso!", "success")
            return redirect(url_for("index"))

    return render_template("cadastrar_animal.html", cidades=cidades)

@app.route("/procurar-animal", methods=["GET", "POST"])
def procurar_animal():
    if request.method == "POST":
        # Obter a cidade selecionada
        cidade = request.form.get("cidade")

        # Obter os dados do formulário
        tipo = request.form.get("tipo")
        porte = request.form.get("porte")
        pelagem = request.form.get("pelagem")
        cor = request.form.get("cor")
        raca = request.form.get("raca")

        # Pesquisar as imagens que correspondem aos dados do formulário

        # Exibir as imagens que correspondem aos dados do formulário

    return render_template("procurar_animal.html", cidades=cidades)

if __name__ == "__main__":
    app.run(debug=True)