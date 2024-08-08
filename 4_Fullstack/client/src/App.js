import logo from './logo.svg';
import './App.css';
import {useState,useEffect} from 'react'
import NewCustForm from './components/NewCustomerForm';
import Login from './components/login';


function App() {
  const [customers,setCustomers] = useState([])
  const [currUser,setCurrUser] = useState(undefined)
  useEffect(()=>{
    fetch('/customers')
    .then(r=>r.json())
    .then(data=>{
      setCustomers(data)
    })

  },[])

  function handleDelete(id){
    fetch(`/customers/${id}`,{
      method:"DELETE"
    })
    .then(r=>r.json())
    .then(data=>{
      const newCustArr = customers.filter(cust => {
        return cust.id != id
      })
      setCustomers(newCustArr)
    })
  }

  return (
    <div className="App">
      <h1>Who are you?</h1>
      <Login setCurrUser={setCurrUser}/>
      {
        customers.map(cust => {
          return (
            <>
              <p>{cust.name}</p>
              {cust.id===currUser?.id ? <button onClick={()=>handleDelete(cust.id)}>DELETE</button>: undefined}
            </>
          )
        })
      }
      <NewCustForm setCustomers={setCustomers} customers={customers}/>
    </div>
  );
}

export default App;
