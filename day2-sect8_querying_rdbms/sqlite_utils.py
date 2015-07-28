import sqlite3

class CursorTable(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.generate_html()
    def format_row(self, html, row):
            html.append("<tr>")
            for col in row:
                html.append("<td>{0}</td>".format(col))
            html.append("</tr>")
    def print_header(self, html, row):
            html.append("<tr>")
            for col in row.keys():
                html.append("<th>{0}</th>".format(col))
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
        self.html = ''.join(html)
          
    def _repr_html_(self):
        return self.html


def run_query(db_name, query):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(query)
    ct = CursorTable(c)
    c.close()
    return ct