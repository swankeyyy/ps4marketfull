<template>
    <Header/>
    <SelectedCategories :slug="slug"/>
</template>

<script>
import Header from "@/components/Header.vue";

import SelectedCategories from "@/components/SelectedCategories.vue";

export default {
    name: "CategoriesView",
    components: {SelectedCategories, Header},
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