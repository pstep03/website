from flask import Flask, render_template, request, redirect, abort, url_for, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'placeholder'

def encrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return(hashed)

def database():
    con = sqlite3.connect('LogInformation.db', check_same_thread=False)
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS UserInfo (
        username TEXT NOT NULL,
        pswrd TEXT NOT NULL
    );''')

    con.commit()
    con.close()

database()

@app.route('/', methods=['GET'])
def start_page():
    return render_template("starting_page.html")

@app.route('/create_account/',methods=['GET'])
def create_account():
    return redirect("/create_account_page")

@app.route('/create_account_page/', methods=['GET', 'POST'])
def create_account_page():
    error_message = request.args.get('error_message', '') 
    return render_template("create_account_page.html", error_message=error_message)

@app.route('/form_submmission/', methods=['GET', 'POST'])
def creation_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        con = sqlite3.connect('LogInformation.db', check_same_thread=False)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM UserInfo WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return redirect("/create_account_page?error_message=Username%20Already%20Exists")
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        cursor.execute("INSERT INTO UserInfo (username, pswrd) VALUES (?, ?)", (username, hashed_password.decode('utf-8')))
        con.commit()
        con.close()
        
        return redirect("/login/welcome/")

    return redirect("/create_account_page/")

@app.route("/login", methods=["GET", "POST"])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        con = sqlite3.connect('LogInformation.db', check_same_thread=False)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM UserInfo WHERE username=?", (username,))
        user = cursor.fetchone()
        
        if user:
            stored_password_hash = user[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                session['logged_in'] = True
                return redirect("/login/welcome/")
            else:
                error_message = "Incorrect Username or Password"
        else:
            error_message = "Incorrect Username or Password"

        con.close()

    return render_template("starting_page.html", error_message=error_message)

@app.route("/login/welcome/")
def home_page():
    if not session.get('logged_in'):
        return redirect('/')

    return render_template("home_page.html")

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)