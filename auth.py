from flask import Blueprint, render_template, request, flash, session
from db_connection import conn

auth = Blueprint('auth', __name__)


# the parameter passed after the html file, a variable passed in can also be accessed html file.
# can pass as many vars as needed
# return render_template('login.html', text="Testing", user="Tim")

# methods parameter specifies what requests the particular function can handle

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':    
        username = request.form.get('username')
        pwd = request.form.get('password')
        cursor = conn.cursor()
        cursor.execute("SELECT * from Retail_Application.Users WHERE Username = %s and pwd = %s", (username, pwd))   
        row = cursor.fetchone()
        
        if row:
            # Create session data, we can access this data in other routes
            session.permanent = False
            session['loggedin'] = True
            session['UserID'] = row[0]
            session['username'] = username
            # Redirect to home page
            return render_template('home.html')
        else:
            flash('Invalid credentials!, please try again.', category='error')
                 
    return render_template('login.html')


@auth.route('/logout')
def logout():

    session.pop('loggedin', None)
    session.pop('UserID', None)
    session.pop('username', None)
    return render_template('home.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get('username')
        address = request.form.get('Address')
        first_name = request.form.get('firstName')
        last_name = request.form.get('LastName')
        secondary = request.form.get('secondary')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        cursor = conn.cursor()
    
        upper_case_count = 1
        special_char_count = 1
        
        for c in password1:
            if c.isupper():
                upper_case_count -= 1

            if c == '#' or c == '$' or c == '?' or c =='!' or c=='@':
                special_char_count -= 1
            

        if len(first_name) < 2:
            flash('First Name must be larger than 1 character!', category='error')
        elif len(last_name) < 2:
            flash('Last Name must be larger than 1 character!', category='error')
        elif len(password1) < 7 or len(password1) > 16:
            flash('Password must be 7 - 16 characters long, please try again!', category='error')
        elif len(password2) != len(password1) or password1 != password2:
            flash('Password length or content mismatch, please try again!', category='error')
        elif special_char_count != 0:
             flash("Password must have at most 1 special character from '?, #, @, $, or !' , try again!", category='error')
        elif upper_case_count != 0:
            flash('Password must have at most 1 upper case character, please try again!', category='error')
        else:
            flash('Successfully created account', category='success')
            
            if not secondary:
                cursor.execute("INSERT INTO Retail_Application.Users (FirstName, LastName, Username, pwd, address) VALUES(%s, %s, %s, %s, %s);", (first_name, last_name, username, password1, address))
            else:  
                cursor.execute("SELECT * from Retail_Application.Users WHERE UserID = %s" , (secondary))
                row = cursor.fetchone()
                cursor.execute("INSERT INTO Retail_Application.Users (FirstName, LastName, Username, pwd, address, parent_account) VALUES(%s, %s, %s, %s, %s, %s);", (first_name, last_name, username, password1, address, row[0]))
                conn.commit()
    
    return render_template('sign_up.html')