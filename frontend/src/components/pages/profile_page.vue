<template>
    <div class="container">
        <div class="row">
            <div class="img_container">
                <img src="@/assets/img/profile_profile_page.jpg" alt="profile_img" class="profile_img">
            </div>
            <div class="row user_info">
                <div class="info_row">Username:
                    <div class="inner"><input class="form-control" type="text" placeholder="Подтянем с DRF"
                                              disabled>
                        <button type="button" class="btn btn-primary" disabled>Обновить</button>
                    </div>
                </div>
                <div class="info_row">Имя:
                    <div class="inner"><input class="form-control" type="text" placeholder="Подтянем с DRF"
                    >
                        <button type="button" class="btn btn-primary">Обновить</button>
                    </div>
                </div>
                <div class="info_row">Фамилия:
                    <div class="inner"><input class="form-control" type="text" placeholder="Подтянем с DRF"
                    >
                        <button type="button" class="btn btn-primary">Обновить</button>
                    </div>
                </div>
                <div class="info_row">email:
                    <div class="inner"><input class="form-control" type="text" placeholder="Подтянем с DRF"
                    >
                        <button type="button" class="btn btn-primary">Обновить</button>
                    </div>
                </div>
                <div class="info_row">Дата рождения:
                    <div class="inner"><input class="form-control" type="text" placeholder="Подтянем с DRF"
                    >
                        <button type="button" class="btn btn-primary">Обновить</button>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "profile_page"
}
</script>

<style scoped>
.inner {
    display: flex;
}

.profile_img {
    max-height: 200px;
    border-radius: 10px;
    border: 5px solid #fff;
    box-shadow: 3px 2px 6px #999999;
}

.img_container {
    margin-top: 2%;
    display: flex;
    justify-content: center;
}

.user_info {
    margin: 20px;
    padding: 5px;
}

.info_row {
    padding: 6px;
    font-size: 18px;
    display: flex;
    justify-content: space-between;
}

.form-control {
    margin: 0 10px;

    width: 500px;
}

.container {
    max-width: 800px;
}
</style>