from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/wrgo project'
# db = SQLAlchemy(app)

# class Contact(db.Model):
#     name = db.Column(db.String, primary_key=True)
#     email = db.Column(db.String(20),  nullable=False)
#     subject = db.Column(db.String(120) , nullable=False)
#     message = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(6), nullable=True)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")
    # if request.method=='POST':

    #     name=request.form.get('name')
    #     email=request.form.get('email')
    #     subject=request.form.get('subject')
    #     message=request.form.get('message')
    #     entry=Contact(name=name,email=email,subject=subject,message=message)
    #     db.session.add(entry)
    #     db.session.comit()

app.run(debug=True)