import React from 'react';
import useGameLogic from './useGameLogic';
import GameBoard from './GameBoard';

function SingleGameBoard({ time, allWords }) {
  const gameMode = 'singleWord';
  const gameLogic = useGameLogic(time, allWords, gameMode);

  return <GameBoard title='Game Mode 1: Single Words, 30 sec' {...gameLogic} />;
}

export default SingleGameBoard;
