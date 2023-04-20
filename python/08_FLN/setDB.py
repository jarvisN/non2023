import mariadb


class ConnectionProvider:
	@staticmethod
	def myConnectionProvider():
		conn = mariadb.connect(
			user="non",
			password="662542",
			host="128.199.245.117",
			port=3306,
			database="testNon"
		)
		return conn
