import React from "react";
import { useState, useEffect, createContext, useContext } from "react";
import "../css/App.css";
import MultiGameBoard from "../gameManagers/multiGameBoard";
import useFetchWords from "../utils/fetchAllWords";
import { NumGameContext } from "../utils/numGamesContext";

function MultiWord() {
  const [numConsecutiveGames, setNumConsecutiveGames] = useState(1);
  const [allWords, fetchWords] = useFetchWords();

  useEffect(() => {
    if (numConsecutiveGames % 15 === 0 && numConsecutiveGames > 0) {
      fetchWords();
      setNumConsecutiveGames(numConsecutiveGames + 1);
      console.log(allWords);
    }
  }, [numConsecutiveGames]);

  return (
    <NumGameContext.Provider
      value={{ numConsecutiveGames, setNumConsecutiveGames }}
    >
      <div className="App flex justify-center items-center">
        <div className="container">
          {console.log(allWords)}
          {console.log(numConsecutiveGames)}
          <MultiGameBoard time={30} allWords={allWords}></MultiGameBoard>
        </div>
      </div>
    </NumGameContext.Provider>
  );
}

export default MultiWord;
