import psycopg2

class Comments(object):
	def __init__(self,message, time_stamp, author, id, role):
		self.id=id
		self.message=message
		self.author=author
		self.role=role



   def run_query(query, inputs):
    """Run queries with inputs"""
    try:
        db_instance = DbConn()
        db_instance.cur.execute(query, inputs)
        db_instance.conn.commit()
        db_instance.close()
        return True

    except psycopg2.Error:
        return False		
		

	def post_comment(self, user_id, ):

         comment = comment.query.filter_by(user_id=user_id).first()
         if  ==
		cur.execute('INSERT INTO * comments {'id','message', 'time_stamp', 'user_id'} VALUE (('%s', '%s', '%s', '%s')(self.id, self.message, self.time_stamp, self.user_id)));
		(cursor)
		conn.commit()


	

	
	def edit_comment(self, input = 'Give me your user_id', ):
		if role='1':

		  cur.execute("UPDATE comments SET message = %s, user_id=%s WHERE id = %s)VALUE (("%s", '%s', '%s', '%s'  )(self.id, self.message, self.time_stamp, self.author)); 
		  conn.commit()

	    else:
	     cur.execute("UPDATE comments SET message = %s, user_id=%s WHERE id = %s)VALUE (("%s", '%s', '%s', '%s'  )(self.id, self.message, self.time_stamp, self.author)); 
		  conn.commit()
		 


		


	def delete_comment(self,id, role):

		if role=='2'or'3':

    	comment = comments.query.filter_by(id=id).first()
        comment.delete()
		cur.execute('DELETE FROM comments WHERE id=%s ', (id))
			conn.commit()

		resp = {
            "message": "success",
            "description": "comment updated succesfully",
            "text": text
        }

			return resp

		else:
			resp = {
            "message": "Unauthorised User",
            "description": " unauthorised user",
            "text": text
        }

		 return 










         


		





		

