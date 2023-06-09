# Import all the necessary modules
from flask import Flask, request, render_template

# Create an Flask app instance
app = Flask(__name__)

# Create a function to calculate BMI
@app.route('/', methods=['GET', 'POST'])
def bmi():
	name = ""
	weight = 1
	height = 1.0
	bmi = 0.0
	bmi_category = ""

	if request.method == "POST" and "username" in request.form:
		name = request.form.get('username')
		height = float(request.form.get('user_height'))
		weight = float(request.form.get('user_weight'))

	# get formatted name of user
	name = formatted_user_name(name)

	# get bmi calculated of user
	bmi = calculated_bmi(height, weight)

	# get user bmi category
	bmi_category = user_bmi_classification(bmi)

	# return the value to template
	return render_template("index.html", name=name, height=height, weight=weight, bmi=bmi, bmi_category=bmi_category)


# User formatted game
def formatted_user_name(name):
	good_name = f"{name.title()}"
	
	return good_name

# User bmi calculation by height and weight
def calculated_bmi(height, weight):
	# height cm -> meter
	height_in_meter = float(height) / 100
	height_square = (height_in_meter * height_in_meter)
	
	# calculate BMI
	bmi = (int(weight) / height_square)
	bmi = round(bmi, 2)

	return bmi

# User's bmi classification by the bmi result
def user_bmi_classification(bmi):
	bmi_category = ""
	# check BMI category
	if bmi < 18.5:
		bmi_category = "Under Weight"
	elif bmi >= 18.5 and bmi <= 24.9:
		bmi_category = "Normal Weight"
	elif bmi >= 25.0 and bmi <= 29.9:
		bmi_category = "Over Weight"
	elif bmi >= 30.0 and bmi <= 34.9:
		bmi_category = "Obese Class I"
	elif bmi >= 35.0 and bmi <= 39.9:
		bmi_category = "Obese Class II"
	elif bmi >= 40.0:
		bmi_category = "Obese Class III"

	return bmi_category


# Run the flask app
app.run(debug=True) # do not set debug=True in production.























