<template>
<div>
    <div>
        <p> Welcome to control panel as a <b>{{role}}</b> </p>
    </div>

    <div v-if="role=='provider'">
        <SubOrderTable :tableData="tableData" :isme="true">
            //TODO:
        </SubOrderTable>
    </div>
    <div v-if="role=='customer'">
        <PlaceMainOrder>
        </PlaceMainOrder>
        <MainOrderTable :tableData="tableData" class="atbottom" :isme="true">
            //TODO:
        </MainOrderTable>
    </div>
</div>
</template>


<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import SubOrderTable from './order/SubOrderTable.vue'
import MainOrderTable from './order/MainOrderTable.vue'
import PlaceMainOrder from './order/PlaceMainOrder.vue'
@Component({
    components: {
        SubOrderTable,
        MainOrderTable,
        PlaceMainOrder
    }
})
export default class Button extends Vue {
    role: string = '';
    tableData = [];
    beforeMount() {
        this.role = sessionStorage.getItem('role') as string;
        let userid: string = sessionStorage.getItem('userid') as string;
        fetch(`/api/user/${userid}/orders`).then(res => res.json())
            .then(res => {
                console.log(res.data);
                if (this.role == 'customer') {
                    this.tableData = res.data.mainOrder;
                } else if (this.role == 'provider') {
                    this.tableData = res.data.subOrder;
                } else {
                    this.tableData = res.data.subOrder + res.data.mainOrder;
                }
            })
    }
}
</script>
