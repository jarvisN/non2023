import React from 'react'
import homePage from './components/homePage'
import firstPage from './components/firstPage'
import { Route,Routes } from 'react-router-dom';


function router() {
  return (
    <div>
        <Routes>
            <Route>
                <Route path = "/" element={<homePage/>}/>
                <Route path = "firstpage" element ={<firstPage/>}/>
            </Route>
        </Routes>
    </div>
  );
}

export default router