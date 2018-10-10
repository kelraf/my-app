from flask import Flask, redirect, url_for, render_template, flash, request
import registration, bucketlist




app = Flask(__name__)
app.secret_key = 'dslmxcjdjkkoijwle'
user = registration.UserDetails()
bucket = bucketlist.UserBucketlist()


@app.route('/')
def main():
    return redirect(url_for('landing'))


@app.route('/landing')
def landing():
    return render_template('landing.htm')


@app.route('/home')
def home():
    return render_template('home.htm')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        new_user = user.register(request.form['username'], request.form['email'], request.form['password'], request.form['confirm_password'])

        if new_user == "user registered successfully":
            flash(new_user)
            return redirect(url_for('login'))
        else:
            flash(new_user)
            return redirect(url_for('register'))
    else:
        return render_template('register.htm')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        get_user = user.login(request.form['username'], request.form['password'])

        if get_user == True:
            return redirect(url_for('home'))
        else:
            flash(get_user)
            return redirect(url_for('login')) 

    else:
        return render_template('login.htm')


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():

    if request.method == "POST":
        reset = user.reset_password(request.form['username'], request.form['password'], request.form['new_password'])

        if reset == "You have successfully updated your password":
            flash(reset)
            return redirect(url_for('login'))
        else:
            flash(reset)
            return redirect(url_for('reset_password'))
    else:
        return render_template('reset_password.htm')


@app.route('/create_bucketlist', methods = ['GET', 'POST'])
def create_bucketlist():

    if request.method == "POST":
        new_backetlist = bucket.create_bucketlist(request.form['bucketlist_name'], request.form['about'], request.form['content'], request.form['created_by'])

        if new_backetlist == "bucketlist has been created successfully":
            flash(new_backetlist)
            return redirect(url_for('view'))
        else:
            flash(new_backetlist)
            return redirect(url_for('create_bucketlist'))
    return render_template('create_bucketlist.htm')


@app.route('/view_all')
def view_all():
    return render_template('view_all.htm', bucket = bucket)


@app.route('/view_content')
def view_content():
    return render_template("view_content.htm")    


@app.route('/view', methods = ['GET', 'POST'])
def view():
    if request.method == "POST":

        get_bucket = bucket.view(request.form['bucketlist_name'])

        if get_bucket == True:
            return redirect(url_for('view_content'))
        else:
            flash(get_bucket)   
            return redirect(url_for('view'))

    else:
        return render_template('view.htm')
          



if __name__ == "__main__":
    app.run(debug=True, port = 8000)    