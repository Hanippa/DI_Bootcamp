import { useState , useEffect } from "react"

const Counter = (props) => {
    const [count, setCount] = useState(0)

    useEffect(()=>{
        console.log('effect')
    } , [])
    const handleClick = () => {
        console.log(count)
        setCount(count+1)
        
        
    }

    return(
        <div>
            <h1>Counter:</h1>
            <h2>{count}</h2>
            <button onClick={handleClick}>Add</button>
        </div>
    )
}

export default Counter