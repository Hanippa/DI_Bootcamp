import {useState} from 'react'


const getctime = () => {
    const cdate = new Date()
    const ctime = `${cdate.getHours()} : ${cdate.getMinutes()} : ${cdate.getSeconds()}`
    return ctime

}

const Clock = () => {


    const [time , setTime] = useState(getctime())
    setInterval(() => {
        setTime(getctime)
    }, 1000)

    return (
        <h1>{time}</h1>
    )

}

export default Clock