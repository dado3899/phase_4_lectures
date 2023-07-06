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

# create vite@latest client
# import { defineConfig } from 'vite'
# import react from '@vitejs/plugin-react'

# // https://vitejs.dev/config/
# export default defineConfig({
#   plugins: [react()],
#   server: {
#     port: 3000,
#     cors:true,
#     proxy: {
#       "/api":{
#         target: "http://127.0.0.1:5555",
#         changeOrigin:true,
#         secure: false,
#         rewrite: (path)=>path.replace(/^\/api/,"")
#       }
#     }
#   }
# })
