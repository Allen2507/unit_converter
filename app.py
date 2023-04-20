from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert/<unit_type>/<from_unit>/<to_unit>/<value>')
def convert(unit_type, from_unit, to_unit, value):
    unit_type = request.form['unit_type']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    value = float(request.form['value'])

    if unit_type == 'time':
        if from_unit == 'seconds' and to_unit == 'minutes':
            converted_value = value / 60
        elif from_unit == 'minutes' and to_unit == 'seconds':
            converted_value = value * 60
        elif from_unit == 'minutes' and to_unit == 'hours':
            converted_value = value / 60
        elif from_unit == 'hours' and to_unit == 'minutes':
            converted_value = value * 60
        else:
            converted_value = value

    elif unit_type == 'temperature':
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            converted_value = (value * 9 / 5) + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            converted_value = (value - 32) * 5 / 9
        else:
            converted_value = value

    elif unit_type == 'currency':
        if from_unit == 'usd' and to_unit == 'eur':
            converted_value = value * 0.85
        elif from_unit == 'eur' and to_unit == 'usd':
            converted_value = value / 0.85
        else:
            converted_value = value

    elif unit_type == 'volume':
        if from_unit == 'liters' and to_unit == 'gallons':
            converted_value = value * 0.264172
        elif from_unit == 'gallons' and to_unit == 'liters':
            converted_value = value / 0.264172
        else:
            converted_value = value

    elif unit_type == 'distance':
        if from_unit == 'meters' and to_unit == 'feet':
            converted_value = value * 3.28084
        elif from_unit == 'feet' and to_unit == 'meters':
            converted_value = value / 3.28084
        else:
            converted_value = value

    elif unit_type == 'speed':
        if from_unit == 'kph' and to_unit == 'mph':
            converted_value = value * 0.621371
        elif from_unit == 'mph' and to_unit == 'kph':
            converted_value = value / 0.621371
        else:
            converted_value = value

    return render_template('result.html', unit_type=unit_type, from_unit=from_unit, to_unit=to_unit, value=value, converted_value=converted_value)

if __name__ == '__main__':
    app.run(debug=True)

    
