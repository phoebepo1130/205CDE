from flask import Flask, render_template , request, url_for ,redirect , session
import pymysql

app = Flask(__name__)
app.secret_key = 'Any string'


db = pymysql.connect("localhost", "root", "py1130", "DE")



@app.route("/signup", methods = ['POST', 'GET'])
def signup():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd =  request.form['password']
		email = request.form['password']

		
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO user (username, password, email) VALUES (%s, %s, %s)""", (usrname, pwd, email))

		db.commit()
	return render_template("signup.html",error = error)

	db.close()

@app.route("/login", methods = ['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd = request.form['password']
		custName=[]
		custPassword=[]

		#
		db = pymysql.connect("localhost", "root", "py1130", "DE")

		cursor = db.cursor()

		#
		
		sql = ("SELECT username, password FROM user WHERE username = '"+usrname+"'")
		cursor.execute(sql)
		#
		db.commit()
		results = cursor.fetchall()
		for row in results:
			custName.append(row[0])
			custPassword.append(row[1])
			#
		if custName ==[]:
			return render_template("login.html",test="wrong username and password")

		if(usrname == custName[0]) and (pwd == custPassword[0]):
			return render_template("tester.html", guest = custName)

		elif usrname == custName[0] and pwd!= custPassword[0]:
			return render_template("login.html",test="wrong password")

		

			

			
	return render_template("login.html", error = error)	


	

	db.close()

@app.route("/logout")
def logout():
	#
	session.pop('username', None)
	return render_template("login.html")
	#

@app.route("/hihi", methods = ['POST', 'GET'])
def hihi():
	error = None
	if request.method == 'POST':
		item =  request.form['item']
		quantity =  request.form['quantity']
		price =  request.form['price']


		
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO product (item, quantity, price) VALUES (%s, %s, %s)""", (item, quantity, price ))

		db.commit()
	return render_template("hihi.html",error = error)

	db.close()

@app.route("/tester")
def tester():
	return render_template("tester.html")

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")



if __name__ == '__main__':
        app.debug = True
        app.run(host="0.0.0.0", port=5000)

