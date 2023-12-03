import React, { Component } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Navbar from "./components/Navbar";
import LoginPage from "./components/LoginPage";
import RegPage from "./components/RegPage";
import About from "./components/About";

// import axios from "axios";
// import { API_URL } from "./config";

// const LOCALHOST = `${API_URL}`;

class AppRouter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      eventData: [],
    };
  }

  //   componentDidMount() {
  //     // axios
  //     //   .get(`${LOCALHOST}/api/events/`)
  //     //   .then((response) => {
  //     //     this.setState({ eventData: response.data });
  //     //   })
  //     //   .catch((error) => {
  //     //     console.error("Error fetching data:", error);
  //     //   });
  //   }

  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/about" element={<About />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<RegPage />} />
          {/* <Route path="/create" element={<CreateEvent />} />
          <Route path="/:eventLink" element={<EventPage events={this.state.eventData} />} /> */}
        </Routes>
      </BrowserRouter>
    );
  }
}

export default AppRouter;
