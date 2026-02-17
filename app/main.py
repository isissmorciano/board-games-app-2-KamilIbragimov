from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.Repositories import giochi_repositories, partite_repositories

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    pass





@bp.route('/lista_giochi', methods=('GET',))
def giochi():
    if request.method =='GET':
            gioco = giochi_repositories.get_giochi()
    return render_template('giochi_html', gioco=gioco)