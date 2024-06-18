import React from "react";
import { useNavigate } from "react-router-dom";
import "../css/App.css";
import leftgoose from "../imgs/goose-transparent-face-left.png";
import rightgoose from "../imgs/goose-transparent-face-right.png";

function Home() {
  const navigate = useNavigate();
  return (
    <div className="App flex justify-center items-center">
      <div>
        <div className="border-b border-gray-900/10 pb-12"></div>
        <div className="flex justify-center">
          <h1 className="title">ABCGoose</h1>
        </div>
        <div className="hover-rotate gap-4 flex">
          <div className="flex justify-end">
            <img className="gooseimgleft" src={rightgoose} alt="" />
          </div>
          <div className="flex justify-start">
            <img className="gooseimgright" src={leftgoose} alt="" />
          </div>
        </div>
        <div className="mt-10 grid grid-cols-1 grid-rows-2">
          <div className="col-md-auto">
            <button
              onClick={() => navigate("/singleWord")}
              className="gameButton"
            >
              Single Word Mode
            </button>
          </div>
        </div>
        <div className="row d-flex justify-content-center">
          <div className="col-md-auto">
            <button
              onClick={() => navigate("/multiWord")}
              className="gameButton"
            >
              Multiple Word Mode
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
