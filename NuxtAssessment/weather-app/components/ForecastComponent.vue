<script setup lang="ts">
import { useWeatherStore } from "@/store/WheaterStore";

const store = useWeatherStore();


function formatDate(inputDate: string) {
    const date = new Date(inputDate);
    const options: Intl.DateTimeFormatOptions = {
        weekday: 'short',  
        day: '2-digit',
        month: 'short'
    };

    const formattedDate = date.toLocaleDateString('en-GB', options);

    return formattedDate;
}


</script>

<template>
    <div class="flex flex-col items-center justify-center">
        <div class="space-y-1 w-full max-w-screen-sm bg-white p-10 rounded-xl ring-8 ring-white ring-opacity-40">
            <div class="flex justify-around items-center" v-for="(nextDay, index) in store.currentWeather.data.forecast.forecastday.slice(1)" :key="index">
                <span class="font-semibold text-lg w-1/4">{{ formatDate(nextDay.date)}}</span>
                <div class="flex items-center justify-end w-1/4 pr-10">
                    <span class="font-semibold">{{ nextDay.day.avghumidity }}%</span>
                    <IconsDropIcon />
                </div>
                <div class="flex items-center justify-between w-1/4">
                    <img class="h-12 w-12" :src="nextDay.day.condition.icon">
                    <div>
                        <span class="font-semibold text-lg w-1/4 text-right" v-if="store.weatherUnit == 'celsius'">{{ nextDay.day.avgtemp_c }}°C</span>
                        <span class="font-semibold text-lg w-1/4 text-right" v-if="store.weatherUnit == 'fahrenheit'">{{ nextDay.day.avgtemp_f }}°F</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>