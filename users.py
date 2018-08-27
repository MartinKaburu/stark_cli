import psycopg2
db_details = "dbname='starks' user='starks' host='localhost' password='starks'"
conn = psycopg2.connect(db_details)
cur = conn.cursor()


class User(object):
    def __init__(self, username, password):
        ''' Initialize user '''
        self.username = input("Username:")
        self.password = input("Password:")

    def user_exists(self):
        """ Check if a user exists in the db """
        conn = open_connection()
        cur = conn.cursor()
        cur.execute("SELECT * from users WHERE username='{}'".format(self.username))
        user = cur.fetchone()
        cur.close()
        conn.commit()
        return user

    def signup(self, role, username, password):
        """Signup the user"""
        role = self.role()
        user_exists = self.user_exists()
        if not user_exists:
            print("that user already exists")
        username = self.username
        password = self.password
        cur.execute('insert into users(username,password, role) values({},{},{})'.format(username,password,role))
        

    def login(self, username, password): 
        """Login the user"""   
        user_exists = self.user_exists()
        if user_exists:
            print ("you have successfully logged in")
        print("wrong username or password")

if __name__ == '__main__':
    
