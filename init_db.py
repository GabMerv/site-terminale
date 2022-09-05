import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, images) VALUES (?, ?)",
            ("SPH - Mécanique Mr Ovido 1ère", "https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/1.jpeg?v=1662149036312 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/2.jpeg?v=1662149087471 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/3.jpeg?v=1662149088184 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/4.jpeg?v=1662149087633 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/5.jpeg?v=1662149089747 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/7.jpeg?v=1662149088012 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/8.jpeg?v=1662149089467 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/9.jpeg?v=1662149089949 https://cdn.glitch.global/cec86228-b0f1-486b-9868-ad1020b4f8c8/10.jpeg?v=1662149096375")
            )

connection.commit()
connection.close()