from db.run_sql import run_sql

from models.milestone import Milestone
from models.goal import Goal
import repositories.goal_repository as goal_repository


def save(milestone):
    sql = "INSERT INTO milestone (mile_title, mile_desc, mile_position, mile_date, goal_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [milestone.mile_title, milestone.mile_desc, milestone.mile_position, milestone.mile_date, milestone.goal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    milestone.id = id
    return milestone

def select_all():
    milestone = []

    sql = "SELECT * FROM milestone"
    results = run_sql(sql)

    for row in results:
        goal = goal_repository.select(row['goal_id'])
        milestones = Milestone(row['mile_title'],  row['mile_desc'], row['mile_position'], row['mile_date'], row['goal_id'], goal )
        milestone.append(milestones)
    return milestone


def select(id):
    milestone = None
    sql = "SELECT * FROM milestone WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        goal = goal_repository.select(result['goal_id'])
        milestone = Milestone(result['mile_title'], result['mile_desc'], result['mile_position'], result['mile_date'], result['goal_id'], goal )
    return milestone


def delete_all():
    sql = "DELETE  FROM milestone"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM milestone WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(milestone):
    sql = "UPDATE milestone SET (mile_title, mile_desc, mile_position, mile_date, goal_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [milestone.mile_title, milestone.mile_desc, milestone.mile_position, milestone.mile_date, milestone.goal.id, milestone.id,]
    run_sql(sql, values)
