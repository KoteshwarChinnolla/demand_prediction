from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
import imageio as iio

dp = pickle.load(open('dpprod.pkl','rb'))

data=pd.read_csv('prod_.csv')

app = Flask(__name__,template_folder='Template')

@app.route('/', methods=['GET','POST'])
def man():
    product=sorted(data['product'].unique())
    return render_template('aac.html',product = product)

k=data['product'].unique().tolist()


@app.route('/predict',methods=['POST'])
def aac():
    d1= request.form['product']
    d2= request.form['year']
    d3= request.form['month']
    arr= np.array([[d1, d2, d3]])
    pred= dp.predict(arr)
    
    return render_template('after.html',data=pred,d = d1,d2= d2,d3= d3)

if __name__ == '__main__':
    app.run(debug=True)