import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import {useEffect,useState} from 'react'
import Link from 'next/link'
import { Router, useRouter } from 'next/router'

const inter = Inter({ subsets: ['latin'] })

export default function Home({currUser,loggedIn}) {
  const router = useRouter()
  // if(!loggedIn){
  //   router.push('/login')
  //   return <div>Not logged in</div>
  // }
  const [user, setUser] = useState(null);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [display, setDisplay] = useState("Hello")
  const [num, setNum] = useState(0)
  
  console.log(loggedIn)
  
  // useEffect(()=>{
  //   fetch('/checklogin')
  //   .then(r => r.json())
  //   .then(user => setUser(user))
  // },[])
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

  const cityList = [
    {
      country: "USA",
      city: "NewYork",
    },
    {
      country: "Spain",
      city: "Madrid",
    },
    {
      country: "England",
      city: "London",
    },
  ];
  
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
  function sendprops() {
    router.push("/test")
  }

  const test = 'test'
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
      <>
      <Link as = {`user/${test}`} href="/user/[something]">Link</Link>
      <a onClick={()=>sendprops()}>click</a>
      <ul>
      {cityList.map((item, index) => (
        <li key={index}>
          <Link as={`/${item.country}/${item.city}`} href="/[country]/[city]">
              {item.country}-{item.city}
          </Link>
        </li>
      ))}
      </ul>
      <button type="button" onClick={() => router.push('/user/test')}>
        Click me
      </button>
      <div>{display}</div>
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
      </>
    )
  }
}
