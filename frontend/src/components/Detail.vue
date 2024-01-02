<template>
    <main>
        <div class="container mt-5">
            <div class="row">
                <div class="col-2">
                    <sidebar/>
                </div>
                <div class="col ps-3 mt-2">
                    <section>
                        <div class="container">
                            <div class="row mb-2">
                                <h2>{{item.title}}</h2>

                            </div>
                            <div class="row">
                                <div class="col-4">
                                    <img :src="url + item.poster" class="poster_img" alt="rdr">

                                </div>
                                <div class="col mt-3 ms-3 pt-2">
                                    <p><b>Название: </b>{{item.title}}</p>
                                    <p><b>Жанры: </b><div v-for="i in item.categories" class="genres">{{i}}, </div></p>
                                    <p><b>Дата выхода: </b>{{item.year}}</p>
                                    <p><b>Производство: </b>ASADASD</p>
                                    <p><b>Язык озвучки: </b>ASDASDASDASDSADASD</p>
                                    <p><b>Платформа: </b>ASDASDASDASDSADASD</p>
                                    <p><b>Ограничения: </b>{{item.age_limit}}+</p>
                                    <div>
                                        <h3 class="price">{{item.price}}р</h3>
                                    </div>
                                </div>
                            </div>
                            <div class="row ps-2 pe-2 mt-2 mb-4">
                                <div v-html="item.description" class="content_text">
                                </div>

                            </div>

                        </div>
                    </section>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import Sidebar from "@/components/UI/body/sidebar.vue";
import {mapActions, mapGetters} from "vuex";
import axios from "axios";


export default {
    name: "Detail",
    components: {Sidebar},
    props: {
        slug: {
            required: true,
            type: String
        }
    },
    data() {
      return {
          item: {}
      }
    },

    computed: {
        ...mapGetters({
            url: "get_backend_url"
        })
    },

    async created() {
        try {
            let response = await axios.get(`http://127.0.0.1:8000/api/products/${this.slug}`)
            this.item = response.data
            console.log(this.item)
        } catch (e) {
            console.log(e)
        }
    }
}
</script>

<style scoped>
.poster_img {
    height: 300px;
}
.genres {
    display: inline;

}
</style>