<template>
<div>
    <Back />
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
import Back from '@/components/Back.vue'
@Component({
    components: {
        SubOrderTable,
        Back
    }
}) 
export default class Button extends Vue {
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
