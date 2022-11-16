from flask import Flask,render_template,request
import numpy as np
import pickle
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        pendapatan_setahun_juta = float(request.form['pendapatan_setahun_juta'])
        durasi_pinjaman_bulan = float(request.form['durasi_pinjaman_bulan'])
        jumlah_tanggungan = float(request.form['jumlah_tanggungan'])
        TIDAK= float(request.form['TIDAK'])
        YA= float(request.form['YA'])
        inp_rata=float(request.form['inp_rata'])

        if(inp_rata <= 30):
            rata1 = 1
            rata2 = 0
            rata3 = 0
            rata4 = 0
            rata5 = 0
            
        elif(inp_rata > 30 and inp_rata <= 45):
            #global rata1,rata2,rata3,rata4,rata5
            rata1 = 0
            rata2 = 1
            rata3 = 0
            rata4 = 0
            rata5 = 0

        elif(inp_rata > 45 and inp_rata <= 60):
            rata1 = 0
            rata2 = 0
            rata3 = 1
            rata4 = 0
            rata5 = 0

        elif(inp_rata > 60 and inp_rata <= 90):
            rata1 = 0
            rata2 = 0
            rata3 = 0
            rata4 = 1
            rata5 = 0

        elif(inp_rata > 90):
            rata1 = 0
            rata2 = 0
            rata3 = 0
            rata4 = 0
            rata5 = 1

        val = np.array([pendapatan_setahun_juta, durasi_pinjaman_bulan, jumlah_tanggungan, TIDAK, YA, inp_rata])

        final_features = [np.array(val)]
        model_path = os.path.join('models', 'modelCreditScore.pkl')
        model = pickle.load(open(model_path, 'rb'))
        res = model.predict(final_features)

        return render_template('index.html', prediction_text=res)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
