import Vue from 'vue'
import Router from 'vue-router'
import Helloworld from '@/components/Helloworld.vue'
import Button from '@/components/Button.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Helloworld
    },
    {
      path: '/nav/11',
      name: 'nav11',
      component: Button
    }
  ]
})
