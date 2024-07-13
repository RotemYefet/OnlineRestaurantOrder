import React from 'react';
import { Link } from 'react-router-dom';

const Header = ({ handleLogout, isAuthenticated }) => {
  return (
    <header>
      <nav>
        <ul className="navigation">
          <li><Link to="/home">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/menu">Menu</Link></li>
          <li><Link to="/payment">Payment</Link></li>
          {isAuthenticated && <li><button onClick={handleLogout}>Logout</button></li>}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
