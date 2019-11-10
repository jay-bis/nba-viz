from flask import render_template, flash, request, redirect
from app import app
from .forms import SearchForm
from .shotChart import create_shot_chart
from .getInfo import getIds

from io import BytesIO
from urllib.parse import quote
from base64 import b64encode
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return(generate_chart(search))
    return render_template('index.html', title="NBAVIZ", form=search)

@app.route("/results")
def generate_chart(search):
    player_name = search.data['search']

    ids = getIds(player_name)
    if ids == "error":
        flash("Name of player not found!")
        return redirect("/")

    fig, _ = create_shot_chart(ids['player_id'], ids['team_id'], player_name)
    # FigureCanvas required for writing file-like objects
    canvas=FigureCanvas(fig)
    # need to convert fig created to base64 encoded value to
    # be able to be sent over proper channels
    png_output = BytesIO()
    canvas.print_png(png_output)
    png_output = b64encode(png_output.getvalue()).decode('ascii')
    return render_template("chart.html", result=quote(png_output.rstrip('\n')))