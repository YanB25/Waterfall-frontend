<template>
  <el-row class="tac" v-if="this.role != 'guest'">
    <el-col :span="24">
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        :router="true"
      >
        <el-submenu index="/orders">
          <template slot="title">
            <i class="el-icon-tickets"></i>
            <span>Orders</span>
          </template>
          <el-menu-item-group title="select orders">
            <el-menu-item index="/orders/main/">Main Orders</el-menu-item>
            <el-menu-item index="/orders/sub/">Sub Orders</el-menu-item>
          </el-menu-item-group>
          <!-- <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-submenu> -->
        </el-submenu>
        <el-menu-item :index="profilePath">
          <template slot="title">
            <i class="el-icon-user"></i>
            <span>Profile</span>
          </template>
        </el-menu-item>
        <el-submenu index="/manage" v-if="this.role == 'manager'">
          <template slot="title">
            <i class="el-icon-setting"></i>
            <span>Manage Center</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/manage/user">User Management</el-menu-item>
            <el-menu-item index="/manage/mainorder">Main Order Management</el-menu-item>
            <el-menu-item index="/manage/suborder">Sub Order Management</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="/control-panel"  v-if="this.role != 'manager'">
          <i class="el-icon-setting"></i>
          <span>Control Panel</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>


<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
@Component
export default class Button extends Vue {
  role : string = "guest";
  profilePath: string = '';

  handleOpen(key: Object, keyPath: Object) {
    console.log(key, keyPath);
  }
  handleClose(key: Object, keyPath: Object) {
    console.log(key, keyPath);
  }
  nav_11() {
    console.log("ok");
    this.$router.push("/nav/11");
  }
  refreshUserRole() {
    let get_role = sessionStorage.getItem('role');
    this.profilePath = `/profile/${sessionStorage.getItem('userid')}`;
    if (get_role == null) {
      this.role = "guest";
    } else {
      this.role = get_role as string;
    }
    console.log(this.role);
  }
  beforeMount() {
    this.refreshUserRole();
  }
}
</script>