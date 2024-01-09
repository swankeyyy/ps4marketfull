<template>
    <Header/>
    <SelectedCategories :slug="slug"/>
    <Footer />
</template>

<script>
import Header from "@/components/Header.vue";

import SelectedCategories from "@/components/SelectedCategories.vue";
import Footer from "@/components/Footer.vue";

export default {
    name: "CategoriesView",
    components: {Footer, SelectedCategories, Header},
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