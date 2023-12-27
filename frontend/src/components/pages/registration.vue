<template>
    <div class="container main">
        <h2>Регистрация</h2>
        <div class="content">
            <form action="" class="register_form" @submit.prevent="onSubmit">
                <div class="error">{{ error }}</div>
                <input class="form-control" type="text" placeholder="Username*" v-model="username">
                <input class="form-control" type="email" placeholder="Email" v-model="email">
                <input class="form-control" type="password" placeholder="Пароль**" v-model="password1">
                <input class="form-control last" type="password" placeholder="Повторите пароль**"
                       v-model="password2">
                <button type="submit" class="btn btn-success reg_button" @click="register">Регистрация</button>
                <p class="annotation">Поля, отмеченные **, обязательны для заполнения</p>
            </form>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";

export default {
    name: "registration",
    data() {
        return {
            username: null,
            email: null,
            password1: null,
            password2: null,
            response: null,
            error: '',
            data: {}
        }
    },
    methods: {
        ...mapGetters({
            url: "get_backend_url"
        }),
        async register() {
            if (this.password1 === this.password2 && this.password1.length > 4) {
                if (this.email !== null) {
                    this.data = {
                        'username': this.username,
                        'password': this.password1,
                        'email': this.email
                    }
                } else {
                    this.data = {
                        'username': this.username,
                        'password': this.password1
                    }
                }
                try {
                    const response = await axios.post(this.url() + 'auth/users/', this.data)
                    if (response.status === 201) {
                        this.$router.push('/')

                    } else {
                        this.error = "Чтото не так("
                    }
                } catch
                    (e) {
                    console.log(e)
                    this.error = "Проверьте правильность введенных данных"
                }
            } else {
                this.error = "Пароли не совпадают!"
            }
        }
    },
    computed: {}
}
</script>


<style scoped>
input {
    font-weight: initial;
}

input:hover {

    border: 3px solid green;
}

.error {
    color: red
}

.annotation {
    font-size: 14px;
    margin-top: 2%;
}

.main {
    margin-top: 8%;
    margin-bottom: 8%;

}

.form-control {
    margin: 8px;
}

.content {
    display: flex;
    align-items: center;
    justify-content: center;
}

h2 {
    text-align: center;
}

.register_form {
    margin: 2%;
    padding: 3%;
    width: 60%;
}

.reg_button {
    margin: auto;
    display: block;
    width: 80%;
}

.last {
    margin-bottom: 8%;
}
</style>