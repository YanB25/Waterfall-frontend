<template>
  <div id="app">

    <el-row>
      <TopBar @login='login' @logout='logout'/>
    </el-row>
    <el-col :span=4>

      <LeftMenu ref="leftMenu"/>
    </el-col>

    <!-- <img src="./assets/logo.png">
    <Button :msg="m" @click.native="hei"> </Button> -->
    <el-col :span=16 :offset=2>
      <router-view class="main"/>
    </el-col>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import VueRouter from 'vue-router'

import LeftMenu from '@/components/LeftMenu.vue'
import Button from '@/components/Button.vue'
import TopBar from '@/components/topbar/TopBar.vue'

// const routes = [
//   { path: '/button', component: Button }
// ]
// const router = new VueRouter({
//   routes
// });

@Component({
  components: {
    Button,
    LeftMenu,
    TopBar
  }
})
export default class App extends Vue {
  m = "hello";
  hasLogin: boolean = false;
  hei() :void {
   this.m = "changed";
 }
 login() {
   (this.$refs.leftMenu as any).refreshUserRole();
 }
 logout() {
   (this.$refs.leftMenu as any).refreshUserRole();
   this.$router.push('/');
 }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}

.main {
  margin-top: 50px;
}

</style>