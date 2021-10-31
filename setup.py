import sqlite3
                
def main():
    conn = sqlite3.connect('data.sl3')
    c = conn.cursor()
    c.execute("create table p (name, dt, prob)")
    conn.commit()
    c.close()

main()
