from flask import *
from flask import render_template,url_for,send_from_directory,request
from flask_sqlalchemy import *
import os



app = Flask(__name__)

global did_name_1_come
global did_name_2_come
global did_name_3_come

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
 


db.session.commit()

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/addthing.html')
def addthing():
    did_name_1_come = request.args.get('nm1')
    did_name_2_come = request.args.get('nm2')
    did_name_3_come = request.args.get('nm3')
    print(did_name_1_come)
    print(did_name_2_come)
    print(did_name_3_come)    
    return render_template('addthing.html', did_name_1_come=did_name_1_come, did_name_2_come=did_name_2_come, did_name_3_come=did_name_3_come)

@app.route('/veiw.html')
def veiw ():
    return render_template('veiw.html')

@app.route('/testing.htm')
def testing():
    name1 = request.args.get('name1')
    return 'name1 is {}'.format(name1)

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')

if __name__ == '__main__':
    app.run(debug=True) 
