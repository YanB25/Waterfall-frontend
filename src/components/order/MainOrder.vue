<template>
 <MainOrderTable :tableData="tableData">
 </MainOrderTable> 
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import MainOrderTable from './MainOrderTable.vue'
interface TableDataInterface {
  address: string,
  comment: string,
  createdate: string,
  createuser: number,
  deadline: string,
  id: string,
  name: string,
  phone: string,
  price: number,
  current_supply: number,
  quantity: number,
  status: number,
  summary: string,
  totalprice: number,
}
@Component({
  components: {
    MainOrderTable
  }
})
export default class Button extends Vue {
  tableData = [{
    // "address": "Mega Center North",
    // "comments": "Very Quick!",
    // "createdate": "2018-01-08 12:00:00",
    // "createuser": 0,
    // "deadline": "2018-01-09 11:11:11",
    // "id": "1",
    // "name": "Shrimp",
    // "phone": "18900230024",
    // "price": 200,
    // "current_supply": 11,
    // "quantity": 3,
    // "status": 0,
    // "summary": "All I need is Shrimp",
    // "totalprice": 600,
  }]
  click(index: number, row: TableDataInterface) {
    console.log(index);
    console.log(row);
    this.$router.push(`/orders/main/${row.id}`)
  }
  beforeCreate() {
    fetch('/api/order/mainOrder?limit=-1', {
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