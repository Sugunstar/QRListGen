from flask import Flask, request, jsonify, render_template,url_for,redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/',methods=['GET','POST'])
def enter_data():
    return render_template('input.html')

@app.route('/file_creation',methods=['GET','POST'] )
def file_creation():
    st=request.form.get("data")
    f=open('file.txt','a')
    flag = 0
    l1=st.split()
    for word in l1:
        f.write(word)
        f.write('\n')
    return redirect(url_for("qrcode"))

@app.route('/qrcode',methods=['GET','POST'])
def qrcode():
    
    f=open('file.txt','r')
    st=f.read()

    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(st)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("image.jpeg")
    return render_template('output.html')
    



if __name__ == '__main__':
    app.run(debug=True)
