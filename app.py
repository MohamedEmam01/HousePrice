from joblib import load
from flask import Flask, request, render_template
app = Flask(__name__, template_folder='C:\\Users\Mohamed\House Salary\\New folder\\template')

model = load("Random_Forest_Model_Regression.pkl")
model2=load('Random_Forset_Model_Classification.pkl')
@app.route("/")
def Home ():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    bedrooms = request.form["bedrooms"]
    bathrooms = request.form["bathrooms"]
    sqft_living = request.form["sqft_living"]
    floors = request.form["floors"]
    view = request.form["view"]
    grade = request.form["grade"]
    sqft_above = request.form["sqft_above"]
    sqft_basement = request.form["sqft_basement"]
    lat = request.form["lat"]
    sqft_lot15 = request.form["sqft_lot15"]
    population = request.form["population"]

    price = model.predict([[bedrooms, bathrooms, sqft_living, floors, view, grade, sqft_above, sqft_basement, lat, sqft_lot15, population]])
    priseKind=model2.predict([[bedrooms, bathrooms, sqft_living, floors, view, grade, sqft_above, sqft_basement, lat, sqft_lot15, population]])
    return render_template("index.html", output = price,output2=priseKind)

if __name__ == "__main__":
    app.run(debug=True)