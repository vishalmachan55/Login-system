from flask import Flask, render_template,url_for,request,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql=Mysql()
app.config["MYSQL_DATABASE_USER"]=  'root'
app.config["MYSQL_DATABASE_PASSWORD"]=  'lalitsanagavarapu'
app.config["MYSQL_DATABASE_DB"]=  '  '
app.config["MYSQL_DATABASE_HOST"]=  'localhost'
mysql.inint_app(app)


@app.route("/login", methods= ['GET','POST'])
def login():
	if request.method == 'POST' :
			username =request.form['email']
			password =request.form['password']
			con=mysql.connect()
			cur=con.cursor()
			cur.execute("SELECT *FROM'register' WHERE 'email' = '"+email+"' and 'password' = '"+password+"'" )
			data=cur.fetchone()
			if data[4] ==email and data[5] ==password:
				return redirect(url_for('home',data=data[0]))
			else:
				error="invalid"
				return render_template("Loginindex.html")
 
@app.route("/register", methods= ['GET','POST'])
def register():
	if request.method == 'POST' :
		 username =request.form['username']
		 birthdate =request.form['birthdate']
		 gender=request.form['gender']
		 email =request.form['email']
		 password =request.form['password']
		 con=mysql.connect()
		 cur=con.cursor()
		 cur.execute("INSERRT INTRO 'register'('username','birthdate', 'gender', 'email', 'password') VALUES (%s,%s,%s,%s,%s,)",(username,birthdate,gender,email,password))
		 con.commit()
		return redirect('login')
	else:	
		return render_template("Registerindex.html")



if(__name__=='__name__'):
	app.run(debug=True)
 
