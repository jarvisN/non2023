import React from 'react'
import HomePage from './components/Home'
import AboutPage from './components/About'
import { Route,Routes } from 'react-router-dom';

function Router() {
  return (
    <div>
      <Routes>
        <Route>
          <Route path="/" element={<HomePage />} />
          <Route path="about" element={<AboutPage />} />
        </Route>
      </Routes>
    </div>
  );
}

export default Router