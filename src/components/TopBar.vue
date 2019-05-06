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
            <SignUp @login="login"/>
            <el-button slot="reference">Sign Up</el-button>
        </el-popover>

        <el-popover
            v-if="!hasLogin"
            class="item"
            placement="left"
            title="Login"
            width="600"
            trigger="click"
        >
            <Login @login="login"/>
            <el-button slot="reference">Login</el-button>
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
import SignUp from "@/components/SignUp.vue";
import Login from "@/components/Login.vue";

@Component({
    components: {
        SignUp,
        Login
    }
})
export default class Button extends Vue {
    hasLogin: Boolean = false;
    handleSelect(key: Object, keyPath: Object) {
        console.log(key, keyPath);
    }
    logout(): void {
        fetch("/api/logout")
            .then(res => {
                return res.json();
            })
            .then(data => {
                if (data.code === 0) {
                    this.hasLogin = false;
                }
            })
    }
    login(): void {
        this.hasLogin = true;
    }
}
</script>

<style>
.nav {
    float: right !important;
}
.item {
    float: right !important;
    margin: 10px;
}
</style>
