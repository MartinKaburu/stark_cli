import psycopg2 as psycopg
import os

from users import  User

auth = User()

CONNECTION = psycopg.connect(\
    dbname='starks', \
    user='postgres', \
    host='localhost', \
    password='kaburu@andela'\
    )

class Comments(object):
	def __init__(self):
		'''Instantiate class
		'''

		self.cursor = CONNECTION.cursor()


	def post_comment(self, comment):
		'''Post a comment
		'''

		try:
			ret, username = auth.auth()
		except:
			return "[+] Please log in to continue"
		sql = 'SELECT * FROM users WHERE username=%s;'
		self.cursor.execute(sql, ([username]))
		user = self.cursor.fetchall()
		user_id = user[0][0]
		role = user[0][3]
		sql = 'INSERT INTO comments(content, user_id) VALUES(%s, %s);'
		self.cursor.execute(sql, (comment, user_id))
		CONNECTION.commit()
		return "[+] Comment posted successfully"

	def all(self):
		'''Get all comments
		'''
		sql = 'SELECT * FROM comments;'
		self.cursor.execute(sql)
		comments = self.cursor.fetchall()
		display = []
		for comment in comments:
			comm = {
				"id": comment[0],
				"user_id": comment[1],
				"content": comment[2]
			}
			display.append(comm)
		return display


	def edit(self):
		'''Edit a comment
		'''


	def delete(self):
		'''Delete a comment
		'''
