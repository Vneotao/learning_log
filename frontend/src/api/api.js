import axiosInstance from ".";

export const login = (username, password) => {
  return axiosInstance.post(`http://0.0.0.0:8000/users/login/`, {username, password})
}

export const getTopics = () => {
  return axiosInstance.get(`http://43.133.32.183:8000/topics/`)
}