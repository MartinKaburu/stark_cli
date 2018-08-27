import psycopg2

class Comments(object):
	def __init__(self,message, time_stamp, author, id):
		self.id=id
		self.message= message
		self.time_stamp=time_stamp
		self.author=author
		

	def post_comment(self, id ,message, time_stamp, author):
	
		
		cur.execute('INSERT INTO * comments {'id','message', 'time_stamp', 'author'} VALUE (('%s', '%s', '%s', '%s')(self.id, self.message, self.time_stamp, self.author)));
		(cursor)
		conn.commit()

		return cur.fetchall()

	
	def edit_comment(self,id, message, time_stamp, author):
		cur.execute("UPDATE comments SET message = %s, time_stamp=%s, author=%s WHERE id = %s)VALUE (("%s", '%s', '%s', '%s'  )(self.id, self.message, self.time_stamp, self.author)); 
		conn.commit()
		


	def delete_comment(self,id):
		cur.execute('DELETE FROM comments WHERE id=%s ', (id))
			conn.commit()










         


		





		

