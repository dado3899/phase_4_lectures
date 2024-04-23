# Create tables
# Routes
# Before Request

# Why add metadata?
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# metadata = MetaData(naming_convention={
#         "ix": "ix_%(column_0_label)s",
#         "uq": "uq_%(table_name)s_%(column_0_name)s",
#         "ck": "ck_%(table_name)s_`%(constraint_name)s`",
#         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#         "pk": "pk_%(table_name)s"
#       })
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#using-custom-metadata-and-naming-conventions
# https://alembic.sqlalchemy.org/en/latest/naming.html#the-importance-of-naming-constraints

# db = SQLAlchemy(metadata=metadata)

# Responses
    # by using make_response and jsonify we can make a specific
    # error
# make_response(jsonify(jsonobject),errorcode)
# Common error codes
# 100's - informational
# 200's - success
    # 201 is a success for post!
# 300's - redirect
# 400's - client error
# 500's - server error

# Up next, using postman