<template>
    <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">Processing Center</el-menu-item>
        <el-popover
            v-if="!hasLogin"
            class="item"
            placement="left"
            title="Sign Up"
            width="600"
            trigger="click"
        >
            <Login/>
            <el-button slot="reference">Sign Up</el-button>
        </el-popover>

        <!-- <el-menu-item v-if="hasLogin" class="nav" index="logout"> -->
        <el-button v-if="hasLogin" class="item" @click="logout">Log Out</el-button>
        <!-- </el-menu-item> -->
        <!-- <el-menu-item index="3" disabled>Info</el-menu-item> -->
        <!-- <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">Orders</a></el-menu-item> -->
    </el-menu>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import Login from "@/components/Login.vue";

@Component({
    components: {
        Login
    }
})
export default class Button extends Vue {
    hasLogin: Boolean = true;
    handleSelect(key: Object, keyPath: Object) {
        console.log(key, keyPath);
    }
    logout(): void {
        this.hasLogin = false;
        fetch("/api/logout");
    }
    login(): void {}
}
</script>

<style>
.nav {
    float: right !important;
}
.item {
    float: right !important;
}
</style>
