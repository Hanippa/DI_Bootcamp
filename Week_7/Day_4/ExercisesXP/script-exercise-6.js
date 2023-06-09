// 🌟 Exercise 6 : Change the navbar


// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
//     First, create a new <li> tag (use the createElement method).
//     Create a new text node with “Logout” as its specified text.
//     Append the text node to the newly created list node (<li>).
//     Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).






div = document.getElementsByTagName('div')[0]

div.setAttribute('id' , 'socialNetworkNavigation')

new_li = document.createElement('li')

new_text = document.createTextNode('Logout')

new_li.appendChild(new_text)

div.children[0].appendChild(new_li)

console.log(div.children[0].firstElementChild.textContent)
console.log(div.children[0].lastElementChild.textContent)