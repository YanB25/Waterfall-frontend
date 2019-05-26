import Vue from 'vue'
import Router from 'vue-router'
import Helloworld from '@/components/Helloworld.vue'
// import Button from '@/components/Button.vue'
import Profile from '@/components/Profile.vue'
import MainOrder from '@/components/MainOrder.vue'
import SubOrder from '@/components/SubOrder.vue'
import MainOrderDetail from '@/components/MainOrderDetail.vue'

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
    },
    {
      path: '/orders/main/:orderid',
      name: 'Main Orders',
      component: MainOrderDetail
    },
    {
      path: '/orders/main/',
      name: 'Main Orders',
      component: MainOrder
    },
    {
      path: '/orders/sub/',
      name: 'Sub Orders',
      component: SubOrder
    }
  ]
})
