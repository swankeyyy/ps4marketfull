<template>
    <li class="nav-item ms-2" v-show="!get_auth()">
        <a class="nav-link active" aria-current="page" href="#" type="button"><img
                src="@/assets/img/login_img.png" alt="userIco" height="24px" data-bs-toggle="modal"
                data-bs-target="#UserModal"></a>
        <div class="modal fade" id="UserModal" tabindex="-1" aria-labelledby="UserModalLabel"
             aria-hidden="true">
            <profile_modal />
        </div>

    </li>
</template>

<script>
import Profile_modal from "@/components/UI/header/profile_modal.vue";
import {mapActions, mapGetters} from "vuex";

export default {
    name: "profile_bar",
    components: {Profile_modal},
    methods: {
        ...mapGetters({
            get_auth: "get_auth"
        }),
        ...mapActions({
            logined: "logined"
        })
    },
    created() {
        this.logined()
    }
}
</script>

<style scoped>

</style>