import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
import os

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jesuisunebicorne'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return redirect(url_for('cours'))


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/admin.html', methods=('GET', 'POST'))
def admin():
    return render_template('admin.html')

@app.route('/adminCode.html', methods=('GET', 'POST'))
def adminCode():
    return render_template('adminCode.html')

@app.route('/contacts.html', methods=('GET', 'POST'))
def contacts():
    return render_template('contacts.html')

@app.route('/corrections.html', methods=('GET', 'POST'))
def corrections():
    return render_template('corrections.html')

@app.route('/cours.html', methods=('GET', 'POST'))
def cours():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('cours.html', posts=posts)

@app.route('/identifiants.html', methods=('GET', 'POST'))
def identifiants():
    return render_template('identifiants.html')

@app.route('/livres.html', methods=('GET', 'POST'))
def livres():
    return render_template('livres.html')

@app.route('/root.html', methods=('GET', 'POST'))
def root():
    return render_template('root.html')

@app.route('/sondages.html', methods=('GET', 'POST'))
def sondages():
    return render_template('sondages.html')


@app.route('/add.html', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        files = request.files.getlist('file')
        images = []
        for f in files:
            title = request.form['title']
            path = "static/images/" + secure_filename(f.filename)
            f.save(path)
            images.append(path)
        images = ' '.join(images)
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, images) VALUES (?, ?)',
                     (title, images))
        conn.commit()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('cours.html', posts=posts)


    return render_template('add.html')

if __name__ == "__main__":
    app.run(threaded=True, debug=False, host='0.0.0.0')