import logo from './logo.svg';
import './App.css';
import {useEffect,useState} from 'react'

function App() {
  const [customers, setCustomers] = useState([])
  const [name,setName] = useState("")
  const [email,setEmail] = useState("")
  // const [newName,setNewName] = useState("")

  useEffect(()=>{
    fetch('/customers')
    .then(r=>r.json())
    .then(data=>setCustomers(data))
  },[])
  
  function addCustomer(e){
    e.preventDefault()
    fetch('/customers',{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        email: email
      }),
    })
    .then(r=>r.json())
    .then(data=>{
      if(data.error){
        alert(data.error)
      }
      else{
        setCustomers([...customers,data])
      }
    })
  }
  function changeName(e,id){
    e.preventDefault()
    fetch(`/customers/${id}`,{
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: e.target.newName.value
      }),
    })
    .then(r=>{
      if (r.ok){
        return r.json()
      }
      else{
        return false
      }
    })
    .then(data=>{
      if (data){
        setCustomers(
          customers.map((customer)=>{
            if( customer.id == id){
              return data
            }
            else{
              return customer
            }
          })
        )
      }
      else{
        alert("Cannot change to that name")
      }
    })
  }

  function handleDelete(id){
    fetch(`/customers/${id}`,{
      method: "DELETE"
    })
    .then(r=>{
      if (r.ok){
        setCustomers(customers.filter(customer=>{
          if (customer.id == id){
            return false
          }
          return true
        }))
      }
      else{
        alert("Cannot delete")
      }
    })
  }

  return (
    <div>
      <form onSubmit={(e)=>addCustomer(e)}>
        <input value = {name} onChange={(e)=>setName(e.target.value)}/>
        <input value = {email} onChange={(e)=>setEmail(e.target.value)}/>
        <button type="submit">Submit</button>
      </form>
      <ul>
        {
          customers.map((customer)=>{
            return (
            <div>
              <button onClick={()=>handleDelete(customer.id)}>Delete</button>
              {customer.name}
              <form onSubmit={(e)=>changeName(e,customer.id)}>
                <input name={"newName"}/>
              </form>
            </div>
            )
          })
        }
      </ul>

    </div>
  );
}

export default App;
