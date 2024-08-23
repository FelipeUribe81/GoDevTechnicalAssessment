import { defineStore } from "pinia";
import useWeatherApi from "~/composables/useWeatherApi";

const weatherApi = useWeatherApi()

export const useWeatherStore = defineStore("WeatherStore", {
    state: () => {
        return {
            currentWeather: null,
            weatherUnit: "celsius"
        }
    },
    actions: {
        async retrieveWeather(cityName) {
            const config = useRuntimeConfig()
            try {
                let current = await weatherApi.get(config.public.apiForecast, {
                    params: {
                        key: config.public.apiKey,
                        q: cityName || config.public.defaultCity,
                        days: config.public.forecastDays,
                    }
                })
                this.currentWeather = current
            } catch (error) {
                this.currentWeather = null
            }
        },
        changeWeatherUnit(weatherUnit) {
            this.weatherUnit = weatherUnit
        }
    },
})