import { connect } from "react-redux";
import { INSERT, DELETE , UPDATE , UPDATE_INDEX } from "../redux/actions";
const TransactionList = (params) => {
    
    const updatefunc = (index) =>{
        params.updateinputs({...params.transactions[index]} , index)
    }
    return (
        <div>
            <h1>Transactions exercise xp week 12 day 2 redux</h1>
            <table>
                <thead>
                    <tr>
                        <th>account number</th>
                        <th>FSC</th>
                        <th>name</th>
                        <th>amount</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                {
                    
            params.transactions.map((transaction , index) => {
                return (
                    <tr key={index}>
                    <td>{transaction.accountNumber}</td>
                    <td>{transaction.FSC}</td>
                    <td>{transaction.name}</td>
                    <td>{transaction.amount}</td>
                    <td><button onClick={() => params.delete(index)}>delete</button></td>
                    <td><button onClick={() => updatefunc(index)}>edit</button></td>
                    </tr>
                )
            })
        }
        </tbody>
        </table>
        </div>
    )
}
const mapStateToProps = (state) => {
    return {
        transactions:state.transactions
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
export default connect(mapStateToProps , mapDispatchToProps)(TransactionList)