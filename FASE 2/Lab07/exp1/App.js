import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Outlet, useParams } from 'react-router-dom';

import Home from './Home';
import About from './About';
import Services from './Services';
import Contact from './Contact';
import './App.css';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Inicio</Link>
          </li>
          <li>
            <Link to="/about">Acerca de</Link>
          </li>
          <li>
            <Link to="/services">Servicios</Link>
          </li>
          <li>
            <Link to="/contact">Contacto</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/services" element={<Services />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/user/:username" element={<User />} />
      </Routes>
    </Router>
  );
}

function User() {
  let { username } = useParams();
  return (
    <div>
      <h2>Usuario: {username}</h2>
    </div>
  );
}

export default App;
