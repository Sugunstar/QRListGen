from flask import Flask, request, jsonify, render_template,url_for,redirect
from flask_cors import CORS
import qrcode 
import os

app = Flask(__name__)
CORS(app)  

@app.route('/',methods=['GET','POST'])
def enter_data():
    return render_template('input.html')

@app.route('/file_creation',methods=['GET','POST'] )
def file_creation():
    st1=request.form.get("data")
    st2=request.form.get("items")

    st=st1+"\n\n"+st2
    f=open('file.txt','a')
    f.write(st)
    return redirect(url_for("qrc"))

@app.route('/qrc',methods=['GET','POST'])
def qrc():
    
    f=open('file.txt','r')
    st=f.read()

    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(st)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    os.chdir("C:/Users/miria/OneDrive/Documents/adi/jmi/static")
    img.save("image.jpeg")
    os.chdir("C:/Users/miria/OneDrive/Documents/adi/jmi")
    return render_template('output.html')
    



if __name__ == '__main__':
    app.run(debug=True)
