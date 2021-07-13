from flask import Flask, render_template
from controllers.milestone_controllers import milestone_blueprint
import repositories.milestone_repository as milestone_repository

app = Flask(__name__)

app.register_blueprint(milestone_blueprint)

@app.route('/')
def home():
    milestones = milestone_repository.select_all()
    return render_template("index.html", all_milestones = milestones)

if __name__ == '__main__':
    app.run(debug=True)