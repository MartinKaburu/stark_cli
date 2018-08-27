'''Define roles for users
'''
import psycopg2 as psycopg

class Users():
    '''user can create comment and edit comment
    '''
    def __init__(self, username, password):
        self.uname = username
        self.password = password
        self.CONNECTION = psycopg.connect(db)
        

    def create_comment(self, comment):
        '''create a comment
        '''

    def edit_comment(self, edit):
        '''edit their comments
        '''

class Moderator(Users):
    '''Define moderator functions
    '''
    def delete_comment(self, id):
        '''delete comment
        '''

class Admin(Moderator):
    '''Define admin priviledges
    '''
