
// Exercise 7 : My Book List
// Instructions

// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

//     In the body of the HTML page, create an empty section:
//     <section class="listBooks"></section>

//     In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
//         title,
//         author,
//         image : a url,
//         alreadyRead : which is a boolean (true or false).

//     Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

//     Requirements : All the instructions below need to be coded in the js file:
//         Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
//         For each book :
//             You have to display the book’s title and the book’s author.
//             Example: HarryPotter written by JKRolling.
//             The width of the image has to be set to 100px.
//             If the book is already read. Set the color of the book’s details to red.






const allBooks = [{'title':'One Piece','author':'echiro oda' , 'image' : 'https://ih1.redbubble.net/image.3304365345.6778/poster,504x498,f8f8f8-pad,600x600,f8f8f8.jpg' , 'alreadyRead' : false},
{'title':'Demons','author':'Fyodor Dostoevsky' , 'image' : 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1524586008l/5695.jpg' , 'alreadyRead' : true}]



const section = document.querySelector('.listBooks')


for (item of allBooks){
    div = document.createElement('div')
    image = document.createElement('img')
    image.setAttribute('src' , item.image)

    h1 = document.createElement('h1')
    title = document.createTextNode(item.title)
    h1.appendChild(title)

    h2 = document.createElement('h2')
    author = document.createTextNode(item.author)
    h2.appendChild(author)

    h22 = document.createElement('h2')
    alreadyread = document.createTextNode(item.alreadyRead)
    h22.appendChild(alreadyread)

    section.appendChild(h1)
    section.appendChild(h2)
    section.appendChild(h22)
    section.appendChild(image)
}
