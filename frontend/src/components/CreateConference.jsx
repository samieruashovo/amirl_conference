import React from "react";
import Layout from "./Layout";
import TextEditor from "./TextEditor";

const CreateConference = () => {
  return (
    <>
      <Layout>
        <div className="container mt-4">
          <h3>HOST A VIRTUAL CONFERENCE</h3>
          <div className="form mt-5">
            <input type="text" className="form-control" placeholder="Conference Title" />
            <input type="text" className="form-control mt-2" placeholder="Conference Acronym" />
            {/* <textarea rows="7" className="form-control mt-2" placeholder="Conference Description" /> */}
            <div className="pb-5 mt-2 mb-2">
              <TextEditor />
            </div>
            <input type="text" className="form-control mt-4" placeholder="Location" />
            <input type="text" className="form-control mt-2" placeholder="Conference Website" />
            <label className="mt-3 mb-1">Conference Date</label>
            <input type="date" className="form-control" />
            <label className="mt-3 mb-1">Submission Start</label>
            <input type="date" className="form-control" />
            <label className="mt-3 mb-1">Submission End</label>
            <input type="date" className="form-control" />
          </div>

          <div className="mt-4">
            <button className="btn btn-primary">Create Conference</button>
          </div>
        </div>
      </Layout>
    </>
  );
};

export default CreateConference;
