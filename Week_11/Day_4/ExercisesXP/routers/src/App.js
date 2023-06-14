import React from 'react';
import { Routes, Route, Link, NavLink, useParams, useLocation } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import ErrorBoundary from './ErrorBoundary';
import PostList from './PostList'

import Example1 from './Example1';
import Example2 from './Example2';
import Example3 from './Example3';



const webhook = async () => {
  const data = await fetch('https://webhook.site/e198add8-819b-4e4b-8dde-8ef3debb9ba5', {
    method:'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body:JSON.stringify({key1: 'myusername',
    email: 'mymail@gmail.com',
    name: 'Isaac',
    lastname: 'Doe',
    age: 27})
  })
  console.log(data)
}

const Home = () => {
  return (
    <h1>Home</h1>
  )
}
const Profile = () => {
  return (
    <h1>Profile</h1>
  )
}
const Shop = () => {
  return (
    <h1>Shop</h1>
  )
}


const App = () => {
  return (
  <>
        <Navbar bg="primary" variant="dark">
          <Container>
            <Navbar.Brand as={NavLink} to="/">Navbar</Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link as={NavLink} to="/">Home</Nav.Link>
              <Nav.Link as={NavLink} to="/profile">Profile</Nav.Link>
              <Nav.Link as={NavLink} to="/shop">Shop</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
        <button onClick={webhook}>webhook</button>
        <PostList/>
        <Example1/>
        <Example2/>
        <Example3/>
        <Routes>
      <Route path="/" element={<ErrorBoundary><Home/></ErrorBoundary>}/>
      <Route path="/profile"  element={<ErrorBoundary><Profile/></ErrorBoundary>} />
      <Route path="/shop" element={<ErrorBoundary><Shop/></ErrorBoundary>} />
    </Routes>
      </>
)};

export default App;