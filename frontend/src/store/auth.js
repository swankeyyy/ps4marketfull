import axios from "axios";

export const user_auth_store = {
    state: () => ({
        isAuth: false,
        user_token: null,
        response: null,
        send_data: {}
    }),
    getters: {
        get_auth(state) {
            return state.isAuth
        },


    },
    mutations: {
        setAuth(state, bool) {
            state.isAuth = bool
        }
    },
    // actions: {
    //     async regUser({state, commit}) {
    //         try {
    //             const response = await axios.post('http://127.0.0.1:8000/auth/users/',
    //                 state.send_data);
    //             commit('setResponse', response)
    //
    //         } catch (error) {
    //             commit('setResponse', error.response)
    //             console.log(error)
    //         }
    //     }
    // },

}