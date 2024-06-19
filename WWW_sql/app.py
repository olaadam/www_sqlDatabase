from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garden.db'  # Œcie¿ka do pliku bazy danych SQLite
db = SQLAlchemy(app)

# Model u¿ytkownika
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    flowers = db.relationship('Flower', backref='user', lazy=True)

# Model kwiatka w ogrodzie
class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Tworzenie tabeli u¿ytkowników i kwiatków jeœli nie istniej¹
@app.before_request
def create_tables():
    inspector = inspect(db.engine)
    if not inspector.has_table(User.__tablename__) or not inspector.has_table(Flower.__tablename__):
        db.create_all()

@app.route('/')
def index():
    error_message = session.pop('error_message', None)
    return render_template('index.html', error_message=error_message)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if User.query.filter_by(username=username).first():
        session['error_message'] = "Username already exists!"
    else:
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('home'))
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if not user:
        session['error_message'] = "User does not exist!"
    elif user.password != password:
        session['error_message'] = "Wrong password!"
    else:
        session['username'] = username
        return redirect(url_for('home'))
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('index'))
    username = session['username']
    user = User.query.filter_by(username=username).first()
    user_flowers = user.flowers
    return render_template('home.html', username=username, user_flowers=user_flowers)

@app.route('/plant_flower/<flower_id>')
def plant_flower(flower_id):
    if 'username' not in session:
        return redirect(url_for('index'))
    username = session['username']
    user = User.query.filter_by(username=username).first()
    new_flower = Flower(name=f'Flower {flower_id}', user=user)
    db.session.add(new_flower)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
