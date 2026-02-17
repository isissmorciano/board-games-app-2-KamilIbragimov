from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.Repositories import giochi_repositories, partite_repositories

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')





@bp.route('/lista_giochi', methods=('GET',))
def giochi():
    if request.method =='GET':
            giochi = giochi_repositories.get_giochi()
    return render_template('giochi.html', giochi=giochi)