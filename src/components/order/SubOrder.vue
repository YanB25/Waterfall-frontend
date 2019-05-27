<template>
  <SubOrderTable :tableData="tableData">
  </SubOrderTable>
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import SubOrderTable from '@/components/order/SubOrderTable.vue'

interface TableDataInterface {
  comments: string,
  createdate: string,
  createuser: number,
  id: string,
  mainOrderId: string,
  phone: string,
  quantity: number,
  status: number,
}
@Component({
  components: {
    SubOrderTable
  }
})
export default class Button extends Vue {
  tableData = []
  // click(index: number, row: TableDataInterface) {
  //   console.log(index);
  //   console.log(row);
  //   this.$router.push(`/orders/sub/${row.id}`)
  // }
  beforeCreate() {
    fetch('/api/order/subOrder?limit=10', {
      method: 'GET'
    }).then(data => {
      return data.json();
    }).then(res => {
      this.tableData = res.data.orders;
    })
  }
}
</script>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>