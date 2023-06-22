import { ReactDOM } from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import { Outlet, Link } from "react-router-dom";


import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Contact from "./components/Contact";
import About from "./components/About";
import Post from "./components/Post";


function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home />}>
        <Route path="/home" element={<Home />} />

        </Route>
        <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/post/:id" element={<Post />} />
      </Routes>
    </BrowserRouter>

  );
}

export default App;
