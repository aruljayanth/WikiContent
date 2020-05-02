import urllib
from bs4 import BeautifulSoup
from flask import *
import requests

app = Flask(__name__)
app.secret_key = "abc"
nam = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    session['response'] = 'ERROR 404 SITE ' + nam + ' NOT FOUND'
    return render_template("main.html")


@app.route('/success', methods=['GET', 'POST'])
def good():
    if request.method == 'POST':
        ab = request.form['link']
        try:
            p = urllib.request.urlopen(ab)
            wiki = requests.get(ab)
            l = []
            soup = BeautifulSoup(wiki.text, 'html.parser')
            tes = soup.find('title')
            print(tes.text + '\n')
            l.append(tes.text + '\n')
            ww2_contents = soup.find_all("div", class_='toc')
            for i in ww2_contents:
                print(i.text)
                l.append(i.text)
            print('Overview\n')
            l.append('\n' + '\n' + 'Overview' + '\n' + '\n')
            overview = soup.find_all('table', class_='infobox vevent')
            for z in overview:
                print(z.text + '\n')
                l.append(z.text)
            return Response(l, status=200, mimetype='text/plain')
        except:
            if 'response' in session:
                s = session['response'];
                resp = make_response(render_template('result_data.html', name=s))
                resp.set_cookie('lasted', ab)
                return resp


@app.route('/lastvisited', methods=['GET', 'POST'])
def lastvis():
    name = str(request.cookies.get('lasted'))
    return '<h1>Last Visited Site:- <br> ' + name + '</h1>'


if __name__ == "__main__":
    app.run(debug=True)
