import sqlite3
import time

class CursorTable(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.generate_html()
    def format_row(self, html, row):
            html.append("<tr>")
            for col in row:
                html.append(u"<td>{0}</td>".format(col))
            html.append("</tr>")
    def print_header(self, html, row):
            html.append("<tr>")
            for col in row.keys():
                html.append(u"<th>{0}</th>".format(col))
            html.append("</tr>")
    def generate_html(self):
        html = ["<table>"]
        # Print the headers
        printed_headers = False
        for row in self.cursor:
            if not printed_headers:
                self.print_header(html,row)
                printed_headers = True
            self.format_row(html, row)
        html.append("</table>")
        self.html = u''.join(html)
          
    def _repr_html_(self):
        return self.html

class SQLiteDatabase(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.limits = True
    def limits_on(self):
        self.limits = True
    def limits_off(self):
        self.limits = False
    def limit_query(self, query):
        if not self.limits:
            return query
        # Limits are on
        if 'limit' in query.lower():
            return query
        if ';' in query:
            query = query.split(';')[0]
        return query + ' limit 10'
    def query(self, query):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(self.limit_query(query))
        ct = CursorTable(c)
        c.close()
        conn.close()
        return ct
