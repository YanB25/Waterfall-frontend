<template>
  <el-menu
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
  >
    <el-menu-item index="1">Processing Center</el-menu-item>
    <el-menu-item class="nav" index="login">
      <el-popover
        placement="left"
        title="Sign Up"
        width="600"
        trigger="click"
      >
      <Login/>

        <el-button slot="reference">Sign up</el-button>
      </el-popover>
    </el-menu-item>
    <!-- <el-menu-item index="3" disabled>Info</el-menu-item> -->
    <!-- <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">Orders</a></el-menu-item> -->
  </el-menu>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import Login from '@/components/Login.vue'

@Component({
    components: {
        Login
    }
})
export default class Button extends Vue {
    handleSelect(key: Object, keyPath: Object) {
        console.log(key, keyPath)
    }
}
</script>

<style>
.nav {
  float: right !important;
}
</style>
