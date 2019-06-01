<template>
<div>
    <el-button @click="back">
        back
    </el-button>
    <div>
        <p> Main Order Detail {{ $route.params.orderid }} </p>
    </div>
    <SubOrderTable :tableData="subOrdersList">
    </SubOrderTable>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import SubOrderTable from '@/components/order/SubOrderTable.vue'
import { Dictionary } from 'vue-router/types/router';
@Component({
    components: {
        SubOrderTable
    }
}) 
export default class Button extends Vue {
    back() {
        // this.$router.push('/orders/main');
        this.$router.go(-1);
    }
    subOrdersList :Dictionary<string>[] = [];
    beforeMount() {
        fetch(`/api/order/mainOrder/${this.$route.params.orderid}/subOrders`)
            .then(res => res.json())
            .then(res => {
                this.subOrdersList = res.data;
            })
    }
}
</script>
