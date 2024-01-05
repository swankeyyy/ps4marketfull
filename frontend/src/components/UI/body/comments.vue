<template>
    <div>
        <div>
            <h5>Оставить комментарий</h5>
            <textarea class="comment_area"></textarea>
            <br>
            <button @click="loadComments">Отправить</button>
            <h4 class="comment_title">Комментарии</h4>
            <div v-if="no_comments">
                <h5>Пока комментариев нет:(</h5>
            </div>
            <div v-else class="comment_body" v-for="comment in comments">
                <h5 class="comment_username">{{comment.user.username}}</h5>
                <div class="comment_body">{{comment.body}}</div>
                <div class="comment_date">{{comment.date}}</div>

            </div>
        </div>

    </div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";

export default {
    name: "comments",
    data() {
        return {
            no_comments: false,
            comments: []
        }
    },
    props: {
        item_id: {
            required: true
        }
    },
    computed: {
        ...mapGetters({
            url: "get_backend_url"
        })
    },
    methods: {
        click() {
            console.log(this.item_id)
        },
        async loadComments() {
            try {
                let response = await axios.get(this.url + `api/comment/${this.item_id}`)
                if (response.data.comments === 'null') {
                    this.no_comments = true
                } else {
                    this.comments = response.data.comments
                }
                console.log(response.data)
            } catch (e) {
                console.log(e)
            }
        }
    }

}
</script>

<style scoped>
.comment_area {
    width: 80%;
    resize: none
}
.comment_title {
    margin: 25px 0;
}
.comment_body {
    margin: 25px 0;
}
.comment_username {
    font-size: 25px;
    color: #0f74a8;
}
.comment_body {
    font-size: 18px;
    color: #1b6d85;
}
.comment_date {
    font-size: 10px;
}
</style>