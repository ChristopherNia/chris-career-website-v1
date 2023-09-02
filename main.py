from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': "Port Moresby",
    'salary': 'K110,000.00/annuam'
  
  },
  {
    'id': 2,
    'title': "Data Science",
    'location': 'Port Moresby',
  },
  {
    'id': 3,
    'title': "Frontend Developer",
    'location': 'Lae',
    'salary': 'K140,000.00/annuam'
  },
  {
    'id': 4,
    'title': "Backend Engineer",
    'location': 'Port Moresby',
    'salary': 'K120,000.00/annuam'
  }
  
]


@app.route("/")
def hello():
 return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
