from http.client import OK
from sklearn import tree
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

#Importing Libraries to perform calculations
import numpy as np
import pandas as pd
import os

#List of the symptoms is listed here in list l1.
class Prediction():
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze']

    #List of Diseases is listed in list disease.

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']

    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    print(l2)


    #Reading the training .csv file
    df=pd.read_csv("dataset/training.csv")

    #Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

    #printing the top 5 rows of the training dataset
    df.head()

    #plotPerColumnDistribution(df, 10, 5)

    X= df[l1]
    y = df[["prognosis"]]
    np.ravel(y)
    """print(X)

    print(y)"""

    #Reading the  testing.csv file
    tr=pd.read_csv("dataset/testing.csv")
    #Using inbuilt function replace in pandas for replacing the values

    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

    #printing the top 5 rows of the testing data
    tr.head()

    X_test= tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)
    #print(X_test)

    #print(y_test)

   
    """**Decision Tree Algorithm**"""


    def DecisionTree( self,name, psymptoms):
        prediction=""
        print(name)

        clf3 = tree.DecisionTreeClassifier() 
        clf3 = clf3.fit(self.X,self.y)

        y_pred=clf3.predict(self.X_test)
        print("Decision Tree")
        print("Accuracy")
        print(accuracy_score(self.y_test, y_pred))
        accuracy= accuracy_score(self.y_test,y_pred)
        print(accuracy_score(self.y_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(self.y_test,y_pred)
        print(conf_matrix)

        #psymptoms = ['constipation','acute_liver_failure','diarrhoea']

        for k in range(0,len(self.l1)):
            for z in psymptoms:
                if(z==self.l1[k]):
                    self.l2[k]=1

        inputtest = [self.l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(self.disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            prediction= " "
            prediction =self.disease[a]
        else:
            prediction= " "
            prediction="Not Found"
        
        print(prediction)
        return prediction, accuracy
