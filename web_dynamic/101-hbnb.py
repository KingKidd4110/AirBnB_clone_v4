#!/usr/bin/python3

""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/101-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('101-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)[?1000h[?1049h[22;0;0t[>4;2m[?1h=[?2004h[?1004h[1;30r[?12h[?12l[22;2t[22;1t[27m[23m[29m[m[H[2J[?25l[2;1H[94m~                                                                                                                       [3;1H~                                                                                                                       [4;1H~                                                                                                                       [5;1H~                                                                                                                       [6;1H~                                                                                                                       [7;1H~                                                                                                                       [8;1H~                                                                                                                       [9;1H~                                                                                                                       [10;1H~                                                                                                                       [11;1H~                                                                                                                       [12;1H~                                                                                                                       [13;1H~                                                                                                                       [14;1H~                                                                                                                       [15;1H~                                                                                                                       [16;1H~                                                                                                                       [17;1H~                                                                                                                       [18;1H~                                                                                                                       [19;1H~                                                                                                                       [20;1H~                                                                                                                       [21;1H~                                                                                                                       [22;1H~                                                                                                                       [23;1H~                                                                                                                       [24;1H~                                                                                                                       [25;1H~                                                                                                                       [26;1H~                                                                                                                       [27;1H~                                                                                                                       [28;1H~                                                                                                                       [29;1H~                                                                                                                       [m[30;103H0,0-1[9CAll[9;52HVIM - Vi IMproved[11;53Hversion 9.0.1165[12;49Hby Bram Moolenaar et al.[13;41HModified by team+vim@tracker.debian.org[14;39HVim is open source and freely distributable[16;46HHelp poor children in Uganda![17;38Htype  :help iccf[34m<Enter>[m       for information [19;38Htype  :q[34m<Enter>[m               to exit         [20;38Htype  :help[34m<Enter>[m  or  [34m<F1>[m  for on-line help[21;38Htype  :help version9[34m<Enter>[m   for version info[1;1H[?25h[?4m[?25l[30;93H^Z[1;1H[30;1H
[?1004l[?2004l[?1l>[?25h[>4;m[?1049l[23;0;0t[?1000l
