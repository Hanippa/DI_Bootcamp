const getMyProducts = async () => {
    try{
        const res = await fetch('localhost:8000/api/products');
        const data = await res.json();
        console.log(data)
    }
    catch (e){
        console.log(e)
    }
}