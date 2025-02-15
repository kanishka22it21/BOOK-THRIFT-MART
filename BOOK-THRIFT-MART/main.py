import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysql import MySQL
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL Database Configuration (values loaded from .env)
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

# AWS S3 Configuration (values loaded from .env)
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('S3_REGION')
)
s3_bucket = os.getenv('S3_BUCKET')

# Main Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cursor.close()
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['user'] = user[0]
            flash('Login successful', 'success')
            return redirect(url_for('explore_genres'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/explore-genres')
def explore_genres():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM genres')
    genres = cursor.fetchall()
    cursor.close()
    return render_template('explore_genres.html', genres=genres)

@app.route('/upload-book-cover', methods=['GET', 'POST'])
def upload_book_cover():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_name = file.filename
            s3.upload_fileobj(file, s3_bucket, file_name)
            flash('File uploaded to S3 successfully', 'success')
            return redirect(url_for('index'))
    return render_template('upload_book_cover.html')

# Additional Genre Routes
@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/thriller')
def thriller():
    return render_template('thriller.html')

@app.route('/romcom')
def romcom():
    return render_template('romcom.html')

@app.route('/Fantasy')
def Fantasy():
    return render_template('Fantasy.html')

@app.route('/Popular')
def Popular():
    return render_template('Popular.html')

@app.route('/Poetry')
def Poetry():
    return render_template('Poetry.html')

@app.route('/fiction')
def fiction():
    return render_template('fiction.html')

@app.route('/nonfiction')
def nonfiction():
    return render_template('nonfiction.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/mystery')
def mystery():
    return render_template('mystery.html')

@app.route('/children_literature')
def children_literature():
    return render_template('children_literature.html')

@app.route('/moral')
def moral():
    return render_template('moral.html')

@app.route('/sci_fic')
def sci_fic():
    return render_template('sci_fic.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/novels')
def novels():
    return render_template('novels.html')

@app.route('/new_arrival')
def new_arrival():
    return render_template('new_arrival.html')

if __name__ == '__main__':
    app.run(debug=True)
