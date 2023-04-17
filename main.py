from auth import auth
from views import views
from db_connection import app

app.register_blueprint(auth)
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
