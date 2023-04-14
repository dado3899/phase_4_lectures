# Cookies and sessions
# cascade = "all,delete"
# Child
# children = relationship("Child", cascade="all,delete,delete-orphan", backref="parent")
# Parent
# (from sqlalchemy.orm import backref)
# parent = relationship(Parent, backref=backref("children", cascade="all,delete,delete-orphan"))
# python-dotenv