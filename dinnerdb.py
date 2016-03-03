import MySQLdb

class dinners:
	db_server   = ""
	db_user     = ""
	db_password = ""
	db_name     = ""

	def __init__(self, user, password, server, db_name):
        	self.db=MySQLdb.connect(host=server, user=user, passwd=password, db=db_name, charset='utf8')

	def get_dinners(self, id=-1):
		cursor = self.db.cursor()
		list = []
		if id == -1:
        		cursor.execute("""SELECT * FROM matretter""")
		else:
			cursor.execute("""SELECT * FROM matretter WHERE id = {}""".format(id))

		result=cursor.fetchall()
		for row in result:
			list.append(row[1])

		return list

	def get_dinner_id(self, name):
		cursor = self.db.cursor()
		self.db.execute("""SELECT * FROM matretter WHERE name = \"{}\"""".format(name))
		row=cursor.fetchone()
		while row is not None:
			return row[0]
		else:
			return None

	def get_dinner_weight(self, name):
                self.db.execute("""SELECT * FROM matretter WHERE name = \"{}\"""".format(name))
                row=self.db.fetchone()
		while row is not None:
			return row[2]
		else:
			return None

