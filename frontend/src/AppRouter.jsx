import React, { Component } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Navbar from "./components/Navbar";
import LoginPage from "./components/LoginPage";
import RegPage from "./components/RegPage";
import About from "./components/About";
import CreateConference from "./components/CreateConference";
import Conference from "./components/Conference";

import axios from "axios";
import { API_URL } from "./config";
import ConferenceList from "./components/ConferenceList";

const LOCALHOST = `${API_URL}`;

class AppRouter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      eventData: [],
    };
  }

  componentDidMount() {
    axios
      .get(`${LOCALHOST}/conference/`)
      .then((response) => {
        this.setState({ eventData: response.data });
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }

  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App conferences={this.state.eventData} />} />
          <Route path="/conference/host" element={<CreateConference />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<RegPage />} />
          <Route path="/about" element={<About />} />
          <Route path="/conference/ag2023" element={<Conference />} />
          {/* <Route path="/create" element={<CreateEvent />} /> */}
          {/* <Route path="/" element={<ConferenceList />} /> */}
        </Routes>
      </BrowserRouter>
    );
  }
}

export default AppRouter;
