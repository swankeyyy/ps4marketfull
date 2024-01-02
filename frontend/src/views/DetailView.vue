<template>
    <Header/>
    <Detail :slug="slug"/>
</template>

<script>
import Header from "@/components/Header.vue";
import Detail from "@/components/Detail.vue";

export default {
    name: "DetailView",
    components: {Detail, Header},
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