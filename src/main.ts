import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import router from './router'

Vue.use(ElementUI)

router.beforeEach((to, from, next) => {
  console.log(`from ${from} to ${to}`)
  let hasLogin: boolean = sessionStorage.getItem('userid') !== null && sessionStorage.getItem('username') != null
  if (!hasLogin && to.path === '/') {
    next()
  } if (hasLogin && to.path === '/welcome') {
    next()
  } else {
    if (hasLogin) {
      next()
      return
    }
    next('/')
  }
})

export default new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
