import axios from "axios";

const fetchAllWords = () => {
  let url = "http://127.0.0.1:5000/api/v1/words";
  let username = "admin";
  let password = "SuperSecretPwd";
  let headers = { Authorization: "Basic " + btoa(`${username}:${password}`) };
  return fetch(url, { method: "GET", headers: headers })
    .then((response) => response.json())
    .then((data) => {
      // Return the fetched data
      return data;
    });
};

export { fetchAllWords };
