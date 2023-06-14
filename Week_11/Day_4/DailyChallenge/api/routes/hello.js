const express = require('express');

const router = express.Router();

const{_hello, _hello_post} = require('../controllers/hello.js')

router.get('/hello', _hello)
router.post('/hello', _hello_post)



module.exports = {
    router
}