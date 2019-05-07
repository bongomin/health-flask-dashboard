from flask import Flask,render_template,url_for


app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/center')
def center():
    return render_template('center.html')








if __name__=='__main__':
    app.run(debug=True)