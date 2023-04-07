# Cookies and sessions
# app.secret_key = 'BAD_SECRET_KEY'
# python -c 'import os; print(os.urandom(16))'
# Storing user specific data
# session['data'] will be different per cookie
# How can use this for user login?

# Use @app.before_request!

# npx create-next-app client --use-npm

# next.config.js for rerouting use rewrites
# module.exports = () => {
#   const rewrites = () => {
#     return [
#       {
#         source: "/:path*",
#         destination: "http://localhost:5555/:path*",
#       },
#     ];
#   };
#   return {
#     rewrites,
#   };
# };