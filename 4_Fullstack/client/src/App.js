import logo from './logo.svg';
import './App.css';
import {useEffect} from 'react'

function App() {
  useEffect(()=>{
    fetch('/students')
    .then(r=>r.json())
    .then(data => console.log(data))
  },[])

  function handlePost(){
    fetch('/students',
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "Test",
        student_code: 100345,
        email: "student@student.com",
        emergency_email: "student@student.com"
      })
    })
    .then(r=>r.json())
    .then(data=>console.log(data))
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <button onClick={handlePost}>Button</button>
    </div>
  );
}

export default App;
