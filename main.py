import ConfigParser, os
import random
import calendar
import dinnerdb

class dinner_planner:
	dinner_list = set()
	
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open('config/config.cfg'))
		self.dinner_db = dinnerdb.dinners(self.config.get("dinnerdb","user"), self.config.get("dinnerdb","password"), self.config.get("dinnerdb","server"), self.config.get("dinnerdb","db_name")) 

	def load_dinners(self):
		self.dinner_list = self.dinner_db.get_dinners()

	def get_plan(self):
		dinner_plan = []
		list_count = len(self.dinner_list)
		for num in range(0, list_count):
			next_dinner  = random.randrange(len(self.dinner_list))
			dinner_plan.append(self.dinner_list[next_dinner])
			del self.dinner_list[next_dinner]
		return dinner_plan

def main():
	planner = dinner_planner()
	planner.load_dinners()
	new_plan = planner.get_plan()

	for dinner in new_plan:
		print "Dinner: {}".format(dinner)

if __name__ == "__main__":
	main()
