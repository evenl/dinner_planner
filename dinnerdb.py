import _mysql

class dinners:
	db_server   = ""
	db_user     = ""
	db_password = ""
	db_name     = ""

	def __init__(self, user, password, server, db_name):
        	self.db=_mysql.connect(server, user, password, db_name)

	def get_dinners(self, id=-1):
		list = []
		if id == -1:
        		self.db.query("""SELECT * FROM matretter""")
		else:
			self.db.query("""SELECT * FROM matretter WHERE id = {}""".format(id))

		result=self.db.store_result()
		dinners = result.fetch_row(maxrows=0, how=1)

		for dinner in dinners:
			list.append(dinner['name'])

		return list

	def get_dinner_id(self, name):
		self.db.query("""SELECT * FROM matretter WHERE name = \"{}\"""".format(name))
		result=self.db.store_result()
		dinners = result.fetch_row(maxrows=0, how=1)

		return dinners[0]['id']

	def get_dinner_weight(self, name):
                self.db.query("""SELECT * FROM matretter WHERE name = \"{}\"""".format(name))
                result=self.db.store_result()
                dinners = result.fetch_row(maxrows=0, how=1)

		return dinners[0]['weight']

