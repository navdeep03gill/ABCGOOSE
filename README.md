# How to Play:

1. Clone the Repository
2. Ensure you have Python, npm, and React installed on your machine
3. Follow instructions below

### Running Backend

cd ABCGoose/database

#### Set up Virtual Environment

If you don't have the pip virtualenv package, do: pip install virtualenv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

./runBackend.sh

### Running Frontend

Open another terminal shell\
cd ABCGoose/frontend/app \
npm start

4. Click the link generated by npm

## Tasks Completed:

- Built webscraper to reliably find words, definitions, and synonyms
- Created database in SQLite to populate webscraper data
- Migrated database from SQLite to PostgreSQL
- Built secure backend API with JWT token Auth to fetch game data
- Converted to fast-rendering and clean React.js + Tailwind.css frontend (model-view-controller paradigm)

## TODO:

- Apply limits on API request endpoints
- Build and deploy a public API
- Build a Machine Learning Verification Layer for user inputs
- Build more game modes (i.e., User manually changes the time limit)
