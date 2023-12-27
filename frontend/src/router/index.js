import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import RegistrationView from "@/views/RegistrationView.vue";


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
    }

]

const router = createRouter({
    routes,
    history: createWebHistory(),

})

export default router
