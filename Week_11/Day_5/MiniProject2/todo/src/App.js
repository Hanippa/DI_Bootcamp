
import './App.css';
import { useState } from 'react';

function App() {
  const [todos , setTodos] = useState([])

  const addTodo = (e) => {
    e.preventDefault()
    setTodos([...todos , e.target.todo.value])
    e.target.todo.value = ''

  }

  const deleteTodo = (todo , e) => {
    const index = todos.indexOf(todo)
    todos.splice(index,1)
    setTodos([...todos])
  }
  return (
    <div className="App">
      <header className="App-header">
      {todos.map((todo) => {
            return (
              <h1 onClick={(e) => deleteTodo(todo , e)}>{todo}</h1>
            )
          })}
        <form onSubmit={(e) => addTodo(e)}>
          <input type='text' placeholder='to do' name='todo'></input>
        </form>
      </header>
    </div>
  );
}

export default App;
