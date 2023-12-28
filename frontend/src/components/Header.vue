<template>
    <header>
        <div class="container">
            <topline/>
            <nav class="navbar navbar-expand-lg navbar-light " style="background-color: #d2d4d6">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">PS4Shop</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 px-3">
                            <main_page_link_header />
                            <header_categories/>
                            <contacts_link_header />
                            <about_link_header />
                            <profile_bar/>
                            <basket_bar/>
                            <profile_link_bar/>
                            <logout_bar/>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </header>
</template>

<script>
import Topline from "@/components/UI/header/topline.vue";
import Header_categories from "@/components/UI/header/header_categories.vue";
import Profile_bar from "@/components/UI/header/profile_bar.vue";
import Basket_bar from "@/components/UI/header/basket_bar.vue";
import Logout_bar from "@/components/UI/header/logout_bar.vue";
import Profile_link_bar from "@/components/UI/header/profile_link_bar.vue";
import Contacts_link_header from "@/components/UI/header/contacts_link_header.vue";
import About_link_header from "@/components/UI/header/about_link_header.vue";
import Main_page_link_header from "@/components/UI/header/main_page_link_header.vue";

export default {
    name: "Header",
    components: {
        Main_page_link_header,
        About_link_header,
        Contacts_link_header, Profile_link_bar, Logout_bar, Basket_bar, Profile_bar, Header_categories, Topline}
}
</script>

<style scoped>

</style>