<template>
    <div class="container">
        <div class="row">
            <div class="img_container">
                <img src="@/assets/img/profile_avatar.jpg" alt="profile_img" class="profile_img">
            </div>
            <div class="row user_info">
                <div class="info_row">Username:
                    <div class="inner"><input class="form-control" type="text" :placeholder="username"
                                              disabled>
                    </div>
                </div>
                <div class="info_row">Имя:
                    <div class="inner"><input class="form-control" type="text" placeholder="Введите имя"
                                              v-model="first_name"
                    >
                    </div>
                </div>
                <div class="info_row">Фамилия:
                    <div class="inner"><input class="form-control" type="text" placeholder="Введите фамилию"
                                              v-model="last_name">
                    </div>
                </div>
                <div class="info_row">email:
                    <div class="inner"><input class="form-control" type="text" placeholder="Почтовый ящик"
                                              v-model="email">
                    </div>
                </div>
                <div class="info_row">Дата рождения:
                    <div class="inner"><input class="form-control" type="date" placeholder="Дата рождения"
                                              v-model="date_birth">
                    </div>
                </div>
                <!--                <div class="info_row">Фото профиля:-->
                <!--                    <div class="inner">-->
                <!--                        <input type="file" ref="file" class="file-input" @change="filechange"-->
                <!--                               placeholder="Добавьте фото">-->
                <!--                        <button @click="uploader">click</button>-->
                <!--                    </div>-->
                <!--                </div>-->
                <div class="buttons_group">
                    <button type="button" class="btn btn-primary" @click="updater">Обновить</button>
                    <button type="button" class="btn btn-success" @click="this.$router.push('/')">Назад</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";
import axios from "axios";

export default {
    name: "profile_page",
    data() {
        return {
            username: '',
            first_name: '',
            last_name: '',
            email: '',
            date_birth: '',
            token: localStorage.getItem('token'),
            file: '',
            id: null,
        }
    },
    methods: {
        ...mapGetters({
            url: "get_backend_url",
        }),

        // filechange() {
        //     this.file = this.$refs.file.files.item(0)
        // },
        //
        //
        // async uploader() {
        //     let formData = new FormData();
        //     formData.append('file', this.file);
        //
        //
        //     try {
        //         let response = await axios.put(this.url() + `api/users/uploadprofile/${this.id}`,
        //             formData,
        //
        //         )
        //         console.log(response);
        //     } catch (e) {
        //         console.log(e);
        //     }
        // }
        // ,

        async updater() {
            try {
                let data = {
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'email': this.email,
                    'date_birth': this.date_birth
                }
                let response = await axios.patch(this.url() + 'auth/users/me/', data)
                alert("Обновлено")
            } catch (e) {
                console.log(e)
            }
        }
    },
    async created() {
        try {
            axios.defaults.headers.common['Authorization'] = this.token
            let response = await axios.get(this.url() + 'auth/users/me/',)
            this.username = response.data.username
            this.first_name = response.data.first_name
            this.last_name = response.data.last_name
            this.email = response.data.email
            this.date_birth = response.data.date_birth
            this.id = response.data.id

        } catch (e) {
            console.log(e)
        }
    }
}
</script>

<style scoped>
.buttons_group{
    display: flex;
    justify-content: space-between;
}
button {
    margin-top: 4%;
    width: 30%;
}

p {
    margin-top: 20px;
    font-size: 12px;
}

.inner {
    display: flex;
}

.profile_img {
    max-height: 200px;
    border-radius: 10px;
    border: 5px solid #fff;
    box-shadow: 3px 2px 6px #999999;
}

.img_container {
    margin-top: 2%;
    display: flex;
    justify-content: center;
}

.user_info {
    margin: 20px;
    padding: 5px;
}

.info_row {
    padding: 6px;
    font-size: 18px;
    display: flex;
    justify-content: space-between;
}

.form-control {
    margin: 0 10px;

    width: 500px;
}

.container {
    max-width: 800px;
}
</style>