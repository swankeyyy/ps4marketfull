<template>
    <Header/>
    <Home />
</template>

<script>
import Header from "@/components/Header.vue";
import Home from "@/components/Home.vue";

export default {
    name: "HomeView",
    components: {Home, Header}
}
</script>

<style scoped>

</style>