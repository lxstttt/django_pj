<template>
    <div>
        <h3>用户</h3>
                <table border="2" cellpadding="0" width="300">
                    <tr>
                        <td>ID</td>
                        <td>姓名</td>
                        <td>生日</td>
                        <td>操作</td>
                    </tr>
                    <tr v-for="(user,index) in users" :key="user.id">
                        <td>{{user.id}}</td>
                        <td>{{user.username}}</td>
                        <td>{{user.bir}}</td>
                        <td><a href="javascript:(0);" @click="del_user(index)">删除</a>|<router-link :to="`/user_detail?id=${user.id}`">用户详情</router-link></td>
                    </tr>
                </table>
    </div>
</template>

<script>
    export default {
        name: "user",
        data:function () {
            return {
                users:[
                    {id: 1, username:"小黑", bir: "2012-12-12"},
                    {id: 2, username:"小白", bir: "2013-12-12"},
                    {id: 3, username:"小红", bir: "2014-12-12"},
                ]
            }
        },
        methods:{
            del_user(index){
                console.log(index);
                this.users.pop(index);
            }
        }
    }
</script>

<style scoped>

</style>
