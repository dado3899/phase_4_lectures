import Link from 'next/link'
import { useState } from 'react'
import { useRouter } from 'next/router'

function User(props) {
  const router = useRouter()
  console.log(props)
  const { something } = router.query
  return (<p>Pid: {something}</p>)
  }

export default User;
  