from gevent import monkey; monkey.patch_all()

from time import sleep
from bottle import route, run

@route('/stream')
def stream():
    print "come on"
    yield 'START'
    sleep(3)
    yield 'MIDDLE'
    sleep(5)
    yield 'END'

run(host='0.0.0.0', port=8080, server='gevent')
