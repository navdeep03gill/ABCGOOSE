import React, { useState, useEffect } from "react";
import "../css/App.css";
import MultiWordGameBoard from "../gameManagers/multiWordGameBoard";
import { fetchAllWords } from "../utils/fetchAllWords";

function MultiWord() {
  const [allWords, setAllWords] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchAllWords();
        //console.log(data);
        let improvedData = data.map((word) => {
          return {
            ...word,
            synonyms: word.synonyms.map((synonym) => synonym.toLowerCase()),
          };
        });
        console.log(improvedData);
        setAllWords(improvedData);
      } catch (error) {
        console.error("Error fetching allWords: ", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="App flex justify-center items-center">
      <div className="container">
        <MultiWordGameBoard time={30} allWords={allWords}></MultiWordGameBoard>
      </div>
    </div>
  );
}

export default MultiWord;
