

const fetchGifs = async (q , rating , limit , offset , api_key) => {
    const url = `https://api.giphy.com/v1/gifs/search?q=${q}&rating=${rating}&api_key=${api_key}&limit=${limit}&offset=${offset}`
    let response = await fetch(url)
    if(response.status !== 200){
        throw new Error('cannot fetch gifs')
    }
    let json = await response.json()

    return json
}

const logdata = async (q , rating , limit ,offset, api_key) =>{
    let response = await fetchGifs(q , rating , limit,offset , api_key )
    let responseimg = document.createElement('iframe')
    responseimg.src = response.data[0].embed_url
    let div = document.createElement('div')
    div.classList.add('imagecon')
    let deleteimg = document.createElement('button')
    deleteimg.innerText = 'del'
    deleteimg.onclick = () => deleteImage(div);
    div.append(responseimg)
    div.append(deleteimg)

    document.getElementsByClassName('gifcontainer')[0].append(div)
    
}
const deleteImage = (div) => {
    div.remove();
  };

let deleteall = document.createElement('button')
deleteall.innerText = 'Delete All'
deleteall.addEventListener('click',() => {
    let gifcontainer = document.getElementsByClassName('gifcontainer');
    for (let i = 0; i < gifcontainer.length; i++) {
        let container = gifcontainer[i];
        container.innerHTML = '';

    }
})
document.getElementsByTagName('body')[0].append(deleteall)


form = document.forms[0]

form.addEventListener('submit', (event) => {
    event.preventDefault()
    category = form.category.value
    logdata(category, 'g' , 1, 0, 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
})