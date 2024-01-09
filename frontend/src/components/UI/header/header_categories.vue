<template>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle nav-link active" href="#" id="navbarDropdown"
           role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Категории
        </a>
        <ul class="dropdown-menu " aria-labelledby="navbarDropdown">
            <li>
                <router-link class="dropdown-item " v-for="category in get_categories"
                             :key="category.id" :to="{name: 'change_categories', params: {slug: category.url}}">
                    {{ category.name }}
                </router-link>
            </li>
        </ul>
    </li>
</template>

<script>
import {mapActions, mapGetters, mapMutations} from "vuex";


export default {
    name: "header_categories",

    computed: {
        ...mapGetters({
            get_categories: "get_categories",
            url: "get_backend_url"
        }),
    },
    methods: {
        ...mapMutations({
            setCategoryList: "setCategory_list"
        }),
        ...mapActions({
            loadCategories: "loadCategories"
        }),

    },
    async created() {
        await this.loadCategories()
    }
}
</script>

<style scoped>

</style>