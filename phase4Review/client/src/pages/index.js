import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import {useEffect,useState} from 'react'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [user, setUser] = useState(null);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  useEffect(()=>{
    fetch('/checklogin')
    .then(r => r.json())
    .then(user => setUser(user))
  },[])
  function handleSubmit(e) {
    e.preventDefault();
    const data = {
      "name": username,
      "password": password
    }

    fetch("/login",{
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
    .then(r => r.json())
    .then(user=>setUser(user))
  }
  console.log(user)
  
  function handleLogout(e) {
    e.preventDefault();
    fetch("/logout",{
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
  }
  
  function checktype(e) {
    e.preventDefault();
    fetch("/get_type")
    .then(r => r.json())
    .then(data => console.log(data))
  }

  if (user) {
    return (
    <>
    <h2>Welcome, {user.name}!</h2>
      <form onSubmit={handleLogout}>
        <button type="submit">Logout</button>
      </form>
      <form onSubmit={checktype}>
        <button type="submit">checktype</button>
      </form>
    </>
    );
  } else {
    return (
      <form onSubmit={handleSubmit}>
        <p>Username</p>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <p>password</p>
        <input
          type="text"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    )
  }
}
