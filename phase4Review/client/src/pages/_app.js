import '@/styles/globals.css'
import {useEffect,useState} from 'react'

export default function App({ Component, pageProps }) {
  const [currUser, setcurrUser] = useState(null);
  const [loggedIn,setloggedIn] = useState(false)
  
  useEffect(()=>{
    fetch('/logged_user')
    .then(r => r.json())
    .then(data => setcurrUser(data))
  },[])

  return (
    <Component {...pageProps} currUser = {currUser} setcurrUser={setcurrUser} setloggedIn={setloggedIn} loggedIn={loggedIn} test ={"test"}/>
  )
}
