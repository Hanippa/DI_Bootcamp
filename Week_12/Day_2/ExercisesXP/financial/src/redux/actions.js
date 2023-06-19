export const INSERT = transaction => {
    return {
        type: 'INSERT',
        payload: transaction
    }
}

export const UPDATE = transaction => {
    return {
        type: 'UPDATE',
        payload: transaction
    }
}

export const UPDATE_INDEX = index => {
    return {
        type: 'UPDATE-INDEX',
        payload: index
    }
}

export const DELETE = index => {
    return {
        type: 'DELETE',
        payload: index
    }
}