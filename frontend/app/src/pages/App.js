import "../css/App.css";
import goose from "../imgs/goose-transparent.png";

function App() {
  return (
    <div className="App">
      <div class="container">
        <div class="border-b border-gray-900/10 pb-12"></div>
        <div class="flex justify-center">
          <h1 class="title">ABCGoose</h1>
        </div>
        <div class="grid grid-cols-2 hover-rotate gap-4 flex justify-center">
          <div class="flex justify-end">
            <img class="gooseimgrvs" src={goose} alt="" />
          </div>
          <div class="flex justify-start">
            <img class="gooseimg" src={goose} alt="" />
          </div>
        </div>
        <div class="mt-10 grid grid-cols-1 grid-rows-2">
          <div class="col-md-auto">
            <a href="singleWordGameMode.html">
              <button class="gameButton hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Single Word Mode
              </button>
            </a>
          </div>
        </div>
        <div class="row d-flex justify-content-center">
          <div class="col-md-auto">
            <a href="wordsGameMode.html">
              <button class="gameButton hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Multiple Word Mode
              </button>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
