<template>
    <el-button @click="back">
        back
    </el-button>
</template>


<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
@Component
export default class Button extends Vue {
    back() {
        this.$router.go(-1);
    }
}
</script>

