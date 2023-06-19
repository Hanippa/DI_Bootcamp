import { useState } from "react";
import { connect, useDispatch } from "react-redux";

import { INSERT, DELETE , UPDATE , UPDATE_INDEX } from "../redux/actions";
import TransactionList from "./TransactionList";
import './TransactionForm.css';


const TransactionForm = (params) => {
    const dispatch = useDispatch()

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
       
        e.preventDefault()
        if(params.currentIndex < 0){

            console.log('inserting');
            localStorage.setItem("transactions-storage",JSON.stringify([...params.transactions ,transaction]));
            params.insert(transaction)
        }
        else{

            const transactionarr = [...params.transactions];

            transactionarr[params.upda] = {...transaction};
            
            params.update(transaction)
            dispatch({type:'UPDATE-INDEX' , payload : -1});
        }
        setTransaction({accountNumber : '',FSC : '',name :'',amount:''});
    }
    const updateinputs = (obj , index) => {
        setTransaction(obj)
        dispatch({type:'UPDATE-INDEX' , payload : index});
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