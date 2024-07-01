import React from "react";
import "../css/App.css";
import MultiGameBoard from "../gameManagers/multiGameBoard";
import useFetchWords from "../utils/fetchAllWords";

function MultiWord() {
  const allWords = useFetchWords();

  return (
    <div className="App flex justify-center items-center">
      <div className="container">
        <MultiGameBoard time={30} allWords={allWords}></MultiGameBoard>
      </div>
    </div>
  );
}

export default MultiWord;
