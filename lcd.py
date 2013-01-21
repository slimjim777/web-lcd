#!/usr/bin/env python

from flask import Flask
from flask import render_template, request
from adafruit.Adafruit_CharLCD import Adafruit_CharLCD

BASE_URL = ''

app = Flask(__name__)

# Initialise the LCD class
lcd = Adafruit_CharLCD()
lcd.begin(16,2)


@app.route("/")
@app.route("/<value>")
def index(value=None):
    print "Message is", value
    return render_template('index.html', value=value)


@app.route("/change", methods=['POST'])
def change():
    if request.method == 'POST':
        # Get the value from the submitted form
        lcdText = request.form['lcd']
        print "---Message is", lcdText
        
        # Send the message to the LCD
        lcd.clear()
        lcd.message(lcdText)
    else:
        lcdText = None
    return render_template('index.html', value=lcdText)


if __name__ == "__main__":
    lcd.clear()
    lcd.message("h")
    app.debug = True
    app.run('0.0.0.0')


