div = document.getElementsByTagName('div')
console.log(div)
const lists = document.getElementsByClassName('list')
lists[0].children[1].innerHTML = 'Richard'

lists[1].children[1].remove()

for (i of document.getElementsByTagName('li')){
    i.innerHTML = 'Dekel'
}

document.getElementsByTagName('ul')[0].classList.add('class')
document.getElementsByTagName('ul')[1].classList.add('class')

document.getElementsByTagName('ul')[0].classList.add('university')
document.getElementsByTagName('ul')[0].classList.add('attentence')
div[0].style.backgroundColor='lightblue' 
div[0].style.padding='50px'
document.getElementsByTagName('body')[0].style.fontSize = '50px'



if (div[0].style.backgroundColor == 'lightblue'){
    alert(`Hello ${lists[0].children[0].innerHTML} and  ${lists[0].children[1].innerHTML}`)
}