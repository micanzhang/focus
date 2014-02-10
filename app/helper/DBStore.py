__author__ = 'micanzhang'

import datetime
import web

class SQLAStore(web.session.Store):
    def __init__(self, table):
        self.table = table
        self.session = web.ctx.orm

    def __contains__(self, item):
        query = self.session.query(self.table).filter(self.table.session_id==item).first()
        return bool(query)

    def __getitem__(self, item):
        s = self.session.query(self.table).filter(self.table.session_id==item).first()
        if not s:
            raise KeyError
        else:
            s.atime = datetime.datetime.now()
            self.session.commit()
            return self.decode(s.data)

    def __setitem__(self, key, value):
        pickled = self.encode(value)
        now = datetime.datetime.now()
        if key in self:
            query = self.session.query(self.table).filter(self.table.session_id==key).first()
            query.data = pickled
            query.atime = now
        else:
            query = self.table(session_id=key,data=pickled)
            self.session.add(query)
        self.session.commit()

    def __delitem__(self, key):
        self.session.query(self.table).filter(self.table.session_id==key).delete()
        self.session.commit()

    def cleanup(self, timeout):
        timeout = datetime.timedelta(timeout/(24 * 60 * 60))
        last_allowed_time = datetime.datetime.now() - timeout
        self.session.query(self.table).filter(self.table.atime < last_allowed_time).delete()
        self.session.commit()
