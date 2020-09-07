from flask import Flask
from flask import request, render_template
from flask import redirect

app=Flask(__name__)

@app.route('/')
def func():
	return render_template('index.html')

@app.route('/registration.html')
def func2():
	return render_template('registration.html')	

@app.route('/success.html')
def func3():
	return render_template('success.html')

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email=data['email']
		name=data['name']
		contact=data['contact']
		interest=data['interest']
		branch=data['branch']
		msg=data['msg']
		file=database.write(f'\n{email}, {name}, {contact}, {interest}, {branch}, {msg}')

@app.route('/submit',methods=['POST','GET'])
def submit():
	if request.method=='POST':
		data=request.form.to_dict()
		write_to_file(data)
		return redirect('/success.html')

		
