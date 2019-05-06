<template>
  <div id="app">

    <el-row>
      <TopBar />
    </el-row>
    <el-col :span=4>

      <LeftMenu />
    </el-col>

    <img src="./assets/logo.png">
    <Button :msg="m" @click.native="hei"> </Button>
    <router-view/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import VueRouter from 'vue-router'

import LeftMenu from '@/components/LeftMenu.vue'
import Button from '@/components/Button.vue'
import TopBar from '@/components/TopBar.vue'

const routes = [
  { path: '/button', component: Button }
]
const router = new VueRouter({
  routes
})

@Component({
  components: {
    Button,
    LeftMenu,
    TopBar
  }
})
export default class App extends Vue {
  m = "hello";

  hei() :void {
   this.m = "changed";
 }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

</style>