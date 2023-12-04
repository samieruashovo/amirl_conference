import React from "react";
import "../css/Homepage.css";
import "../css/ConferenceList.css";
import { Clock } from "react-bootstrap-icons";
import { Link } from "react-router-dom";
import ConferenceList from "./ConferenceList";
import Conference from "./Conference";
import axios from "axios";
import { API_URL } from "../config";

const LOCALHOST = `${API_URL}`;

const HomePage = ({ conferences }) => {
  function truncateDescription(text, maxLength = 300) {
    if (text.length > maxLength) {
      return text.slice(0, maxLength) + "...";
    }
    return text;
  }

  function formatDate(date) {
    const options = { year: "numeric", month: "long", day: "numeric" };
    const formattedDate = new Date(date).toLocaleDateString(undefined, options);
    return formattedDate;
  }
  const [organizers, setOrganizers] = React.useState([]);

  React.useEffect(() => {
    conferences.forEach((conference) => {
      conference.organizers.forEach((organizer) => {
        axios
          .get(`${LOCALHOST}/api/user/${organizer}/`)
          .then((response) => {
            setOrganizers((prevOrganizers) => [...prevOrganizers, response.data]);
          })
          .catch((error) => {
            console.error("Error fetching data", error);
          });
      });
    });
  }, [conferences]);
  console.log("organizers", organizers);
  return (
    <>
      {/* <div className="banner">
        <h1 class="title">Welcome to AMIR Editorial Management</h1>
      </div> */}

      <div class="image-box">
        <div class="image-box__background"></div>
        <div class="image-box__overlay"></div>
        <div class="image-box__content">
          <h1 class="title">Welcome to AMIR Editorial Management</h1>
          <br />
          <div class="t">Create conference virtually and manage the paper submission and review process.</div>
          <div className="mt-4">
            <Link
              to="/conference/host"
              class="bnr-btn"
              style={{
                marginRight: "10px",
              }}
            >
              Host a Conference
            </Link>
            <a href="" class="bnr-btn">
              Learn More
            </a>
          </div>
        </div>
      </div>
      <div className="container mt-5 ">
        <h3>RECENT CONFERENCES</h3>

        <hr />

        {conferences.map((conference, index) => (
          <ConferenceList conferenceID={conference.id} key={index} name={conference.name} acronym={conference.acronym} description={truncateDescription(conference.description)} organizers={organizers} submissionStart={formatDate(conference.submission_start)} submissionDeadline={formatDate(conference.submission_deadline)} conferenceDate={formatDate(conference.conference_date)} place={conference.place} website={conference.website} reviewers={conference.reviewers} thumbnail={conference.thumbnail} />
        ))}
      </div>
    </>
  );
};

export default HomePage;
