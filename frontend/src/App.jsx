import React, { useState, useEffect } from "react";
import { Routes, Route, Navigate, useLocation, useNavigate } from 'react-router-dom';
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Users from "./pages/Users/Users";
import Home from "./pages/Users/Home";
import Menu from "./pages/Users/Menu";
import About from "./pages/Users/About";
import Payment from "./pages/Users/Payment";
import Auth from "./pages/auth/Auth";
import Header from "./components/Header";
import PrivateRoute from "./components/PrivateRoute"; // Import the PrivateRoute component

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true); // Add loading state
  const navigate = useNavigate(); // Hook for navigation

  useEffect(() => {
    // Check local storage for authentication state on initial load
    const storedAuthState = localStorage.getItem('isAuthenticated');
    if (storedAuthState) {
      setIsAuthenticated(JSON.parse(storedAuthState));
    }
    setIsLoading(false); // Set loading to false after checking local storage
  }, []);

  const handleLogin = () => {
    setIsAuthenticated(true);
    localStorage.setItem('isAuthenticated', true); // Save authentication state to local storage
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('isAuthenticated'); // Remove authentication state from local storage
    navigate("/login"); // Redirect to login page
  };

  const location = useLocation();
  const showHeader = location.pathname !== "/login";

  if (isLoading) {
    return <div>Loading...</div>; // Show loading indicator while checking authentication state
  }

  return (
    <div>
      {showHeader && <Header handleLogout={handleLogout} isAuthenticated={isAuthenticated} />}
      <Routes>
        <Route path="/home" element={<PrivateRoute isAuthenticated={isAuthenticated}><Home /></PrivateRoute>} />
        <Route path="/about" element={<PrivateRoute isAuthenticated={isAuthenticated}><About /></PrivateRoute>} />
        <Route path="/menu" element={<PrivateRoute isAuthenticated={isAuthenticated}><Menu /></PrivateRoute>} />
        <Route path="/payment" element={<PrivateRoute isAuthenticated={isAuthenticated}><Payment /></PrivateRoute>} />
        <Route path="/users" element={<PrivateRoute isAuthenticated={isAuthenticated}><Users /></PrivateRoute>} />
        <Route path="/login" element={<Auth setIsAuthenticated={handleLogin} />} />
        <Route path="*" element={<Navigate to="/home" />} /> {/* Redirect any unknown paths to /home */}
      </Routes>
    </div>
  );
};

export default App;
