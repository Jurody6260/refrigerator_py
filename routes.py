from api import *


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# @login_required
@app.route("/")
def index():
    print("loaded index")
    return render_template("index.html", page='home')

@app.route('/login')
def login():
    return render_template('pages/login.html', page='login')

@app.route('/reports')
def reports():
    return render_template('pages/reports.html', page='reports')

@app.route('/orders')
def orders():
    return render_template('pages/orders.html', page='orders')

@app.route('/help')
def help():
    return render_template('pages/help.html', page='help')