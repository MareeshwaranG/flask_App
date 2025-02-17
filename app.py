from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flashing messages

# Predefined username and password
USERNAME = 'admin'
PASSWORD = 'password123'

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('home'))  # Redirect to the home page on successful login
        else:
            flash('Invalid username or password')  # Show an error message

    return render_template('login.html')

# Route for the home page
@app.route('/')
def home():
    
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')

# Route for the flashcard page
@app.route('/flashcard')
def flashcard():
    return render_template('flashcard.html')

# Route for the second flashcard page
@app.route('/flashcard2')
def flashcard2():
    return render_template('flashcard2.html')

# Route for the quiz page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Route for the second quiz page
@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')

# Route for the quiz result page
@app.route('/quiz_result')
def quiz_result():
    return render_template('quiz_result.html')

if __name__ == '__main__':
    app.run(debug=True)