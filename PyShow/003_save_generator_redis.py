import random
import string
import redis

forSelect = string.ascii_letters + string.digits


def generate_code( count, length ):
    for x in range( count ):
        Re = ""
        for y in range( length ):
            Re += random.choice( forSelect )
        yield Re


def save_code( ):
    r = redis.Redis( host = '127.0.0.1', port = '16379' )
    codes = generate_code( 200, 20 )
    p = r.pipeline( )
    for code in codes:
        p.sadd( 'code', code )
    p.execute( )
    return r.scard( 'code' )


if __name__ == '__main__':
    save_code( )

# smember code 查看