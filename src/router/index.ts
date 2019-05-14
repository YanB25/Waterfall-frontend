import Vue from 'vue'
import Router from 'vue-router'
import Helloworld from '@/components/Helloworld.vue'
// import Button from '@/components/Button.vue'
import Profile from '@/components/Profile.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Helloworld
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    }
  ]
})
