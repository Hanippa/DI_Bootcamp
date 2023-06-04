const largeNumber = 356;

const currentdatetime = () => {
    let currentdate = new Date();
    return "Last Sync: " + currentdate.getDay() + "/" + currentdate.getMonth() 
    + "/" + currentdate.getFullYear() + " @ " 
    + currentdate.getHours() + ":" 
    + currentdate.getMinutes() + ":" + currentdate.getSeconds();
}


module.exports = {
    currentdatetime,
    largeNumber
}