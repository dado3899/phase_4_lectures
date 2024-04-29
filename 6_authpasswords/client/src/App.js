import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react'

function App() {
  const [user,setUser] = useState(undefined)
  const [signup,setSignup] = useState(false)
  const [loginUser,setLoginUser] = useState("")
  const [loginPassword,setLoginPassword] = useState("")

  const [checkPassword,setCheckPassword] = useState("")
  const [newPassword,setNewPassword] = useState("")
  const [stayLoggedIn, setStayLoggedIn] = useState(false)

  console.log(user)
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
          username: loginUser,
          password: loginPassword,
          stayLoggedIn: stayLoggedIn
        }
      )
    })
    .then(r=>{
      if(r.ok){
        setLoginPassword("")
        setLoginUser("")
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

  function signup_user(e){
    e.preventDefault()
    fetch('/signup',
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(
        {
          username: loginUser,
          password: loginPassword
        }
      )
    })
    .then(r=>{
      if(r.ok){
        setLoginPassword("")
        setLoginUser("")
        return r.json()
      }
      else{
        alert("Not valid login credentials")
        return undefined
      }
    })
    .then(data=>setUser(data))
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
  function handlePasswordChange(){
    fetch('change_password',{
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(
        {
          id: user.id,
          existing_password: checkPassword,
          new_password: newPassword
        }
      )
    })
    .then(r=>r.json())
    .then(data =>{
      setCheckPassword("")
      setNewPassword("")
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        {
          user? 
          <>
            <h1>{user.username}</h1>
            <input placeholder='existing password' value={checkPassword} onChange={(e)=>setCheckPassword(e.target.value)}/>
            <input placeholder='new password' value={newPassword} onChange={(e)=>setNewPassword(e.target.value)}/>
            <button onClick={()=>handlePasswordChange()}>CHANGE PASSWORD</button>
            <button onClick={()=>logout()}>Logout</button>
            <button onClick={()=> fetchBlog()}>Read Blog</button>
          </>
          :
          signup?
          <>
            <form onSubmit={(e)=>signup_user(e)}>
              <input placeholder='username' value={loginUser} onChange={(e)=>setLoginUser(e.target.value)}/>
              <input type = "password" placeholder='password' value={loginPassword} onChange={(e)=>setLoginPassword(e.target.value)}/>
              <button type = "submit">Signup</button>
            </form>
            <button onClick={()=>setSignup(false)}>Switch to Login</button>
          </>
          :
          <>
            <form onSubmit={(e)=>login(e)}>
              <input placeholder='username' value={loginUser} onChange={(e)=>setLoginUser(e.target.value)}/>
              <input type = "password" placeholder='password' value={loginPassword} onChange={(e)=>setLoginPassword(e.target.value)}/>
              <input type="checkbox" value={stayLoggedIn} onChange={()=>setStayLoggedIn(!stayLoggedIn)}/>
              <button type = "submit">Login</button>
            </form>
            <button onClick={()=>setSignup(true)}>Switch to Signup</button>
          </>
        }
      </header>
    </div>
  );
}

export default App;
