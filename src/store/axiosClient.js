import axios from 'axios';

const axios_client = axios.create({
 // baseURL: process.env.REACT_APP_BASE_URL || "http://localhost:8080",
  baseURL:  "http://localhost:8080"
});

export default axios_client;
