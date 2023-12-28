import {createStore} from 'vuex'
import {categories} from "@/store/categories";


export default createStore({
    state: {
        isAuth: false,
        backend_url: 'http://127.0.0.1:8000/',

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
        }

    },
    mutations: {
        set_token(state, token) {
            state.token = token
        },
        set_auth(state, bool) {
            state.isAuth = bool
        }
    },
    actions: {
        logined({state, commit}) {
            if (localStorage.token) {
                commit('set_auth', true)
            }
            console.log(state.isAuth)
        }
    },
    modules: {
        categories: categories
    },

})
