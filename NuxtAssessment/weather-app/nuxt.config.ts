// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ["@pinia/nuxt"],
  alias: {
    pinia: "/node_modules/@pinia/nuxt/node_modules/pinia/dist/pinia.mjs"
  },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  runtimeConfig: {

    apiKey: process.env.API_KEY,

    public: {
      apiBaseUrl: process.env.API_BASE_URL,
      apiCurrentWeather: "/current.json", 
      apiForecast: "/Forecast.json", 
      apiHistory: "/History.json" 
    }
  },
})