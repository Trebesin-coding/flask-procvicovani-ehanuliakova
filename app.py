from flask import Flask, render_template, request, redirect, url_for
# flask = Třída z knihovny Flask, která je použita k vytvoření instance aplikace.
# render_template= Funkce umožňující vykreslování HTML šablon.
# request= Objekt, který uchovává informace o příchozích HTTP požadavcích (GET, POST atd.).
# redirect a url_for= Funkce pro přesměrování uživatele na jinou URL adresu.

app = Flask(__name__)
# Vytvoření instance aplikace, která bude obsluhovat HTTP požadavky.


@app.route("/")
# Dekorátor, který definuje URL routu aplikace.


# name = request.args.get("name")                                                                 # Extrahuje parametr name z dotazu URL, například /?name=John
# input_class = request.args.get("class")
# message = request.args.get("message")

#     return redirect(url_for("result", name=name, form_class=input_class, message=message))         # Přesměrovává uživatele na jinou routu s těmito parametry
    


# name = request.form.get("name")                                                                    # Získává hodnotu z odeslaného HTML formuláře (metodou POST) s polem name.
# input_class = request.form.get("class")
# message = request.form.get("message")

#     return redirect(url_for("result", name=name, form_class=input_class, message=message))        # Přesměrování na imaginární routu "result".
    





if __name__ == "__main__":
    # Kontroluje, zda je skript spuštěn přímo (ne importován jako modul).
    app.run(debug=True) #spouštění flaskové aplikace
