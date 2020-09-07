import Vue from 'vue'
import Router from 'vue-router'

import home from "../components/home";
import user from "../components/user";
import user_detail from "../components/user_detail";

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/home', component:home,},
    {path: '/', component:home,},
    {path: '/user', component:user,},
    {path: '/user_detail/', component:user_detail,},
  ]
})
