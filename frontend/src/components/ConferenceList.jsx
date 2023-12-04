import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { API_URL } from "../config";

const LOCALHOST = `${API_URL}`;

const ConferenceList = ({ name, acronym, description, thumbnail, organizers, submissionStart, submissionDeadline, conferenceDate, place, website, reviewers }) => {
  console.log("PPPPPPPPP", organizers);
  const organizerz = Array.from(new Set(organizers.map((item) => item.id))).map((id) => organizers.find((item) => item.id === id));
  return (
    <Link to={`conference/${acronym}`}>
      <div className="conference-wrap">
        <img className="conference-image" src={thumbnail} alt={acronym} />
        <div className="conference-details">
          <div className="conference-title">{name}</div>
          <div className="conference-date">
            <i className="bi bi-clock " style={{ marginRight: "6px" }} />
            {conferenceDate} &nbsp; - &nbsp; Submission Start: {submissionStart}, Submission End: {submissionDeadline}
          </div>
          <dv className="conference-locaton">
            <i className="bi bi-geo-alt" style={{ marginRight: "6px" }} />
            {place} - {organizerz.map((organizer, index) => organizer.username).join(", ")}
          </dv>
          <div className="conference-description">{description}</div>
        </div>
      </div>
    </Link>
  );
};

export default ConferenceList;
