import React from "react";
import "../css/Navbar.css"; // Updated import path
import "bootstrap/dist/css/bootstrap.min.css";
import { NavLink } from "react-router-dom"; // Import NavLink instead of Link

const Navbar = () => {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-blurry">
        <div className="container">
          <img src="/logo.png" alt="AMIREM Logo" className="navbar-logo" />
          <div className="collapse navbar-collapse justify-content-left mx-4" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? "nav-link active-link" : "nav-link")} exact to="/">
                  Home
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? "nav-link active-link" : "nav-link")} to="/about">
                  About
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? "nav-link active-link" : "nav-link")} to="/terms">
                  Terms
                </NavLink>
              </li>
            </ul>
          </div>
          <div className="d-flex align-items-center ms-auto">
            <NavLink className={({ isActive }) => (isActive ? "sf-link active" : "sf-link")} exact to="/login">
              Login
            </NavLink>
            {/* <i className='text-white'>/</i> */}
            <NavLink className="sf-link" to="/signup">
              Signup
            </NavLink>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
