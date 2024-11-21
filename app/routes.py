from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/coincidencias')
def coincidencias():
    return render_template('coincidencias.html')

@main.route('/registro/empresa', methods=['GET', 'POST'])
def registro_empresa():
    if request.method == 'POST':
        nombre = request.form['nombre']
        sector = request.form['sector']
        ubicacion = request.form['ubicacion']
        ofertas = request.form['ofertas']

        # Guardar en el archivo CSV
        with open('C:\\Users\\usuario\\Desktop\\PROYECTO TINDER EMPRESAS\\empresas.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([nombre, sector, ubicacion, ofertas])

        return redirect(url_for('main.home'))

    return render_template('registro_empresa.html')
