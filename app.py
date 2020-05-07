from flask import Flask
from flask import request
import requests
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/test')
def test():
    return "Whats up!"

@app.route('/jobs', methods=['GET','POST'])
def jobs():
    if request.method == 'GET':
        jobs = requests.get('http://localhost:5000/jobs').json()
        return render_template("index.html", jobs=jobs)
    elif request.method == 'POST':
        data = {'title':request.form.get('title'),
                'description':request.form.get('description')}
        requests.post('http://localhost:5000/jobs',data=data)
        jobs = requests.get('http://localhost:5000/jobs').json()
        return render_template("index.html", jobs=jobs)

@app.route('/jobs/<int:job_id>')
def job(job_id):
    job = requests.get(f'http://localhost:5000/jobs/{job_id}').json()
    builds = requests.get(f'http://localhost:5000/jobs/{job_id}/builds').json()

    return render_template("index.html", job=job, builds=builds)

@app.route('/nodes')
def nodes():
    nodes = requests.get('http://localhost:5000/nodes').json()
    return render_template("index.html", nodes=nodes)

@app.route('/create_job')
def create_job_view():
    return render_template("index.html", create_job=True)

if __name__ == '__main__':
    app.run(port=8000, debug=False)