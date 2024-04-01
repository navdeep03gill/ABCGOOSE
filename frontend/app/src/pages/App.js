import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "../css/App.css";
import goose from "../imgs/goose-transparent.png";
import Home from "./home";
import MultiWord from "./multiWord";
import SingleWord from "./singleWord";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/singleWord" element={<SingleWord />} />
        <Route path="/multiWord" element={<MultiWord />} />
      </Routes>
    </Router>
  );
}

export default App;
