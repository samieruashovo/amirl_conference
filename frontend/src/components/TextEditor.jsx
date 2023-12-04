import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css"; // import styles

const TextEditor = () => {
  const [content, setContent] = useState("");

  //   const formats = ["bold", "italic", "underline"];

  return (
    <div>
      <ReactQuill style={{ height: "150px" }} theme="snow" value={content} onChange={setContent} placeholder="Conference Description" />
    </div>
  );
};

export default TextEditor;
