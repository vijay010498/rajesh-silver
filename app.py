from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config["MYSQL_HOST"] ="localhost"
app.config["MYSQL_USER"] ="root"
app.config["MYSQL_PASSWORD"] ="1234"
app.config["MYSQL_DB"] ="silver"
mysql=MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/details')
def details():
    return render_template('details.html') 

@app.route('/service')
def service ():
    return render_template('service.html') 

@app.route('/design')
def design ():
    return render_template('design.html') 

@app.route('/back')
def back():
    return render_template('index.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method =='POST':
        a=request.form
        name  = a["name"]
        phone = a["phone"]
        email= a["email"]
        forshop=a["checkbox"]
        wholer=a["checkbox"]
        state=a["state"]
        about=a["about"]
        cur = mysql.connection.cursor( )
        cur.execute("insert into silvers(name,phone,email,forshop,wholer,state,about) values (%s,%s,%s,%s,%s,%s,%s)",
                    [ name, phone, email, forshop,wholer,state,about])
        mysql.connection.commit( )
        cur.close( )
        return "YOUR DETAILS SEND SUCCESS"
    return render_template("contact.html")

if (__name__=='__main__'):
    app.run(debug=True)
