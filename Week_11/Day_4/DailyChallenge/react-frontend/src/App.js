
import './App.css';
import React from 'react';
import {useState, useEffect} from 'react';



function App() {
  let [message , setMessage] = useState('');
  useEffect(() => {
    fetch('http://localhost:8000/api/hello')
    .then(data => data.json())
    .then(msg => {
      
      setMessage(msg.msg)
    })
  }, []) 

  const handleSumbit = (e) => {
    e.preventDefault()
    fetch('http://localhost:8000/api/hello' ,{
      method:'POST',
      body:e.target
    })
    .then(data => data.json())
    .then(message => {
      console.log(message)
      setMessage(message.msg)
    })

  }
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>{message}</h1>
        <form onSubmit={handleSumbit}>
          <input type='text' name='message'></input>
          <input type='submit'></input>
        </form>
      </header>
    </div>
  );
}

export default App;
