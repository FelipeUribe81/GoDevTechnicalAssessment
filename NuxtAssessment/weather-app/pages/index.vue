<script setup lang="ts">
import { useWeatherStore } from "@/store/WheaterStore";
import { onMounted } from 'vue'

const store = useWeatherStore();

onMounted(() => {
    store.retrieveWeather()
})

</script>
<template>
  <div
    class="flex flex-col items-center justify-evenly h-[1000px] xl:h-full xl: min-h-screen w-full bg-gradient-to-br from-blue-400 via-blue-300 via-blue-200 to-green-200">
    <div class="flex flex-col items-center w-[60%]">
      <p class="font-bold text-4xl mt-8 xl:font-bold text-4xl mb-10 mt-0">GoDev Weather App</p>
      <div class="flex flex-row justify-evenly w-full">
        <SearchComponent/>
        <SwitchTemperatureUnit/>
      </div>
    </div>
    <div v-if="!store.currentWeather" class="flex flex-row justify-center w-full">
      <WeatherErrorComponent/>
    </div>
    <div v-else class="flex flex-col items-center h-full md:w-[85%] xl:flex-row justify-evenly xl:w-[75%]">
      <WeatherComponent class="w-[400px]" />
      <ForecastComponent class="w-[550px]" />
    </div>
  </div>
</template>
