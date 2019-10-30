from flask import Flask, request, render_template
from functions import fetchdata

app = Flask(__name__)


@app.route('/')
def page():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def values():
    try:
        if request.method == 'POST':
            Country =request.form['Country']
            City = request.form['City']
            Station = request.form['Station']
            FromDirection = request.form['FromDirection']
            FromDistance = request.form['FromDistance']
            ToDirection = request.form['ToDirection']
            ToDistance = request.form['ToDistance']
            data = fetchdata(Country, City, Station, FromDirection, int(FromDistance), ToDirection, int(ToDistance))
            return str(len(data))
        else:
            return render_template('index.html')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)