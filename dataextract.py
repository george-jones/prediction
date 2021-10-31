import sqlite3

def get_row():
    conn = sqlite3.connect('data.sl3')
    cur = conn.cursor()
    cur.execute('SELECT name, dt, prob FROM p ORDER BY dt ASC, name ASC')
    rows = cur.fetchall()
    for row in rows:
        yield row
    cur.close()

def main():
    for row in get_row():
        print "%s:%s:%s" % (row[0], row[1], row[2])

if __name__ == '__main__':
    main()
