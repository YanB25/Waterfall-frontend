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

        <username v-if="hasLogin" class="item" :username="username" @logout="logout"> </username>
    </el-menu>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import SignUp from "./SignUp.vue";
import Login from "./Login.vue";
import Username from './Username.vue';

@Component({
    components: {
        SignUp,
        Login,
        Username
    }
})
export default class Button extends Vue {
    hasLogin: Boolean = false;
    username: String = '';
    userid: Number = 0;
    handleSelect(key: Object, keyPath: Object) {
        console.log(key, keyPath);
    }
    logout(): void {
        fetch("/api/user/logout")
            .then(res => {
                return res.json();
            })
            .then(data => {
                if (data.code === 0) {
                    this.hasLogin = false;
                    this.$emit('logout');
                }
            })
    }
    login(username: string, userid: number): void {
        this.hasLogin = true;
        this.username = username;
        this.userid = userid;
        console.log(username);
        console.log(userid);
        this.$emit('login', username, userid);
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
