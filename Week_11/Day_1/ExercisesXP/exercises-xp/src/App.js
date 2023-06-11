import logo from './logo.svg';
import './App.css';
import UserFafoviteColors from './UserFavoriteColors';
import Exercise4 from './Exercise4';



// Exercise 3 : Object
// Instructions

// Using the following object:

// const user = {
//   firstName: 'Bob',
//   lastName: 'Dylan',
//   favAnimals : ['Horse','Turtle','Elephant','Monkey']
// };

//     In the React App, render the first name and the last name of the user in two <h3>.
//     In a separate Javascript file, create a new Component called UserFavoriteColors. Use props to pass the fav_animals array to the UserFavoriteColors component.
//     In the UserFavoriteColors component, use the map function to create a new array of <li>‘s.
//         Each <li> corresponds to one animal from the fav_animals array.
//         Display the <li>‘s. Tip : You can use the second parameter of the map function as a key to uniquely identify each HTML item

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>

        <UserFafoviteColors fav_animals={user.favAnimals}/>
        <Exercise4/>
      </header>
    </div>
  );
}

export default App;
