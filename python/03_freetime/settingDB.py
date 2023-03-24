import mariadb


class ConnectionProvider:
	@staticmethod
	def myConnectionProvider():
		conn = mariadb.connect(
			user="monty",
			password="123456",
			host="128.199.200.28",
			port=3306,
			database="testDB"
		)
		return conn
