from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, template_folder='templates')

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = f"Título de la entrada #{id}"
    return render_template('entrada.html', titulo=titulo, id=id)