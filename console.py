import pdb
from models.milestone import Milestone
from models.goal import Goal

import repositories.milestone_repository as milestone_repository
import repositories.goal_repository as goal_repository

milestone_repository.delete_all()
goal_repository.delete_all()


goal1 = Goal("Visit Therme, Romania", "Arrange family trip", 1, "2021-11-12")
goal_repository.save(goal1)
goal2 = Goal("Visit Disneyland", "Create savings plan", 1, "2021-9-12")
goal_repository.save(goal2)

goal_repository.select_all()

milestone_1 = Milestone("Do some research on opening times", "Contact spa and confirm times it is open and hotel availability.", 1, "2021-7-12", goal1)
milestone_repository.save(milestone_1)

milestone_2 = Milestone("Write a short plan for saving", "Create a shared document in Google drive and list todo.", 1, "July", goal2)
milestone_repository.save(milestone_2)

milestone_4 = Milestone("Set up a savings account", "Research best savings accounts online.", 2, "Wed 4th", goal2)
milestone_repository.save(milestone_4)

milestone_5 = Milestone("Research places to go and see", "Go to library and get some travel books on Disneyland and region.", 12, "2pm tomorrow", goal2)
milestone_repository.save(milestone_5)

milestone_6 = Milestone("Learn to speak some French", "Look for online course and intercambios on meetup groups.", 4, "By next week 4th", goal2)
milestone_repository.save(milestone_6)

milestone_7 = Milestone("Find out if there are other places to visit", "Contact some friends who live there (Julie and Martin) and ask where are the best places to visit.", 2, "2021-10-12", goal2)
milestone_repository.save(milestone_7)

milestone_8 = Milestone("But a new camera for trip", "Go online and look for some reviews on action pros and action cameras that can get wet.", 7, "2021-9-12", goal2)
milestone_repository.save(milestone_8)

milestone_9 = Milestone("Look for reviews online", "Go to Trip Advisor and websites like that and find out what is good to do and see.", 6, "July 5th", goal2)
milestone_repository.save(milestone_9)

milestone_10 = Milestone("Contact Julie to arrange to meet up there", "Give Julie a call on Monday and arrange to visit.", 9, "Wednesday 15th", goal2)
milestone_repository.save(milestone_10)

# milestone_11 = Milestone("Find out about insurance policy", "Check the bank insurance policy and that we are covered for France.", 2, "By weekend", goal2)
# milestone_repository.save(milestone_11)



# pdb.set_trace()
