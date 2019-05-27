<template>
<div>
    <div>
        <p> Welcome to control pane as a <b>{{role}}</b> </p>
    </div>
    <!-- TODO: -->
    <PlaceMainOrder>
    </PlaceMainOrder>
    <div v-if="role=='provider'">
        <SubOrderTable :tableData="[]">
            //TODO:
        </SubOrderTable>
    </div>
    <div v-if="role=='customer'">
        <MainOrderTable :tableData="[]">
            //TODO:
        </MainOrderTable>
    </div>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import SubOrderTable from './order/SubOrderTable.vue'
import MainOrderTable from './order/MainOrderTable.vue'
import PlaceMainOrder from './PlaceMainOrder.vue'
@Component({
    components: {
        SubOrderTable,
        MainOrderTable,
        PlaceMainOrder
    }
})
export default class Button extends Vue {
    role: string = '';
    beforeMount() {
        this.role = sessionStorage.getItem('role') as string;
    }
}
</script>
