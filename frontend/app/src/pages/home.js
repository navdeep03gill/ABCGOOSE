import { React, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/App.css';
import leftgoose from '../imgs/goose-transparent-face-left.png';
import rightgoose from '../imgs/goose-transparent-face-right.png';

function Home() {
  const navigate = useNavigate();
  const [singleWordClick, setSingleWordClick] = useState(false);
  const [multipleWordClick, setMultipleWordClick] = useState(false);
  return (
    <div className='App flex justify-center items-center'>
      <div>
        <div className='border-b border-gray-900/10 pb-12'></div>
        <div className='flex justify-center'>
          <h1 className='title'>ABCGoose</h1>
        </div>
        <div className='flex justify-center hover-rotate gap-4 flex'>
          <div className='flex justify-end'>
            <img className='gooseimgleft' src={rightgoose} alt='' />
          </div>
          <div className='flex justify-start'>
            <img className='gooseimgright' src={leftgoose} alt='' />
          </div>
        </div>
        <div className='m-5'>
          <h2
            style={{
              display: 'inline-block',
              fontSize: 20,
              fontWeight: 600,
            }}
          >
            Select a Game
          </h2>
        </div>
        <div style={{ marginBottom: '30px' }} className='mt-10 grid '>
          <div className='col-md-auto'>
            <button
              onClick={() => setSingleWordClick(!singleWordClick)}
              className='gameButton'
            >
              Single Word Mode
            </button>
            {!!singleWordClick ? (
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'center',
                }}
              >
                <div className='description-box'>
                  <div style={{ flex: 3 }}>
                    <div className='game-description-header'>
                      Game Description
                    </div>
                    <div
                      style={{ marginTop: '5px' }}
                      className='game-description'
                    >
                      Under a 30 second game clock, attempt to guess as many
                      valid synonyms for just one word and its definition.
                    </div>
                  </div>
                  <div className='go-to-button'>
                    <button
                      onClick={() => navigate('/singleWord')}
                      className='altGameButton'
                    >
                      Play
                    </button>
                  </div>
                </div>
              </div>
            ) : null}
          </div>
        </div>
        <div
          style={{ marginBottom: '50px' }}
          className='row d-flex justify-content-center'
        >
          <div className='col-md-auto'>
            <button
              onClick={() => setMultipleWordClick(!multipleWordClick)}
              className='gameButton'
            >
              Multiple Word Mode
            </button>
            {!!multipleWordClick ? (
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'center',
                }}
              >
                <div className='description-box'>
                  <div style={{ flex: 3 }}>
                    <div className='game-description-header'>
                      Game Description
                    </div>
                    <div
                      style={{ marginTop: '5px' }}
                      className='game-description'
                    >
                      Under a 30 second game clock, attempt to guess a valid
                      synonyms for the given word and its definition. Once a
                      correct guess is made, the given word changes.
                    </div>
                  </div>
                  <div className='go-to-button'>
                    <button
                      onClick={() => navigate('/multiWord')}
                      className='altGameButton'
                    >
                      Play
                    </button>
                  </div>
                </div>
              </div>
            ) : null}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
