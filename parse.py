#!/usr/bin/python

'''Parse the CLI arguments
'''
import sys
import getopt


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: usage")
        exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'slu:p:c:der:i:' , ['signup', 'login', 'username=', 'password=', 'comment=', 'delete', 'edit=', 'role=', 'id='])
    except getopt.GetoptError:
        print('Invalid argument')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['--username', '-u']:
            username = arg
        if opt in ['--id', '-i']:
            user_id = arg
        elif opt in ['--password', '-p']:
            password = arg
        elif opt in ['--role', '-r']:
            role = arg
        elif opt in ['--comment', '-c']:
            comment = arg
            print(user_id, comment)
            #post_comment(id, comment)
        elif opt in ['--edit', '-e']:
            edited = arg
        elif opt in ['--login', '-l']:
            print(username, password)
            #login(username, password)
        elif opt in ['--signup', '-s']:
            print(role, username, password)
            #signup(role, password, username)
