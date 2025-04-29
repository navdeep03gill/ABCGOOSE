import React from 'react';
import { useState, useEffect, createContext, useContext } from 'react';
import '../css/App.css';
import AIGameBoard from '../gameManagers/aiGameBoard';
import useFetchMLWords from '../utils/fetchAllMLWords';
import { NumGameContext } from '../utils/numGamesContext';

function AIWord() {
  const [numConsecutiveGames, setNumConsecutiveGames] = useState(1);
  const [allWords, fetchWords] = useFetchMLWords();
  console.log(allWords);

  useEffect(() => {
    if (numConsecutiveGames % 15 === 0 && numConsecutiveGames > 0) {
      fetchWords();
      setNumConsecutiveGames(numConsecutiveGames + 1);
    }
  }, [numConsecutiveGames]);

  return (
    <NumGameContext.Provider
      value={{ numConsecutiveGames, setNumConsecutiveGames }}
    >
      <div className='App flex justify-center items-center'>
        <div className='container'>
          <AIGameBoard time={30} allWords={allWords}></AIGameBoard>
        </div>
      </div>
    </NumGameContext.Provider>
  );
}

export default AIWord;
