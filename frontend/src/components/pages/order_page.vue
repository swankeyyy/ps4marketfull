<template>
    <div class="container">
        <h2>Список покупок</h2>
        <div class="list">
            <p v-if="empty">Корзина пустая(</p>
            <div v-else>
                <p v-for="item in items">{{item.product.title}} - {{item.quantity}} шт. По цене: {{item.product.price}}
                за штуку</p>
                <h3>Итого: {{total}} рублей</h3>
            </div>
            <button type="button" class="btn btn-success">Заказать
            </button>
        </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";
import axios from "axios";

export default {
    name: "order_page",
    data() {
        return {
            items: [],
            empty: false,
            total: null
        }
    },
    computed: {
        ...mapGetters({
            id: "get_user_id",
            url: "get_backend_url"
        })
    },
    methods: {

    },
    async created() {
        try {
            let response = await axios.get(this.url + 'api/basket/basket/' + this.id)
            console.log(response.data)
            if (response.data.basket === 'null') {
                this.empty = true
            }
            else {
                this.items = response.data.basket
                this.total = response.data.total_price
            }
        } catch(e) {

        }
    }
}
</script>

<style scoped>
h3 {
    margin-top: 100px;
    margin-bottom: 20px;
}
.container {
    margin-top: 8%;
    margin-bottom: 2%;
    text-align: center;
}

.list {
    margin-top: 30px;

}
</style>