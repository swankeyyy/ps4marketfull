<template>
    <Header/>
    <Home />
    <Footer />

</template>

<script>
import Header from "@/components/Header.vue";
import Home from "@/components/Home.vue";
import Footer from "@/components/Footer.vue";

export default {
    name: "HomeView",
    components: {Footer, Home, Header}
}
</script>

<style scoped>

</style>