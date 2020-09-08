<template>
    <div>
        <h3>留言板</h3>
        <input type="text" v-model="msg">
        <button @click="add_note">发表留言</button>
        <br>
        <ul>
        <li v-for="(msg,index) in msg_list">{{msg}}<a href="javascript:(0);" @click="del_note(index)">删除</a></li>
        </ul>
        <span>总数量：{{msg_list.length}}条</span>
        <input type="button" value="删除所有" @click="del_all" v-show="msg_list.length!=0">

    </div>
</template>

<script>
    import index from "../router";

    export default {
        name: "home",
        data: function () {
            return {
                msg: '',
                msg_list: localStorage.msgs ? JSON.parse(localStorage.msgs) : [],
            }
        },
        methods: {
            add_note() {
                let msg = this.msg;
                if (msg) {
                    this.msg_list.push(this.msg);
                    localStorage.msgs = JSON.stringify(this.msg_list);
                    this.msg = '';
                }
            },
            del_note(index){
                this.msg_list.splice(index,1);
                localStorage.msgs = JSON.stringify(this.msg_list);
            },
            del_all(){
                if(confirm('确定要清空吗')){
                    localStorage.clear();
                    this.msg_list = [];
                }
            }
        }
    }
</script>
