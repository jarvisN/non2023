import React from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import router from '../router';

const Home = () => {
    const navigate = useNavigate();
    const navigateTofirstPage = () => {
        navigate('/firstPage');
    };

    const navigateHome = () => {
        navigate('/');
    };
    return (
        <>
        // <router>

            <h1>
                My profile
            </h1>
            <button onClick={navigateHome}> Home </button>
            <button onClick={navigateTofirstPage}> FirstPage </button>
        // </router>

         </>
    );
};
export default Home;
