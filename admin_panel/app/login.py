from flask_login import LoginManager

login = LoginManager()
login.login_view = 'homePage.login'
