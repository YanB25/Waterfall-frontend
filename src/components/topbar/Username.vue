<template>
  <el-popover placement="bottom" width="200" trigger="hover">
    <el-collapse>
      <el-collapse-item class="logout-btn" title="Log Out" name="1" @click.native.prevent="logout"></el-collapse-item>
    </el-collapse>
    <el-button type="text" slot="reference"><div class="user-container"><i class="el-icon-user"></i>{{ username }}</div></el-button>
  </el-popover>
</template>


<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

@Component
export default class SignUp extends Vue {
  username: string = '';
    beforeMount() {
      console.log('username mount')
      this.username = sessionStorage.getItem('username') as string;
    }
    logout(): void {
      this.$emit('logout');
    }
}
</script>
