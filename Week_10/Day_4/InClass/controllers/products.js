const {getAllProducts , getProduct , searchProduct , insertProduct , deleteProduct , updateProduct} = require('../modules/products.js');




const _getAllProducts = (req,res) => {
    getAllProducts().then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
const _getProduct = (req,res) => {
    getProduct(req.params.id).then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
const _searchProduct = (req,res) => {
    searchProduct(req.params.name).then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}

const _insertProduct = (req,res) => {
    insertProduct(req.body).then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
const _deleteProduct = (req,res) => {
    deleteProduct(req.body).then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
const _updateProduct = (req,res) => {
    updateProduct(req.params.id,req.body).then(data => {
        res.json(data)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
module.exports = {
    _getAllProducts,
    _getProduct,
    _searchProduct,
    _insertProduct,
    _deleteProduct,
    _updateProduct
}