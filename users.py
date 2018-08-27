import psycopg2
db_details = "dbname='starks' user='starks' host='localhost' password='starks'"
conn = psycopg2.connect(db_details)
cur = conn.cursor()


class User(object):
    def signup(self, role, username, password):
        """Signup the user"""
        cur = conn.cursor()
        cur.execute("SELECT * from users WHERE username='{}'".format(username))
        user_exists = cur.fetchone()
        if not user_exists:
            print("that user already exists")
        cur.execute('insert into users(username,password, role) values({},{},{})'.format(username,password,role))
        print("Successfully registered")
        

    def login(self, username, password): 
        """Login the user"""   
        cur = conn.cursor()
        cur.execute("SELECT * from users WHERE username='{}'".format(username))
        user_exists = cur.fetchone()
        if user_exists:
            print ("you have successfully logged in")
        print("wrong username or password")