import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import router from './router'

Vue.use(ElementUI)

router.beforeEach((to, from, next) => {
  console.log(`from ${from} to ${to}`)
  if (to.path === '/') {
    next()
  } else {
    if (sessionStorage.getItem('userid')) {
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
