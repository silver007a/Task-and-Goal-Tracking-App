import pdb
from models.milestone import Milestone
from models.goal import Goal

import repositories.milestone_repository as milestone_repository
import repositories.goal_repository as goal_repository

milestone_repository.delete_all()
goal_repository.delete_all()


goal1 = Goal("Visit Therme, Romania", "Arrange family trip", 1, "2021-11-12")
goal_repository.save(goal1)
goal2 = Goal("Save for holiday", "Create savings plan", 1, "2021-9-12")
goal_repository.save(goal2)

goal_repository.select_all()

milestone_1 = Milestone("Do some research on opening times", "Contact spa and confirm times it is open and hotel availability.", 1, "2021-7-12", goal1)
milestone_repository.save(milestone_1)

milestone_2 = Milestone("Write a short plan for saving", "Create a shared document in Google drive and list todo.", 1, "2021-9-12", goal2)
milestone_repository.save(milestone_2)

milestone_3 = Milestone("Set up a savings account", "Research best savings accounts online.", 2, "2021-10-12", goal2)
milestone_repository.save(milestone_3)


# pdb.set_trace()
