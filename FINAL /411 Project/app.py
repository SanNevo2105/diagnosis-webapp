## DISEASES: EVERYTHING TO DISPLAY: 

## SYMPTOMS: EVERYTHING TO DISPLAY: 

## LOCATION: EVERYTHING TO DISPLAY: 

# from flask import Flask, render_template, request
# import queries as Q

# app = Flask(__name__)

# # home page
# @app.route('/')
# def home_page(): 
#     return render_template('home.html')


# # Routes for symptoms
# @app.route('/symptoms_input_page')
# def symptoms_input_page():
#     return render_template('symptoms.html')

# @app.route('/submit_symptoms', methods=['POST'])
# def submit_symptoms():
#     symptoms_list = request.form['symptoms']
#     suggested_disease = Q.get_suggested_disease(symptoms_list)
#     symptom_percentages = Q.get_symptom_percentages(suggested_disease)
#     return render_template('symptoms_result.html', suggested_disease=suggested_disease, symptom_percentages=symptom_percentages)

# # Routes for diseases
# @app.route('/diseases_input_page')
# def diseases_input_page():
#     return render_template('diseases.html')

# @app.route('/submit_diseases', methods=['POST'])
# def submit_diseases():
#     disease_name = request.form['diseases']
#     disease_info = Q.get_disease_information(disease_name)
#     top_drugs = Q.get_top_five_drugs(disease_name)
#     return render_template('diseases_result.html', disease_info=disease_info, top_drugs=top_drugs) 

# # Routes for drugs information
# @app.route('/drugs_input_page')
# def drugs_input_page():
#     return render_template('drugs.html')

# @app.route('/submit_drugs', methods=['POST'])
# def submit_drugs():
#     drug_name = request.form['drug_name']
#     drug_info = Q.get_drug_information(drug_name)
#     drug_reviews = Q.get_drug_reviews(drug_name)
#     substitute_drugs = Q.get_substitute_drugs(drug_name)
#     return render_template('drugs_result.html', drug_info=drug_info, drug_reviews=drug_reviews, substitute_drugs=substitute_drugs)




# # Route for locations
# @app.route('/locations_input_page')
# def locations_input_page():
#     return render_template('locations.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
import queries as Q
from datetime import date, timedelta

app = Flask(__name__)

# Home page
@app.route('/')
def home_page(): 
    return render_template('home.html')

# Routes for symptoms
@app.route('/symptoms_input_page')
def symptoms_input_page():
    return render_template('symptoms.html')

@app.route('/submit_symptoms', methods=['POST'])
def submit_symptoms():
    symptoms_list = request.form['symptoms']
    suggested_disease = Q.get_suggested_disease(symptoms_list)
    symptom_percentages = Q.get_symptom_percentages(suggested_disease)
    return render_template('symptoms_result.html', suggested_disease=suggested_disease, symptom_percentages=symptom_percentages)

# Routes for diseases
@app.route('/diseases_input_page')
def diseases_input_page():
    return render_template('diseases.html')

@app.route('/submit_diseases', methods=['POST'])
def submit_diseases():
    disease_name = request.form['diseases']
    disease_info = Q.get_disease_information(disease_name)
    top_drugs = Q.get_top_five_drugs(disease_name)
    return render_template('diseases_result.html', disease_info=disease_info, top_drugs=top_drugs) 

# Routes for drugs information
@app.route('/drugs_input_page')
def drugs_input_page():
    return render_template('drugs.html')

@app.route('/submit_drugs', methods=['POST'])
def submit_drugs():
    drug_name = request.form['drug_name']
    drug_info = Q.get_drug_information(drug_name)
    drug_reviews = Q.get_drug_reviews(drug_name)
    substitute_drugs = Q.get_substitute_drugs(drug_name)
    return render_template('drugs_result.html', drug_info=drug_info, drug_reviews=drug_reviews, substitute_drugs=substitute_drugs)

# # Routes for location input

@app.route('/locations_input_page')
def locations_input_page():
    return render_template('locations.html')

@app.route('/submit_locations', methods=['POST'])
def submit_locations():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    symptom_name = request.form['symptom_name']
    
    # Hard code today's date in SQL DATE format
    input_date = '2023-06-19'
    
    # Set duration to last 100 days
    duration = 100
    
    # Set distance to 20 km
    distance = 20
    
    user_location = 'POINT({}, {})'.format(longitude, latitude)

    top_five_symptoms = Q.get_top_five_symptoms(user_location, input_date, duration, distance)
    
    return render_template('locations_result.html', symptom_name=symptom_name, top_five_symptoms=top_five_symptoms)

    # latitude = request.form['latitude']
    # longitude = request.form['longitude']
    # symptom_name = request.form['symptom_name']
    
    # # Hard code today's date in SQL DATE format
    # input_date = '2023-06-19'
    
    # # Set duration to last 100 days
    # duration = 100
    
    # # Set distance to 20 km
    # distance = 20
    
    # user_location = 'POINT('+ longitude + ", " + latitude + ")" 
    # # user_location = (longitude, latitude) 

    # top_five_symptoms_result = Q.user_input(symptom_name, user_location, input_date, duration, distance)

    # # Fetch the result from the cursor
    # top_five_symptoms = []
    # for row in top_five_symptoms_result:
    #     top_five_symptoms.append(row)  # Assuming each row contains symptom and occurrence

    # return render_template('locations_result.html', symptom_name=symptom_name, top_five_symptoms=top_five_symptoms)


if __name__ == '__main__':
    app.run(debug=True)                                                                         