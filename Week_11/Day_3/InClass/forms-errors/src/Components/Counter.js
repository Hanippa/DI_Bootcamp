import React from 'react'
import { useState } from 'react'

const Counter = () => {

    const [count, setCount] = useState(0)

    const add = () => {
        setCount(count+1)
    }
    return (
        <>
        <h1>{count}</h1>
        <button onClick={add}>+</button>
        </>
    )
}

export default Counter