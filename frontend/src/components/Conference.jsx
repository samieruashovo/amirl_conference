import React from "react";
import Layout from "./Layout";
import "../css/ConferencePage.css";

const Conference = () => {
  return (
    <>
      <Layout>
        <div className="cntainer mt-4">
          <center>
            <img className="thumbnail" src="https://images.pexels.com/photos/974314/pexels-photo-974314.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="" srcset="" />
          </center>
        </div>
      </Layout>
    </>
  );
};

export default Conference;
