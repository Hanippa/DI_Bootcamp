import { useContext } from 'react';
import { AppContext } from '../App';

const api_key = 'fDtMRB4Zsh0cFBqspsmIqrcJFpC0mQ9YIwV3M36GrJUoPDgetnHqa5xC'






const Search = (props) => {


    const {searchres , setSearchres} = useContext(AppContext)

    const searchphotos = (search) => {
  
        fetch(`https://api.pexels.com/v1/search?query=${search}&per_page=20` , {
          method:"GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: api_key
          }
      })
        .then((response) => response.json())
        .then((data) => {
          setSearchres(data.photos)
        })
        .catch((error) => {
          console.error('Error fetching API:', error);
        });
    }
    const handleSubmit = (e) => {
        e.preventDefault()
        searchphotos(e.target.searchvalue.value)
    }
    
    return (
        <div>
            

            <form onSubmit={handleSubmit}>   
            <label htmlFor="default-search" className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
            <div className="relative">
                <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <svg aria-hidden="true" className="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                <input name='searchvalue' type="search" id="default-search" className="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Mockups, Logos..." required/>
                <button type="submit" className="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
            </div>
        </form>
            <button  className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded" onClick={() => searchphotos('Mountain')}>Mountain</button>
            <button  className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded" onClick={() => searchphotos('Beaches')}>Beaches</button>
            <button  className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded" onClick={() => searchphotos('Birds')}>Birds</button>
            <button  className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded" onClick={() => searchphotos('Food')}>Food</button>
            

    <div className="grid grid-cols-2 md:grid-cols-3 gap-4 m-10 border-x-4 border-indigo-500 p-5">
  

        {searchres.map((res , i) => {
            return <div  key={i}><img className="object-cover h-70 w-120 h-50 max-w-full rounded-lg" key={i} src={res.src.large} alt={res.id}/></div>
            
        })}
        </div>
        </div>
    )
}
export default Search