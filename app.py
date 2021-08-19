from flask import Flask,render_template,url_for,request
import joblib

filename = 'pickle.pkl'
clf = joblib.load("amazon_review.pkl")
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = clf.predict(data)
	return render_template('index.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)