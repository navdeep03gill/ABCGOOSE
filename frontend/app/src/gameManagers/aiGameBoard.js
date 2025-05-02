import React from 'react';
import useAIGameLogic from './useAIGameLogic';
import GameBoard from './GameBoard';

function AIGameBoard({ time, allWords }) {
  const gameLogic = useAIGameLogic(time, allWords);

  return <GameBoard title='Game Mode 2: Many Words, 30 sec' {...gameLogic} />;
}

export default AIGameBoard;
