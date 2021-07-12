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
    return goal