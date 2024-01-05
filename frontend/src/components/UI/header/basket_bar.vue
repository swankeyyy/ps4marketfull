<template>
    <li class="nav-item " v-show="get_auth()">
        <a class="nav-link active" aria-current="page" href="#" type="button" @click="loadBasket"><img
                src="@/assets/img/cart_header.png" alt="userIco" height="24px" data-bs-toggle="modal"
                data-bs-target="#CartModal"></a>

        <!-- Modal -->
        <div class="modal fade" id="CartModal" tabindex="-1" aria-labelledby="CartModalLabel"
             aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="CartModalLabel">Список покупок</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                    </div>
                    <div class="modal-body">

                        <ul v-if="!empty">
                            <li v-for="item in basket" :key="item.id"
                            >{{ item.product.title }} - {{ item.quantity }} шт.
                                <a href="#" @click="remove(item.id)"><img src="@/assets/img/trash.png"
                                                                          height="20px"></a></li>
                        </ul>
                        <ul v-else>
                            <li>Корзина пуста</li>
                        </ul>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary"
                                data-bs-dismiss="modal">Закрыть
                        </button>
                        <button type="button" class="btn btn-primary">Перейти к
                            оформлению
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </li>
</template>

<script>
import {mapGetters, mapMutations} from "vuex";
import axios from "axios";

export default {
    name: "basket_bar",
    data() {
        return {
            id: null,
            empty: false,
            basket: []
        }
    },
    computed: {

        ...mapGetters({
            url: "get_backend_url"
        })
    },
    watch: {

    },
    methods: {
        ...mapGetters({
            get_auth: "get_auth",
        }),
        async remove(item) {
            let response = await axios.delete(this.url + 'api/basket/basket/' + this.id,
                {
                    data: {
                        'basket_id': item
                    }
                })
            if (response.data.status_del === 'done') {
                await this.loadBasket()
            }
        },
        async loadBasket() {
            let response = await axios.get(this.url + 'auth/users/me/',)
            this.id = response.data.id

            response = await axios.get(this.url + 'api/basket/basket/' + this.id)
            if (response.data.basket !== 'null') {
                this.basket = (response.data.basket)
            } else {
                this.empty = true
            }
        }
    },
}
</script>

<style scoped>

</style>