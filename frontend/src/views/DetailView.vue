<template>
    <Header/>
    <Detail :slug="slug"/>
    <Footer />
</template>

<script>
import Header from "@/components/Header.vue";
import Detail from "@/components/Detail.vue";
import Footer from "@/components/Footer.vue";

export default {
    name: "DetailView",
    components: {Footer, Detail, Header},
    props: {
        slug: {
            required: true,
            type: String
        }
    }
}
</script>

<style scoped>

</style>