import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [customers,setCustomers] = useState([])

  useEffect(()=>{
    fetch("/api/customers")
    .then(r=>r.json())
    .then(data=>setCustomers(data))
  },[])

  function onDelete(id){
    fetch(`/api/customers/${id}`,{
      method:"DELETE"
    })
    .then(r=>{
      console.log(r)
      if(r.ok){
        return r.json()
      }
      else{
        console.log("NOT DELETED")
      }
    })
    .then(data => {
      console.log(data)
      const newCustomers = customers.filter((customer)=>customer.id!=id)
      setCustomers(newCustomers)
    })
  }
  function onSubmitCustomer(e){
    e.preventDefault()
    fetch('/api/customers',{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: e.target.name.value,
        email: e.target.email.value
      })
    })
    .then(r=>{
      if(r.ok){
        return r.json()
      }
      else{
        return undefined
      }
    })
    .then(data=>{
      if(data){
        setCustomers([...customers,data])
      }
      else{
        console.log("Not submitted")
      }
    })
  }
  function onUpdateCustomer(e,id){
    e.preventDefault()
    fetch(`/api/customers/${id}`,{
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: e.target.name.value
      })
    })
    .then(r=>r.json())
    .then(data=> {
      console.log(data)
      const newCust = customers.map((customer)=>{
        if (customer.id == id){
          return data
        }
        return customer
      })
      setCustomers(newCust)
    })
  }

  function onAddProduct(e,id){
    e.preventDefault()
    fetch('/api/custprod',{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: e.target.name.value,
        company: e.target.company.value,
        quantity: e.target.quantity.value,
        price: e.target.price.value,
        cust_id: id
      })
    })
  }

  return (
    <>
      <form onSubmit={(e)=>onSubmitCustomer(e)}>
        <input name="name"></input>
        <input name="email"></input>
        <button type="submit">Submit</button>
      </form>
      {customers.map((customer)=>{
        return(
          <div>
            <p>{customer.name}</p>
            <p>{customer.email}</p>
            <button onClick={()=>onDelete(customer.id)}> DELETE </button>
            <form onSubmit={(e)=>onUpdateCustomer(e,customer.id)}>
              <input name="name" defaultValue="NEW NAME"></input>
              <button type="Submit">Edit name</button>
            </form>
            <form onSubmit={(e)=>onAddProduct(e,customer.id)}>
              <input name="name"></input>
              <input name="company"></input>
              <input name="quantity"></input>
              <input name ="price"></input>
              <button type="submit">Buy product</button>
            </form>
          </div>
        )
      })}
    </>
  )
}

export default App
