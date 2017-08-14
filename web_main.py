from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import TS_main

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    text = TextField('', validators=[validators.required()])
    word = TextField('', validators=[validators.required()])
    model_CWI = TextField('', validators=[validators.required()])
    treshold = TextField('', validators=[validators.required()])
    CWI_NER = TextField('', validators=[validators.required()])
    metode= TextField('', validators=[validators.required()])
    model_SR = TextField('', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        text = request.form['text']
        model_CWI = request.form['model_CWI']
        treshold = request.form['treshold']
        CWI_NER = request.form['CWI_NER']
        metode = request.form['metode']
        model_SR = request.form['model_SR']

        SSSG_WSD = True
        if metode == "noWSD" :
            SSSG_WSD = False

        try :
            treshold = float(treshold)
        except :
            flash('Error: Treshold Empty ')
        print("Input ->",text, model_CWI, treshold, CWI_NER, SSSG_WSD, metode, model_SR)
        hasil, definition = TS_main.main(text, model_CWI, treshold, CWI_NER, SSSG_WSD, metode, model_SR)
        temp_definition = ""
        for line in definition :
            temp_definition+="- "+line+"\n"
        if form.validate():
            # Save the comment here.
            flash(text)
            flash(hasil)
            flash(temp_definition)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('view.html', form=form)


if __name__ == "__main__":
    app.run()