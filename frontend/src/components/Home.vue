<template>
    <main>
        <div class="container mt-5">
            <div class="row">
                <div class="col-2">
                    <sidebar/>
                </div>
                <div class="col ps-3 mt-2">
                    <section>
                        <div class="row row-cols-3">
                            <div class="col" v-for="product in products" :key="product.id">
                                <product_card :product="product"/>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import Sidebar from "@/components/UI/body/sidebar.vue";
import Product_card from "@/components/UI/body/product_card.vue";
import {mapActions, mapGetters} from "vuex";

export default {
    name: "Home",
    components: {Product_card, Sidebar},
    computed: {
        ...mapGetters({
            products: "get_products_list"
        }),

    },
    methods: {
        ...mapActions({
            loadProducts: "loadProducts"
        })
    },
    created() {
        this.loadProducts()
    }
}
</script>

<style scoped>

</style>