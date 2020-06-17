from flask import Flask,render_template,request
app = Flask(__name__)

import pickle

# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')
model=pickle.load(file)
file.close()

@app.route('/' ,methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        mydict = request.form
        Age = int(mydict['Age'])
        Gender = int(mydict['Gender'])
        body_temperature = float(mydict['body temperature'])
        dry_cough = int(mydict['Dry Cough'])
        sour_throat = int(mydict['sour throat'])
        weakness = int(mydict['weakness'])
        breathing_difficulty = int(mydict['breathing problem'])
        drowsiness = int(mydict['drowsiness'])
        pain_in_chest = int(mydict['pain in chest'])
        travelToinfectedCountry = int(mydict['travelTOinfectedCOUNTRY'])
        diabities = int(mydict['diabetes'])
        heart_disease = int(mydict['heart disease'])
        lung_disease = int(mydict['lung disease'])
        stroke = int(mydict['stroke or reduced immunity'])
        symptompts_progressed = int(mydict['symptoms progressed'])
        high_bp = int(mydict['high blood pressue'])
        kidney_disease = int(mydict['kidney disease'])
        changeINappetite = int(mydict['change in appetide'])
        lossINsmell = int(mydict['Loss of sense of smell'])    
        x = model.predict([[Age,Gender,body_temperature,dry_cough,sour_throat,weakness,breathing_difficulty,drowsiness,pain_in_chest,travelToinfectedCountry,diabities,heart_disease,lung_disease,stroke,symptompts_progressed,high_bp,kidney_disease,changeINappetite,lossINsmell]])
        result=""
        if x>=0.5:
            result="You may be infected. Please go see a doctor."
        else :
            result="You need not worry, you are not infected. But please follow preventive measures."
        print(result)
        return render_template('show.html',y=result)
    return render_template('index.html')
    
    #return 'Hello, World!'+str(prob)

if __name__=="__main__":
    app.run(debug=True)