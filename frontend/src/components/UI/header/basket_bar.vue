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

                        <ul>
                            <li v-for="item in basket" :key="item.id"
                            >{{item.product.title}} - {{item.product.price}}р.</li>

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
            id: null
        }
    },
    computed: {

        ...mapGetters({
            basket: "get_basket",
            url: "get_backend_url"
        })
    },
    methods: {
        ...mapMutations({
            set_basket: "set_basket",
            set_user_id: "set_user_id"
        }),
        ...mapGetters({
            get_auth: "get_auth",

        }),

        async loadBasket() {
            let response = await axios.get(this.url + 'auth/users/me/',)
            this.id = response.data.id
            this.set_user_id(this.id)
            response = await axios.get(this.url + 'api/basket/basket/' + this.id)
            this.set_basket(response.data.basket)
            console.log(this.basket)
        }

    },
    created() {
        // this.loadBasket()
    }

}
</script>

<style scoped>

</style>