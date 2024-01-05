import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import RegistrationView from "@/views/RegistrationView.vue";
import ProfileView from "@/views/ProfileView.vue";
import DetailView from "@/views/DetailView.vue";
import CategoriesView from "@/views/CategoriesView.vue";
import OrderView from "@/views/OrderView.vue";


const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationView
    },
    {
        path: '/profile',
        name: 'profile',
        component: ProfileView
    },
    {
        path: '/games/:slug',
        name: 'single',
        component: DetailView,
        props: true
    },
    {
        path: '/:slug',
        name: 'change_categories',
        component: CategoriesView,
        props: true
    },
    {
        path: '/order',
        name: 'order',
        component: OrderView,
        props: true,
    }

]

const router = createRouter({
    routes,
    history: createWebHistory(),

})

export default router
