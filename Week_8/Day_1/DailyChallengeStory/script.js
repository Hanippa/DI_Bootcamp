const form = document.getElementById('libform')

const button = document.getElementsByTagName('button')[0]

sentence = '3 jumped in the 2 1 and gone with the 4 in 5.'

button.addEventListener('click' , (e) => {
e.preventDefault();
const words = []
let i = 1
for (input of form.getElementsByTagName('input')){
    input.value = input.value.replaceAll(" " , "")
    if(input.value.length >= 3){
        sentence = sentence.replace(i.toString() , input.value)
    }
    i++
}
console.log(sentence)
})
