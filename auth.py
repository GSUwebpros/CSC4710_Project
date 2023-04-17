from flask import Blueprint, redirect, render_template, request, flash, session, url_for
from db_connection import conn

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    message = ""
    if request.method == 'POST':    
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        cursor = conn.cursor()
        cursor.execute("SELECT * from Retail_Application.Users WHERE Username = %s and pwd = %s", (username, pwd))   
        row = cursor.fetchone()
        
        if row:
            session['loggedin'] = True
            session['UserID'] = row[0]
            session['username'] = row[3]
            return render_template('index.html')
        else:
            message = 'Invalid credentials!, please try again.'
    
    return render_template('login.html', message = message)


@auth.route('/logout')
def logout():

    session.pop('loggedin', None)
    session.pop('UserID', None)
    session.pop('username', None)
    session.pop('shopping_cart', None)
    session.pop('cart_total', None)
    session.pop('tokens', None)
    session.pop('reward', None)
    session.pop('discount_notTaken', None)
    
    return redirect(url_for("views.home"))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    
    message = ""
    is_valid = ""
    if request.method == 'POST':

        username = request.form.get('username')
        address = request.form.get('address')
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        password1 = request.form.get('pwd')
        password2 = request.form.get('cpwd')
        cursor = conn.cursor()
        
        
        upper_case_count = 1
        special_char_count = 1
        user_exists = False 
        
        for c in password1:
            if c.isupper():
                upper_case_count -= 1

            if c == '#' or c == '$' or c == '?' or c =='!' or c=='@':
                special_char_count -= 1
        
        cursor.execute("SELECT username From retail_application.users")
        users = cursor.fetchall()
        
        for user in users:
            
            if user[0] == username:
                user_exists = True
                break
        
        if user_exists:
            message = "username already exists, please try again!"
            is_valid = False
        elif len(first_name) < 2:
            message = 'First Name must be larger than 1 character!'
            is_valid = False
        elif len(last_name) < 2:
            message = 'Last Name must be larger than 1 character!'
            is_valid = False
        elif len(password1) < 7 or len(password1) > 16:
            message = 'Password must be 7 - 16 characters long, please try again!'
            is_valid = False
        elif len(password2) != len(password1) or password1 != password2:
            message = 'Password length or content mismatch, please try again!'
            is_valid = False
        elif special_char_count != 0:
            message = "Password must have at most 1 special character from '?, #, @, $, or !' , try again!"
            is_valid = False
        elif upper_case_count != 0:
            message = 'Password must have at most 1 upper case character, please try again!'
            is_valid = False
        else:
            message = 'Successfully created account'
            is_valid = True
            cursor.execute("INSERT INTO Retail_Application.Users (FirstName, LastName, Username, pwd, address) VALUES(%s, %s, %s, %s, %s);", (first_name, last_name, username, password1, address))
            conn.commit()
                                
    return render_template('signup.html', message = message, is_valid = is_valid)

            
              