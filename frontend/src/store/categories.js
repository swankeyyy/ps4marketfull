import axios from "axios";

export const categories = {
    state: () => ({
        category_list: [],
    }),
    getters: {
        get_categories(state) {
            return [...state.category_list]
        }
    },
    mutations: {
        setCategory_list(state, category_list) {
            state.category_list = category_list
        }

    },
    actions: {
        async loadCategories({state, commit}) {
            try {
                let response = await axios.get( 'http://127.0.0.1:8000/api/products/categories/')
                commit('setCategory_list', response.data)

            } catch (e) {
                console.log(e)
            }
        }

    },


}