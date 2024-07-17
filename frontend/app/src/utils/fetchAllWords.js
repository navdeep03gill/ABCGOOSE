import { useState, useEffect } from "react";

const fetchAuthToken = async () => {
  let url = "http://127.0.0.1:5000/get-csrf-token";
  try {
    const response = await fetch(url, { method: "GET" });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    const token = data["csrf_token"];
    console.log(token);
    return token;
  } catch (error) {
    console.error(error.message);
  }
};

const fetchAllWords = async () => {
  const url = "http://127.0.0.1:5000/thesaurus/get_words";
  const auth_token = await fetchAuthToken();
  const headers = { Authorization: auth_token };
  return fetch(url, { method: "GET", headers: headers })
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
};

// const fetchAllWordsOld = async () => {
//   let url = "http://127.0.0.1:5000/api/v1/words";
//   let username = "admin";
//   let password = "SuperSecretPwd";
//   let headers = { Authorization: "Basic " + btoa(`${username}:${password}`) };
//   return fetch(url, { method: "GET", headers: headers })
//     .then((response) => response.json())
//     .then((data) => {
//       return data;
//     });
// };

const useFetchWords = () => {
  const [allWords, setAllWords] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchAllWords();
        let improvedData = data.map((word) => {
          return {
            ...word,
            synonyms: word.synonyms.map((synonym) => synonym.toLowerCase()),
          };
        });
        setAllWords(improvedData);
      } catch (error) {
        console.error("Error fetching allWords: ", error);
      }
    };
    fetchData();
  }, []);

  console.log("useFetchWords", allWords.length);
  return allWords;
};

export default useFetchWords;
