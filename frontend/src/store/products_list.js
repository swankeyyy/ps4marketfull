import axios from "axios";

export const products_list = {
    state: () => ({
        products_list: [],
    }),
    getters: {
        get_products_list(state) {
            return [...state.products_list]
        }
    },
    mutations: {
        setProducts_list(state, products_list) {
            state.products_list = products_list
        }
    },
    actions: {
        async loadProducts({state, commit}) {
            try {
                let response = await axios.get( 'http://127.0.0.1:8000/api/products/products/')
                commit('setProducts_list', response.data)
                console.log(response.data)
            } catch (e) {
                console.log(e)
            }
        }

    },


}