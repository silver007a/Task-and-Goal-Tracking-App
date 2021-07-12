from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
from repositories import goal_repository, milestone_repository
from models.milestone import Milestone

from flask import Blueprint

goals_blueprint = Blueprint("milestones", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@goals_blueprint.route("/")
def tasks():
    milestones = milestone_repository.select_all() # NEW
    return render_template("/index.html", all_milestones = milestones)