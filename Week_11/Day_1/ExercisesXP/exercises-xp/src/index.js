import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));

const h1 = React.createElement('h1' , null , 'I do not use JSX')

// Exercise 2: with JSX
// Instructions

//     Display a “Hello World!” message on the page.
//     Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page.
//     Create a constant variable named sum, which value is 5 + 5. Render on the page, the following sentence "React is <sum> times bette
const myelement = <h1>I Love JSX!</h1>;
const sum = 5+5


// Exercise 1 : no JSX
// Instructions

//     Create an element without JSX and render it. The element should be an <h1> with the content “I do not use JSX”

const better = <h1>React is {sum} times better with JSX</h1>



root.render(
  // <React.StrictMode>
  //   <App />
  // </React.StrictMode>
  <>
  <App/>
  {myelement}
  {h1}
  {better}
  </>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
