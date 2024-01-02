import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import RegistrationView from "@/views/RegistrationView.vue";
import ProfileView from "@/views/ProfileView.vue";
import DetailView from "@/views/DetailView.vue";


const routes = [
    {
        path: '',
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
        component: DetailView
    }

]

const router = createRouter({
    routes,
    history: createWebHistory(),

})

export default router
