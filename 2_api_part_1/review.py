# Create tables
# Routes
# Before Request


# Forgot to cover
# Why add metadata?
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

# db = SQLAlchemy(metadata=metadata)

# Responses
    # by using make_response and jsonify we can make a specific
    # error
# make_response(jsonify(jsonobject),errorcode)
# Common error codes
# 100's - informational
# 200's - success
# 300's - redirect
# 400's - client error
# 500's - server error