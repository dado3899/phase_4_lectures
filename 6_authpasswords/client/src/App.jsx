import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  function buttonPost(){
    fetch('/api/students',
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        data: count
      })
    })
    .then(r=>r.json())
    .then(data=>console.log(data))
  }

  function getButton(){
    fetch('/api/students')
    .then(r=>r.json())
    .then(data => console.log(data))
  }

  function onLogin(e){
    e.preventDefault()
    console.log(e.target.user.value)
    console.log(e.target.password.value)
    fetch('/api/login',
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user: e.target.user.value,
        password: e.target.password.value
      })
    })
    .then(r=>r.json())
    .then(data=>console.log(data))
  }

  function handleLogout(){
    fetch('/api/logout', {method: "DELETE"})
    .then(r=>r.json())
    .then(data=>console.log(data))
  }

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <form onSubmit={onLogin}>
        <input name="user"></input>
        <input name="password"></input>
        <button type="Submit">Login</button>
      </form>
      <button onClick={buttonPost}>Post</button>
      <button onClick={getButton}>Get</button>
      <button onClick={handleLogout}>logout</button>
    </>
  )
}

export default App
