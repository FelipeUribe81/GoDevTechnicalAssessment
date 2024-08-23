<script setup lang="ts">
import { useWeatherStore } from "@/store/WheaterStore";

const store = useWeatherStore();
</script>

<template>
  <div class="flex justify-center items-center">
  
  <div class="flex rounded-full bg-white p-2 rounded-xl ring-8 ring-white ring-opacity-40">
    <button x-data
            @click="store.changeWeatherUnit('celsius')"
            class="rounded-full h-8 w-8 
                   text-gray-500 hover:text-gray-900 
                   hover:bg-gray-300
                   flex items-center justify-center 
                   focus:outline-none"
            :class="store.weatherUnit == 'celsius' ? 'bg-blue-700 text-white' : ''"
    >
      <span>C°</span>
    </button>
    <button x-data
           @click="store.changeWeatherUnit('fahrenheit')"
            class="rounded-full h-8 w-8 
                   text-gray-500 hover:text-gray-900
                   hover:bg-gray-300
                   flex items-center justify-center 
                   focus:outline-none"
            :class="store.weatherUnit == 'fahrenheit' ? 'bg-blue-700 text-white' : ''"
    >
      <span>F°</span>
    </button>
  </div>
  
</div>
</template>
