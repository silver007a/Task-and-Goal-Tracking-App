from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
from repositories import goal_repository, milestone_repository
from models.milestone import Milestone

from flask import Blueprint

goals_blueprint = Blueprint("milestones", __name__)


@goals_blueprint.route("/goals")
def milestones():
    milestones = milestone_repository.select_all()
    return render_template("goals/index.html", all_milestones = milestones)