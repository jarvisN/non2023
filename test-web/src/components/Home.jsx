import React from 'react';
import MyButton from './MyButton';
import { Routes, Route, useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();
    const navigateToAbout = () => {
        navigate('/about');
    };

    const navigateHome = () => {
        navigate('/');
    };
    return (
        <>
            <h1>
                My profile
            </h1>
            <MyButton />
            <button onClick={navigateHome}> Home </button>
            <button onClick={navigateToAbout}> About </button>
        </>
    );
};
export default Home;
