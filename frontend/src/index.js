import React from "react";
import ReactDOM from "react-dom";
import AppRouter from "./AppRouter";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <AppRouter />
  </React.StrictMode>
);
