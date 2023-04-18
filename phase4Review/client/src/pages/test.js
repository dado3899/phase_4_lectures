import { useRouter } from 'next/router'
export default function Test() {
    const router = useRouter()
    const { num,setNum } = router.query
    console.log(setNum)
    return (
    <>
    <div>{num}</div>
    <button onClick={()=>setNum(num+1)}>plus</button>
    </>
    )
}