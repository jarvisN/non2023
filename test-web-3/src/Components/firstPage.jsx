import React from 'react'
import { Routes,Route,useNavigate} from 'react-router-dom'


const firstPage = () =>{
    const navigate = useNavigate()
    const navigateSecond =()=>{
        navigate('/second')
    }
    const navigateFirst = () =>{
        navigate('/first')
    }
    return(
        <>
            <h1>
                testFirst
            </h1>
            <button onClick={navigateFirst}> First </button>
            <button onClick={navigateSecond}> Second </button>
        </>
    )

}

export default firstPage