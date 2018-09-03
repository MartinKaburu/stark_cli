import psycopg2, psycopg2.extras


class Database:
    def __init__(self):
        self.con = None

        """ local credentials """
        self.dbhost = '127.0.0.1'
        self.dbname = 'starks'
        self.dbuser = 'postgres'
        self.dbpassword = 'kaburu@andela'

        """ postgres credentials """
        self.db_postgres_host = '127.0.0.1'
        self.db_postgres_dbname = 'postgres'
        self.db_postgres_user = 'postgres'
        self.db_postgres_password = 'kaburu@andela'

        self.tables = (
            """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(500) NOT NULL,
                role INT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS comments(
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                content text NOT NULL,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS user_trail(
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                lastLoggedInAt TIMESTAMP,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )

    def process_configuration(self):
        try:
            con = psycopg2.connect(dbname=self.db_postgres_dbname, user=self.db_postgres_user, host=self.db_postgres_host, password=self.db_postgres_password)
            con.autocommit = True
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute("select * from pg_database where datname = '{}';".format(self.dbname))
            answer = cur.fetchall()

            """ check if database exists to drop it first """
            if answer:
                print("Database {} exists".format(self.dbname))
                cur.execute("DROP DATABASE {};".format(self.dbname))
                con.commit()
                con.close()
                self.create_database_and_user()
                self.create_tables()
            else:
                print("Database {} does NOT exist".format(self.dbname))
                con.commit()
                con.close()
                self.create_database_and_user()
                self.create_tables()
        except Exception as e:
            print ("process_configuration: "+str(e))

    def create_database_and_user(self):
        try:
            con = psycopg2.connect(dbname=self.db_postgres_dbname, user=self.db_postgres_user,
                                   host=self.db_postgres_host, password=self.db_postgres_password)
            con.autocommit = True
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('CREATE DATABASE {} OWNER {};'.format(self.dbname, self.dbuser))
            con.commit()
            con.close()

        except Exception as e:
            print("create_database_and_user error: " + str(e))

    def create_tables(self):
        con = psycopg2.connect(dbname=self.dbname, user=self.dbuser, host=self.dbhost,
                               password=self.dbpassword)
        con.autocommit = True
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        for command in self.tables:
            try:
                cur.execute(command)
                con.commit()
            except Exception as e:
                print("table error: "+str(e))
        con.close()


db = Database()

db.process_configuration()
