#%% Main file for Cloud computing Project

from flask import Flask, render_template
# Make App
app = Flask(__name__)


@app.route('/')
def test():
    list = [
            {"col_1":"val_11", "col_2":"val_12", "col_3":"val_13"},
            {"col_1":"val_21", "col_2":"val_22", "col_3":"val_23"},
            {"col_1":"val_31", "col_2":"val_32", "col_3":"val_33"}
        ];
    return render_template('test.html',list=list)
    