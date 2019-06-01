<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    class="main">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="Address">
            <span>{{ props.row.address }}</span>
          </el-form-item>
          <el-form-item label="Comment">
            <span>{{ props.row.comment }}</span>
          </el-form-item>
          <el-form-item label="Create Date">
            <span>{{ props.row.createdate }}</span>
          </el-form-item>
          <el-form-item label="Create User">
            <span>{{ props.row.createuser }}</span>
          </el-form-item>
          <el-form-item label="Deadline">
            <span>{{ props.row.deadline }}</span>
          </el-form-item>
          <el-form-item label="Id">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="Name">
            <span>{{ props.row.name }}</span>
          </el-form-item>

          <el-form-item label="Phone">
            <span>{{ props.row.phone }}</span>
          </el-form-item>
          <el-form-item label="Price">
            <span>{{ props.row.price }}</span>
          </el-form-item>
          <el-form-item label="Currentn Supply">
            <span>{{ props.row.current_supply }}</span>
          </el-form-item>
          <el-form-item label="Quantity">
            <span>{{ props.row.quantity }}</span>
          </el-form-item>
          <el-form-item label="Remain Quantity">
            <span>{{ props.row.remain_quantity }}</span>
          </el-form-item>
          <el-form-item label="Status">
            <span>{{ props.row.status }}</span>
          </el-form-item>
          <el-form-item label="Summary">
            <span>{{ props.row.summary }}</span>
          </el-form-item>
          <el-form-item label="Total Price">
            <span>{{ props.row.totalprice }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      sortable
      label="ID"
      prop="id">
    </el-table-column>
    <el-table-column
      sortable
      label="Name"
      prop="name">
    </el-table-column>
    <el-table-column
      sortable
      label="Create User ID"
      prop="createuser">
    </el-table-column>
    <el-table-column
      sortable
      label="Price"
      prop="price">
    </el-table-column>
    <el-table-column
      sortable
      label="Rem Quantity"
      prop="remain_quantity">
    </el-table-column>
    <el-table-column label="Operation">
      <template slot-scope="scope">
        <el-button icon="el-icon-search" circle
        @click="info(scope.$index, scope.row)"></el-button>
        <el-button type="primary" icon="el-icon-edit" circle v-if="role == 'provider'"
          :disabled="scope.row.remain_quantity == 0"
         @click="provide(scope.$index, scope.row)">
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Table } from 'element-ui';
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
  remain_quantity: number,
  status: number,
  summary: string,
  totalprice: number,
}
@Component
export default class Button extends Vue {
  @Prop() tableData !: TableDataInterface[];
  role: string = sessionStorage.getItem('role') as string;
  info(index: number, row: TableDataInterface) {
    console.log(index);
    console.log(row);
    this.$router.push(`/orders/main/${row.id}`)
  }
  provide(index: number, row: TableDataInterface) {
    console.log(index, row);
    console.log(`debug, will go to ${row.id}`)
    this.$router.push(`/orders/provide/${row.id}`)
  }
}
</script>

<style>
  .main {
    margin-bottom: 100px;
  }
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