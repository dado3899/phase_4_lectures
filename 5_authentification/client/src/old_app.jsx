import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  useEffect(()=>{
    fetch('/api/session')
    .then(r=>r.json())
    .then(data => setCount(data.count))
  },[])

  return (
    <>
    {
      count > 5 ?
      <div>NO MORE READING</div>
      :
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
        <button onClick={() => {
          fetch('/api/session')
        }}>Button2</button>
        <button onClick={() => {
          fetch('/api/session',
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              Test: "In session Chrome"
            })
          })
          .then(r => r.json())
          .then(data => setCount(data.count))
        }}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      </>
    }
    </>
  )
}

// export default App
