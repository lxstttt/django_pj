<template>
    <div>
        用户详情页面:detail---> : {{$route.query.id}}
        <h4>用户详情展示</h4>

        <br>
        <button @click="re_home">返回主页</button>
        <button @click="re_user">返回用户页</button>
    </div>
<!--    <h4>用户详情展示</h4>-->

<!--    <br>-->
<!--    <button>返回主页</button>-->
<!--    <button>返回用户页</button>-->
</template>

<script>
    export default {
        name: "user_detail",
        methods:{
            re_home(){
                this.$router.push('/home');
            },
            re_user(){
                this.$router.push('/user');
            }
        }
    }
</script>

<style scoped>

</style>
