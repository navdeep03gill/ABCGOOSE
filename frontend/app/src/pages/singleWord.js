import React from "react";
import "../css/App.css";
import SingleGameBoard from "../gameManagers/singleGameBoard";
import useFetchWords from "../utils/fetchAllWords";

function SingleWord() {
  const allWords = useFetchWords();

  return (
    <div className="App flex justify-center items-center">
      <div className="container">
        <SingleGameBoard time={30} allWords={allWords}></SingleGameBoard>
      </div>
    </div>
  );
}

export default SingleWord;
