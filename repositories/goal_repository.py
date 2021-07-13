from db.run_sql import run_sql

from models.goal import Goal
from models.milestone import Milestone


def save(goal):
    sql = "INSERT INTO goals (title, description, position, event_date) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [goal.title, goal.description, goal.position, goal.event_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    goal.id = id
    return goal


def select_all():
    goals = []

    sql = "SELECT * FROM goals"
    results = run_sql(sql)

    for row in results:
        goal = Goal(row['title'], row['description'], row['position'], row['event_date'], row['id'] )
        goals.append(goal)
    return goals


def select(id):
    goal = None
    sql = "SELECT * FROM goals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        goal = Goal(result['title'], result['description'], result['position'], result['event_date'], result['id'] )
    return goal


def delete_all():
    sql = "DELETE FROM goals"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM goals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(goal):
    sql = "UPDATE goals SET (title, description, positon, event_date) = (%s, %s, %s, %s) WHERE id = %s"
    values = [goal.title, goal.description, goal.positon, goal.event_date, goal.id]
    run_sql(sql, values)

def milestones(goal):
    milestones = []

    sql = "SELECT * FROM milestone WHERE goal_id = %s"
    values = [goal.id]
    results = run_sql(sql, values)

    for row in results:
        milestone = Milestone(row['mile_title'], row['mile_desc'], row['mile_position'], row['mile_date'], row['goal_id'] )
        milestones.append(milestone)
    return milestones