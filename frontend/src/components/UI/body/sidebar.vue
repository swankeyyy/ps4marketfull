<template>
    <div class="left__sidebar">
        <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white">
            <div class="position-sticky">
                <div class="list-group list-group-flush ">
                    <router-link :to="{name: 'change_categories', params: {slug: category.url}}" class="list-group-item list-group-item-action py-2 ripple item-card"
                    v-for="category in categories">
                        <i class="fas fa-chart-area fa-fw me-3"></i><span>{{category.name}}</span>
                    </router-link>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    name: "sidebar",
    computed: {
        ...mapGetters({
            categories: "get_categories"
        })
    }
}
</script>

<style scoped>
.item-card{
    font-size: 15px;

}

.item-card:hover{
    color: red;
}


</style>