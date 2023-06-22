import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Navbar from './components/Navbar'
import Footer from './components/Footer';

import Landing from './components/Landing';
import Movie from './components/Movie';

function App() {
  return (
    <div className="App">


 <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Landing />}>
        <Route path="/home" element={<Landing />} />
        <Route exact path="/" component={Landing} />
            <Route exact path="/movie/:id" component={Movie} />
        </Route>
      </Routes>
      <Footer/>
    </BrowserRouter>
    </div>
  );
}

export default App;
