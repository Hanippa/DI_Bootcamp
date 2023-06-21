import {useState , useEffect} from 'react'
const autocomplete = require('../autocomplete.json')

const api_key = 'xCL9WlTjw2PU8rQ1SfVMSG8QkVmI8Hri'

const Search = (params) => {

    const handleInput = (event) => {
        const inputValue = event.target.value;
        // fetch(`http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=${api_key}&q=${inputValue}&language=en-us` , {
        //     method:"GET"
        // })
        //   .then((response) => response.json())
        //   .then((data) => {
        //     setSearchres(data || []);
        //   })
        //   .catch((error) => {
        //     console.error('Error fetching API:', error);
        //   });
        setSearchres(autocomplete || []);
      };

    const [searchres, setSearchres] = useState([])
    return (
        <div>
            <input onChange={handleInput} type="text" placeholder="search"/>     
            <div className="autocomplete-container">
                {
                        searchres.map(res => {
                            return <h1>{res.LocalizedName}</h1>
                        })
                    
               }
            </div>
            </div>
    )
}

export default Search