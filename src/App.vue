<template>
  <div id="app">

    <el-row>
      <TopBar/>
    </el-row>
    <el-col :span=4>

      <LeftMenu />
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
  // userid: number = -1;
  // username: string = "";

  hei() :void {
   this.m = "changed";
 }
//  beforeCreate() {
//    fetch('/api/user/login', {
//      method: 'GET',
//    }).then(res => {
//      return res.json();
//    }).then(data => {
//      if (data.code === 0) {
//        this.userid = data.data.userid;
//        sessionStorage.setItem('userid', this.userid.toString());
//        fetch(`/api/user/${this.userid}`)
//         .then(res => {
//           return res.json();
//         })
//         .then(res => {
//           this.username = res.data.username;
//         })
//      } else {
//        sessionStorage.clear();
//        this.userid = -1;
//        this.username = '';
//      }
//    })
//  }
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