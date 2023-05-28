// Instructions

//     Create a form with two fields (name, last name) and a submit button.
//     When you click the Send button, retrieve the data from the inputs, and append it on the DOM as a JSON string.

form = document.forms.id

const  handlesubmit = (e) => {
    e.preventDefault()
    h2 = document.createElement('h2')
    let object = {};
    const formdata = new FormData(form)
    formdata.forEach((value, key) => {
        object[key] = value;
    });
    
    const json = JSON.stringify(object);
    h2.innerText = json
    form.append(h2)
};
