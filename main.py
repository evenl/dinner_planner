import ConfigParser, os
import dinnerdb

def main():
	config = ConfigParser.ConfigParser()
	config.readfp(open('config/config.cfg'))
	dinner_db = dinnerdb.dinners(config.get("dinnerdb","user"), config.get("dinnerdb","password"), config.get("dinnerdb","server"), config.get("dinnerdb","db_name")) 

	dinners = dinner_db.get_dinners()
	
	for dinner in dinners:
		print dinner_db.get_dinner_weight(dinner)

if __name__ == "__main__":
	main()
