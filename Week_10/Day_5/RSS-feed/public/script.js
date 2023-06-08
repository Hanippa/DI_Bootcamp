
const title_search_button = document.getElementsByClassName('search-button-title')[0];
const category_search_button = document.getElementsByClassName('search-button-category')[0];

title_search_button.addEventListener('click' , (event) =>{
    
    event.preventDefault()
    const form = document.getElementsByClassName('search-title')[0]
    const title = form.title.value
    fetch(`http://localhost:8000/search/title?title=${title}`).then((res) => {
        console.log(res)
    })
})
category_search_button.addEventListener('click' , (event) =>{
    event.preventDefault()
    const form = document.getElementsByClassName('search-category')[0]
    const category = form.category.value
    fetch(`http://localhost:8000/search/category?category=${category}`).then((res) => {
        console.log(res)
    })
})