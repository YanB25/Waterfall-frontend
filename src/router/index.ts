import Vue from 'vue'
import Router from 'vue-router'
import Helloworld from '@/components/Helloworld.vue'
// import Button from '@/components/Button.vue'
import Profile from '@/components/Profile.vue'
import MainOrder from '@/components/order/MainOrder.vue'
import SubOrder from '@/components/order/SubOrder.vue'
import MainOrderDetail from '@/components/order/MainOrderDetail.vue'
import Welcome from '@/components/Welcome.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/orders/main/:orderid',
      name: 'Main Orders Detail',
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
    },
    {
      path: '/',
      name: 'root',
      component: Helloworld
    },
    {
      path: '/welcome',
      name: 'welcome',
      component: Welcome
    }
  ]
})
