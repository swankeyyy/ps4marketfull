<template>
    <div class="app">
        <router-view/>
    </div>
</template>

<style>
.container {
    font-size: 20px;
    font-family: FreeMono, monospace;
}
body {
    background-color: #f0f1f2;
}
</style>
<script setup>

import HomeView from "@/views/HomeView.vue";
</script>