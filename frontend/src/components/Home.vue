<template>
    <main>
        <div class="container mt-5">
            <div class="row">
                <div class="col-2">
                    <sidebar />
                </div>
                <div class="col ps-3 mt-2">
                    <section>
                        <div class="row row-cols-3">
                            <div class="col">
                                <div class="card p-1 ms-1">
                                    <img src="img/rdr.jpg" class="card-img-top p-1" alt="">
                                    <div class="card-body ms-2">
                                        <h5 class="card-title">Card title</h5>
                                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                                        <p class="card-text ">Some quick example text to build on the card title and
                                            make
                                            up the bulk of the card's content.</p>
                                        <a href="#" class="btn btn-outline-secondary">Перейти к описанию</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card p-1 ms-1">
                                    <img src="img/rdr.jpg" class="card-img-top p-1" alt="">
                                    <div class="card-body ms-2">
                                        <h5 class="card-title">Card title</h5>
                                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                                        <p class="card-text ">Some quick example text to build on the card title and
                                            make
                                            up the bulk of the card's content.</p>
                                        <a href="#" class="btn btn-outline-secondary">Перейти к описанию</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card p-1">
                                    <img src="img/rdr.jpg" class="card-img-top p-1" alt="">
                                    <div class="card-body ms-2">
                                        <h5 class="card-title">Card title</h5>
                                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                                        <p class="card-text ">Some quick example text to build on the card title and
                                            make
                                            up the bulk of the card's content.</p>
                                        <a href="#" class="btn btn-outline-secondary">Перейти к описанию</a>
                                    </div>
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

export default {
    name: "Home",
    components: {Sidebar}
}
</script>

<style scoped>

</style>