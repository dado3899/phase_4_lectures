import { useState } from "react"

function NewCustForm({customers,setCustomers}){
    const [name,setName] = useState("")
    const [email,setEmail] = useState("")
    const [semail,setSEmail] = useState("")
    function handlePost(e){
        e.preventDefault()
        const new_cust = {
            name: name,
            email: email,
            email2: semail ? semail : undefined
        }
        fetch('/customers',{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify(new_cust),
        })
        .then( r =>{
            if(r.ok){
                return r.json()
            }
            else{
                throw new Error
            }
        })
        .then( data =>{
            setCustomers([...customers,data])
        })
        .catch(()=>alert("Not valid data"))
            
    }


    return(
        <form onSubmit={(e)=> handlePost(e)}>
            <input placeholder="name" value={name} onChange={(e)=>setName(e.target.value)}/>
            <input placeholder="email" value={email} onChange={(e)=>setEmail(e.target.value)}/>
            <input placeholder="secondary email" value={semail} onChange={(e)=>setSEmail(e.target.value)}/>
            <button type="submit">Submit</button>
        </form>
    )
}

export default NewCustForm