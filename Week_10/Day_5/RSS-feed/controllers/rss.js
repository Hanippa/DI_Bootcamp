const {getfactsitems , searhcitemscategory , searhcitemstitle , getCategories} = require('../modules/rss.js');
const ejs = require('ejs');




const _home = (req,res) => {
    getfactsitems().then((result) => {
        res.render('index' , {
            'items' : result
        })
    })
    .catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}

const _search = (req,res) => {
    getfactsitems().then((result) => {
        getCategories().then((categories) => {
            res.render('search' , {
                'items' : result,
                'categories' : categories
            })
        })
    })
    .catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}


const _search_title = (req,res) => {
    searhcitemstitle(req.query.title).then((result) => {
        res.render('search' , {
            'items' : result
        })
    })
    .catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}

const _search_category = (req,res) => {
    searhcitemscategory(req.query.category).then((result) => {
        res.render('search' , {
            'items' : result
        })
    })
    .catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}


module.exports = {
    _home,
    _search,
    _search_category,
    _search_title
}