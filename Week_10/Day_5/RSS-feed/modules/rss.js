
const Parser = require('rss-parser')

const parser = new Parser()


const getCategories = async () => {
    try {
      const feed = await parser.parseURL('https://thefactfile.org/feed/');
      const categories = [...new Set(feed.items.map(item => item.categories).flat())];
      return categories;
    } catch (error) {
      console.error('Error retrieving categories:', error);
      return [];
    }
  }


const getfactsitems = async () => {
    let feed = await parser.parseURL('https://thefactfile.org/feed/');
    return feed.items
  };

  const searhcitemscategory = async (category) => {
    let feed = await parser.parseURL('https://thefactfile.org/feed/');
    return feed.items
  };

  
  const searhcitemstitle = async (title) => {
    let feed = await parser.parseURL('https://thefactfile.org/feed/');
    return feed.items
  };

module.exports = {
    getCategories,
    getfactsitems,
    searhcitemscategory,
    searhcitemstitle
}
