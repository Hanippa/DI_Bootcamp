import { useState } from "react";
import { connect } from "react-redux";
import { INSERT, DELETE , UPDATE , UPDATE_INDEX } from "../redux/actions";
import TransactionList from "./TransactionList";



const TransactionForm = (params) => {

    const [transaction , setTransaction] = useState( {
        accountNumber : '',
        FSC : '',
        name :'',
        amount:''
    })

    

    const handleInputChange = (e) => {
        
        const data = e.target.value
        setTransaction({...transaction , [e.target.name] : data})
    }
    const handleSubmit = (e) => {
        console.log('handle submit');
        e.preventDefault()
        localStorage.setItem("transactions-storage",JSON.stringify([...params.transactions ,transaction]));
        params.insert(transaction)
    }
    const handleUpdate = (e , index) => {
        console.log('handleupdate')
        e.preventDefault()
        const transactionarr = [...params.transactions]
        transactionarr[index] = {...transaction}
        console.log('transactiono arrya => ',transaction)
        // localStorage.setItem("transactions-storage",JSON.stringify([...transactionarr]));
        // params.update(transaction)
        const form = document.getElementById("tranform")
        form.onsubmit = handleSubmit
    }
    const updateinputs = (obj) => {
        setTransaction(obj)
        const form = document.getElementById("tranform")
        form.onsubmit = handleUpdate
        console.log(form.onsubmit);
    }

    
    return (
        
        <div>
            <TransactionList updateinputs={updateinputs}/>
            <form onSubmit={handleSubmit} id="tranform">
                <input value={transaction.accountNumber} onChange={handleInputChange} type="text" placeholder="account number" name="accountNumber" id="accountnumber"/>
                <input value={transaction.FSC} onChange={handleInputChange} type="text" placeholder="FSC"  name="FSC" id="fsc"/>
                <input value={transaction.name} onChange={handleInputChange} type="text" placeholder="name"  name="name" id="name"/>
                <input value={transaction.amount} onChange={handleInputChange} type="number" placeholder="amount"  name="amount" id="amount"/>
                <input type="submit" placeholder="submit"/>
            </form>
        </div>
    )
}

const mapStateToProps = (state) => {
    return {
        transactions:state.transactions,
        currentIndex:state.currentIndex
    }
}

const mapDispatchToProps = dispatch => {
    return {
    insert: (payload) => dispatch(INSERT(payload)),
    delete: (payload) => dispatch(DELETE(payload)),
    update: (payload) => dispatch(UPDATE(payload)),
    update_index: (payload) => dispatch(UPDATE_INDEX(payload))
    }
}

export default connect(mapStateToProps , mapDispatchToProps)(TransactionForm)