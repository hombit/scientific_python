from io import BytesIO

import matplotlib; matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sin/<value>")
def sin_value(value):
    value = float(value)
    return str(np.sin(value))

@app.route("/sin/<omega>.png")
def sin_omega(omega):
    omega = float(omega)
    return Response(create_figure(omega), mimetype='image/png')

def create_figure(omega):
    fig = Figure()
    canvas = FigureCanvasAgg(fig)
    axis = fig.add_subplot(111)
    x = np.r_[0:2*np.pi:100j]
    y = np.sin(omega*x)
    axis.set_xlabel('x')
    axis.set_ylabel('y')
    axis.plot(x, y)
    data = BytesIO()
    fig.savefig(data, format='png')
    return data.getvalue()
    
app.run('0.0.0.0', 5000)