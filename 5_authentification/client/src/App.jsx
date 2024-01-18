import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [user, setUser] = useState(null);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [stay,setStay] = useState(false)
  function handleSubmit(e) {
    e.preventDefault();
    fetch('/api/login',{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_name: username,
        password: password,
        stay: stay
      })
    })
    .then(r=> {
      if(r.ok){
        return r.json()
      }
      else{
        return null
      }
    })
    .then(data => setUser(data))
  }
  function handleLogout(){
    fetch('/api/logout',{method:"DELETE"})
    .then(r=>setUser(null))
  }
  useEffect(()=>{
    fetch('/api/check_session')
    .then(r =>{
      if(r.ok){
        return r.json()
      }
      else{
        return null
      }
    })
    .then(data => setUser(data))
  },[])
  
    return (
      <>
      {
        user ? 
        <>
          <h2>Welcome, {user.user_name}!</h2> 
          <button onClick={handleLogout}>Logout</button>
        </>
        :
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="text"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <input type ="checkbox" onChange={(e)=>setStay(!stay)}></input>
        <button type="submit">Login</button>
      </form>
      }
      </>
    )
  
}

export default App
