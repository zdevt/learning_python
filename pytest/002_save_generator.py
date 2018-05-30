import random
import string
import sqlite3

forSelect = string.ascii_letters + string.digits


def generate_code( count, length ):
    for x in range( count ):
        Re = ""
        for y in range( length ):
            Re += random.choice( forSelect )
        yield Re


def save_code( ):
    conn = sqlite3.connect( 'a.db' )
    cursor = conn.cursor( )
    codes = generate_code( 200, 20 )
    cursor.execute( 'create table if not exists user (id varchar primary key);' )
    for code in codes:
        cursor.execute( "insert into user(id) values('%s');" % (code) )
        # print(code)
    conn.commit( )
    cursor.close( )


if __name__ == '__main__':
    save_code( )
