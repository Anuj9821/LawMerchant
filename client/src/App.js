// App.js
import React from 'react';
import './App.css';
import Hero from './components/Hero/hero';
import Navbar from './components/Navbar/navbar';
import Search from './components/Search/search';
import About from './components/About/about';

function App() {

  return (
    <div className="App">
      <div className='main-cnt'>
        <Navbar />
        <Hero />
        <Search/>
        <About/>
      </div>
    </div>
  );
}

export default App;
