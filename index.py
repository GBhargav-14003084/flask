from flask import Flask,render_template,request,json
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='college',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'Hey World'

@app.route("/reg")
def registerPage():
    return render_template('reg.html')

@app.route('/register',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
     name=request.form['name']
     email=request.form['email']
     try:
  

      with connection.cursor() as cursor:
      # Read a single record
        sql = "INSERT INTO users (name,email) VALUES (%s, %s)"
        cursor.execute(sql, (name,email))
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"

@app.route("/users")
def users():
    return render_template('userList.html')

if __name__ == '__main__':
   app.run()