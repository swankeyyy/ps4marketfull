<template>
    <li class="nav-item ">
        <a class="nav-link active" aria-current="page" href="#" type="button"><img
                src="@/assets/img/cart_header.png" alt="userIco" height="24px" data-bs-toggle="modal"
                data-bs-target="#CartModal"></a>

        <!-- Modal -->
        <div class="modal fade" id="CartModal" tabindex="-1" aria-labelledby="CartModalLabel"
             aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="CartModalLabel">Список покупок</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                    </div>
                    <div class="modal-body">

                        <ul>
                            <li>Вафли</li>
                            <li>Вафли</li>
                            <li>Вафли</li>
                        </ul>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary"
                                data-bs-dismiss="modal">Закрыть
                        </button>
                        <button type="button" class="btn btn-primary">Перейти к
                            оформлению
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </li>
</template>

<script>
export default {
    name: "basket_bar"
}
</script>

<style scoped>

</style>