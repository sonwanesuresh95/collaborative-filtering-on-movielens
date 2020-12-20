from flask import Flask, request, render_template

from recommend import Lens

app = Flask(__name__)
#app.debug = True

lens = Lens()
mapping = lens.mapping


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    title = request.form['titles']
    most_similar = lens.recommend_similar(title)
    return render_template('index.html', title=mapping[title], most_similar=most_similar)


if __name__ == '__main__':
    app.run()
