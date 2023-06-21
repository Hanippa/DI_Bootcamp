import './components/Search.css'
import {createContext, useState} from 'react'
import Search from './components/Search'

export const AppContext = createContext()
function App() {

  const [searchres, setSearchres] = useState([])
  return (
    <AppContext.Provider value={{searchres , setSearchres}}>
    <div className="App">
      <Search/>
    </div>
    </AppContext.Provider>
  );
}

export default App;
