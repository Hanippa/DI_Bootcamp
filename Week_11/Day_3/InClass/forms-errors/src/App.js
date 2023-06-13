import logo from './logo.svg';
import './App.css';
import Parent from './Components/Parent';
import Counter from './Components/Counter';
import ErrorBoundary from './ErrorBoundary';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Parent/>
        <ErrorBoundary>
      <Counter/>
      </ErrorBoundary>
      </header>
    </div>
  );
}

export default App;
