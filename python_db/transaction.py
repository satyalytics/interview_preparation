# making database transactions


# creating a new database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItems  # table names and declarative_base object

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine   
DBSession = session_maker(bind=engine)   # binds the database
Myfirstrestaurant = Restaurant(name="piza palace")    # stage the changes
session.commit()    # commit the changes

# Let's create a cheesepizza item in our database
cheesepizza = MenuItem(name='cheesepizza', description='built with cheese', course='entry', price='$8.99', restaurant=MyFirstRestaurant)
session.add(cheesepizza)
session.commit()

# query the database
session.query(MenuItem).all()

first = session.query(MenuItem).first()
items = session.query(MenuItem).all()

for item in items:
  print(item.name)
  
  
# updating the database
""" The steps for updating an entry in the database is:
1. Find the entry
2. Reset the value
3. Add to the session
4. Commit the changes """


# updating the change

vegieburger = session.query(MenuItem).filter_by(name='veggie')

vegieburger = session.query(MenuItem).filter_by(name='veggie').one()
vegieberger.price = '$2.99'

session.add(vegieburger)
session.commit()



# deleting an item
""" deleting an item is a 3 step process in a database
1. Find the entry
2. Delete the entry
3. commit the session """


spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.delete(spinach)
session.commit()


