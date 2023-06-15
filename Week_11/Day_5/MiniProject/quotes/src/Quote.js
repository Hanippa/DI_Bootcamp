import './Quote.css';
import {useState , useEffect} from 'react'
const Quotes = require('./quotes-list.js')

const Quote = () => {
    const [quotenum , setQuotenum] = useState(0)

    useEffect(() => {
        setQuotenum(Math.floor(Math.random() * Quotes.length))
    })

    const handleClick = () => {
        document.getElementsByClassName('App-header')[0].style.backgroundColor = '#000000'
        let random = Math.floor(Math.random() * Quotes.length)
        while(random === quotenum){
            random = Math.floor(Math.random() * Quotes.length)
        }
        setQuotenum(random)
    }
      
    return ( <div className='quote-container'>
        <h1>{Quotes[quotenum].quote}</h1>
        <h4>{Quotes[quotenum].author}</h4>
        <button onClick={handleClick}>new quote</button>
        </div>
    )
}

export default Quote