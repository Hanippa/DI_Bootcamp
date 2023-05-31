const url = 'https://www.swapi.tech/api/people';
const options = {
	method: 'GET',
};
data_selector = ['height' , 'gender', 'birth_year' , 'homeworld']

person_container = document.getElementsByClassName('person-container')[0]
find_button = document.getElementsByClassName('find-button')[0]

const getRandomPerson = async () =>{
    const randomNumber = Math.floor(Math.random()*83)+1
    const personurl = `${url}/${randomNumber}`
    let load = document.createElement('div')
    load.innerHTML = '<div class="lds-ring"><div></div><div></div><div></div><div></div></div>'
    person_container.append(load)
    try {
        const response = await fetch(personurl, options);
        const result = await response.json();
        load.remove()
        return result;
    } catch (error) {
        load.remove()
        console.error(error);
    }
}

const displayPerson =async (person) => {

        const name = document.createElement('h1')
        name.innerHTML = person.properties.name
        person_container.append(name)

for(datapoint of Object.entries(person.properties)){
    if(data_selector.includes(datapoint[0])){
    let h2 = document.createElement('h2')
    if (datapoint[0] == 'homeworld'){
        let homeworldrequest =  await fetch(datapoint[1])
        let homeworld = await homeworldrequest.json()

        h2.innerText = `Home world : ${homeworld.result.properties.name}`
    }
    else{
    h2.innerText = `${datapoint[0]} : ${datapoint[1]}`}
    person_container.append(h2)
    }
}
}


find_button.addEventListener('click', () => {
    person_container.innerHTML = ''
    getRandomPerson().then(result => displayPerson(result.result))
})

