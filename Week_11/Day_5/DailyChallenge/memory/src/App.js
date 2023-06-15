import { useState , useEffect} from 'react';
import './App.css';
import Herocard from './Herocard';
const herosjson = require('./superheros.json')

const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
  }
}

function App() {
  const [heros , setHeros] = useState([])
  const [score , setScore] = useState([])
  const [highScore , setHighScore] = useState(0)

  const handleClick = (name) => {
    if(!score.includes(name)){
      score.push(name)
      setScore([...score])
    }
    else{
      setScore([])
    }
    if (highScore < score.length){
      setHighScore(score.length)
    }
    shuffleArray(heros)
    setHeros([...heros])
    
  }
  
  useEffect(() => {
    setHeros(herosjson.superheroes)
  })
  
  return (
    <div className="App">
      <header className="App-header">
        <div className='navbar'>
        <h1>High Score {highScore}</h1>
        <h1>Score : {score.length}</h1>
        </div>
        <div className='main-container'>
        {heros.map((hero) => {
          return <Herocard  img={hero.image} name={hero.name} occupation={hero.occupation} handleClick={handleClick}/>
        })}
        </div>
      </header>
    </div>
  );
}

export default App;
