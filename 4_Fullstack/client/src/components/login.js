import { useState } from "react"
function Login({setCurrUser}){
    //gbowers@example.org
    const [email,setEmail] = useState("")
    function handleLogin(e){
        e.preventDefault()
        fetch('/login',{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify({email:email}),
        })
        .then(r=>{
            if (r.ok){
                return r.json()
            }
            else{throw new Error}
        })
        .then(data=>{
            setCurrUser(data)
        })
        .catch(()=>alert("Not valid credentials"))
    }
    return(
        <form onSubmit={(e)=>handleLogin(e)}>
            <input placeholder="email" value={email} onChange={(e)=>setEmail(e.target.value)}/>
            <button type="submit">Login</button>
        </form>
    )
}
export default Login