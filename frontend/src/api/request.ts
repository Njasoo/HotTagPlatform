import axios from "axios";

// const temporary_BASE_URL = "http://10.22.44.62:8000/api/";

const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  // baseURL: temporary_BASE_URL,
  timeout: 5000,
});

export default request;
