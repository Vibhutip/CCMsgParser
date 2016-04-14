import cgi
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

import MySQLdb
import os
import jinja2

class CreditCardDAO:
    

    def init(self):
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            self.db = MySQLdb.connect(
                '/cloudsql/' + _INSTANCE_NAME, 'creditcardmessage', 'root', 'utf8')
        else:
            self.db = MySQLdb.connect(host='127.0.0.1', port=3306, db='creditcardmessage', user='root', passwd="toor", charset='utf8')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, db='guestbook', user='root', charset='utf8')

        self.cursor = self.db.cursor()
        # Note that the only format string supported is %s
        # cursor.execute('INSERT INTO entries (guestName, content) VALUES (%s, %s)', (fname, content))
        # db.commit()
        # db.close()

    def commit(self):
        self.db.commit()
        self.db.close()

    def close(self):
        self.db.close()
