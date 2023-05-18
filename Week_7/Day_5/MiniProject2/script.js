


input = document.createElement('input')
body = document.getElementsByTagName('div')[0]
body.appendChild(input)


function number(num){
     input.value += num
    

}
function operator(operator){
     input.value += operator
}
function equal(){
    let result = eval(input.value)
    input.value = result

}
function resetcontent(){

    input.value = ''

}
function clearcontent(){

    input.value = ''
}