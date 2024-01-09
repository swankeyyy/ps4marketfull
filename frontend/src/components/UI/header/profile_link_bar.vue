<template>
    <li class="nav-item" v-show="get_auth()" @click="this.$router.push('/profile')">
        <a class="nav-link active" aria-current="page" type="button"><img
                src="@/assets/img/profile_header_ico.png" alt="userIco" height="25px"
        ></a>
    </li>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    name: "profile_link_bar",
    methods: {
        ...mapGetters({
            get_auth: "get_auth"
        }),

    }
}
</script>

<style scoped>

</style>