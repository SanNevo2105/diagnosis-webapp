import mysql.connector
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
from shapely.geometry import Point
from shapely.wkb import dumps

warnings.filterwarnings("ignore")

def connect_to_mysql():
    try:
        cnx = mysql.connector.connect(
            user='root', password='test1234', host='34.171.103.233', database='team059'
        )

        return cnx
    except mysql.connector.Error as err:
        print(err)

def send_query(query):
    cnx = connect_to_mysql()

    cursor = cnx.cursor()

    cursor.execute(query)

    res = cursor.fetchall()
    if len(res) == 0:
        return None
    
    cursor.close()
    cnx.close()

    return res

#========================================================================================================================
# Get Precautions
def get_precautions(symptom_name):
    query = """
    WITH disease_list as (
        select disease as name from Symptoms group by disease having case when """ + symptom_name + """ = 'itching' then avg(itching) >= 0.5 when """ + symptom_name + """ = 'skin_rash' then avg(skin_rash) >= 0.5 when """ + symptom_name + """ = 'nodal_skin_eruptions' then avg(nodal_skin_eruptions) >= 0.5 when """ + symptom_name + """ = 'continuous_sneezing' then avg(continuous_sneezing) >= 0.5 when """ + symptom_name + """ = 'shivering' then avg(shivering) >= 0.5 when """ + symptom_name + """ = 'chills' then avg(chills) >= 0.5 when """ + symptom_name + """ = 'joint_pain' then avg(joint_pain) >= 0.5 when """ + symptom_name + """ = 'stomach_pain' then avg(stomach_pain) >= 0.5 when """ + symptom_name + """ = 'acidity' then avg(acidity) >= 0.5 when """ + symptom_name + """ = 'ulcers_on_tongue' then avg(ulcers_on_tongue) >= 0.5 when """ + symptom_name + """ = 'muscle_wasting' then avg(muscle_wasting) >= 0.5 when """ + symptom_name + """ = 'vomiting' then avg(vomiting) >= 0.5 when """ + symptom_name + """ = 'burning_micturition' then avg(burning_micturition) >= 0.5 when """ + symptom_name + """ = 'spotting_urination' then avg(spotting_urination) >= 0.5 when """ + symptom_name + """ = 'fatigue' then avg(fatigue) >= 0.5 when """ + symptom_name + """ = 'weight_gain' then avg(weight_gain) >= 0.5 when """ + symptom_name + """ = 'anxiety' then avg(anxiety) >= 0.5 when """ + symptom_name + """ = 'cold_hands_and_feets' then avg(cold_hands_and_feets) >= 0.5 when """ + symptom_name + """ = 'mood_swings' then avg(mood_swings) >= 0.5 when """ + symptom_name + """ = 'weight_loss' then avg(weight_loss) >= 0.5 when """ + symptom_name + """ = 'restlessness' then avg(restlessness) >= 0.5 when """ + symptom_name + """ = 'lethargy' then avg(lethargy) >= 0.5 when """ + symptom_name + """ = 'patches_in_throat' then avg(patches_in_throat) >= 0.5 when """ + symptom_name + """ = 'irregular_sugar_level' then avg(irregular_sugar_level) >= 0.5 when """ + symptom_name + """ = 'cough' then avg(cough) >= 0.5 when """ + symptom_name + """ = 'high_fever' then avg(high_fever) >= 0.5 when """ + symptom_name + """ = 'sunken_eyes' then avg(sunken_eyes) >= 0.5 when """ + symptom_name + """ = 'breathlessness' then avg(breathlessness) >= 0.5 when """ + symptom_name + """ = 'sweating' then avg(sweating) >= 0.5 when """ + symptom_name + """ = 'dehydration' then avg(dehydration) >= 0.5 when """ + symptom_name + """ = 'indigestion' then avg(indigestion) >= 0.5 when """ + symptom_name + """ = 'headache' then avg(headache) >= 0.5 when """ + symptom_name + """ = 'yellowish_skin' then avg(yellowish_skin) >= 0.5 when """ + symptom_name + """ = 'dark_urine' then avg(dark_urine) >= 0.5 when """ + symptom_name + """ = 'nausea' then avg(nausea) >= 0.5 when """ + symptom_name + """ = 'loss_of_appetite' then avg(loss_of_appetite) >= 0.5 when """ + symptom_name + """ = 'pain_behind_the_eyes' then avg(pain_behind_the_eyes) >= 0.5 when """ + symptom_name + """ = 'back_pain' then avg(back_pain) >= 0.5 when """ + symptom_name + """ = 'constipation' then avg(constipation) >= 0.5 when """ + symptom_name + """ = 'abdominal_pain' then avg(abdominal_pain) >= 0.5 when """ + symptom_name + """ = 'diarrhoea' then avg(diarrhoea) >= 0.5 when """ + symptom_name + """ = 'mild_fever' then avg(mild_fever) >= 0.5 when """ + symptom_name + """ = 'yellow_urine' then avg(yellow_urine) >= 0.5 when """ + symptom_name + """ = 'yellowing_of_eyes' then avg(yellowing_of_eyes) >= 0.5 when """ + symptom_name + """ = 'acute_liver_failure' then avg(acute_liver_failure) >= 0.5 when """ + symptom_name + """ = 'fluid_overload' then avg(fluid_overload) >= 0.5 when """ + symptom_name
    + """ = 'swelling_of_stomach' then avg(swelling_of_stomach) >= 0.5 when """ + symptom_name + """ = 'swelled_lymph_nodes' then avg(swelled_lymph_nodes) >= 0.5 when """ + symptom_name + """ = 'malaise' then avg(malaise) >= 0.5 when """ + symptom_name + """ = 'blurred_and_distorted_vision' then avg(blurred_and_distorted_vision) >= 0.5 when """ + symptom_name + """ = 'phlegm' then avg(phlegm) >= 0.5 when """ + symptom_name + """ = 'throat_irritation' then avg(throat_irritation) >= 0.5 when """ + symptom_name + """ = 'redness_of_eyes' then avg(redness_of_eyes) >= 0.5 when """ + symptom_name + """ = 'sinus_pressure' then avg(sinus_pressure) >= 0.5 when """ + symptom_name + """ = 'runny_nose' then avg(runny_nose) >= 0.5 when """ + symptom_name + """ = 'congestion' then avg(congestion) >= 0.5 when """ + symptom_name + """ = 'chest_pain' then avg(chest_pain) >= 0.5 when """ + symptom_name + """ = 'weakness_in_limbs' then avg(weakness_in_limbs) >= 0.5 when """ + symptom_name + """ = 'fast_heart_rate' then avg(fast_heart_rate) >= 0.5 when """ + symptom_name + """ = 'pain_during_bowel_movements' then avg(pain_during_bowel_movements) >= 0.5 when """ + symptom_name + """ = 'pain_in_anal_region' then avg(pain_in_anal_region) >= 0.5 when """ + symptom_name + """ = 'bloody_stool' then avg(bloody_stool) >= 0.5 when """ + symptom_name + """ = 'irritation_in_anus' then avg(irritation_in_anus) >= 0.5 when """ + symptom_name + """ = 'neck_pain' then avg(neck_pain) >= 0.5 when """ + symptom_name + """ = 'dizziness' then avg(dizziness) >= 0.5 when """ + symptom_name + """ = 'cramps' then avg(cramps) >= 0.5 when """ + symptom_name + """ = 'bruising' then avg(bruising) >= 0.5 when """ + symptom_name + """ = 'obesity' then avg(obesity) >= 0.5 when """ + symptom_name + """ = 'swollen_legs' then avg(swollen_legs) >= 0.5 when """ + symptom_name + """ = 'swollen_blood_vessels' then avg(swollen_blood_vessels) >= 0.5 when """ + symptom_name + """ = 'puffy_face_and_eyes' then avg(puffy_face_and_eyes) >= 0.5 when """ + symptom_name + """ = 'enlarged_thyroid' then avg(enlarged_thyroid) >= 0.5 when """ + symptom_name + """ = 'brittle_nails' then avg(brittle_nails) >= 0.5 when """ + symptom_name + """ = 'swollen_extremeties' then avg(swollen_extremeties) >= 0.5 when """ + symptom_name + """ = 'excessive_hunger' then avg(excessive_hunger) >= 0.5 when """ + symptom_name + """ = 'extra_marital_contacts' then avg(extra_marital_contacts) >= 0.5 when """ + symptom_name + """ = 'drying_and_tingling_lips' then avg(drying_and_tingling_lips) >= 0.5 when """ + symptom_name + """ = 'slurred_speech' then avg(slurred_speech) >= 0.5 when """ + symptom_name + """ = 'knee_pain' then avg(knee_pain) >= 0.5 when """ + symptom_name + """ = 'hip_joint_pain' then avg(hip_joint_pain) >= 0.5 when """ + symptom_name + """ = 'muscle_weakness' then avg(muscle_weakness) >= 0.5 when """ + symptom_name + """ = 'stiff_neck' then avg(stiff_neck) >= 0.5 when """ + symptom_name + """ = 'swelling_joints' then avg(swelling_joints) >= 0.5 when """ + symptom_name + """ = 'movement_stiffness' then avg(movement_stiffness) >= 0.5 when """ + symptom_name + """ = 'spinning_movements' then avg(spinning_movements) >= 0.5 when """ + symptom_name + """ = 'loss_of_balance' then avg(loss_of_balance) >= 0.5 when """ + symptom_name + """ = 'unsteadiness' then avg(unsteadiness) >= 0.5 when """ + symptom_name + """ = 'weakness_of_one_body_side' then avg(weakness_of_one_body_side) >= 0.5 when """ + symptom_name + """ = 'loss_of_smell' then avg(loss_of_smell) >= 0.5 when """ + symptom_name + """ = 'bladder_discomfort' then avg(bladder_discomfort) >= 0.5 when """ + symptom_name
    + """ = 'foul_smell_of_urine' then avg(foul_smell_of_urine) >= 0.5 when """ + symptom_name + """ = 'continuous_feel_of_urine' then avg(continuous_feel_of_urine) >= 0.5 when """ + symptom_name + """ = 'passage_of_gases' then avg(passage_of_gases) >= 0.5 when """ + symptom_name + """ = 'internal_itching' then avg(internal_itching) >= 0.5 when """ + symptom_name + """ = 'toxic_look_typhos' then avg(toxic_look_typhos) >= 0.5 when """ + symptom_name + """ = 'depression' then avg(depression) >= 0.5 when """ + symptom_name + """ = 'irritability' then avg(irritability) >= 0.5 when """ + symptom_name + """ = 'muscle_pain' then avg(muscle_pain) >= 0.5 when """ + symptom_name + """ = 'altered_sensorium' then avg(altered_sensorium) >= 0.5 when """ + symptom_name + """ = 'red_spots_over_body' then avg(red_spots_over_body) >= 0.5 when """ + symptom_name + """ = 'belly_pain' then avg(belly_pain) >= 0.5 when """ + symptom_name + """ = 'abnormal_menstruation' then avg(abnormal_menstruation) >= 0.5 when """ + symptom_name + """ = 'dischromic_patches' then avg(dischromic_patches) >= 0.5 when """ + symptom_name + """ = 'watering_from_eyes' then avg(watering_from_eyes) >= 0.5 when """ + symptom_name + """ = 'increased_appetite' then avg(increased_appetite) >= 0.5 when """ + symptom_name + """ = 'polyuria' then avg(polyuria) >= 0.5 when """ + symptom_name + """ = 'family_history' then avg(family_history) >= 0.5 when """ + symptom_name + """ = 'mucoid_sputum' then avg(mucoid_sputum) >= 0.5 when """ + symptom_name + """ = 'rusty_sputum' then avg(rusty_sputum) >= 0.5 when """ + symptom_name + """ = 'lack_of_concentration' then avg(lack_of_concentration) >= 0.5 when """ + symptom_name + """ = 'visual_disturbances' then avg(visual_disturbances) >= 0.5 when """ + symptom_name + """ = 'receiving_blood_transfusion' then avg(receiving_blood_transfusion) >= 0.5 when """ + symptom_name + """ = 'receiving_unsterile_injections' then avg(receiving_unsterile_injections) >= 0.5 when """ + symptom_name + """ = 'coma' then avg(coma) >= 0.5 when """ + symptom_name + """ = 'stomach_bleeding' then avg(stomach_bleeding) >= 0.5 when """ + symptom_name + """ = 'distention_of_abdomen' then avg(distention_of_abdomen) >= 0.5 when """ + symptom_name + """ = 'history_of_alcohol_consumption' then avg(history_of_alcohol_consumption) >= 0.5 when """ + symptom_name + """ = 'blood_in_sputum' then avg(blood_in_sputum) >= 0.5 when """ + symptom_name + """ = 'prominent_veins_on_calf' then avg(prominent_veins_on_calf) >= 0.5 when """ + symptom_name + """ = 'palpitations' then avg(palpitations) >= 0.5 when """ + symptom_name + """ = 'painful_walking' then avg(painful_walking) >= 0.5 when """ + symptom_name + """ = 'pus_filled_pimples' then avg(pus_filled_pimples) >= 0.5 when """ + symptom_name + """ = 'blackheads' then avg(blackheads) >= 0.5 when """ + symptom_name + """ = 'scurring' then avg(scurring) >= 0.5 when """ + symptom_name + """ = 'skin_peeling' then avg(skin_peeling) >= 0.5 when """ + symptom_name + """ = 'silver_like_dusting' then avg(silver_like_dusting) >= 0.5 when """ + symptom_name + """ = 'small_dents_in_nails' then avg(small_dents_in_nails) >= 0.5 when """ + symptom_name + """ = 'inflammatory_nails' then avg(inflammatory_nails) >= 0.5 when """ + symptom_name + """ = 'blister' then avg(blister) >= 0.5 when """ + symptom_name + """ = 'ed_sore_around_nose' then avg(ed_sore_around_nose) >= 0.5 when """ + symptom_name + """ = 'yellow_crust_ooze' then avg(yellow_crust_ooze) >= 0.5 end
        )
        select precaution, count(precaution)
		from (
			select precaution_1 as precaution from Diseases natural join disease_list
			union all
            select precaution_2 as precaution from Diseases natural join disease_list
            union all
            select precaution_3 as precaution from Diseases natural join disease_list
            union all
            select precaution_4 as precaution from Diseases natural join disease_list
		) as temp
		group by precaution
		order by count(precaution) desc, precaution;
"""
    return send_query(query)


# Top 5 symptoms in area and timeframe

def user_input(symptoms, location, date, duration = 20, distance = 100):
    if duration is None:
        duration = 20
    if distance is None:
        distance = 100
    symptom_names = ['itching', 'skin_rash', 'nodal_skin_eruptions',
        'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
        'vomiting', 'burning_micturition', 'spotting_ urination',
        'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
        'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
        'patches_in_throat', 'irregular_sugar_level', 'cough',
        'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
        'dehydration', 'indigestion', 'headache', 'yellowish_skin',
        'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
        'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
        'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
        'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
        'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
        'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        'fast_heart_rate', 'pain_during_bowel_movements',
        'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
        'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
        'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
        'excessive_hunger', 'extra_marital_contacts',
        'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
        'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
        'swelling_joints', 'movement_stiffness', 'spinning_movements',
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
        'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        'abnormal_menstruation', 'dischromic _patches',
        'watering_from_eyes', 'increased_appetite', 'polyuria',
        'family_history', 'mucoid_sputum', 'rusty_sputum',
        'lack_of_concentration', 'visual_disturbances',
        'receiving_blood_transfusion', 'receiving_unsterile_injections',
        'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'fluid_overload.1',
        'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
        'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
        'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
        'inflammatory_nails', 'blister', 'red_sore_around_nose']
        # 'yellow_crust_ooze']
    s = [int(symptom in symptoms) for symptom in symptom_names]
    # s = tuple(s) + (location, date, duration, distance)

    # s_str = "s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26],s[27],s[28],s[29],s[30],s[31],s[32],s[33],s[34],s[35],s[36],s[37],s[38],s[39],s[40],s[41],s[42],s[43],s[44],s[45],s[46],s[47],s[48],s[49],s[50],s[51],s[52],s[53],s[54],s[55],s[56],s[57],s[58],s[59],s[60],s[61],s[62],s[63],s[64],s[65],s[66],s[67],s[68],s[69],s[70],s[71],s[72],s[73],s[74],s[75],s[76],s[77],s[78],s[79],s[80],s[81],s[82],s[83],s[84],s[85],s[86],s[87],s[88],s[89],s[90],s[91],s[92],s[93],s[94],s[95],s[96],s[97],s[98],s[99],s[100],s[101],s[102],s[103],s[104],s[105],s[106],s[107],s[108],s[109],s[110],s[111],s[112],s[113],s[114],s[115],s[116],s[117],s[118],s[119],s[120],s[121],s[122],s[123],s[124],s[125],s[126],s[127],s[128],s[129],s[130],s[131],"
    print(s)
    
    # query = send_query("call user_input("+s_str + str(location) + "," + str(date) + "," + str(duration) + "," + str(distance) + ");")

    procedure_name = "user_input"

    cnx = connect_to_mysql()
    cursor = cnx.cursor()



    s = tuple(s) + ("ST_GeomFromText(POINT(73.199394, 59.865848))", date, duration, distance)


    cursor.callproc(procedure_name, s)

    
    query = cursor.stored_results()

    for result in query:
        for row in result.fetchall():
            print(row)



    if (query == None):
        return ["This is a very healthy neighborhood! No information on symptoms in the area."]

    return query

def get_top_five_symptoms(user_location, input_date, duration, distance):
    query = """
    with symptom_list as (
				SELECT *
				FROM User_Queries
				WHERE 2 * 6371 * ASIN(SQRT((1-COS(ST_Y(""" + user_location + """)-ST_Y(location))+COS(ST_Y(""" + user_location + """))*COS(ST_Y(location))*(1-COS(ST_X(""" + user_location + """)-ST_X(location))))/2)) <= """ + str(distance) + """ 
                -- distance calculated using Haversine formula in km, latitude is y and longitude is x
				AND ABS("""+ input_date +""" - date) <= """+ str(duration) + """) 
			
			SELECT symptom , count(symptom) AS occurrence
				from (
					select 'itching' as symptom from symptom_list where symptom_list.itching = 1 union all select 'skin_rash' as symptom from symptom_list where symptom_list.skin_rash = 1 union all select 'nodal_skin_eruptions' as symptom from symptom_list where symptom_list.nodal_skin_eruptions = 1 union all select 'continuous_sneezing' as symptom from symptom_list where symptom_list.continuous_sneezing = 1 union all select 'shivering' as symptom from symptom_list where symptom_list.shivering = 1 union all select 'chills' as symptom from symptom_list where symptom_list.chills = 1 union all select 'joint_pain' as symptom from symptom_list where symptom_list.joint_pain = 1 union all select 'stomach_pain' as symptom from symptom_list where symptom_list.stomach_pain = 1 union all select 'acidity' as symptom from symptom_list where symptom_list.acidity = 1 union all select 'ulcers_on_tongue' as symptom from symptom_list where symptom_list.ulcers_on_tongue = 1 union all select 'muscle_wasting' as symptom from symptom_list where symptom_list.muscle_wasting = 1 union all select 'vomiting' as symptom from symptom_list where symptom_list.vomiting = 1 union all select 'burning_micturition' as symptom from symptom_list where symptom_list.burning_micturition = 1 union all select 'spotting_urination' as symptom from symptom_list where symptom_list.spotting_urination = 1 union all select 'fatigue' as symptom from symptom_list where symptom_list.fatigue = 1 union all select 'weight_gain' as symptom from symptom_list where symptom_list.weight_gain = 1 union all select 'anxiety' as symptom from symptom_list where symptom_list.anxiety = 1 union all select 'cold_hands_and_feets' as symptom from symptom_list where symptom_list.cold_hands_and_feets = 1 union all select 'mood_swings' as symptom from symptom_list where symptom_list.mood_swings = 1 union all select 'weight_loss' as symptom from symptom_list where symptom_list.weight_loss = 1 union all select 'restlessness' as symptom from symptom_list where symptom_list.restlessness = 1 union all select 'lethargy' as symptom from symptom_list where symptom_list.lethargy = 1 union all select 'patches_in_throat' as symptom from symptom_list where symptom_list.patches_in_throat = 1 union all select 'irregular_sugar_level' as symptom from symptom_list where symptom_list.irregular_sugar_level = 1 union all select 'cough' as symptom from symptom_list where symptom_list.cough = 1 union all select 'high_fever' as symptom from symptom_list where symptom_list.high_fever = 1 union all select 'sunken_eyes' as symptom from symptom_list where symptom_list.sunken_eyes = 1 union all select 'breathlessness' as symptom from symptom_list where symptom_list.breathlessness = 1 union all select 'sweating' as symptom from symptom_list where symptom_list.sweating = 1 union all select 'dehydration' as symptom from symptom_list where symptom_list.dehydration = 1 union all select 'indigestion' as symptom from symptom_list where symptom_list.indigestion = 1 union all select 'headache' as symptom from symptom_list where symptom_list.headache = 1 union all select 'yellowish_skin' as symptom from symptom_list where symptom_list.yellowish_skin = 1 union all select 'dark_urine' as symptom from symptom_list where symptom_list.dark_urine = 1 union all select 'nausea' as symptom from symptom_list where symptom_list.nausea = 1 union all select 'loss_of_appetite' as symptom from symptom_list where symptom_list.loss_of_appetite = 1 union all select 'pain_behind_the_eyes' as symptom from symptom_list where symptom_list.pain_behind_the_eyes = 1 union all select 'back_pain' as symptom from symptom_list where symptom_list.back_pain = 1 union all select 'constipation' as symptom from symptom_list where symptom_list.constipation = 1 union all select 'abdominal_pain' as symptom from symptom_list where symptom_list.abdominal_pain = 1 union all select 'diarrhoea' as symptom from symptom_list where symptom_list.diarrhoea = 1 union all select 'mild_fever' as symptom from symptom_list where symptom_list.mild_fever = 1 union all select 'yellow_urine' as symptom from symptom_list where symptom_list.yellow_urine = 1 union all select 'yellowing_of_eyes' as symptom from symptom_list where symptom_list.yellowing_of_eyes = 1 union all select 'acute_liver_failure' as symptom from symptom_list where symptom_list.acute_liver_failure = 1 union all select 'fluid_overload' as symptom from symptom_list where symptom_list.fluid_overload = 1 union all select 'swelling_of_stomach' as symptom from symptom_list where symptom_list.swelling_of_stomach = 1 union all select 'swelled_lymph_nodes' as symptom from symptom_list where symptom_list.swelled_lymph_nodes = 1 union all select 'malaise' as symptom from symptom_list where symptom_list.malaise = 1 union all select 'blurred_and_distorted_vision' as symptom from symptom_list where symptom_list.blurred_and_distorted_vision = 1 union all select 'phlegm' as symptom from symptom_list where symptom_list.phlegm = 1 union all select 'throat_irritation' as symptom from symptom_list where symptom_list.throat_irritation = 1 union all select 'redness_of_eyes' as symptom from symptom_list where symptom_list.redness_of_eyes = 1 union all select 'sinus_pressure' as symptom from symptom_list where symptom_list.sinus_pressure = 1 union all select 'runny_nose' as symptom from symptom_list where symptom_list.runny_nose = 1 union all select 'congestion' as symptom from symptom_list where symptom_list.congestion = 1 union all select 'chest_pain' as symptom from symptom_list where symptom_list.chest_pain = 1 union all select 'weakness_in_limbs' as symptom from symptom_list where symptom_list.weakness_in_limbs = 1 union all select 'fast_heart_rate' as symptom from symptom_list where symptom_list.fast_heart_rate = 1 union all select 'pain_during_bowel_movements' as symptom from symptom_list where symptom_list.pain_during_bowel_movements = 1 union all select 'pain_in_anal_region' as symptom from symptom_list where symptom_list.pain_in_anal_region = 1 union all select 'bloody_stool' as symptom from symptom_list where symptom_list.bloody_stool = 1 union all select 'irritation_in_anus' as symptom from symptom_list where symptom_list.irritation_in_anus = 1 union all select 'neck_pain' as symptom from symptom_list where symptom_list.neck_pain = 1 union all select 'dizziness' as symptom from symptom_list where symptom_list.dizziness = 1 union all select 'cramps' as symptom from symptom_list where symptom_list.cramps = 1 union all select 'bruising' as symptom from symptom_list where symptom_list.bruising = 1 union all select 'obesity' as symptom from symptom_list where symptom_list.obesity = 1 union all select 'swollen_legs' as symptom from symptom_list where symptom_list.swollen_legs = 1 union all select 'swollen_blood_vessels' as symptom from symptom_list where symptom_list.swollen_blood_vessels = 1 union all select 'puffy_face_and_eyes' as symptom from symptom_list where symptom_list.puffy_face_and_eyes = 1 union all select 'enlarged_thyroid' as symptom from symptom_list where symptom_list.enlarged_thyroid = 1 union all select 'brittle_nails' as symptom from symptom_list where symptom_list.brittle_nails = 1 union all select 'swollen_extremeties' as symptom from symptom_list where symptom_list.swollen_extremeties = 1 union all select 'excessive_hunger' as symptom from symptom_list where symptom_list.excessive_hunger = 1 union all select 'extra_marital_contacts' as symptom from symptom_list where symptom_list.extra_marital_contacts = 1 union all select 'drying_and_tingling_lips' as symptom from symptom_list where symptom_list.drying_and_tingling_lips = 1 union all select 'slurred_speech' as symptom from symptom_list where symptom_list.slurred_speech = 1 union all select 'knee_pain' as symptom from symptom_list where symptom_list.knee_pain = 1 union all select 'hip_joint_pain' as symptom from symptom_list where symptom_list.hip_joint_pain = 1 union all select 'muscle_weakness' as symptom from symptom_list where symptom_list.muscle_weakness = 1 union all select 'stiff_neck' as symptom from symptom_list where symptom_list.stiff_neck = 1 union all select 'swelling_joints' as symptom from symptom_list where symptom_list.swelling_joints = 1 union all select 'movement_stiffness' as symptom from symptom_list where symptom_list.movement_stiffness = 1 union all select 'spinning_movements' as symptom from symptom_list where symptom_list.spinning_movements = 1 union all select 'loss_of_balance' as symptom from symptom_list where symptom_list.loss_of_balance = 1 union all select 'unsteadiness' as symptom from symptom_list where symptom_list.unsteadiness = 1 union all select 'weakness_of_one_body_side' as symptom from symptom_list where symptom_list.weakness_of_one_body_side = 1 union all select 'loss_of_smell' as symptom from symptom_list where symptom_list.loss_of_smell = 1 union all select 'bladder_discomfort' as symptom from symptom_list where symptom_list.bladder_discomfort = 1 union all select 'foul_smell_of_urine' as symptom from symptom_list where symptom_list.foul_smell_of_urine = 1 union all select 'continuous_feel_of_urine' as symptom from symptom_list where symptom_list.continuous_feel_of_urine = 1 union all select 'passage_of_gases' as symptom from symptom_list where symptom_list.passage_of_gases = 1 union all select 'internal_itching' as symptom from symptom_list where symptom_list.internal_itching = 1 union all select 'toxic_look_typhos' as symptom from symptom_list where symptom_list.toxic_look_typhos = 1 union all select 'depression' as symptom from symptom_list where symptom_list.depression = 1 union all select 'irritability' as symptom from symptom_list where symptom_list.irritability = 1 union all select 'muscle_pain' as symptom from symptom_list where symptom_list.muscle_pain = 1 union all select 'altered_sensorium' as symptom from symptom_list where symptom_list.altered_sensorium = 1 union all select 'red_spots_over_body' as symptom from symptom_list where symptom_list.red_spots_over_body = 1 union all select 'belly_pain' as symptom from symptom_list where symptom_list.belly_pain = 1 union all select 'abnormal_menstruation' as symptom from symptom_list where symptom_list.abnormal_menstruation = 1 union all select 'dischromic_patches' as symptom from symptom_list where symptom_list.dischromic_patches = 1 union all select 'watering_from_eyes' as symptom from symptom_list where symptom_list.watering_from_eyes = 1 union all select 'increased_appetite' as symptom from symptom_list where symptom_list.increased_appetite = 1 union all select 'polyuria' as symptom from symptom_list where symptom_list.polyuria = 1 union all select 'family_history' as symptom from symptom_list where symptom_list.family_history = 1 union all select 'mucoid_sputum' as symptom from symptom_list where symptom_list.mucoid_sputum = 1 union all select 'rusty_sputum' as symptom from symptom_list where symptom_list.rusty_sputum = 1 union all select 'lack_of_concentration' as symptom from symptom_list where symptom_list.lack_of_concentration = 1 union all select 'visual_disturbances' as symptom from symptom_list where symptom_list.visual_disturbances = 1 union all select 'receiving_blood_transfusion' as symptom from symptom_list where symptom_list.receiving_blood_transfusion = 1 union all select 'receiving_unsterile_injections' as symptom from symptom_list where symptom_list.receiving_unsterile_injections = 1 union all select 'coma' as symptom from symptom_list where symptom_list.coma = 1 union all select 'stomach_bleeding' as symptom from symptom_list where symptom_list.stomach_bleeding = 1 union all select 'distention_of_abdomen' as symptom from symptom_list where symptom_list.distention_of_abdomen = 1 union all select 'history_of_alcohol_consumption' as symptom from symptom_list where symptom_list.history_of_alcohol_consumption = 1 union all select 'blood_in_sputum' as symptom from symptom_list where symptom_list.blood_in_sputum = 1 union all select 'prominent_veins_on_calf' as symptom from symptom_list where symptom_list.prominent_veins_on_calf = 1 union all select 'palpitations' as symptom from symptom_list where symptom_list.palpitations = 1 union all select 'painful_walking' as symptom from symptom_list where symptom_list.painful_walking = 1 union all select 'pus_filled_pimples' as symptom from symptom_list where symptom_list.pus_filled_pimples = 1 union all select 'blackheads' as symptom from symptom_list where symptom_list.blackheads = 1 union all select 'scurring' as symptom from symptom_list where symptom_list.scurring = 1 union all select 'skin_peeling' as symptom from symptom_list where symptom_list.skin_peeling = 1 union all select 'silver_like_dusting' as symptom from symptom_list where symptom_list.silver_like_dusting = 1 union all select 'small_dents_in_nails' as symptom from symptom_list where symptom_list.small_dents_in_nails = 1 union all select 'inflammatory_nails' as symptom from symptom_list where symptom_list.inflammatory_nails = 1 union all select 'blister' as symptom from symptom_list where symptom_list.blister = 1 union all select 'ed_sore_around_nose' as symptom from symptom_list where symptom_list.ed_sore_around_nose = 1 union all select 'yellow_crust_ooze' as symptom from symptom_list where symptom_list.yellow_crust_ooze = 1 
                    ) as temp
					group by symptom
					ORDER BY occurrence DESC, symptom
					LIMIT 5
"""
    

    print("Complete SQL Query:", query)

    output = send_query(query)

    print(output)
    
    # print ("hdhfwodhwfo           " + output + "                  nkdvjerkf")

    if (output == None):
        return "HEALTHY NEIGHBOURHOOD!"

    return output




# Drugs and Drug relations
def get_combined_drug_information(medical_condition):
    query = "SELECT drug_name, medical_condition, sideEffect0, sideEffect1, sideEffect2, rating, pregnancy_category, alcohol FROM Combined_Drugs_SE WHERE " 
    + medical_condition + "IN (SELECT name FROM Diseases)"

    return send_query(query)

# Diseases
def get_diseases():
    query = "select * from Diseases;"
    return send_query(query)[0][1:]

#Create Drug reviews
# This already exists below??
def get_drug_reviews_diff(drug_name):
    query = """SELECT uniqueID, LOWER(drugName), condition_, review, rating, date_, usefulCount
    FROM Temp_DrugsReview 
    WHERE""" + drug_name + """IN (SELECT Drugs.name FROM Drugs);"""
    return send_query(query)
    


#========================================================================================================================

def get_disease_information(disease_name):
    query = "SELECT * FROM Diseases WHERE name = '" + disease_name + "'"

    res = send_query(query)
    if res == None:
        return "No information found for " + disease_name
    
    final_res = []
    final_res.append("About: " + res[0][1])
    precautions = "Precautions: "
    for i in range(2, len(res[0])):
        precautions += str(res[0][i])

        if i < len(res[0]) - 1:
            precautions += ", "
        if i == len(res[0]) - 2:
            precautions += "and "

    final_res.append(precautions)

    return final_res

def get_top_five_drugs(disease_name):
    query = "SELECT name, rating FROM Drugs WHERE disease = '" + disease_name + "' ORDER BY rating DESC LIMIT 5"

    res = send_query(query)
    if res == None:
        return "No information found for " + disease_name
    
    final_res = []
    for i in range(len(res)):
        final_res.append(
            res[i][0] + ": " + str(res[i][1])
        )

    return final_res

def get_symptom_percentages(suggested_disease):
    query = """
        SELECT AVG(avg_ratio) AS average_ratio
	    FROM (
            SELECT SUM(case WHEN s1.itching = 1 AND s2.itching = 1 THEN 1 WHEN s1.skin_rash = 1 AND s2.skin_rash = 1 THEN 1 WHEN s1.nodal_skin_eruptions = 1 AND s2.nodal_skin_eruptions = 1 THEN 1 WHEN s1.continuous_sneezing = 1 AND s2.continuous_sneezing = 1 THEN 1 WHEN s1.shivering = 1 AND s2.shivering = 1 THEN 1 WHEN s1.chills = 1 AND s2.chills = 1 THEN 1 WHEN s1.joint_pain = 1 AND s2.joint_pain = 1 THEN 1 WHEN s1.stomach_pain = 1 AND s2.stomach_pain = 1 THEN 1 WHEN s1.acidity = 1 AND s2.acidity = 1 THEN 1 WHEN s1.ulcers_on_tongue = 1 AND s2.ulcers_on_tongue = 1 THEN 1 WHEN s1.muscle_wasting = 1 AND s2.muscle_wasting = 1 THEN 1 WHEN s1.vomiting = 1 AND s2.vomiting = 1 THEN 1 WHEN s1.burning_micturition = 1 AND s2.burning_micturition = 1 THEN 1 WHEN s1.spotting_urination = 1 AND s2.spotting_urination = 1 THEN 1 WHEN s1.fatigue = 1 AND s2.fatigue = 1 THEN 1 WHEN s1.weight_gain = 1 AND s2.weight_gain = 1 THEN 1 WHEN s1.anxiety = 1 AND s2.anxiety = 1 THEN 1 WHEN s1.cold_hands_and_feets = 1 AND s2.cold_hands_and_feets = 1 THEN 1 WHEN s1.mood_swings = 1 AND s2.mood_swings = 1 THEN 1 WHEN s1.weight_loss = 1 AND s2.weight_loss = 1 THEN 1 WHEN s1.restlessness = 1 AND s2.restlessness = 1 THEN 1 WHEN s1.lethargy = 1 AND s2.lethargy = 1 THEN 1 WHEN s1.patches_in_throat = 1 AND s2.patches_in_throat = 1 THEN 1 WHEN s1.irregular_sugar_level = 1 AND s2.irregular_sugar_level = 1 THEN 1 WHEN s1.cough = 1 AND s2.cough = 1 THEN 1 WHEN s1.high_fever = 1 AND s2.high_fever = 1 THEN 1 WHEN s1.sunken_eyes = 1 AND s2.sunken_eyes = 1 THEN 1 WHEN s1.breathlessness = 1 AND s2.breathlessness = 1 THEN 1 WHEN s1.sweating = 1 AND s2.sweating = 1 THEN 1 WHEN s1.dehydration = 1 AND s2.dehydration = 1 THEN 1 WHEN s1.indigestion = 1 AND s2.indigestion = 1 THEN 1 WHEN s1.headache = 1 AND s2.headache = 1 THEN 1 WHEN s1.yellowish_skin = 1 AND s2.yellowish_skin = 1 THEN 1 WHEN s1.dark_urine = 1 AND s2.dark_urine = 1 THEN 1 WHEN s1.nausea = 1 AND s2.nausea = 1 THEN 1 WHEN s1.loss_of_appetite = 1 AND s2.loss_of_appetite = 1 THEN 1 WHEN s1.pain_behind_the_eyes = 1 AND s2.pain_behind_the_eyes = 1 THEN 1 WHEN s1.back_pain = 1 AND s2.back_pain = 1 THEN 1 WHEN s1.constipation = 1 AND s2.constipation = 1 THEN 1 WHEN s1.abdominal_pain = 1 AND s2.abdominal_pain = 1 THEN 1 WHEN s1.diarrhoea = 1 AND s2.diarrhoea = 1 THEN 1 WHEN s1.mild_fever = 1 AND s2.mild_fever = 1 THEN 1 WHEN s1.yellow_urine = 1 AND s2.yellow_urine = 1 THEN 1 WHEN s1.yellowing_of_eyes = 1 AND s2.yellowing_of_eyes = 1 THEN 1 WHEN s1.acute_liver_failure = 1 AND s2.acute_liver_failure = 1 THEN 1 WHEN s1.fluid_overload = 1 AND s2.fluid_overload = 1 THEN 1 WHEN s1.swelling_of_stomach = 1 AND s2.swelling_of_stomach = 1 THEN 1 WHEN s1.swelled_lymph_nodes = 1 AND s2.swelled_lymph_nodes = 1 THEN 1 WHEN s1.malaise = 1 AND s2.malaise = 1 THEN 1 WHEN s1.blurred_and_distorted_vision = 1 AND s2.blurred_and_distorted_vision = 1 THEN 1 WHEN s1.phlegm = 1 AND s2.phlegm = 1 THEN 1 WHEN s1.throat_irritation = 1 AND s2.throat_irritation = 1 THEN 1 WHEN s1.redness_of_eyes = 1 AND s2.redness_of_eyes = 1 THEN 1 WHEN s1.sinus_pressure = 1 AND s2.sinus_pressure = 1 THEN 1 WHEN s1.runny_nose = 1 AND s2.runny_nose = 1 THEN 1 WHEN s1.congestion = 1 AND s2.congestion = 1 THEN 1 WHEN s1.chest_pain = 1 AND s2.chest_pain = 1 THEN 1 WHEN s1.weakness_in_limbs = 1 AND s2.weakness_in_limbs = 1 THEN 1 WHEN s1.fast_heart_rate = 1 AND s2.fast_heart_rate = 1 THEN 1 WHEN s1.pain_during_bowel_movements = 1 AND s2.pain_during_bowel_movements = 1 THEN 1 WHEN s1.pain_in_anal_region = 1 AND s2.pain_in_anal_region = 1 THEN 1 WHEN s1.bloody_stool = 1 AND s2.bloody_stool = 1 THEN 1 WHEN s1.irritation_in_anus = 1 AND s2.irritation_in_anus = 1 THEN 1 WHEN s1.neck_pain = 1 AND s2.neck_pain = 1 THEN 1 WHEN s1.dizziness = 1 AND s2.dizziness = 1 THEN 1 WHEN s1.cramps = 1 AND s2.cramps = 1 THEN 1 WHEN s1.bruising = 1 AND s2.bruising = 1 THEN 1 WHEN s1.obesity = 1 AND s2.obesity = 1 THEN 1 WHEN s1.swollen_legs = 1 AND s2.swollen_legs = 1 THEN 1 WHEN s1.swollen_blood_vessels = 1 AND s2.swollen_blood_vessels = 1 THEN 1 WHEN s1.puffy_face_and_eyes = 1 AND s2.puffy_face_and_eyes = 1 THEN 1 WHEN s1.enlarged_thyroid = 1 AND s2.enlarged_thyroid = 1 THEN 1 WHEN s1.brittle_nails = 1 AND s2.brittle_nails = 1 THEN 1 WHEN s1.swollen_extremeties = 1 AND s2.swollen_extremeties = 1 THEN 1 WHEN s1.excessive_hunger = 1 AND s2.excessive_hunger = 1 THEN 1 WHEN s1.extra_marital_contacts = 1 AND s2.extra_marital_contacts = 1 THEN 1 WHEN s1.drying_and_tingling_lips = 1 AND s2.drying_and_tingling_lips = 1 THEN 1 WHEN s1.slurred_speech = 1 AND s2.slurred_speech = 1 THEN 1 WHEN s1.knee_pain = 1 AND s2.knee_pain = 1 THEN 1 WHEN s1.hip_joint_pain = 1 AND s2.hip_joint_pain = 1 THEN 1 WHEN s1.muscle_weakness = 1 AND s2.muscle_weakness = 1 THEN 1 WHEN s1.stiff_neck = 1 AND s2.stiff_neck = 1 THEN 1 WHEN s1.swelling_joints = 1 AND s2.swelling_joints = 1 THEN 1 WHEN s1.movement_stiffness = 1 AND s2.movement_stiffness = 1 THEN 1 WHEN s1.spinning_movements = 1 AND s2.spinning_movements = 1 THEN 1 WHEN s1.loss_of_balance = 1 AND s2.loss_of_balance = 1 THEN 1 WHEN s1.unsteadiness = 1 AND s2.unsteadiness = 1 THEN 1 WHEN s1.weakness_of_one_body_side = 1 AND s2.weakness_of_one_body_side = 1 THEN 1 WHEN s1.loss_of_smell = 1 AND s2.loss_of_smell = 1 THEN 1 WHEN s1.bladder_discomfort = 1 AND s2.bladder_discomfort = 1 THEN 1 WHEN s1.foul_smell_of_urine = 1 AND s2.foul_smell_of_urine = 1 THEN 1 WHEN s1.continuous_feel_of_urine = 1 AND s2.continuous_feel_of_urine = 1 THEN 1 WHEN s1.passage_of_gases = 1 AND s2.passage_of_gases = 1 THEN 1 WHEN s1.internal_itching = 1 AND s2.internal_itching = 1 THEN 1 WHEN s1.toxic_look_typhos = 1 AND s2.toxic_look_typhos = 1 THEN 1 WHEN s1.depression = 1 AND s2.depression = 1 THEN 1 WHEN s1.irritability = 1 AND s2.irritability = 1 THEN 1 WHEN s1.muscle_pain = 1 AND s2.muscle_pain = 1 THEN 1 WHEN s1.altered_sensorium = 1 AND s2.altered_sensorium = 1 THEN 1 WHEN s1.red_spots_over_body = 1 AND s2.red_spots_over_body = 1 THEN 1 WHEN s1.belly_pain = 1 AND s2.belly_pain = 1 THEN 1 WHEN s1.abnormal_menstruation = 1 AND s2.abnormal_menstruation = 1 THEN 1 WHEN s1.dischromic_patches = 1 AND s2.dischromic_patches = 1 THEN 1 WHEN s1.watering_from_eyes = 1 AND s2.watering_from_eyes = 1 THEN 1 WHEN s1.increased_appetite = 1 AND s2.increased_appetite = 1 THEN 1 WHEN s1.polyuria = 1 AND s2.polyuria = 1 THEN 1 WHEN s1.family_history = 1 AND s2.family_history = 1 THEN 1 WHEN s1.mucoid_sputum = 1 AND s2.mucoid_sputum = 1 THEN 1 WHEN s1.rusty_sputum = 1 AND s2.rusty_sputum = 1 THEN 1 WHEN s1.lack_of_concentration = 1 AND s2.lack_of_concentration = 1 THEN 1 WHEN s1.visual_disturbances = 1 AND s2.visual_disturbances = 1 THEN 1 WHEN s1.receiving_blood_transfusion = 1 AND s2.receiving_blood_transfusion = 1 THEN 1 WHEN s1.receiving_unsterile_injections = 1 AND s2.receiving_unsterile_injections = 1 THEN 1 WHEN s1.coma = 1 AND s2.coma = 1 THEN 1 WHEN s1.stomach_bleeding = 1 AND s2.stomach_bleeding = 1 THEN 1 WHEN s1.distention_of_abdomen = 1 AND s2.distention_of_abdomen = 1 THEN 1 WHEN s1.history_of_alcohol_consumption = 1 AND s2.history_of_alcohol_consumption = 1 THEN 1 WHEN s1.blood_in_sputum = 1 AND s2.blood_in_sputum = 1 THEN 1 WHEN s1.prominent_veins_on_calf = 1 AND s2.prominent_veins_on_calf = 1 THEN 1 WHEN s1.palpitations = 1 AND s2.palpitations = 1 THEN 1 WHEN s1.painful_walking = 1 AND s2.painful_walking = 1 THEN 1 WHEN s1.pus_filled_pimples = 1 AND s2.pus_filled_pimples = 1 THEN 1 WHEN s1.blackheads = 1 AND s2.blackheads = 1 THEN 1 WHEN s1.scurring = 1 AND s2.scurring = 1 THEN 1 WHEN s1.skin_peeling = 1 AND s2.skin_peeling = 1 THEN 1 WHEN s1.silver_like_dusting = 1 AND s2.silver_like_dusting = 1 THEN 1 WHEN s1.small_dents_in_nails = 1 AND s2.small_dents_in_nails = 1 THEN 1 WHEN s1.inflammatory_nails = 1 AND s2.inflammatory_nails = 1 THEN 1 WHEN s1.blister = 1 AND s2.blister = 1 THEN 1 WHEN s1.ed_sore_around_nose = 1 AND s2.ed_sore_around_nose = 1 THEN 1 WHEN s1.yellow_crust_ooze = 1 AND s2.yellow_crust_ooze = 1 THEN 1 ELSE 0 END) / COUNT(*) AS avg_ratio
            FROM (
                SELECT itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, chills, joint_pain, stomach_pain, acidity, ulcers_on_tongue, muscle_wasting, vomiting, burning_micturition, spotting_urination, fatigue, weight_gain, anxiety, cold_hands_and_feets, mood_swings, weight_loss, restlessness, lethargy, patches_in_throat, irregular_sugar_level, cough, high_fever, sunken_eyes, breathlessness, sweating, dehydration, indigestion, headache, yellowish_skin, dark_urine, nausea, loss_of_appetite, pain_behind_the_eyes, back_pain, constipation, abdominal_pain, diarrhoea, mild_fever, yellow_urine, yellowing_of_eyes, acute_liver_failure, fluid_overload, swelling_of_stomach, swelled_lymph_nodes, malaise, blurred_and_distorted_vision, phlegm, throat_irritation, redness_of_eyes, sinus_pressure, runny_nose, congestion, chest_pain, weakness_in_limbs, fast_heart_rate, pain_during_bowel_movements, pain_in_anal_region, bloody_stool, irritation_in_anus, neck_pain, dizziness, cramps, bruising, obesity, swollen_legs, swollen_blood_vessels, puffy_face_and_eyes, enlarged_thyroid, brittle_nails, swollen_extremeties, excessive_hunger, extra_marital_contacts, drying_and_tingling_lips, slurred_speech, knee_pain, hip_joint_pain, muscle_weakness, stiff_neck, swelling_joints, movement_stiffness, spinning_movements, loss_of_balance, unsteadiness, weakness_of_one_body_side, loss_of_smell, bladder_discomfort, foul_smell_of_urine, continuous_feel_of_urine, passage_of_gases, internal_itching, toxic_look_typhos, depression, irritability, muscle_pain, altered_sensorium, red_spots_over_body, belly_pain, abnormal_menstruation, dischromic_patches, watering_from_eyes, increased_appetite, polyuria, family_history, mucoid_sputum, rusty_sputum, lack_of_concentration, visual_disturbances, receiving_blood_transfusion, receiving_unsterile_injections, coma, stomach_bleeding, distention_of_abdomen, history_of_alcohol_consumption, blood_in_sputum, prominent_veins_on_calf, palpitations, painful_walking, pus_filled_pimples, blackheads, scurring, skin_peeling, silver_like_dusting, small_dents_in_nails, inflammatory_nails, blister, ed_sore_around_nose, yellow_crust_ooze
                FROM Symptoms
                WHERE disease = '""" + suggested_disease + """'
            ) AS s1
            CROSS JOIN (
                SELECT itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, chills, joint_pain, stomach_pain, acidity, ulcers_on_tongue, muscle_wasting, vomiting, burning_micturition, spotting_urination, fatigue, weight_gain, anxiety, cold_hands_and_feets, mood_swings, weight_loss, restlessness, lethargy, patches_in_throat, irregular_sugar_level, cough, high_fever, sunken_eyes, breathlessness, sweating, dehydration, indigestion, headache, yellowish_skin, dark_urine, nausea, loss_of_appetite, pain_behind_the_eyes, back_pain, constipation, abdominal_pain, diarrhoea, mild_fever, yellow_urine, yellowing_of_eyes, acute_liver_failure, fluid_overload, swelling_of_stomach, swelled_lymph_nodes, malaise, blurred_and_distorted_vision, phlegm, throat_irritation, redness_of_eyes, sinus_pressure, runny_nose, congestion, chest_pain, weakness_in_limbs, fast_heart_rate, pain_during_bowel_movements, pain_in_anal_region, bloody_stool, irritation_in_anus, neck_pain, dizziness, cramps, bruising, obesity, swollen_legs, swollen_blood_vessels, puffy_face_and_eyes, enlarged_thyroid, brittle_nails, swollen_extremeties, excessive_hunger, extra_marital_contacts, drying_and_tingling_lips, slurred_speech, knee_pain, hip_joint_pain, muscle_weakness, stiff_neck, swelling_joints, movement_stiffness, spinning_movements, loss_of_balance, unsteadiness, weakness_of_one_body_side, loss_of_smell, bladder_discomfort, foul_smell_of_urine, continuous_feel_of_urine, passage_of_gases, internal_itching, toxic_look_typhos, depression, irritability, muscle_pain, altered_sensorium, red_spots_over_body, belly_pain, abnormal_menstruation, dischromic_patches, watering_from_eyes, increased_appetite, polyuria, family_history, mucoid_sputum, rusty_sputum, lack_of_concentration, visual_disturbances, receiving_blood_transfusion, receiving_unsterile_injections, coma, stomach_bleeding, distention_of_abdomen, history_of_alcohol_consumption, blood_in_sputum, prominent_veins_on_calf, palpitations, painful_walking, pus_filled_pimples, blackheads, scurring, skin_peeling, silver_like_dusting, small_dents_in_nails, inflammatory_nails, blister, ed_sore_around_nose, yellow_crust_ooze
                FROM Symptoms
            ) AS s2
        ) AS s;
    """

    res = send_query(query)
    if res == None:
        return "No information found for " + suggested_disease
    
    return "Percentage: " + str(float(res[0][0])) + "%"

def get_substitute_drugs(drug_name):
    query = """SELECT drug2 FROM Drug_Relations WHERE drug1 = '""" + drug_name + """' UNION SELECT drug1 FROM Drug_Relations WHERE drug2 = '""" + drug_name + "'"

    res = send_query(query)
    if res == None:
        return "No information found for " + drug_name
    
    final_res = []
    for i in range(min(len(res), 5)):
        final_res.append(res[i][0])
    
    return final_res

def get_drug_information(drug_name):
    query = "SELECT * FROM Drugs WHERE name = '" + drug_name + "'"

    res = send_query(query)
    if res == None:
        return "No information found for " + drug_name
    
    final_res = []
    final_res.append("Drug: " + res[0][0])
    side_effects = "Side Effects: "
    for i in range(1, 4):
        if res[0][i] == None:
            continue

        side_effects += str(res[0][i])

        if i < 4 - 1:
            side_effects += ", "
        if i == 4 - 2:
            side_effects += "and "
    
    final_res.append(side_effects)
    final_res.append("Rating: " + str(res[0][4]))
    final_res.append("Pregnancy Category: " + str(res[0][5]))
    final_res.append("Alcohol: " + str(res[0][6]))

    return final_res

def get_drug_reviews(drug_name):
    query = "SELECT * FROM Drugs_Reviews WHERE drugName = '" + drug_name + "'"

    res = send_query(query)
    if res == None:
        return "No information found for " + drug_name
    
    final_res = []
    for i in range(1, min(5, len(res))):
        final_res.append(
            "Drug: " + res[i][1] + ", Condition: " + res[i][2] + ", Review: " + str(res[i][3]) + ", Rating: " + str(res[i][4]) + ", Date: " + str(res[i][5]) + ", Useful Count: " + str(res[i][6])
        )
    
    return final_res

def get_special_rating(): # helper query
    query = """
        SELECT name, (0.7*AVG(usefulCount) + 0.3*AVG(rating))
        FROM Drugs LEFT JOIN Drugs_Reviews ON name = drugName
        GROUP BY name
    """

    res = send_query(query)
    if res == None:
        return "No information found"

    return res
#=========================================================================================================



def prediction(data, model, disease, symptoms):
    result = []
    for i in range(0,len(symptoms)):
        result.append(0)

    for i in range(0,len(symptoms)):
        for k in data:
            if(k == symptoms[i]):
                result[i]=1

    labels = [result]

    predict = model.predict(labels)
    predicted = predict[0]

    done = 'no'
    for a in range(0, len(disease)):
        if(predicted == a):
            done = 'yes'
            break

    if (done == 'yes'):
        return disease[a]
    else:
        return "Not Found"

def get_suggested_disease(symptoms_list):
    symptoms_list = symptoms_list.split(',')
    with open('forest.pkl', 'rb') as f:
        forest = pickle.load(f)
    
    #List of the symptoms.
    symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']

    disease= ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        'Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']
    
    return prediction(symptoms_list, forest, disease, symptoms)