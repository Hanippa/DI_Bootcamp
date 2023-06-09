// Instructions

//     Use Express to create a few routes:
//         The route /aboutMe/:hobby: displays the name of one hobby (ie. the value of the route parameter).
//             If the parameter is not a string (ie. numbers or else), set the status to 404.
//         The route /pic : displays an HTML file with a picture of your choice.
//         The route /form : displays an HTML file.
//             Requirements:
//                 The HTML file must be in the public folder.
//                 The HTML file must contain a form to contact you.
//                 The form must contain the inputs email and message. (add some HTML form validations)
//             Output:
//                 You should get the data and display it on the browser at the route /formData.
//                 For example, “john@gmail.com sent you a message “Love your new website”.





const express = require('express');

const app = express();

app.listen(3000, ()=>{
    console.log(`Server is running on http://localhost:3000`);
})

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

app.get('/aboutMe/:hobby',  (req, res)=>{
        const hobby = req.params.hobby
        if(Number(hobby)) {
          return res.status(418).json({message:'hobby is not a string'})
        }
        res.status(200).json(hobby)
      })

app.get('/pic',  (req, res)=>{
    res.sendFile(__dirname + '/kiwi.jpg');
})

app.get('/form', (req, res) => {
  res.sendFile(__dirname + '/public' + '/form.html');
});

app.post('/form', (req, res) => {
  const email = req.body.email;
  const message = req.body.message;


  res.send(`${email} sent you a message "${message}"`);
});
