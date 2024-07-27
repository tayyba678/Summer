import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Education from './components/Education';
import Skills from './components/Skills';
import Contact from './components/Contact';


function App() {
  return (
    <div>
      <Navbar/>
      <Hero />
      <About />
      <Education />
      <Skills />
      <Contact />
    </div>
  );
}

export default App;
