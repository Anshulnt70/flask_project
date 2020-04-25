from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='')


@app.route('/', methods= [ 'POST' , 'GET' ] )
def hellok():
	if request.method == 'POST':
		result = request.form
		print(result["name"])
		print(result["email"])
		print(result["comments"])
		return render_template('anji/Thank You Mam.html', name=result["name"], email=result["email"], comments=result["comments"])
	else :
		return render_template('abouts.html')


@app.route('/anshuljoshi/dj2/aj/static/index1234/')
def root():
    return app.send_static_file('index1234.html')


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
