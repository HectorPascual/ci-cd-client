from flask import Flask
import requests
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/test')
def test():
    return "Whats up!"

@app.route('/jobs')
def jobs():
    jobs = requests.get('http://localhost:5000/jobs').json()
    return render_template("index.html", jobs=jobs)

@app.route('/jobs/<int:job_id>')
def job(job_id):
    job = requests.get(f'http://localhost:5000/jobs/{job_id}').json()
    builds = requests.get(f'http://localhost:5000/jobs/{job_id}/builds').json()

    return render_template("index.html", job=job, builds=builds)


if __name__ == '__main__':
    app.run(port=8000, debug=False)