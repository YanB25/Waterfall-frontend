<template>
<div>
    <el-button @click="back">
        back
    </el-button>
    <div>
        <p> Main Order Detail {{ $route.params.orderid }} </p>
    </div>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
@Component
export default class Button extends Vue {
    back() {
        this.$router.push('/orders/main');
    }
}
</script>
