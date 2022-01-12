from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

import joblib
import numpy as np
from supervised.automl import AutoML
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from random import shuffle
import gmpy2
from time import time
from Crypto.Util.number import getPrime
from django.shortcuts import render
from . models import details



def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def int_time():
    return int(round(time() * 1000))

class PrivateKey(object):
    def __init__(self, p, q, n):
        self.p = p
        self.q = q
        self.l = (p-1) * (q-1)
        self.m = gmpy2.invert(self.l, n)  #1/fi(n)
    def __repr__(self):
        return '<PrivateKey: %s %s>' % (self.l, self.m)

class PublicKey(object):

    @classmethod
    def from_n(cls, n):
        return cls(n)
    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1
    def __repr__(self):
        return '<PublicKey: %s>' % self.n

def generate_keypair(bits):
    p_equal_q = True
    while p_equal_q:
        p = getPrime(bits // 2)
        q = getPrime(bits // 2)
        if (p!=q):
            p_equal_q = False
    n = p * q
    return PrivateKey(p, q, n), PublicKey(n)

def encrypt(pub, plain):
    one = gmpy2.mpz(1)
    state = gmpy2.random_state(int_time())
    r = gmpy2.mpz_random(state,pub.n)
    while gmpy2.gcd(r,pub.n) != one:
        state = gmpy2.random_state(int_time())
        r = gmpy2.mpz_random(state,pub.n)
    x = gmpy2.powmod(r,pub.n,pub.n_sq)
    cipher = gmpy2.f_mod(gmpy2.mul(gmpy2.powmod(pub.g,plain,pub.n_sq),x),pub.n_sq)
    return cipher


name = ""
age = ""
weight = ""
sex = ""

pub_key = ""
priv_key = ""



def home(request):
    return render(request,"home.html")

@csrf_exempt
def find_disease(request):
    
    cls = joblib.load("seven_disease.sav")

    disease_code = {2:'Allergy',4:'Diabetes',1:'Jaundice',5:'Hepatitis C',3:'Common Cold',0:'Heart attack',6:'Hypothyroidism'}
    
    disease_page = {'Allergy':'/allergy_severity','Diabetes':'/diabetes_severity','Jaundice':'/jaundice_severity','Common Cold':'/cold_severity'
    ,'Heart attack':'/cardio_severity','Hypothyroidism':'/thyroid_severity','Hepatitis C':'/hepatitis_severity'}
    
    col = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

    l2 = []
    for j in range(0,len(col)):
        l2.append(0)

    input_sym = []
    input_sym.append(request.POST.get('symptom1'))
    input_sym.append(request.POST.get('symptom2'))
    input_sym.append(request.POST.get('symptom3'))
    input_sym.append(request.POST.get('symptom4'))
    input_sym.append(request.POST.get('symptom5'))


    for k in range(0,len(col)):
        for sym in input_sym:
            if(sym == col[k]):
                l2[k]=1

    l2 = [l2]
    sample = np.array(l2)

    print(sample)
    print(len(col))

    predict = cls.predict(sample)
    predicted_sample = predict[0]

    predicted_disease = disease_code[predicted_sample]
    dis_name = disease_page[predicted_disease]
    
    return JsonResponse({'restext':predicted_disease,'name':dis_name},status = 200)


@csrf_exempt
def store_data(request):

    global name,age,sex,weight,priv_key,pub_key
    

    priv_key, pub_key = generate_keypair(100)
    
    name_val = request.POST.get('name_val')
    name = int.from_bytes(name_val.encode('utf-8'), byteorder='big')

    with open("keys.txt", "a") as F:
        string = str(name) + " - " + str(pub_key.n) + '  ' +str(priv_key.p) + '  ' +str(priv_key.q)
        F.write(string + "\n")
    
    age = encrypt(pub_key,int(request.POST.get('age_val')))
    sex = encrypt(pub_key,int(request.POST.get('gender_val')))
    weight = encrypt(pub_key,int(request.POST.get('weight_val')))

    text = "Data submitted"
    
    return JsonResponse({'restext':text},status = 200)

def result(dis, sev):
    obj = details()
    global name,age,sex,weight,pub_key,priv_key
    
    obj.Name=name
    obj.Age=age
    obj.Sex=sex
    obj.Weight=weight

    disease_code = {'Allergy':2,'Diabetes':4,'Jaundice':1,'Hepatitis':5,'Common Cold':3,'Heart attack':0,'Hypothyroidism':6}
    severity_code = {'Benign':0,'Malignant':1}
    
    dis_enc = encrypt(pub_key,disease_code[dis]) 
    sev_enc = encrypt(pub_key,severity_code[sev])
    
    obj.Disease = dis_enc
    obj.Severity = sev_enc
    obj.save()


def cardio_severity(request):
    return render(request,"cardio_severity.html")

@csrf_exempt
def cardio_disease(request):
    
    index = [1]
    col = ['AGE','GENDER','HEIGHT','WEIGHT','AP_HIGH','AP_LOW','CHOLESTEROL','GLUCOSE'	,'SMOKE'	,'ALCOHOL']
   
    cardio_model = joblib.load("dismodels\cardio_model.sav")

    final_input = []
    input = []
    input_enc = []
    
    
    input.append(int(request.POST.get('age_val')))
    input.append(int(request.POST.get('gender_val')))
    input.append(int(request.POST.get('height_val')))
    input.append(int(request.POST.get('weight_val')))
    input.append(int(request.POST.get('sbp_val')))
    input.append(int(request.POST.get('dbp_val')))
    input.append(int(request.POST.get('cho_val')))
    input.append(int(request.POST.get('glucose_val')))
    input.append(int(request.POST.get('smoke_val')))
    input.append(int(request.POST.get('alcohol_val')))

    global priv_key, pub_key

    for i in input:
       input_enc.append(encrypt(pub_key, i))

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = cardio_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Heart attack",t1)

    return JsonResponse({'restext':text},status = 200)

def jaundice_severity(request):
    return render(request,"jaundice_severity.html")

@csrf_exempt
def jaundice_disease(request):

    index = [1]
    col = ['AGE','GENDER','Total_Bilirubin','Direct_Bilirubin',	'Alkaline_Phosphotase',	'Alamine_Aminotransferase',	'Total_Protiens',	'Albumin']

    jaundice_model = joblib.load("dismodels\jaundice_model.sav")
    

    final_input = []
    input = []
    input_enc = []
   
    
    input.append(float(request.POST.get('age_val')))
    input.append(float(request.POST.get('gender_val')))
    input.append(float(request.POST.get('total_bil_val')))
    input.append(float(request.POST.get('direct_bil_val')))
    input.append(float(request.POST.get('alkp_val')))
    input.append(float(request.POST.get('amino_val')))
    input.append(float(request.POST.get('total_pro_val')))
    input.append(float(request.POST.get('albmn_val')))

    global priv_key, pub_key

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = jaundice_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Jaundice",t1)

    return JsonResponse({'restext':text},status = 200)
    

def allergy_severity(request):
    return render(request,"allergy_severity.html")


@csrf_exempt
def allergy_disease(request):

    index = [1]
    col = ['COUGH',	'MUSCLE_ACHES',	'TIREDNESS','SORE_THROAT','RUNNY_NOSE',	'LOSS_OF_TASTE','LOSS_OF_SMELL','SNEEZING','PINK_EYE']
    allergy_model = joblib.load("dismodels\Allergy_model.sav")
    
    final_input = []
    input = []
    input_enc = []
   
    
    input.append(int(request.POST.get('symp1_val')))
    input.append(int(request.POST.get('symp2_val')))
    input.append(int(request.POST.get('symp3_val')))
    input.append(int(request.POST.get('symp4_val')))
    input.append(int(request.POST.get('symp5_val')))
    input.append(int(request.POST.get('symp6_val')))
    input.append(int(request.POST.get('symp7_val')))
    input.append(int(request.POST.get('symp8_val')))
    input.append(int(request.POST.get('symp9_val')))

    global priv_key, pub_key

    for i in input:
       input_enc.append(encrypt(pub_key, i))

    

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = allergy_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Allergy",t1)

    return JsonResponse({'restext':text},status = 200)

def cold_severity(request):
    return render(request,"cold_severity.html")


@csrf_exempt
def cold_disease(request):
    cold_model = joblib.load("dismodels\common_cold_model.sav")

    index = [1]
    col = ['COUGH',	'MUSCLE_ACHES',	'TIREDNESS',	'SORE_THROAT',	'RUNNY_NOSE',	'FEVER',	'LOSS_OF_TASTE',	'LOSS_OF_SMELL',	'SNEEZING']
    
    final_input = []
    input = []
    input_enc = []
    input_dec = []
    
    input.append(int(request.POST.get('symp1_val')))
    input.append(int(request.POST.get('symp2_val')))
    input.append(int(request.POST.get('symp3_val')))
    input.append(int(request.POST.get('symp4_val')))
    input.append(int(request.POST.get('symp5_val')))
    input.append(int(request.POST.get('symp6_val')))
    input.append(int(request.POST.get('symp7_val')))
    input.append(int(request.POST.get('symp8_val')))
    input.append(int(request.POST.get('symp9_val')))

    global priv_key, pub_key

    for i in input:
       input_enc.append(encrypt(pub_key, i))

    

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = cold_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Common Cold",t1)

    return JsonResponse({'restext':text},status = 200)


def diabetes_severity(request):
    return render(request,"diabetes_severity.html")


@csrf_exempt
def diabetes_disease(request):
    diabetes_model = joblib.load("dismodels\diabetes_model.sav")

    index = [1]
    col = ['POLYURIA','POLYDIPSIA','SUDDEN_WEIGHT_LOSS','WEAKNESS','POLYPHAGIA','VISUAL_BLURRING','ITCHING','DELAYED_HEALING','PARTIAL_PARESIS','MUSCLE_STIFFNESS']
    
    final_input = []
    input = []
    input_enc = []
    
    input.append(int(request.POST.get('symp1_val')))
    input.append(int(request.POST.get('symp2_val')))
    input.append(int(request.POST.get('symp3_val')))
    input.append(int(request.POST.get('symp4_val')))
    input.append(int(request.POST.get('symp5_val')))
    input.append(int(request.POST.get('symp6_val')))
    input.append(int(request.POST.get('symp7_val')))
    input.append(int(request.POST.get('symp8_val')))
    input.append(int(request.POST.get('symp9_val')))
    input.append(int(request.POST.get('symp10_val')))

    global priv_key, pub_key

    for i in input:
       input_enc.append(encrypt(pub_key, i))

    
    final_input.append(input)

    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = diabetes_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Diabetes",t1)

    return JsonResponse({'restext':text},status = 200)

def thyroid_severity(request):
    return render(request,"thyroid_severity.html")


@csrf_exempt
def thyroid_disease(request):
    thyroid_model = joblib.load("dismodels\hypothyroid_model.sav")

    index = [1]
    col = ['Age', 'on_thyroxine', 'thyroid_surgery', 'query_hypothyroid', 'query_hyperthyroid', 'sick', 'TT4', 'FTI']
    
    
    final_input = []
    input = []
    input_enc = []
    
    input.append(int(request.POST.get('age_val')))
    input.append(int(request.POST.get('symp1_val')))
    input.append(int(request.POST.get('symp2_val')))
    input.append(int(request.POST.get('symp3_val')))
    input.append(int(request.POST.get('symp4_val')))
    input.append(int(request.POST.get('symp5_val')))
    input.append(int(request.POST.get('tt4_val')))
    input.append(int(request.POST.get('fti_val')))
    
    
    global priv_key, pub_key

    for i in input:
       input_enc.append(encrypt(pub_key, i))

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = thyroid_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Hypothyroidism",t1)

    return JsonResponse({'restext':text},status = 200)

def hepatitis_severity(request):
    return render(request,"hepatitis_severity.html")


@csrf_exempt
def hepatitis_disease(request):
    hepatitis_model = joblib.load("dismodels\hepatitis_model.sav")

    index = [1]
    col = ['AGE','GENDER','TOTAL_BILIRUBIN','DIRECT_BILIRUBIN','ALKALINE_PHOSPHOTASE','ALAMINE_AMINOTRANSFERASE','ASPARTATE_AMINOTRANSFERASE','TOTAL_PROTEINS','ALBUMIN','ALBUMIN_AND_GLOBULIN_RATIO']
    
    final_input = []
    input = []
    input_enc = []
    
    
    input.append(float(request.POST.get('symp1_val')))
    input.append(float(request.POST.get('symp2_val')))
    input.append(float(request.POST.get('symp3_val')))
    input.append(float(request.POST.get('symp4_val')))
    input.append(float(request.POST.get('symp5_val')))
    input.append(float(request.POST.get('symp6_val')))
    input.append(float(request.POST.get('symp7_val')))
    input.append(float(request.POST.get('symp8_val')))
    input.append(float(request.POST.get('symp9_val')))
    input.append(float(request.POST.get('symp10_val')))

    global priv_key, pub_key

    final_input.append(input)
    print(final_input)
    data = np.array(final_input)
    test = pd.DataFrame(data,index,col)

    predict = hepatitis_model.predict_proba(test)
    predicted = predict[0]

    if(predicted[1] > predicted[0]):
        text = "Malignant - Immediate treatment is required"
        t1 = "Malignant"
    else:
        text = "Benign - Beginning stage. Medicines would be sufficient"
        t1 = "Benign"

    result("Hepatitis",t1)

    return JsonResponse({'restext':text},status = 200)


              




