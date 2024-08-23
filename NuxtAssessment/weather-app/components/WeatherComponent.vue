<script setup lang="ts">
import { useWeatherStore } from "@/store/WheaterStore";
import { ref, computed } from 'vue';

const store = useWeatherStore();

const currentDate = ref(new Date());
const nextFiveHours = computed(() => {
    const result = [];
    const now = currentDate.value;

    const fisrtDoDays = store.currentWeather.data.forecast.forecastday.slice(0, 2)
    const fisrtDoDaysHours = fisrtDoDays.reduce((hours: any, day: any) => {
        return hours.concat(day.hour);
    }, []);

    for (let i = 1; i <= 5; i++) {
        const futureDate = new Date(now);
        futureDate.setHours(now.getHours() + i);

        const year = futureDate.getFullYear();
        const month = String(futureDate.getMonth() + 1).padStart(2, '0');
        const day = String(futureDate.getDate()).padStart(2, '0');
        const hours = String(futureDate.getHours()).padStart(2, '0');

        const fullNextDate = fisrtDoDaysHours.find((hour: { time: string; }) => hour.time === `${year}-${month}-${day} ${hours}:00`);

        result.push(fullNextDate);

    }
    return result;
});

function extractHour(inputDate: string) {
    const parts = inputDate.split(' ');
    const timePart = parts.slice(-1)[0];
    return timePart;
}

</script>

<template>
    <div class="flex flex-col items-center justify-center">
        <div class="w-full max-w-screen-sm bg-white p-10 rounded-xl ring-8 ring-white ring-opacity-40">
            <div class="flex justify-between">
                <div class="flex flex-col">
                    <span class="text-6xl font-bold" v-if="store.weatherUnit == 'celsius'">{{
                        store.currentWeather.data.current.feelslike_c }}°C</span>
                    <span class="text-6xl font-bold" v-if="store.weatherUnit == 'fahrenheit'">{{
                        store.currentWeather.data.current.feelslike_f }}°F</span>
                    <span class="font-semibold mt-1 text-gray-500">{{ store.currentWeather.data.location.name }},
                        {{ store.currentWeather.data.location.country }}</span>
                </div>
                <img class="h-24 w-24" :src="store.currentWeather.data.current.condition.icon">
                <!-- <IconsSunIcon class="ml-5" color="yellow-400" high="24" width="24"/> -->
            </div>

            <div class="flex justify-center">
                <p class="font-bold text-2xl mb-5">Weather for the next hours</p>
            </div>
            <div class="flex justify-between">
                <div class="flex flex-col items-center" v-for="(nextHour, index) in nextFiveHours" :key="index">
                    <span class="font-semibold text-lg" v-if="store.weatherUnit == 'celsius'">{{ nextHour.feelslike_c
                        }}°C</span>
                    <span class="font-semibold text-lg" v-if="store.weatherUnit == 'fahrenheit'">{{ nextHour.feelslike_f
                        }}°F</span>
                    <!-- <IconsSunIcon class="mt-3" color="gray-400" high="10" width="10" /> -->
                    <img class="h-15 w-15" :src="nextHour.condition.icon">
                    <p class="truncate text-ellipsis text-center overflow-hidden text-xs font-semibold text-gray-400 w-[50px]">{{ nextHour.condition.text }}</p>
                    <span class="font-semibold mt-1 text-sm">{{ extractHour(nextHour.time) }}</span>
                </div>
            </div>
        </div>
    </div>
</template>