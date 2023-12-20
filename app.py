from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'  # Change this to a secure secret key

login_manager = LoginManager(app)

@app.route('/')
def index():
    return render_template('index.html')

# Define route for the products page
@app.route('/products')
def products():
    return render_template('products.html')

# Example User class (replace with your own User model if using a database)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes for authentication
@app.route('/login')
def login():
    user = User('user_id')  # Replace with your user retrieval logic
    login_user(user)
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
