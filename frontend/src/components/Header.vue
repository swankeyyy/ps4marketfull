<template>
    <header>
        <div class="container">
            <topline />
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">PS4Shop</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 px-3">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#">Главная</a>
                            </li>
                            <header_categories />
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#">Контакты</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#">О нас</a>
                            </li>
                            <profile_bar />
                            <basket_bar />
                            <logout_bar />
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

export default {
    name: "Header",
    components: {Logout_bar, Basket_bar, Profile_bar, Header_categories, Topline}
}
</script>

<style scoped>
.container {
    font-size: 20px;
    font-family: Comic Sans MS, Comic Sans, cursive;
}
</style>