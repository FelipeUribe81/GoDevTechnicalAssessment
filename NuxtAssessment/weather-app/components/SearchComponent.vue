<script setup lang="ts">
import { ref } from 'vue';
import { useWeatherStore } from "@/store/WheaterStore";

const store = useWeatherStore();

const inputValue = ref('');

const searchForCity = () => {
    console.log(inputValue.value);
    store.retrieveWeather(inputValue.value)
};
</script>

<template>
    <div class="w-[80%]">
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <IconsSearchIcon />
            </div>
            <input v-model="inputValue" type="search" id="default-search" @keyup.enter="searchForCity()"
                class="block w-full p-4 ps-10 text-sm text-gray-900 bg-white p-10 rounded-xl ring-8 ring-white ring-opacity-40 focus:outline-none focus:ring-8 focus:ring-blue-400"
                placeholder="Search for city..." required />
            <button @click="searchForCity()"
                class="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
        </div>
    </div>
</template>
