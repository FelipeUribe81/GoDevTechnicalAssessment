import axios from 'axios'

const baseURL = "http://api.weatherapi.com/v1"

export default () => {
  return axios.create({
    baseURL: baseURL
  })
}