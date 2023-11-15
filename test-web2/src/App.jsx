import { useState } from 'react'
import './App.css'
import { Routes, Route, useNavigate } from 'react-router-dom';
import router from './router.jsx';

function App() {
  // const [count, setCount] = useState(0)
  // const [name, setName] = useState("Non")

  const navigate = useNavigate();
  // const navigateToAbout = () => {
  //   navigate('/about');
  // };

  // const navigateHome = () => {
  //   navigate('/');
  // };

  return (
    // <>
    <router>
      <h1>
        My profile
      </h1>
      {/* <button onClick={navigateHome}> Home </button>
      <button onClick={navigateToAbout}> About </button> */}
    </router>
    // </>
  )
}

export default App
