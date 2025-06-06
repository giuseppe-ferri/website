from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Ohio, United States',
        'salary': 'R$ 10,000'},
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Maringa, Brazil',
        'salary': 'R$ 5,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'North Virginia, United States',
        'salary': 'R$ 13,000'
    },
    {
        'id': 5,
        'title': 'Full Stack Senior',
        'location': 'Oregon, United States',
        'salary': 'R$ 20,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Ferri Tech')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
