const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const products_router = require('./routes/products.js')

const app = express();
dotenv.config()

app.listen(process.env.PORT || 3000 ,() => {
    console.log(`server running on port ${process.env.PORT || 3000}`)
});


app.use(cors());
app.use(express.urlencoded({extended:true}))
app.use(express.json())
app.use( '/api' , products_router.router)



