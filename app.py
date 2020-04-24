from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from predict_flair import get_prediction

app = Flask(__name__)
# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'fsdjgvs4it8ysfdjkvnsorut456'
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

class SingleTest(FlaskForm):
    url = StringField('Enter URL of the Reddit post', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index_single_test():
    single_test = SingleTest()
    result = ""
    if single_test.validate_on_submit():
        url = single_test.url.data
        single_test.url.data = ""
        result = get_prediction(url)
    return render_template('single-test.html', form=single_test, message=result)

@app.route('/automated_testing', methods=['POST'])
def get_request():
    file = request.files['upload_file']
    urls = file.readlines()
    response = dict()
    for url in urls:
        url = url.decode("utf-8")
        response[url] = get_prediction(url)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
