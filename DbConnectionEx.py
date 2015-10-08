#!/usr/bin/python
import psycopg2
import datetime

class YLabDb:
    # Need to set some basic value types to variables for python
    conn = ''
    cur = ''

    def connectionDb(self):
        try:
            self.conn = psycopg2.connect("dbname='ylabdb' user='ylabclass' host='192.168.10.126' password='YlabLock'")
            print('connection init')

            self.cur = self.conn.cursor()
        except ConnectionError as e:
            print(' could not connect')
            print(e)
            self.closeDb()
            return False

        return True

    def insertionDb(self, username, message):
        try:
            self.cur.execute("INSERT INTO classdata (username, message, user_time) VALUES (%s, %s, %s)", (username, message, datetime.datetime.utcnow()))
            print(datetime.datetime.now().time())
            self.conn.commit()
        except ConnectionError as e:
            print(e)

    def retrieveDb(self):
        try:
            self.cur.execute('SELECT * FROM classdata')
            result = self.cur.fetchall()
            for row in result:
                print(row)
        except ConnectionError as e:
            print(e)

    def closeDb(self):
        print('close connections')
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

ylab = YLabDb()

ylab.connectionDb()

ylab.retrieveDb()

#ylab.insertionDb('Kirby', 'Im in too')

#ylab.retrieveDb()

ylab.closeDb()





