import psycopg2 as psycopg
import os


CONNECTION = psycopg.connect(\
    dbname='d9qvciej6svij7', \
    user='fespiavtetjgwe', \
    host='ec2-184-72-247-70.compute-1.amazonaws.com', \
    password='3c3c12bb6a3f2501e64ddb098111c41ee4807c8fd00b0f6e529b6fbf58fc22ed'\
    )


class User(object):

    def __init__(self):
        self.cursor = CONNECTION.cursor()


    def signup(self, role, username, password):
        """Signup the user"""
        sql = 'SELECT * from users WHERE username=%s;'
        self.cursor.execute(sql, ([username]))
        user_exists = self.cursor.fetchall()
        if not user_exists:
            sql = 'INSERT INTO users(username,password, role) VALUES(%s,%s,%s);'
            self.cursor.execute(sql, (username,password,role))
            CONNECTION.commit()
            return("[+] Successfully registered")
        return("[-] that user already exists")


    def login(self, username, password):
        """Login the user"""
        self.cursor.execute("SELECT * from users WHERE username='{}' AND password='{}';".format(username, password))
        user_exists = self.cursor.fetchone()
        if user_exists:
            if os.path.isfile('.starks'):
                os.remove('.starks')
            f = open('.starks', 'w')
            f.write(username+' '+password)
            f.close()
            return("[+] you have successfully logged in")
        return("[-] wrong username or password")


    def auth(self):
        if os.path.isfile('.starks'):
            f = open('.starks', 'r')
            line = f.readline()
            username, password = line.split(' ')
            ret = self.login(username, password)
            if "[+] you have successfully logged in" in ret:
                return ret, username
            return "[+] Invalid credentials"
        return("[+] please login to continue")
