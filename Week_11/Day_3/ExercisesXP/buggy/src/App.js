import logo from './logo.svg';
import './App.css';
import React from 'react'
import ErrorBoundary from './ErrorBoundary';
import Color , Child} from './Components/Color'

class BuggyCounter extends React.Component{
  constructor(props){
    super(props)
    this.state = {counter:0}
  }
  handleclick = () => {
    this.setState({counter:this.state.counter+1})
  }
  render(){
    if(this.state.counter > 5){
      throw new Error('five');
    }
    return (
      <h1 onClick={this.handleclick}>{this.state.counter}</h1>
    )
  }
}


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Child/>
        <Color/>
        <ErrorBoundary>
      <BuggyCounter/>
      </ErrorBoundary>
      </header>
    </div>
  );
}

export default App;
