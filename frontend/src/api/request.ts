import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL;

console.log("baseURL:", baseURL);

const request = axios.create({
  baseURL: "https://hottagplatform.onrender.com/api/",
  timeout: 5000,
});

export default request;
