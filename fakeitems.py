from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sqlalchemy_utils

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Jon Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()


category1 = Category(name="soccer", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="soccer cleats", user_id=35, description="Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. They can be conical or blade-like in shape, and made of plastic, rubber or metal. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions. Similarly, in British English the term 'studs' can be used to refer to 'football boots' or 'rugby boots', for instance, in a similar manner to the way 'spikes' is often used to refer to athletics shoes. The type of studs worn depends on the environment of play, whether it be grass, ice, artificial turf, or other grounds requiring versatility.",category=category1)
session.add(item1)
session.commit()

item2=CategoryItem(name="jersey",id=40,description="Jersey is a knit fabric used predominantly for clothing manufacture. It was originally made of wool, but is now made of wool, cotton, and synthetic fibres.
",category=category1)
session.commit(item2)
session.add()


item3=CategoryItem(name="shinguards",id=30,description="A shin guard or shin pad is a piece of equipment worn on the front of a player’s shin to protect them from injury. These are commonly used in sports including association football (soccer), baseball, ice hockey, field hockey, lacrosse, rugby, cricket, and other sports. This is due to either being required by the rules/laws of the sport or worn voluntarily by the participants for protective measures.

Co",category=category1)
session.commit(item3)
session.add()


item4=CategoryItem(name="two shinguards",id=45,description="A shin guard or shin pad is a piece of equipment worn on the front of a player’s shin to protect them from injury. These are commonly used in sports including association football (soccer), baseball, ice hockey, field hockey, lacrosse, rugby, cricket, and other sports. This is due to either being required by the rules/laws of the sport or worn voluntarily by the participants for protective measures.

Co",category=category1)
session.commit(item4)
session.add()

category2 = Category(name="basketball", user_id=2)

session.add(category2)
session.commit()



category3 = Category(name="baseball", user_id=3)

session.add(category3)
session.commit()

item1 = CategoryItem(name="bat", user_id=10, description="Till now you might have got some idea about the acronym, abbreviation or meaning of BAT. What does BAT mean? is explained earlier.
You might also like some similar terms related to BAT to know more about it.", category=category3)

session.add(item1)
session.commit()


category4 = Category(name="frisbee", user_id=4)

session.add(category4)
session.commit()

item1=CategoryItem(name="frisbee",id=15,description="A frisbee (also called a flying disc or simply a disc) is a gliding toy or sporting item that is generally plastic and roughly 20 to 25 centimetres (8 to 10 in) in diameter with a lip,[1] used recreationally and competitively for throwing and catching, for example, in flying disc games. The shape of the disc, an airfoil in cross-section, allows it to fly by generating lift as it moves through the air while spinning.",category=category4)
session.add(item1)
session.commit()



category5=Category(name="snowboarding",id=5 )
session.add(category5)
session.commit()

item1=CategoryItem(name="goggles",id=20,description="Goggles or safety glasses are forms of protective eyewear that usually enclose or protect the area surrounding the eye in order to prevent particulates, water or chemicals from striking the eyes. They are used in chemistry laboratories and in woodworking. They are often used in snow sports as well, and in swimming. Goggles are often worn when using power tools such as drills or chainsaws to prevent flying particles from damaging the eyes. Many types of goggles are available as prescription goggles for those with vision problems.",category=category5)
session.add(category5)
session.commit()

category6=Category(name="rock climbing",id=6)
session.add(category6)
session.commit()



category7=Category(name="foosball",id=7)
session.add(category7)
session.commit()


category8=Category(name="skating",id=8)
session.add(category8)
session.commit()


category9=Category(name="hockey ",id=9)
session.add(category9)
session.commit()




categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name