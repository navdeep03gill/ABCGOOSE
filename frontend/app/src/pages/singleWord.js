import React from 'react';
import { useState, useEffect, createContext, useContext } from 'react';
import '../css/App.css';
import SingleGameBoard from '../gameManagers/singleGameBoard';
import useFetchWords from '../utils/fetchAllWords';
import { NumGameContext } from '../utils/numGamesContext';

function SingleWord() {
  const [numConsecutiveGames, setNumConsecutiveGames] = useState(1);
  const [allWords, fetchWords] = useFetchWords();
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
          <SingleGameBoard time={30} allWords={allWords}></SingleGameBoard>
        </div>
      </div>
    </NumGameContext.Provider>
  );
}

export default SingleWord;
