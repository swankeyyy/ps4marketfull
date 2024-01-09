import {createStore} from 'vuex'
import {categories} from "@/store/categories";
import {products_list} from "@/store/products_list";
import axios from "axios";


export default createStore({
    state: {
        isAuth: false,
        user_id: null,
        backend_url: 'http://127.0.0.1:8000/',
        basket: []
    },
    getters: {
        get_backend_url(state) {
            return state.backend_url
        },
        get_token(state) {
            return state.token
        },
        get_auth(state) {
            return state.isAuth
        },
        get_user_id(state) {
            return state.user_id
        },
        get_basket(state) {
            return [...state.basket]
        }
    },
    mutations: {
        set_token(state, token) {
            state.token = token
        },
        set_auth(state, bool) {
            state.isAuth = bool
        },
        set_user_id(state, id) {
            state.user_id = id
        },
        set_basket(state, basket) {
            state.basket = basket
        }
    },
    actions: {
        async logined({state, commit}) {
            if (localStorage.token) {
                commit('set_auth', true)
                axios.defaults.headers.common['Authorization'] = localStorage.token


            }

        }
    },
    modules: {
        categories: categories,
        products_list: products_list,

    },

})
