import logo from './logo.svg';
import './App.css';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Carousel>
                <div>
                    <img src="/images/panda.png" alt='panda'/>
                    <p className="panda">Panda</p>
                </div>
                <div>
                    <img src="/images/foxes.png" />
                    <p className="foxes">Foxes</p>
                </div>
                <div>
                    <img src="/images/kiwi.png" />
                    <p className="Kiwis">Kiwis</p>
                </div>
            </Carousel>
      </header>
    </div>
  );
}

export default App;
