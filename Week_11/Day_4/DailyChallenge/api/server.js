const express = require('express');
const hello_router = require('./routes/hello.js')
const cors = require('cors')


const app = express();
port = 8000


app.listen(port, ()=> {
    console.log(`running on port ${port}`);
});



app.use(cors());
app.use(express.urlencoded({extended:true}));
app.use(express.json());


app.use('/api',hello_router.router)