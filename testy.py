from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    tweets = db.relationship('Tweet', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Tweet('{self.title}', '{self.date_posted}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash('Logged in successfully.', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Incorrect email or password.', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=request.form['username'], email=request.form['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/home')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    tweets = Tweet.query.order_by(Tweet.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', tweets=tweets)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route('/tweet', methods=['GET', 'POST'])
@login_required
def tweet():
    if request.method == 'POST':
        tweet_post = Tweet(title=request.form['title'], content=request.form['content'], author=current_user)
        db.session.add(tweet_post)
        db.session.commit()
        flash('Your tweet has been posted!', 'success')
        return redirect(url_for('home'))
    return render_template('tweet.html', title='Tweet')

@app.route('/tweet/<int:tweet_id>')
def tweet_detail(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    return render_template('tweet_detail.html', title=tweet.title, tweet=tweet)

@app.route('/tweet/<int:tweet_id>/update', methods=['GET', 'POST'])
@login_required
def tweet_update(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    if tweet.author != current_user:
        abort(403)
    if request.method == 'POST':
        tweet.title = request.form['title']
        tweet.content = request.form['content']
        db.session.commit()
        flash('Your tweet has been updated!', 'success')
        return redirect(url_for('tweet_detail', tweet_id=tweet.id))
    elif request.method == 'GET':
        return render_template('tweet_update.html', title='Update Tweet', tweet=tweet)

@app.route('/tweet/<int:tweet_id>/delete', methods=['POST'])
@login_required
def tweet_delete(tweet_id):
    tweet = Tweet.query.get_or_404(tweet_id)
    if tweet.author != current_user:
        abort(403)
    db.session.delete(tweet)
    db.session.commit()
    flash('Your tweet has been deleted!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)