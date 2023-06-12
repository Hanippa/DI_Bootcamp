import logo from './logo.svg';
import './App.css';
import Counter from './components/Counter';
import CounterC from './components/CounterC';
function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Counter/>
      <CounterC/>
      </header>
    </div>
  );
}

export default App;
