import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Auth = ({ setIsAuthenticated }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistered, setIsRegistered] = useState(false);
  const navigate = useNavigate(); // Hook for navigation

  const handleSubmit = async (event) => {
    event.preventDefault();

    const url = isLogin
      ? 'http://localhost:8090/api/login'
      : 'http://localhost:8090/api/signup';

    const payload = { user_name: username, password };

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      if (response.ok) {
        if (isLogin) {
          setIsAuthenticated(true); // Set authentication state
          localStorage.setItem('isAuthenticated', true); // Save authentication state to local storage
          navigate('/home'); // Navigate to the home page
        } else {
          setIsRegistered(true); // Set state to indicate successful registration
          navigate('/login'); // Navigate to the login page after signup
        }
      } else {
        alert(data.error || 'Request failed. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="auth-container">
      <h2>{isLogin ? 'Login' : 'Sign Up'}</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">{isLogin ? 'Login' : 'Sign Up'}</button>
      </form>
      <div>
        {isLogin ? 'First time here?' : 'Already have an account?'}
        <button onClick={toggleAuthMode}>
          {isLogin ? 'Sign Up' : 'Login'}
        </button>
      </div>
      {isRegistered && <p>Registration successful! Proceed to login.</p>}
    </div>
  );
};

export default Auth;
