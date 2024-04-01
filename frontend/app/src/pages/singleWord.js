import React, { useState, useEffect } from "react";
import "../css/App.css";
import SingleWordGameBoard from "../gameManagers/singleWordGameBoard";
import { fetchAllWords } from "../utils/fetchAllWords";
//import singleWordGame from "../gameManagers/singleWordGame";

function SingleWord() {
  const [allWords, setAllWords] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchAllWords();
        console.log(data);
        setAllWords(data);
      } catch (error) {
        console.error("Error fetching allWords: ", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="App flex justify-center items-center">
      <div className="container">
        <SingleWordGameBoard
          time={30}
          allWords={allWords}
        ></SingleWordGameBoard>
      </div>
    </div>
  );
}

export default SingleWord;
