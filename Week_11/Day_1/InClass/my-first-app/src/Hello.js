import './Hello.css'
import React from 'react'

const Hello = () => {
    const users = [{
        username:'Mia',
        email:'Mia@gmail.com'
    },
    {
        username:'Lisa',
        email:'Lisa@gmail.com'
    },
    {
        username:'Sarha',
        email:'Sarha@gmail.com'
    }]
    return (
        <div className="users-container" style={{color:"lightpink",border:"2px solid lightpink", padding:"20px"}}>
            {users.map(item => {
                return (
                    <h1 key={item.username}>{item.email} - {item.username}</h1>
                )
            })}
        </div>
    )
}

export default Hello