from flask import Flask, render_template
from controllers.milestone_controllers import milestone_blueprint
import repositories.milestone_repository as milestone_repository

app = Flask(__name__)

app.register_blueprint(milestone_blueprint)
#appregister (goals_blue) and new goals_contoller and html pages is all that's needed

@app.route('/')
def homepage():
    milestones = milestone_repository.select_all()
    return render_template("index.html", all_milestones = milestones)

@app.route('/goals/home')
def home():
    milestones = milestone_repository.select_all()
    return render_template("goals/home.html", all_milestones = milestones)

if __name__ == '__main__':
    app.run(debug=True)