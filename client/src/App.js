// App.js
import React from 'react';
import './App.css';
import Hero from './components/Hero/hero';
import Navbar from './components/Navbar/navbar';
import Search from './components/Search/search';

function App() {

  return (
    <div className="App">
      <div className='main-cnt'>
        <Navbar />
        <Hero />
        <Search/>
      </div>
    </div>
  );
}

export default App;
