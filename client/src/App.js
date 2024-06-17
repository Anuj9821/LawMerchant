// App.js
import React from 'react';
import './App.css';
import Hero from './components/Hero/hero';
import Navbar from './components/Navbar/navbar';

function App() {

  return (
    <div className="App">
      <div className='main-cnt'>
        <Navbar />
        <Hero />
      </div>
    </div>
  );
}

export default App;
