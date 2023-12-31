<template>
  <Header />
  <Detail />
</template>

<script>
import Header from "@/components/Header.vue";
import Detail from "@/components/Detail.vue";

export default {
    name: "DetailView",
    components: {Detail, Header}
}
</script>

<style scoped>

</style>