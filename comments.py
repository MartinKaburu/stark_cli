import psycopg2 as psycopg
import os

from users import  User

auth = User()

CONNECTION = psycopg.connect(\
dbname='d9qvciej6svij7', \
user='fespiavtetjgwe', \
host='ec2-184-72-247-70.compute-1.amazonaws.com', \
password='3c3c12bb6a3f2501e64ddb098111c41ee4807c8fd00b0f6e529b6fbf58fc22ed'\
)

class Comments():
    '''Define comment methods
    '''
    def __init__(self):
        '''Instantiate class
        '''
        self.cursor = CONNECTION.cursor()


    def check_auth(self):
        '''check authorization
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
        return user_id, role

    def post_comment(self, comment):
        '''Post a comment
        '''
        try:
            user_id, role = self.check_auth()
        except:
            return self.check_auth()
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
            sql = 'SELECT * FROM users WHERE id=%s;'
            self.cursor.execute(sql, ([comment[1]]))
            user = self.cursor.fetchone()
            comm = {
            "comment_id": comment[0],
            "user_id": comment[1],
            "author": user[1],
            "comment": comment[2]
            }
            display.append(comm)
        return display


    def edit(self, update, id):
        '''Edit a comment
        '''
        try:
            user_id, role = self.check_auth()
        except:
            return "[+] Please log in to continue"
        if role == 1 or role == 2:
            sql = 'SELECT * FROM comments WHERE id=%s AND user_id=%s;'
            self.cursor.execute(sql, (id, user_id))
            comment = self.cursor.fetchone()
            if comment:
                sql = 'UPDATE comments SET content=%s WHERE id=%s AND user_id=%s;'
                self.cursor.execute(sql, (update, id, user_id))
                CONNECTION.commit()
                return "[+] Comment updated successfully"
            return "[+] You can only edit your own comments"
        elif role == 3:
            sql = 'UPDATE comments SET content=%s WHERE id=%s;'
            self.cursor.execute(sql, (update, id))
            CONNECTION.commit()
            return "[+] Admin comment updated"
        return "[+] Invalid role"




    def delete(self, id):
        '''Delete a comment
        '''
        try:
            user_id, role = self.check_auth()
        except:
            return "[+] Please log in to continue"
        if role == 3 or role == 2:
            sql = 'DELETE FROM comments WHERE id=%s;'
            self.cursor.execute(sql, ([id]))
            CONNECTION.commit()
            return "[+] Comment deleted successfully"
        return "[+] Ooops your role doesn't authorize that"
