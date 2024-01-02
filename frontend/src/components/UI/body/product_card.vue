<template>
    <div class="card p-1 mt-1">
        <img :src="url + product.poster" class="card-img-top p-1 c_img" alt="">
        <div class="card-body ms-2">
            <h5 class="card-title">{{ product.title }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ product.price }}p.</h6>
            <p class="card-text" v-if="product.short_description.length<90"
            >{{ product.short_description }}</p>
            <p class="card-text" v-else>{{ product.short_description.substring(0, 90) + ".." }}</p>
            <router-link :to="{name: 'single', params: {slug: product.url}}"  class="btn btn-outline-secondary btn-text"
            >Перейти к описанию</router-link>
        </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    name: "product_card",
    computed: {
        ...mapGetters({
            url: "get_backend_url"
        })
    },
    props: {
        product: {
            required: true,
            type: Object
        }
    }
}
</script>

<style scoped>
.card-text {
    font-size: 14px;
    line-height: 1.4;
}
.btn-text {
    font-size: 14px;
    font-weight: bolder;
}

.card{
    box-shadow: 0 2px 5px 0 rgba(0,0,0,0.6);
    transition: all .3s;
}

.card:hover{
    box-shadow: 0 14px 30px -15px rgba(0,0,0,0.75);
}

</style>