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
                            <div class="col" v-for="product in this.products" :key="product.id">
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
import axios from "axios";

export default {
    name: "SelectedCategories",
    components: {Product_card, Sidebar},
    props: {
        slug: {
            required: true,
            type: String
        }
    },
    data() {
        return {
            products: [],
            url: this.slug
        }
    },
    computed: {},
    methods: {
        async loaddata() {
            try {
                let response = await axios.get(`http://127.0.0.1:8000/api/products/categories/${this.url}`)
                this.products = response.data

            } catch (e) {
                console.log(e)
            }
        }
    },
    watch: {}
    ,

    created() {
        this.loaddata()
    }
}
</script>

<style scoped>

</style>