let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => groceries.fruits.forEach(fruit => console.log(fruit))

displayGroceries()


const cloneGroceries = () => {
    const user = client
    client = "Betty"
    const shopping = groceries
    shopping.totalPrice = 35 // we will see the modification in groceries becuase the is not a copy, but a pointer to the same variable in memory.
    shopping.payed = false // same ""
    console.log(shopping)

}
console.log(groceries)
cloneGroceries()