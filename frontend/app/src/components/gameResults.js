import React, { useState } from 'react';
import '../css/table.css';

function GameResults({ data }) {
  const [filter, setFilter] = useState('all');
  const [selectedSpan, setSelectedSpan] = useState(null);

  const classify = (value) => {
    switch (value) {
      case 0:
        return 'incorrect-guess';
      case 1:
        return 'correct-guess';
      case 2:
        return 'already-guessed';
      default:
        return 'Unknown';
    }
  };

  const getWordsLengths = (guesses) => {
    switch (guesses) {
      case 'all':
        return data.length;
      case 'correct':
        let cor = data.filter(([, , number]) => number === 1);
        return cor.length;
      case 'wrong':
        let wr = data.filter(([, , number]) => number === 0);
        return wr.length;
      default:
        return 0;
    }
  };

  const filterData = () => {
    switch (filter) {
      case 'correct':
        return data.filter(([, , number]) => number === 1);
      case 'wrong':
        return data.filter(([, , number]) => number === 0);
      default:
        return data;
    }
  };

  return (
    <div className='game-results'>
      <div className='tabs'>
        <div>
          <button className='tab-button' onClick={() => setFilter('all')}>
            All Guesses {`(${getWordsLengths('all')})`}
          </button>
          <button className='tab-button' onClick={() => setFilter('correct')}>
            Correct Guesses {`(${getWordsLengths('correct')})`}
          </button>
          <button className='tab-button' onClick={() => setFilter('wrong')}>
            Wrong Guesses {`(${getWordsLengths('wrong')})`}
          </button>
        </div>
      </div>
      <div className='word-list'>
        {filterData().map(([string1, string2, number], index) => (
          <div key={index} className='word-container-wrapper'>
            <span
              className={`word-container ${classify(number)}`}
              onClick={() =>
                setSelectedSpan(selectedSpan === index ? null : index)
              }
            >
              {string1}
            </span>
            {selectedSpan === index && (
              <div className='detail-container'>{string2}</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default GameResults;
