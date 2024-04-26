import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react'

function App() {
  const [user,setUser] = useState(undefined)
  const [loginUser,setLoginUser] = useState("")

  useEffect(()=>{
    fetch('/check_sessions')
    .then(r=>{
      if(r.ok){
        return r.json()
      }
      else{
        return undefined
      }
    })
    .then(data => setUser(data))
  },[])

  function login(e){
    e.preventDefault()
    fetch('/login',
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(
        {
          username: loginUser
        }
      )
    })
    .then(r=>{
      if(r.ok){
        return r.json()
      }
      else{
        alert("Not valid login credentials")
        return undefined
      }
    })
    .then(data=>setUser(data))
    // .then(data=>{{
    //   if(data.error){
    //     alert("Not valid login")
    //   }
    //   else{
    //     setUser(data)
    //   }
    // }})
  }

  function logout(){
    fetch('/logout',{
      method: "DELETE"
    })
    .then(r=> setUser(undefined))
  }
  function fetchBlog(){
    fetch('/blog/1')
    .then(r=>r.json())
    .then(data=> console.log(data))
  }

  return (
    <div className="App">
      <header className="App-header">
        {
          user? 
          <>
            <h1>{user.username}</h1>
            <button onClick={()=>logout()}>Logout</button>
            <button onClick={()=> fetchBlog()}>Read Blog</button>
          </>
          :
          <form onSubmit={(e)=>login(e)}>
            <input placeholder='username' value={loginUser} onChange={(e)=>setLoginUser(e.target.value)}/>
            <button type = "submit">Login</button>
          </form>
        }
      </header>
    </div>
  );
}

export default App;
