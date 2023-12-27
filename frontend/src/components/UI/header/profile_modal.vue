<template>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="UserModalLabel">Профиль</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"
                        aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="mb-3">
                        <label for="recipient-name" class="col-form-label">Имя
                            пользователя:</label>
                        <input type="text" class="form-control" id="recipient" v-model="username">
                    </div>
                    <div class="mb-3">
                        <label for="recipient-name"
                               class="col-form-label">Пароль:</label>
                        <input type="password" class="form-control" id="recipient-name" v-model="password">
                    </div>
                </form>
            </div>
            <div class="modal-footer">

                <button type="button" @click="logIn" class="btn btn-success" data-bs-dismiss="modal">Авторизация
                </button>
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Регистрация
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {mapGetters, mapMutations, mapState} from "vuex";
import axios from "axios";

export default {
    name: "profile_modal",

    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        ...mapMutations({
            set_auth: "set_auth",
        }),
        ...mapGetters({
            url: "get_backend_url",
            get_auth: "get_auth"
        }),
        async logIn() {
            if (this.username.length > 3 && this.password.length > 3) {
                try {
                    const response = await axios.post(this.url() + 'auth/token/login/', {
                        "username": this.username,
                        "password": this.password,
                    })
                    localStorage.token = ('Token ' + response.data.auth_token)
                    this.set_auth(true)
                } catch (e) {
                    alert("Проверьте правильность введенных данных!")
                }
            } else {
                alert("Логин должен содержать не менее 4 символов, пароль не менее 7")
            }
        },
    },
}
</script>

<style scoped>

</style>