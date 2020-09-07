<template>
    <div id="app">
        <h3>欢迎来到百知信息管理系统</h3>
        <router-link to="/home">首页</router-link>
        <router-link to="/user">用户页</router-link>
        <hr>
        <!--      <hr>-->
        <router-view></router-view>
    </div>
</template>


<script>


    export default {
        name: 'App',
    }
</script>

