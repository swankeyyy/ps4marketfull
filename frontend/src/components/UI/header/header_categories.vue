<template>
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle nav-link active" href="#" id="navbarDropdown"
           role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Категории
        </a>
        <ul class="dropdown-menu " aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item " href="#">Категория</a></li>
            <li><a class="dropdown-item" href="#">Категория</a></li>
            <li><a class="dropdown-item" href="#">Категория</a></li>
            <li><a class="dropdown-item" href="#">Категория</a></li>
            <li><a class="dropdown-item" href="#">Категория</a></li>
            <li><a class="dropdown-item" href="#">Категория</a></li>
        </ul>
    </li>
</template>

<script>
import {mapActions, mapGetters, mapMutations} from "vuex";
import axios from "axios";

export default {
    name: "header_categories",
    data() {
        return {
            categories: this.get_categories
        }
    },
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