import logo from './logo.svg';
import './App.css';
import Car from './Components/Car';
import Events from './Components/Events';
import Phone from './Components/Phone';
import Color from './Components/Color'





function App() {

  const carinfo = {name: "Ford", model: "Mustang"};
  return (
    <div className="App">
      <header className="App-header">
      <Car carinfo={carinfo}/>
      <Events/>
      <Phone/>
      <Color/>
      </header>
    </div>
  );
}

export default App;
