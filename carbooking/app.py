from flask import Flask,request,render_template,url_for,flash,redirect
from models import db,User,Car,Booking
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'iyke'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('cars.html',cars = cars)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hased_pw = generate_password_hash(password, method='sha256')
        new_user = User(username=username,password=hased_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration has been done!!, you can now login')
        return redirect('login')
    return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user= User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password, password):
            logout_user(user)
            return redirect(url_for('home'))
        flash('invalid credentials')
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')

@app.route('/book/<int:car_id>')
@login_required
def book(car_id):
    car = Car.query.get_or_404(car_id)
    if not car.available:
        flash('car is already booked')
        return redirect(url_for('home'))
    booking = Booking(user_id=current_user.id, car_id=car_id)
    car.available = False
    db.session.add(booking)
    db.session.commit()
    flash('car booked successfully')
    return redirect(url_for('home'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)