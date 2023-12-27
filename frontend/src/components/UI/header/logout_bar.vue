<template>
    <li class="nav-item" v-show="get_auth()">
        <a class="nav-link active" aria-current="page" type="button" @click="logOut"><img
                src="@/assets/img/logout_header.png" alt="userIco" height="25px"
        ></a>
    </li>
</template>

<script>
import Profile_modal from "@/components/UI/header/profile_modal.vue";
import {mapActions, mapGetters, mapMutations} from "vuex";

export default {
    name: "logout_bar",
    components: {Profile_modal},
    methods: {
        ...mapGetters({
            get_auth: "get_auth"
        }),
        ...mapActions({
            logined: "logined"
        }),
        ...mapMutations({
            set_auth: "set_auth"
        }),
        logOut() {
            this.set_auth(false)
            localStorage.removeItem('token')
        }
    }
}
</script>

<style scoped>

</style>