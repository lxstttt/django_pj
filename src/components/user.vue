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
                        <td><a href="javascript:(0);" @click="del_user(index)">删除</a>|<router-link :to="`/user_detail/${JSON.stringify(user)}`">用户详情</router-link></td>
                    </tr>
                </table>
        <br>
        id：<input type="text" v-model="id"><br>
        姓名：<input type="text" v-model="username"><br>
        生日：<input type="text" v-model="bir"><br>
        <button @click="add_user">添加用户</button>
    </div>
</template>

<script>
    export default {
        name: "user",
        data:function () {
            return {
                id:'',
                username:'',
                bir:'',
                users:localStorage.users ? JSON.parse(localStorage.users):[],
            }
        },
        methods:{
            del_user(index){
                console.log(index);
                this.users.splice(index,1)
                localStorage.users = JSON.stringify(this.users)
            },
            add_user(){
              if(this.id && this.username && this.bir){
                  this.users.push({id:this.id,username:this.username,bir:this.bir});
                  localStorage.users = JSON.stringify(this.users);
                  this.id='';
                  this.username='';
                  this.bir='';
              }
            }
        }
    }
</script>

<style scoped>

</style>
