import { useState, useEffect } from 'react';

const fetchAuthToken = async () => {
  let url = `${process.env.REACT_APP_TESTING_URL}/auth/get-auth-token`;
  try {
    const response = await fetch(url, { method: 'GET' });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    const token = data['auth_token'];
    return token;
  } catch (error) {
    console.error(error.message);
  }
};

const fetchAllMLWords = async () => {
  const url = `${process.env.REACT_APP_TESTING_URL}/ml/get_ml_words`;
  const auth_token = await fetchAuthToken();
  const headers = { Authorization: auth_token };

  try {
    const response = await fetch(url, { method: 'GET', headers: headers });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error(error.message);
  }
};

const useFetchMLWords = () => {
  const [allWords, setAllWords] = useState([]);
  const fetchData = async () => {
    try {
      const data = await fetchAllMLWords();
      if (data) {
        setAllWords(data);
      } else {
        console.error('fetchAllMLWords returned no data');
      }
    } catch (error) {
      console.error('Error fetching allWords:\n', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return [allWords, fetchData];
};

export default useFetchMLWords;
