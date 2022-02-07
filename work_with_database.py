from pprint import pprint
import sqlalchemy

db = 'postgresql://azvezdin:********@localhost:5432/hw_2'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
sel = connection.execute("""SELECT title, year_issue FROM album WHERE year_issue = 2018;""").fetchall()
pprint(sel)
print()
sel = connection.execute("""SELECT title, duration FROM track ORDER BY duration DESC LIMIT 1;""").fetchall()
pprint(sel)
print()
sel = connection.execute("""SELECT title FROM track WHERE duration >= 3.5;""").fetchall()
pprint(sel)
print()
sel = connection.execute("""SELECT title FROM collection WHERE year_issue BETWEEN 2018 AND 2020;""").fetchall()
pprint(sel)
print()
sel = connection.execute("""SELECT singer_name FROM singer WHERE NOT singer_name LIKE '%% %%' ;""").fetchall()
pprint(sel)
print()
sel = connection.execute("""SELECT title FROM track WHERE title LIKE '%%my%%' OR title LIKE '%%мой%%';""").fetchall()
pprint(sel)
