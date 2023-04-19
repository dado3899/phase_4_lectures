import Link from 'next/link'
export default function home({currUser}){
    console.log(currUser)
    if(currUser){
        return <div> Hello {currUser.name}</div>
    }
    return <Link href="/login"> Please Log in </Link>
}