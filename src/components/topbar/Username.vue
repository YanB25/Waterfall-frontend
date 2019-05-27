<template>
  <el-popover
    placement="bottom"
    :title="username"
    width="200"
    trigger="hover"
  >
    <el-button @click="logout">Log Out</el-button>
    <el-button type="text" slot="reference"> {{ username }} </el-button>
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