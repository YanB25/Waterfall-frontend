<template>
 <MainOrderTable :tableData="tableData" v-loading="isloading">
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
  isloading: boolean = true;
  tableData = [{
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
    }).catch(err => {
      this.$message({
        message: `err`,
        type: "error"
      })
    }).finally(() => {
      this.isloading = false;
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