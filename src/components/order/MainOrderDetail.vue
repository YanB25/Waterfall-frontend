<template>
<div>
    <Back />
    <div>
        <p> Main Order Detail {{ $route.params.orderid }} </p>
    </div>
    <el-progress :text-inside="true" :stroke-width="26" :percentage="remain_percentage"></el-progress>
    <SubOrderTable :tableData="subOrdersList">
    </SubOrderTable>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import SubOrderTable from '@/components/order/SubOrderTable.vue'
import { Dictionary } from 'vue-router/types/router';
import Back from '@/components/Back.vue'
@Component({
    components: {
        SubOrderTable,
        Back
    }
}) 
export default class Button extends Vue {
    subOrdersList :Dictionary<string>[] = [];
    remain_percentage :number = 0;
    beforeMount() {
        fetch(`/api/order/mainOrder/${this.$route.params.orderid}/subOrders`)
            .then(res => res.json())
            .then(res => {
                this.subOrdersList = res.data;
            })
        fetch(`/api/order/mainOrder/${this.$route.params.orderid}`)
            .then(res => res.json())
            .then(res => {
                console.log(res.data);
                let quantity = res.data.order.quantity;
                let remain = res.data.order.remain_quantity;
                this.remain_percentage = (quantity - remain) / quantity;
                if (!res.data.order) {
                    this.remain_percentage = 0;
                } else if (this.remain_percentage >= 1) {
                    this.remain_percentage = 1;
                } else {
                    this.remain_percentage *= 100;
                }
                console.log(remain, quantity, this.remain_percentage);
            })
    }
}
</script>
