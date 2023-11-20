from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    num = random.randint(0,10)
    year = datetime.datetime.today().year
    return render_template('index.html', num=num, year=year)

@app.route('/guess/<name>')
def guess(name):
    param = {
        "name": name,
    }
    agify = requests.get('https://api.agify.io', params=param)
    agify.raise_for_status()
    data = agify.json()
    age = data["age"]
    cap_name = name.capitalize()

    genderize = requests.get('https://api.genderize.io', params=param)
    genderize.raise_for_status()
    data_ = genderize.json()
    gender = data_["gender"]
    return render_template('guess.html', age=age, name=cap_name, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    data = response.json()
    print(num)
    return render_template('blog.html', posts=data)



if __name__ == '__main__':
    app.run()
