
const from = document.getElementById('from')
const to = document.getElementById('to')
let amount = document.getElementById('amount')

let finalresult = document.getElementById('result')
const fetchOptions = async () => {
    result = await fetch('https://v6.exchangerate-api.com/v6/2d725187f3131c0f05f57cda/codes')
    resultjson = await result.json()
    return resultjson.supported_codes
}


fetchOptions().then((result) => {
    for (const currency of result){
        option = document.createElement('option')
        option.innerText = currency
        option.value = currency[0]
        option2 = document.createElement('option')
        option2.innerText = currency
        option2.value = currency[0]
        from.append(option)
        to.append(option2)
    }
})

const fetchConvertion = async (currencyfrom , currencyto) => {
    result = await fetch(`https://v6.exchangerate-api.com/v6/2d725187f3131c0f05f57cda/latest/${currencyfrom}`)
    resultjson = await result.json()
    return resultjson.conversion_rates[currencyto]
}

const displayResult = (value) => {
    finalresult.innerHTML = (value*amount.value).toFixed(2)
}

amount.addEventListener('input' , () => {fetchConvertion(from.value , to.value).then(result => displayResult(result))})
to.addEventListener('input' , () => {fetchConvertion(from.value , to.value).then(result => displayResult(result))})
from.addEventListener('input' , () => {fetchConvertion(from.value , to.value).then(result => displayResult(result))})