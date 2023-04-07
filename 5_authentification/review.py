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