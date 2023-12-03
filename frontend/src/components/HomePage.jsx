import React from "react";
import "../css/Homepage.css";
import "../css/ConferenceList.css";
import { Clock } from "react-bootstrap-icons";

const HomePage = () => {
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
          <p class="text">Create conference virtually and manage the paper submission and review process.</p>
          <div className="mt-4">
            <a
              href=""
              class="bnr-btn"
              style={{
                marginRight: "10px",
              }}
            >
              Host a Conference
            </a>
            <a href="" class="bnr-btn">
              Learn More
            </a>
          </div>
        </div>
      </div>
      <div className="container mt-4 ">
        <h3>RECENT CONFERENCES</h3>
        <hr />
        <a href="#">
          <div className="conference-wrap">
            <img className="conference-image" src="https://images.pexels.com/photos/974314/pexels-photo-974314.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="" srcset="" />
            <div className="conference-details">
              <div className="conference-title">Confernece on Agriculture</div>
              <div className="conference-date">
                <i className="bi bi-clock " style={{ marginRight: "6px" }} />
                Sunday, Mar 24, 2024 &nbsp; - &nbsp; Submission Start: Mar 27, End: Apr 27
              </div>
              <dv className="conference-locaton">
                <i className="bi bi-geo-alt" style={{ marginRight: "6px" }} />
                Online - IEEE
              </dv>
              <div className="conference-description">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus facilis ipsam perferendis est placeat atque consequuntur illo enim nesciunt? Aspernatur?</div>
            </div>
          </div>
        </a>
        <a href="#">
          <div className="conference-wrap">
            <img className="conference-image" src="https://images.pexels.com/photos/40568/medical-appointment-doctor-healthcare-40568.jpeg" alt="" srcset="" />
            <div className="conference-details">
              <div className="conference-title">Confernece on Medical</div>
              <div className="conference-date">
                <i className="bi bi-clock " style={{ marginRight: "6px" }} />
                Sunday, Mar 24, 2024 &nbsp; - &nbsp; Submission Start: Mar 27, End: Apr 27
              </div>
              <dv className="conference-locaton">
                <i className="bi bi-geo-alt" style={{ marginRight: "6px" }} />
                NYC, USA - IEEE
              </dv>
              <div className="conference-description">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus facilis ipsam perferendis est placeat atque consequuntur illo enim nesciunt? Aspernatur?</div>
            </div>
          </div>
        </a>
      </div>
    </>
  );
};

export default HomePage;
