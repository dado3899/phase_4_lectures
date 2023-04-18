import Link from 'next/link'
import { useState } from 'react'
import { useRouter } from 'next/router'

function User({stud,test}) {
  const router = useRouter()
  console.log(stud,test)
  const { something } = router.query
  return (<p>Pid: {something}</p>)
  }

export default User;
  